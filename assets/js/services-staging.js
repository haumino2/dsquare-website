(() => {
  const menuButton = document.querySelector('.menu-button');
  const menu = document.querySelector('.service-menu');

  const setMenu = (open) => {
    menuButton?.setAttribute('aria-expanded', open ? 'true' : 'false');
    menu?.setAttribute('aria-hidden', open ? 'false' : 'true');
    menu?.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
  };

  menuButton?.addEventListener('click', () => {
    setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
  });
  menu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setMenu(false);
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.reveal').forEach((item) => revealObserver.observe(item));

  document.querySelectorAll('[data-carousel]').forEach((shell) => {
    const track = shell.querySelector('.case-carousel');
    const cards = [...track.querySelectorAll('.case-card')];
    const count = shell.querySelector('[data-carousel-count]');

    const setActive = (index) => {
      cards.forEach((card, cardIndex) => card.classList.toggle('is-active', cardIndex === index));
      if (count) count.textContent = `${String(index + 1).padStart(2, '0')} / ${String(cards.length).padStart(2, '0')}`;
    };

    const closestCard = () => {
      const left = track.getBoundingClientRect().left;
      let index = 0;
      let distance = Infinity;
      cards.forEach((card, cardIndex) => {
        const value = Math.abs(card.getBoundingClientRect().left - left);
        if (value < distance) {
          distance = value;
          index = cardIndex;
        }
      });
      return index;
    };

    let frame;
    track.addEventListener('scroll', () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => setActive(closestCard()));
    }, { passive: true });

    shell.querySelector('[data-carousel-prev]')?.addEventListener('click', () => {
      cards[Math.max(0, closestCard() - 1)]?.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
    });
    shell.querySelector('[data-carousel-next]')?.addEventListener('click', () => {
      cards[Math.min(cards.length - 1, closestCard() + 1)]?.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
    });
    setActive(0);
  });
})();
