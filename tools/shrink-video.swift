// Herencodeert een video naar H.264 met vaste breedte en bitrate, plus AAC-geluid.
// Mobiele versie van een reel (zo zijn de *-m.mp4 bestanden gemaakt):
//   swiftc -O tools/shrink-video.swift -o /tmp/shrink && /tmp/shrink assets/video/x.mp4 assets/video/x-m.mp4 360 500
// Gebruik: swift shrink.swift <in.mp4> <out.mp4> <breedte> <video-kbps>
import AVFoundation

let a = CommandLine.arguments
let src = URL(fileURLWithPath: a[1]), dst = URL(fileURLWithPath: a[2])
let width = Int(a[3])!, kbps = Int(a[4])!
try? FileManager.default.removeItem(at: dst)

let asset = AVURLAsset(url: src)
let sema = DispatchSemaphore(value: 0)
var vTrack: AVAssetTrack!, aTrack: AVAssetTrack?
Task {
    vTrack = try! await asset.loadTracks(withMediaType: .video).first!
    aTrack = try? await asset.loadTracks(withMediaType: .audio).first
    sema.signal()
}
sema.wait()

let size = vTrack.naturalSize.applying(vTrack.preferredTransform)
let srcW = abs(size.width), srcH = abs(size.height)
var outW = width, outH = Int((Double(srcH) * Double(width) / Double(srcW)).rounded())
outH -= outH % 2; outW -= outW % 2

let reader = try! AVAssetReader(asset: asset)
let writer = try! AVAssetWriter(outputURL: dst, fileType: .mp4)
writer.shouldOptimizeForNetworkUse = true

// Video: via een videocompositie schalen en de rotatie toepassen.
let comp = AVMutableVideoComposition(propertiesOf: asset)
comp.renderSize = CGSize(width: outW, height: outH)
let fps = vTrack.nominalFrameRate > 0 ? vTrack.nominalFrameRate : 30
comp.frameDuration = CMTime(value: 1, timescale: CMTimeScale(fps.rounded()))
let instr = AVMutableVideoCompositionInstruction()
instr.timeRange = CMTimeRange(start: .zero, duration: asset.duration)
let layer = AVMutableVideoCompositionLayerInstruction(assetTrack: vTrack)
let scale = CGFloat(outW) / srcW
layer.setTransform(vTrack.preferredTransform.concatenating(CGAffineTransform(scaleX: scale, y: scale)), at: .zero)
instr.layerInstructions = [layer]
comp.instructions = [instr]

let vOut = AVAssetReaderVideoCompositionOutput(videoTracks: [vTrack], videoSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA])
vOut.videoComposition = comp
reader.add(vOut)
let vIn = AVAssetWriterInput(mediaType: .video, outputSettings: [
    AVVideoCodecKey: AVVideoCodecType.h264, AVVideoWidthKey: outW, AVVideoHeightKey: outH,
    AVVideoCompressionPropertiesKey: [AVVideoAverageBitRateKey: kbps * 1000, AVVideoProfileLevelKey: AVVideoProfileLevelH264MainAutoLevel,
                                      AVVideoMaxKeyFrameIntervalKey: Int(fps.rounded()) * 2, AVVideoAllowFrameReorderingKey: true]])
vIn.expectsMediaDataInRealTime = false
writer.add(vIn)

var aOut: AVAssetReaderTrackOutput?, aIn: AVAssetWriterInput?
if let t = aTrack {
    aOut = AVAssetReaderTrackOutput(track: t, outputSettings: [AVFormatIDKey: kAudioFormatLinearPCM])
    reader.add(aOut!)
    aIn = AVAssetWriterInput(mediaType: .audio, outputSettings: [AVFormatIDKey: kAudioFormatMPEG4AAC, AVNumberOfChannelsKey: 2, AVSampleRateKey: 44100, AVEncoderBitRateKey: 96000])
    writer.add(aIn!)
}

reader.startReading(); writer.startWriting(); writer.startSession(atSourceTime: .zero)
let group = DispatchGroup()
func pump(_ input: AVAssetWriterInput, _ output: AVAssetReaderOutput, _ q: String) {
    group.enter()
    input.requestMediaDataWhenReady(on: DispatchQueue(label: q)) {
        while input.isReadyForMoreMediaData {
            if let buf = output.copyNextSampleBuffer() { input.append(buf) } else { input.markAsFinished(); group.leave(); return }
        }
    }
}
pump(vIn, vOut, "v")
if let i = aIn, let o = aOut { pump(i, o, "a") }
group.wait()
writer.finishWriting { sema.signal() }
sema.wait()
if writer.status != .completed { print("FOUT", writer.error ?? "", reader.error ?? ""); exit(1) }
print(outW, "x", outH)
