/* THE 좋은식판 사이트 공통 스크립트 — 헤더 스크롤, 모바일 메뉴, 히어로 영상 */
(function () {
  'use strict';

  /* 헤더: 히어로 위에서는 투명, 스크롤하면 바탕색 */
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 24) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* B안: 데스크톱 고정 CTA는 첫 화면을 지나면 표시 (모바일은 항상) */
  var sticky = document.querySelector('.sticky-cta');
  function onStickyScroll() {
    if (!sticky) return;
    if (window.scrollY > 520) sticky.classList.add('show');
    else sticky.classList.remove('show');
  }
  window.addEventListener('scroll', onStickyScroll, { passive: true });
  onStickyScroll();

  /* 모바일 메뉴 */
  var toggle = document.getElementById('navToggle');
  var panel = document.getElementById('mnav');
  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      var open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? '메뉴 닫기' : '메뉴 열기');
      document.body.classList.toggle('menu-open', open);
    });
    function closeMenu() {
      panel.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', '메뉴 열기');
      document.body.classList.remove('menu-open');
    }
    panel.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeMenu); });
    /* ESC로 닫고 포커스를 토글 버튼으로 되돌린다 */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('open')) { closeMenu(); toggle.focus(); }
    });
  }

  /* 히어로 배경 영상: 모바일·데이터절약·움직임줄이기에서는 정지 이미지로 */
  var hero = document.getElementById('hero');
  var v = document.getElementById('bgv');
  if (!hero || !v) return;

  var isSmall = window.matchMedia('(max-width: 768px)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var conn = navigator.connection || {};
  var saveData = conn.saveData === true;
  var slow = /^(slow-2g|2g|3g)$/.test(conn.effectiveType || '');

  if (isSmall || reduce || saveData || slow) {
    v.removeAttribute('autoplay');
    v.removeAttribute('src');
    v.querySelectorAll('source').forEach(function (s) { s.remove(); });
    v.load();
    hero.classList.add('no-video');
    return;
  }

  var p = v.play();
  if (p && typeof p.catch === 'function') {
    p.catch(function () { hero.classList.add('no-video'); });
  }
  /* 영상 파일이 없거나 못 읽으면 포스터로 */
  v.addEventListener('error', function () { hero.classList.add('no-video'); }, true);

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { v.play().catch(function () {}); }
        else { v.pause(); }
      });
    }, { threshold: 0.1 }).observe(hero);
  }
})();
