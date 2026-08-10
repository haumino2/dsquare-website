(() => {
  document.documentElement.classList.add("js");
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => links.classList.remove("open"));
    });
  }

  const reveals = document.querySelectorAll(".reveal");
  const show = (el) => el.classList.add("visible");
  // Immediately show anything already in (or near) the viewport
  reveals.forEach((el) => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.95 && rect.bottom > 0) show(el);
  });
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            show(entry.target);
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -5% 0px" }
    );
    reveals.forEach((el) => {
      if (!el.classList.contains("visible")) io.observe(el);
    });
  } else {
    reveals.forEach(show);
  }

  const form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const note = form.querySelector("[data-form-status]");
      if (note) {
        note.hidden = false;
        note.textContent =
          "Thanks — this prototype form does not send email yet. Please reach thework@dsquare.com.vn directly.";
      }
      form.reset();
    });
  }

  // AEO Review bilingual toggle
  const langBtns = document.querySelectorAll("[data-set-lang]");
  if (langBtns.length) {
    const applyLang = (lang) => {
      document.body.dataset.reviewLang = lang;
      document.documentElement.lang = lang;
      document.querySelectorAll("[data-lang]").forEach((el) => {
        const match = el.getAttribute("data-lang") === lang;
        el.hidden = !match;
        if (match) {
          el.querySelectorAll(".reveal").forEach((r) => r.classList.add("visible"));
        }
      });
      langBtns.forEach((btn) => {
        const on = btn.getAttribute("data-set-lang") === lang;
        btn.classList.toggle("is-active", on);
        btn.setAttribute("aria-pressed", on ? "true" : "false");
      });
      try {
        localStorage.setItem("dsquare-aeo-lang", lang);
      } catch (_) {}
    };
    let initial = "en";
    try {
      const saved = localStorage.getItem("dsquare-aeo-lang");
      if (saved === "en" || saved === "vi") initial = saved;
    } catch (_) {}
    const hash = (location.hash || "").replace("#", "");
    if (hash === "vi" || hash === "en") initial = hash;
    applyLang(initial);
    langBtns.forEach((btn) => {
      btn.addEventListener("click", () => applyLang(btn.getAttribute("data-set-lang")));
    });
  }
})();
