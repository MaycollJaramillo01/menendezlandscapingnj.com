import { animate, stagger } from "animejs";

const menuButton = document.querySelector(".menu-toggle");
const nav = document.querySelector("#primary-nav");

if (menuButton && nav) {
  const menuLabel = menuButton.querySelector(".sr-only");
  const setMenu = (open) => {
    menuButton.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
    if (menuLabel) menuLabel.textContent = open ? "Close menu" : "Open menu";
  };

  menuButton.addEventListener("click", () => {
    setMenu(menuButton.getAttribute("aria-expanded") !== "true");
  });
  nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => setMenu(false)));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMenu(false);
  });
  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target) && !menuButton.contains(event.target)) setMenu(false);
  });
}

const serviceDropdown = document.querySelector("[data-service-dropdown]");
if (serviceDropdown) {
  const trigger = serviceDropdown.querySelector(".nav-dropdown__trigger");
  const panel = serviceDropdown.querySelector(".nav-dropdown__panel");
  if (trigger && panel) {
    const setServiceMenu = (open) => {
      trigger.setAttribute("aria-expanded", String(open));
      panel.hidden = !open;
      if (open && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        animate(panel, { opacity: [0, 1], translateY: [-5, 0], duration: 180, ease: "out(3)" });
      }
    };

    trigger.addEventListener("click", () => {
      setServiceMenu(trigger.getAttribute("aria-expanded") !== "true");
    });
    serviceDropdown.addEventListener("focusout", (event) => {
      if (!serviceDropdown.contains(event.relatedTarget)) setServiceMenu(false);
    });
    document.addEventListener("click", (event) => {
      if (!serviceDropdown.contains(event.target)) setServiceMenu(false);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        setServiceMenu(false);
        trigger.focus();
      }
    });
  }
}

const filterButtons = document.querySelectorAll("[data-filter]");
const galleryCards = document.querySelectorAll(".gallery-card[data-category]");

if (filterButtons.length && galleryCards.length) {
  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const filter = button.dataset.filter;
      filterButtons.forEach((other) => {
        const active = other === button;
        other.classList.toggle("is-active", active);
        other.setAttribute("aria-pressed", String(active));
      });
      galleryCards.forEach((card) => {
        card.hidden = filter !== "all" && card.dataset.category !== filter;
      });
    });
  });
}

const serviceSelect = document.querySelector("#service-select");
if (serviceSelect) {
  const requestedService = new URLSearchParams(window.location.search).get("service");
  if (requestedService && Array.from(serviceSelect.options).some((option) => option.value === requestedService)) {
    serviceSelect.value = requestedService;
  }
}

const form = document.querySelector("[data-contact-form]");
if (form) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const status = document.querySelector("#form-status");
    const button = form.querySelector('[type="submit"]');
    const label = button?.querySelector(".submit-label");
    const idleLabel = label?.textContent || "Send estimate request";
    const payload = Object.fromEntries(new FormData(form).entries());
    payload._replyto = payload.email;

    if (button) button.disabled = true;
    if (label) label.textContent = "Sending request…";
    form.setAttribute("aria-busy", "true");
    if (status) {
      status.dataset.state = "sending";
      status.textContent = "Sending your request securely…";
    }

    try {
      const response = await fetch(form.dataset.ajaxEndpoint, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      const result = await response.json();
      const activationPending = String(result.message || "").toLowerCase().includes("activation");
      if (activationPending) {
        form.reset();
        if (status) {
          status.dataset.state = "pending";
          status.textContent = "Your request is saved. Email delivery needs a one-time confirmation. For a quicker response, call (609) 516-6584.";
        }
        return;
      }
      if (!response.ok || result.success === false || result.success === "false") {
        throw new Error(result.message || "The form service could not accept the request.");
      }

      form.reset();
      if (status) {
        status.dataset.state = "success";
        status.textContent = "Your request has been received. Menendez Landscaping will follow up shortly.";
      }
    } catch (error) {
      console.error("Contact form submission failed", error);
      if (status) {
        status.dataset.state = "error";
        status.textContent = "We couldn't send the request online. Please call (609) 516-6584 or use the email link below.";
      }
    } finally {
      form.removeAttribute("aria-busy");
      if (button) button.disabled = false;
      if (label) label.textContent = idleLabel;
      if (status && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        animate(status, { opacity: [0.72, 1], translateY: [4, 0], duration: 320, ease: "out(3)" });
      }
    }
  });
}

document.querySelectorAll("[data-current-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const heroImage = document.querySelector(".hero__image");

if (!reduceMotion) {
  const heroContent = document.querySelector(".hero__content");
  if (heroContent) {
    animate(heroContent.children, {
      opacity: [0, 1],
      translateY: [20, 0],
      duration: 820,
      delay: stagger(105),
      ease: "out(4)",
    });
  }

  if (heroImage) {
    animate(heroImage, { scale: [1, 1.045], duration: 16000, ease: "inOut(2)", alternate: true, loop: true });
  }

  const revealTargets = Array.from(document.querySelectorAll("[data-reveal]"));
  if (revealTargets.length) {
    document.documentElement.classList.add("motion-ready");
    if (typeof window.IntersectionObserver === "function") {
      const revealObserver = new IntersectionObserver((entries) => {
        const visibleTargets = entries.filter((entry) => entry.isIntersecting).map((entry) => entry.target);
        if (!visibleTargets.length) return;

        visibleTargets.forEach((element) => {
          element.classList.add("motion-entered");
          revealObserver.unobserve(element);
        });
        animate(visibleTargets, {
          opacity: [0, 1],
          translateY: [26, 0],
          filter: ["blur(2px)", "blur(0px)"],
          duration: 760,
          delay: stagger(90),
          ease: "out(4)",
        });
      }, { threshold: 0.08, rootMargin: "0px 0px -8% 0px" });

      revealTargets.forEach((element) => revealObserver.observe(element));
    } else {
      const revealVisibleTargets = () => {
        const visibleTargets = revealTargets.filter((element) => {
          if (element.classList.contains("motion-entered")) return false;
          const bounds = element.getBoundingClientRect();
          return bounds.top < window.innerHeight * 0.92 && bounds.bottom > 0;
        });
        if (!visibleTargets.length) return;
        visibleTargets.forEach((element) => element.classList.add("motion-entered"));
        animate(visibleTargets, {
          opacity: [0, 1],
          translateY: [26, 0],
          duration: 760,
          delay: stagger(90),
          ease: "out(4)",
        });
      };
      window.addEventListener("scroll", revealVisibleTargets, { passive: true });
      window.addEventListener("resize", revealVisibleTargets);
      revealVisibleTargets();
    }
  }

  document.querySelectorAll(".home-service__photo img, .work-item img").forEach((image) => {
    image.addEventListener("mouseenter", () => {
      animate(image, { scale: 1.025, duration: 350, ease: "out(3)" });
    });
    image.addEventListener("mouseleave", () => {
      animate(image, { scale: 1, duration: 380, ease: "out(3)" });
    });
  });
}
