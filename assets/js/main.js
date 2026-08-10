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
})();
