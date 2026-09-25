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
    if (stored) {
      apply(stored);
    } else {
      cookie.hidden = false;
    }
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
