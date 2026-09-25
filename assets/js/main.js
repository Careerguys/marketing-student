/* Marketing Student — main.js. Geen dependencies, alles progressive enhancement. */
(function () {
  "use strict";

  /* ---------- Mobiel menu ---------- */
  var burger = document.querySelector("[data-menu-toggle]");
  var panel = document.getElementById("mobile-nav");
  function setMenu(open) {
    if (!burger || !panel) return;
    panel.classList.toggle("is-open", open);
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Menu sluiten" : "Menu openen");
    panel.inert = !open;
    document.body.classList.toggle("menu-open", open);
  }
  if (burger && panel) {
    panel.inert = true;
    burger.addEventListener("click", function () {
      setMenu(burger.getAttribute("aria-expanded") !== "true");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && panel.classList.contains("is-open")) {
        setMenu(false);
        burger.focus();
      }
    });
    window.matchMedia("(min-width: 1100px)").addEventListener("change", function (e) {
      if (e.matches) setMenu(false);
    });
  }

  /* ---------- Dropdown desktop ---------- */
  document.querySelectorAll(".has-dropdown").forEach(function (li) {
    var btn = li.querySelector("button");
    if (!btn) return;
    function close() {
      li.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    }
    btn.addEventListener("click", function () {
      var open = !li.classList.contains("is-open");
      li.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
    li.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(); btn.focus(); }
    });
    li.addEventListener("focusout", function (e) {
      if (!li.contains(e.relatedTarget)) close();
    });
    document.addEventListener("click", function (e) {
      if (!li.contains(e.target)) close();
    });
  });

  /* ---------- Formulier op mobiel onderaan, op desktop in de hero ---------- */
  var heroForm = document.querySelector("[data-form-hero]");
  var formSlot = document.querySelector("[data-form-slot]");
  var formOrigin = document.querySelector("[data-form-origin]");
  if (heroForm && formSlot && formOrigin) {
    var narrow = window.matchMedia("(max-width: 1099px)");
    var placeForm = function () {
      if (narrow.matches && heroForm.parentNode !== formSlot) formSlot.appendChild(heroForm);
      else if (!narrow.matches && heroForm.parentNode !== formOrigin) formOrigin.appendChild(heroForm);
    };
    placeForm();
    narrow.addEventListener("change", placeForm);
  }

  /* ---------- Secties zacht in beeld, eenmalig ---------- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll(".section:not(.showcase) > .container > *, .showcase");
  if (reduce || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0 });
    targets.forEach(function (el) {
      /* Wat bij het laden al in beeld staat, blijft gewoon staan: geen flits. */
      if (el.getBoundingClientRect().top < window.innerHeight && !el.classList.contains("showcase")) return;
      if (!el.classList.contains("showcase")) el.classList.add("reveal");
      io.observe(el);
    });
  }

  /* ---------- Reels: draaiende ring, alleen de voorste video speelt, geluid alleen na een tik ---------- */
  document.querySelectorAll("[data-reels]").forEach(function (wrap) {
    var stage = wrap.querySelector(".reels");
    var ring = wrap.querySelector(".reels__ring");
    var cards = Array.prototype.slice.call(ring.querySelectorAll(".reel"));
    var videos = cards.map(function (c) { return c.querySelector("video"); });
    var n = cards.length, step = 360 / n;
    var angle = 0, target = null, hover = false, inView = false, sound = -1, drag = null, last = 0, front = -1;
    var speed = reduce ? 0 : step / 8; /* graden per seconde: elke 8 seconden een video verder */

    function setSound(i, on) {
      var b = cards[i].querySelector(".reel__sound");
      videos[i].muted = !on;
      b.setAttribute("aria-pressed", String(on));
      b.setAttribute("aria-label", b.getAttribute("aria-label").replace(/^Geluid (aan|uit)/, on ? "Geluid uit" : "Geluid aan"));
      sound = on ? i : (sound === i ? -1 : sound);
    }
    function frontIndex() { return ((Math.round(-angle / step) % n) + n) % n; }
    function render() {
      ring.style.transform = "translateZ(calc(var(--r) * -1)) rotateY(" + angle + "deg)";
      cards.forEach(function (c, i) {
        var rel = ((i * step + angle) % 360 + 540) % 360 - 180; /* -180..180, 0 = voor */
        var a = Math.abs(rel);
        c.style.opacity = a > 95 ? 0 : String(1 - a / 140);
        c.style.pointerEvents = a > 75 ? "none" : "";
      });
      var f = frontIndex();
      if (f !== front) {
        front = f;
        videos.forEach(function (v, i) {
          if (i === f && inView) { v.play().catch(function () {}); }
          else { v.pause(); if (sound === i) setSound(i, false); }
        });
      }
    }
    function tick(t) {
      var dt = last ? Math.min((t - last) / 1000, 0.1) : 0;
      last = t;
      if (target !== null) {
        var d = target - angle;
        angle += d * Math.min(1, dt * 6);
        if (Math.abs(d) < 0.2) { angle = target; target = null; }
      } else if (!hover && !drag && sound < 0 && inView) {
        angle -= speed * dt;
      }
      render();
      requestAnimationFrame(tick);
    }
    function go(dir) { target = Math.round(((target !== null ? target : angle) - dir * step) / step) * step; }
    function bringToFront(i) { var base = Math.round(angle / step) * step; var rel = ((i * step + base) % 360 + 540) % 360 - 180; target = base - rel; }

    cards.forEach(function (c, i) {
      c.querySelector(".reel__sound").addEventListener("click", function (e) {
        e.stopPropagation();
        var on = videos[i].muted;
        videos.forEach(function (v, j) { if (j !== i && !v.muted) setSound(j, false); });
        setSound(i, on);
        if (on) { bringToFront(i); videos[i].play(); }
      });
      c.addEventListener("click", function () { if (frontIndex() !== i) bringToFront(i); });
    });
    wrap.querySelector("[data-reels-prev]").addEventListener("click", function () { go(-1); });
    wrap.querySelector("[data-reels-next]").addEventListener("click", function () { go(1); });
    stage.addEventListener("mouseenter", function () { hover = true; });
    stage.addEventListener("mouseleave", function () { hover = false; });
    stage.addEventListener("focusin", function () { hover = true; });
    stage.addEventListener("focusout", function () { hover = false; });
    stage.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") drag = { x: e.clientX, a: angle, moved: false }; });
    stage.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var dx = e.clientX - drag.x;
      if (Math.abs(dx) > 6) drag.moved = true;
      angle = drag.a + dx * 0.35; target = null;
    });
    ["pointerup", "pointercancel"].forEach(function (ev) {
      stage.addEventListener(ev, function () { if (drag && drag.moved) target = Math.round(angle / step) * step; drag = null; });
    });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        inView = entries[0].isIntersecting;
        front = -1;
        if (!inView) videos.forEach(function (v, i) { v.pause(); if (sound === i) setSound(i, false); });
      }, { threshold: 0.35 }).observe(stage);
    } else { inView = true; }
    wrap.classList.add("is-3d");
    render();
    requestAnimationFrame(tick);
  });

  /* ---------- Formulieren: validatie en Netlify-verzending ---------- */
  function fieldError(input, msg) {
    var field = input.closest(".field");
    if (!field) return;
    var err = field.querySelector(".field__error");
    field.classList.toggle("is-invalid", !!msg);
    input.setAttribute("aria-invalid", msg ? "true" : "false");
    if (err) err.textContent = msg || "";
  }
  function check(input) {
    var v = input.value.trim();
    if (input.required && !v) return "Vul dit veld in.";
    if (input.type === "email" && v && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) return "Vul een geldig e-mailadres in.";
    if (input.type === "tel" && v && v.replace(/[^0-9]/g, "").length < 9) return "Vul een geldig telefoonnummer in.";
    return "";
  }
  document.querySelectorAll("form[data-validate]").forEach(function (form) {
    var inputs = form.querySelectorAll("input:not([type=hidden]):not([type=radio]):not([name=bot-field]), textarea");
    inputs.forEach(function (input) {
      input.addEventListener("blur", function () {
        if (input.value.trim() || input.getAttribute("aria-invalid") === "true") fieldError(input, check(input));
      });
    });
    form.addEventListener("submit", function (e) {
      var first = null;
      inputs.forEach(function (input) {
        var msg = check(input);
        fieldError(input, msg);
        if (msg && !first) first = input;
      });
      if (first) {
        e.preventDefault();
        first.focus();
        return;
      }
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: "form_submit", form_name: form.getAttribute("name") });
    });
  });

  /* ---------- Kaarten van de vestigingen: Google Maps pas na een klik (of na cookie-akkoord) ---------- */
  var maps = document.querySelectorAll("[data-map]");
  function loadMap(box) {
    if (box.querySelector("iframe")) return;
    var f = document.createElement("iframe");
    f.src = "https://maps.google.com/maps?q=" + encodeURIComponent(box.getAttribute("data-map")) + "&z=15&output=embed";
    f.title = box.getAttribute("data-map-title");
    f.loading = "lazy";
    f.referrerPolicy = "no-referrer-when-downgrade";
    box.innerHTML = "";
    box.appendChild(f);
  }
  if (maps.length) {
    var consent = null;
    try { consent = localStorage.getItem("ms_consent"); } catch (err) {}
    maps.forEach(function (box) {
      var btn = box.querySelector("[data-map-load]");
      if (btn) btn.addEventListener("click", function () { loadMap(box); });
      if (consent === "granted") loadMap(box);
    });
  }

  /* ---------- Klikken op bellen en mailen meten ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
    if (!a) return;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: a.href.indexOf("tel:") === 0 ? "phone_click" : "email_click", link_url: a.href });
  });

  /* ---------- Cookiebanner (alleen aanwezig als GTM actief is) ---------- */
  var cookie = document.getElementById("cookie");
  if (cookie) {
    var KEY = "ms_consent";
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (err) {}
    function apply(value) {
      if (typeof window.gtag !== "function") return;
      window.gtag("consent", "update", { analytics_storage: value === "granted" ? "granted" : "denied" });
    }
    /* Een eerdere keuze zet het inline script in <head> al vóór GTM; hier alleen de banner tonen als er nog geen keuze is. */
    if (!stored) cookie.hidden = false;
    cookie.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-consent]");
      if (!btn) return;
      var value = btn.getAttribute("data-consent") === "grant" ? "granted" : "denied";
      try { localStorage.setItem(KEY, value); } catch (err) {}
      apply(value);
      cookie.hidden = true;
    });
    document.querySelectorAll("[data-cookie-settings]").forEach(function (b) {
      b.addEventListener("click", function () { cookie.hidden = false; });
    });
  }
})();
