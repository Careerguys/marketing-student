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
