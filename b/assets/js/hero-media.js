/* B안 히어로 영상 칸 — 마우스를 올리면 화면 전체로 커지고, 떼면 제자리로 (FLIP 전환) */
(function () {
  'use strict';
  var hm = document.getElementById('hm');
  var box = document.getElementById('hmBox');
  var wrap = document.getElementById('heroPhoto');
  var vid = document.getElementById('heroVid');
  var closeBtn = document.getElementById('hmClose');
  if (!hm || !box || !wrap || !vid) return;

  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var busy = false;

  /* 데스크톱은 칸 안에서 음소거 자동재생, 모바일은 포스터만 (열면 재생) */
  if (canHover && !reduce) { vid.play().catch(function () {}); }

  function setRect(r) {
    hm.style.top = r.top + 'px'; hm.style.left = r.left + 'px';
    hm.style.width = r.width + 'px'; hm.style.height = r.height + 'px';
  }
  function open() {
    if (busy || hm.classList.contains('full')) return;
    busy = true;
    setRect(hm.getBoundingClientRect());
    hm.classList.add('fixed');
    wrap.classList.add('expanded');
    document.body.classList.add('hm-open');
    vid.play().catch(function () {});
    requestAnimationFrame(function () { requestAnimationFrame(function () {
      hm.classList.add('full');
      setTimeout(function () { busy = false; }, 480);
    }); });
  }
  function close() {
    if (busy || !hm.classList.contains('full')) return;
    busy = true;
    setRect(box.getBoundingClientRect());
    hm.classList.remove('full');
    setTimeout(function () {
      hm.classList.remove('fixed');
      hm.style.top = hm.style.left = hm.style.width = hm.style.height = '';
      wrap.classList.remove('expanded');
      document.body.classList.remove('hm-open');
      if (!canHover) vid.pause();
      busy = false;
    }, 480);
  }

  if (canHover) {
    hm.addEventListener('mouseenter', open);
    hm.addEventListener('mouseleave', close);
  } else {
    hm.addEventListener('click', function () { if (!hm.classList.contains('full')) open(); });
  }
  hm.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
  if (closeBtn) closeBtn.addEventListener('click', function (e) { e.stopPropagation(); close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  window.addEventListener('resize', function () { if (hm.classList.contains('full')) setRect({ top: 0, left: 0, width: innerWidth, height: innerHeight }); });
})();
