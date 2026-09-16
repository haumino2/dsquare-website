(() => {
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('#site-nav');
  const icon = toggle?.querySelector('img');
  const setMenu = (open, returnFocus = false) => {
    if (!toggle || !menu) return;
    menu.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (icon) icon.src = 'assets/images/mmv-icons/' + (open ? 'close' : 'menu') + '.svg';
    if (returnFocus) toggle.focus();
  };
  toggle?.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  menu?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') setMenu(false, true);
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.mmv-header')) setMenu(false);
  });
  matchMedia('(min-width: 921px)').addEventListener('change', () => setMenu(false));
  const links = [...document.querySelectorAll('.mmv-case-nav a')];
  const sections = links.map(link => document.querySelector(link.hash)).filter(Boolean);
  let queued = false;
  const updateChapter = () => {
    const cutoff = document.querySelector('.mmv-case-nav').offsetHeight + 100;
    let current = null;
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= cutoff) current = section.id;
    }
    links.forEach(link => {
      if (link.hash === '#' + current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    queued = false;
  };
  addEventListener('scroll', () => {
    if (!queued) { queued = true; requestAnimationFrame(updateChapter); }
  }, { passive: true });
  addEventListener('resize', updateChapter);
  updateChapter();
})();
