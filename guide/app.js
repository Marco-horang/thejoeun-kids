(() => {
  // 원본(thejoeun-kids-guide.luvyang1120.chatgpt.site)의 app.js에 한국어/영어 전환을 더한 버전.
  // 언어 결정 순서: 주소의 ?lang=en|ko > 이 브라우저에서 마지막으로 고른 언어 > 브라우저 언어(한국어가 아니면 영어)
  const UI = {
    ko: {
      skip:'본문 바로가기', homeAria:'더좋은 키즈 가이드 홈', wordmark:'더좋은<span>키즈</span><small>사용자 가이드</small>', topNav:'상단 메뉴',
      navGuide:'이용 안내', navFaq:'자주 묻는 질문', openApp:'더좋은 키즈 열기', openMenu:'가이드 메뉴 열기', sidebar:'가이드 목차', sideHead:'더좋은 키즈 가이드',
      closeMenu:'메뉴 닫기', searchLabel:'가이드 검색', searchPh:'궁금한 내용 검색', sideNav:'주제별 안내', grpStart:'시작하기', grpApply:'신청과 결제',
      grpManage:'이용 중 관리', grpHelp:'도움이 필요할 때', faqTitle:'자주 묻는 질문', contactQ:'신청·결제가 어려우신가요?', contactName:'더좋은식판 고객센터',
      topicOpen:'주제 선택', crumb:'사용자 가이드', shareAria:'현재 안내 링크 공유', share:'링크 공유', footQ:'찾으시는 안내가 없으신가요?',
      footCall:'고객센터 <strong>1668-5243</strong>', footBrand:'더좋은식판', footSlogan:'아이의 매일을 함께 준비합니다.', footDate:'안내 기준 · 2026년 11월',
      tocAria:'이 안내의 목차', tocHead:'이 안내에서', videoHead:'영상으로 따라 해요', videoSub:'신청 안내 영상 보기', dialogCloseAria:'화면 확대 닫기',
      dialogClose:'닫기 ×', pinch:'손가락으로 확대하여 확인하실 수 있어요.', screen:'안내 화면',
      pageTitle:'더좋은 키즈 사용자 가이드', titleSuffix:' | 더좋은 키즈', toggle:'EN', toggleAria:'Switch to English', toggleLang:'en',
      zoom:' 확대', tapZoom:'눌러서 크게 보기',
      descriptions:{apply:'아이 정보부터 신청 완료까지', payment:'승인 알림톡에서 계좌·카드 등록', pause:'잠시 이용을 쉬고 다시 시작하기', cancel:'종료일과 해지 신청 확인'},
      parent:'보호자', center:'기관', jApply:'서비스 신청', jApprove:'신청 확인·승인', jPay:'결제수단 등록', jSub:'각 항목을 누르면 자세한 방법을 볼 수 있어요.',
      mAccount:'계좌로 등록하기', mAccountText:'은행을 선택하고 계좌번호를 입력한 뒤 ‘결제정보 확인’을 눌러 주세요.',
      mCard:'카드로 등록하기', mCardText:'카드번호와 유효기간을 입력하고 다음 단계로 이동해 주세요.',
      faqEyebrow:'도움이 필요할 때', faqIntro:'신청과 이용 중 궁금한 내용을 먼저 확인해 보세요.', related:'관련 이용 방법 보기',
      faqToc:['신청·알림톡','결제 확인','일시정지·해지'],
      homeHead:'<div class="eyebrow">학부모님 가이드</div><h1>더좋은 키즈 이용 안내</h1><p class="intro">신청부터 이용 관리까지,<br class="mobile-break"> 필요한 안내를 한곳에서 확인하세요.</p><div class="overview-top"><p class="greeting">처음 이용하신다면</p><h2>아이의 식판 신청,<br>차근차근 함께해요.</h2><p>휴대폰에서 직접 신청하고,<br>승인 알림톡에서 결제수단을 등록해 주세요.</p>',
      homeApply:'신청 방법 알아보기', homeVideo:'안내 영상 보기',
      searchTitle:'검색 결과', searchFound:v=>`‘${v}’에 대한 안내를 찾았어요.`, searchCount:n=>`검색 결과 ${n}개`,
      searchEmpty:'일치하는 안내가 없어요. ‘신청’, ‘알림톡’, ‘카드’, ‘해지’처럼 짧은 단어로 다시 검색해 주세요.',
      copied:'안내 링크를 복사했어요.', copyFail:'주소창의 링크를 복사해 공유해 주세요.'
    },
    en: {
      skip:'Skip to content', homeAria:'Thejoeun Kids guide home', wordmark:'Thejoeun<span>Kids</span><small>User Guide</small>', topNav:'Top menu',
      navGuide:'Guide', navFaq:'FAQ', openApp:'Open app', openMenu:'Open guide menu', sidebar:'Guide contents', sideHead:'Thejoeun Kids Guide',
      closeMenu:'Close menu', searchLabel:'Search the guide', searchPh:'Search for help', sideNav:'Topics', grpStart:'Getting started', grpApply:'Application & payment',
      grpManage:'Managing your service', grpHelp:'Need help?', faqTitle:'FAQ', contactQ:'Need help applying or paying?', contactName:'Thejoeun Customer Center',
      topicOpen:'Topics', crumb:'User Guide', shareAria:'Share a link to this page', share:'Share link', footQ:'Can’t find what you’re looking for?',
      footCall:'Customer Center <strong>1668-5243</strong>', footBrand:'Thejoeun Kids', footSlogan:'Getting ready for your child’s every day, together.', footDate:'Updated November 2026',
      tocAria:'On this page', tocHead:'On this page', videoHead:'Follow along by video', videoSub:'Watch the how-to video (Korean)', dialogCloseAria:'Close enlarged screen',
      dialogClose:'Close ×', pinch:'Pinch with your fingers to zoom in.', screen:'Screen',
      pageTitle:'Thejoeun Kids User Guide', titleSuffix:' | Thejoeun Kids', toggle:'한국어', toggleAria:'한국어로 보기', toggleLang:'ko',
      zoom:' (enlarge)', tapZoom:'Tap to enlarge',
      descriptions:{apply:'From your child’s details to a completed application', payment:'Register an account or card from the approval message', pause:'Take a break and start again', cancel:'Request cancellation and check the end date'},
      parent:'Parent', center:'Center', jApply:'Apply for the service', jApprove:'Review & approval', jPay:'Register payment', jSub:'Tap each step to see how it works.',
      mAccount:'Register a bank account', mAccountText:'Select your bank, enter your account number, then tap “Confirm payment details” (결제정보 확인).',
      mCard:'Register a card', mCardText:'Enter your card number and expiry date, then go to the next step.',
      faqEyebrow:'Need help?', faqIntro:'Check here first for common questions about applying and using the service.', related:'See related instructions',
      faqToc:['Applying & messages','Payment','Pause & cancellation'],
      homeHead:'<div class="eyebrow">Parent guide</div><h1>Getting Started with Thejoeun Kids</h1><p class="intro">Everything you need, from applying to managing your service, in one place.</p><div class="overview-top"><p class="greeting">New to the service?</p><h2>Applying for your child’s meal tray, one step at a time.</h2><p>Apply on your phone, then register a payment method from the approval message on KakaoTalk.</p>',
      homeApply:'How to apply', homeVideo:'Watch the video (Korean)',
      searchTitle:'Search results', searchFound:v=>`Results for “${v}”.`, searchCount:n=>`${n} result${n===1?'':'s'}`,
      searchEmpty:'No matching help found. Try a short word such as “apply”, “Kakao”, “card” or “cancel”.',
      copied:'Link copied.', copyFail:'Please copy the link from the address bar to share it.'
    }
  };
  const content = document.getElementById('content');
  const search = document.getElementById('guide-search');
  const sidebar = document.getElementById('sidebar');
  const scrim = document.querySelector('.drawer-scrim');
  const menuButton = document.querySelector('.mobile-menu');
  const langButton = document.getElementById('lang-toggle');
  const videoUrl = 'https://youtu.be/tlE0K8xrHPY';
  let lang = pickLang();
  let t = UI[lang];
  let articles, questions;
  let route = 'home';
  let toastTimer;
  const escape = value => String(value).replace(/[&<>"']/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character]));
  function pickLang() {
    const param = new URLSearchParams(location.search).get('lang');
    if (param === 'en' || param === 'ko') return param;
    try { const saved = localStorage.getItem('guide-lang'); if (saved === 'en' || saved === 'ko') return saved; } catch {}
    return /^ko\b/i.test(navigator.language || 'ko') ? 'ko' : 'en';
  }
  function applyLanguage() {
    t = UI[lang];
    articles = lang === 'en' ? window.GUIDE_EN : window.GUIDE;
    questions = lang === 'en' ? window.FAQS_EN : window.FAQS;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach(node => { node.textContent = t[node.dataset.i18n]; });
    document.querySelectorAll('[data-i18n-html]').forEach(node => { node.innerHTML = t[node.dataset.i18nHtml]; });
    document.querySelectorAll('[data-i18n-aria]').forEach(node => node.setAttribute('aria-label', t[node.dataset.i18nAria]));
    document.querySelectorAll('[data-i18n-ph]').forEach(node => node.setAttribute('placeholder', t[node.dataset.i18nPh]));
    document.querySelectorAll('[data-title]').forEach(node => { node.textContent = articles[node.dataset.title].title; });
    langButton.textContent = t.toggle;
    langButton.setAttribute('aria-label', t.toggleAria);
    langButton.setAttribute('lang', t.toggleLang);
  }
  function setLanguage(next) {
    lang = next;
    try { localStorage.setItem('guide-lang', next); } catch {}
    const url = new URL(location.href);
    if (next === 'en') url.searchParams.set('lang', 'en'); else url.searchParams.delete('lang');
    history.replaceState(null, '', url.href);
    applyLanguage();
    search.value = '';
    routeFromHash();
  }
  function closeDrawer() {
    const wasOpen = sidebar.classList.contains('open');
    sidebar.classList.remove('open');
    scrim.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    if (wasOpen) menuButton.focus({preventScroll:true});
  }
  function openDrawer() {
    sidebar.classList.add('open');
    scrim.hidden = false;
    menuButton.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    document.querySelector('.drawer-close').focus();
  }
  function updateHeader(id, title) {
    document.title = title + t.titleSuffix;
    document.getElementById('crumb-current').textContent = title;
    document.getElementById('mobile-current').textContent = title;
    document.querySelectorAll('[data-guide]').forEach(link => {
      const active = link.dataset.guide === id;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current');
    });
  }
  function imageMarkup(section) {
    return `<figure class="screen-figure"><button class="screen-button" data-image="${section.image}" data-caption="${escape(section.caption)}" aria-label="${escape(section.caption + t.zoom)}"><img src="assets/${section.image}" alt="${escape(section.caption)}" loading="lazy" width="1920" height="1080"></button><figcaption><span>${escape(section.caption)}</span><span>${t.tapZoom}</span></figcaption></figure>`;
  }
  function sectionMarkup(section) {
    let html = `<section class="guide-section" id="${section.id}"><h2>${escape(section.title)}</h2>`;
    if (section.text) html += `<p>${escape(section.text)}</p>`;
    if (section.type === 'journey') html += `<div class="journey"><a href="#apply"><span class="step-circle">1</span><div><span class="who">${t.parent}</span><strong>${t.jApply}</strong></div></a><a href="#home/finish"><span class="step-circle">2</span><div><span class="who">${t.center}</span><strong>${t.jApprove}</strong></div></a><a href="#payment"><span class="step-circle">3</span><div><span class="who">${t.parent}</span><strong>${t.jPay}</strong></div></a></div><p class="section-sub">${t.jSub}</p>`;
    if (section.type === 'checklist') html += `<ul class="checklist">${section.items.map(item=>`<li>${escape(item)}</li>`).join('')}</ul>`;
    if (section.type === 'topics') html += `<div class="topic-list">${Object.entries(t.descriptions).map(([id,description])=>`<a class="topic-row" href="#${id}"><div><strong>${escape(articles[id].title)}</strong><small>${escape(description)}</small></div><span class="circle-plus" aria-hidden="true">+</span></a>`).join('')}</div>`;
    if (section.type === 'payment-methods') html += `<div class="method-grid"><div class="method"><strong>${t.mAccount}</strong><p>${escape(t.mAccountText)}</p></div><div class="method"><strong>${t.mCard}</strong><p>${escape(t.mCardText)}</p></div></div>`;
    if (section.steps) html += `<ol class="steps">${section.steps.map(([title,description],index)=>`<li><span class="step-circle" aria-hidden="true">${index+1}</span><div class="step-copy"><h3>${escape(title)}</h3><p>${escape(description)}</p></div></li>`).join('')}</ol>`;
    if (section.image) html += imageMarkup(section);
    if (section.note) html += `<div class="note">${escape(section.note)}</div>`;
    if (section.next) html += `<div class="next-article"><a href="#${section.next.id}">${escape(section.next.label)}</a></div>`;
    return html + '</section>';
  }
  function renderFaq() {
    updateHeader('faq', t.faqTitle);
    content.innerHTML = `<div class="eyebrow">${t.faqEyebrow}</div><h1>${t.faqTitle}</h1><p class="intro">${t.faqIntro}</p><div class="faq-list">${questions.map((item,index)=>`<details id="question-${index}"><summary>${escape(item.q)}</summary><div class="faq-answer">${escape(item.a)}<br><a href="#${item.related}">${t.related}</a></div></details>`).join('')}</div>`;
    document.getElementById('toc-list').innerHTML = `<a href="#question-0" data-faq-anchor="question-0">${t.faqToc[0]}</a><a href="#question-4" data-faq-anchor="question-4">${t.faqToc[1]}</a><a href="#question-7" data-faq-anchor="question-7">${t.faqToc[2]}</a>`;
  }
  function renderArticle(id, anchor) {
    route = id;
    if (id === 'faq') renderFaq();
    else {
      const article = articles[id];
      updateHeader(id, article.title);
      const titleBlock = id === 'home' ? `${t.homeHead}<div class="home-tools"><a class="button" href="#apply">${t.homeApply}</a><a class="button secondary" href="${videoUrl}" target="_blank" rel="noopener"><span aria-hidden="true">▶</span> ${t.homeVideo}</a></div></div>` : `<div class="eyebrow">${escape(article.group)}</div><h1>${escape(article.title)}</h1><p class="intro">${escape(article.intro)}</p>`;
      content.innerHTML = titleBlock + article.sections.map(sectionMarkup).join('');
      document.getElementById('toc-list').innerHTML = article.sections.map(section=>`<a href="#${id}/${section.id}">${escape(section.title)}</a>`).join('');
    }
    if (anchor) requestAnimationFrame(()=>document.getElementById(anchor)?.scrollIntoView({behavior:'auto'}));
    else window.scrollTo({top:0,behavior:'instant'});
  }
  function routeFromHash() {
    search.value='';
    const parts = location.hash.slice(1).split('/');
    let id;
    try { id = decodeURIComponent(parts[0] || 'home'); } catch { id = 'home'; }
    if (id.startsWith('question-')) {
      renderArticle('faq');
      requestAnimationFrame(()=>{const target=document.getElementById(id);if(target){target.open=true;target.scrollIntoView();}});
      return;
    }
    if (!(id in articles) && id !== 'faq') id='home';
    renderArticle(id, parts[1]);
    closeDrawer();
  }
  function searchGuide() {
    const value = search.value.trim();
    if (!value) { renderArticle(route); return; }
    const query = value.toLocaleLowerCase();
    const results = [];
    for (const [id,article] of Object.entries(articles)) {
      for (const section of article.sections) {
        const raw = [section.title,section.text,section.note,...(section.items||[]),...(section.steps||[]).flat()].filter(Boolean).join(' ');
        if (raw.toLocaleLowerCase().includes(query) || article.title.toLocaleLowerCase().includes(query)) results.push({title:section.title,description:raw.startsWith(section.title)?raw.slice(section.title.length).trim():raw,href:`#${id}/${section.id}`,category:article.title});
      }
    }
    questions.forEach((item,index)=>{if((item.q+item.a).toLocaleLowerCase().includes(query))results.push({title:item.q,description:item.a,href:`#question-${index}`,category:t.faqTitle});});
    updateHeader('', t.searchTitle);
    document.getElementById('toc-list').innerHTML='';
    content.innerHTML=`<div class="eyebrow">${t.searchLabel}</div><h1>${t.searchTitle}</h1><p class="intro">${t.searchFound(escape(value))}</p><div class="search-results"><p class="search-count" role="status">${t.searchCount(results.length)}</p>${results.length?results.map(result=>`<a class="search-result" href="${result.href}"><span class="section-sub">${escape(result.category)}</span><strong>${escape(result.title)}</strong><p>${escape(result.description.slice(0,150))}${result.description.length>150?'…':''}</p></a>`).join(''):`<div class="empty-search">${t.searchEmpty}</div>`}</div>`;
  }
  function toast(message) {
    clearTimeout(toastTimer);
    const element = document.getElementById('toast');
    element.textContent=message;element.classList.add('visible');
    toastTimer=setTimeout(()=>element.classList.remove('visible'),3000);
  }
  langButton.addEventListener('click',()=>setLanguage(lang === 'en' ? 'ko' : 'en'));
  menuButton.addEventListener('click',openDrawer);
  document.getElementById('topic-open').addEventListener('click',openDrawer);
  document.querySelector('.drawer-close').addEventListener('click',closeDrawer);
  scrim.addEventListener('click',closeDrawer);
  search.addEventListener('input',searchGuide);
  search.addEventListener('keydown',event=>{if(event.key==='Enter'&&search.value.trim()){event.preventDefault();closeDrawer();document.getElementById('main').focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});}});
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape')closeDrawer();
    if(event.key==='/'&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)){event.preventDefault();if(matchMedia('(max-width:800px)').matches)openDrawer();search.focus();}
    if(event.key==='Tab'&&sidebar.classList.contains('open')){
      const nodes=[...sidebar.querySelectorAll('button,input,a')].filter(node=>node.offsetParent!==null);
      if(event.shiftKey&&document.activeElement===nodes[0]){event.preventDefault();nodes.at(-1).focus();}
      else if(!event.shiftKey&&document.activeElement===nodes.at(-1)){event.preventDefault();nodes[0].focus();}
    }
  });
  document.addEventListener('click',event=>{
    const skip=event.target.closest('.skip');
    if(skip){event.preventDefault();document.getElementById('main').focus();return;}
    const screen=event.target.closest('[data-image]');
    if(screen){const image=document.getElementById('dialog-image');image.src='assets/'+screen.dataset.image;image.alt=screen.dataset.caption;document.getElementById('image-caption').textContent=screen.dataset.caption;document.getElementById('image-dialog').showModal();}
    const anchor=event.target.closest('[data-faq-anchor]');
    if(anchor){event.preventDefault();const target=document.getElementById(anchor.dataset.faqAnchor);target.open=true;target.scrollIntoView();}
    const internal=event.target.closest('a[href^="#"]');
    if(internal&&internal.getAttribute('href')===location.hash&&!anchor){event.preventDefault();routeFromHash();}
  });
  document.getElementById('dialog-close').addEventListener('click',()=>document.getElementById('image-dialog').close());
  document.getElementById('image-dialog').addEventListener('click',event=>{if(event.target===event.currentTarget)event.currentTarget.close();});
  document.getElementById('share').addEventListener('click',async()=>{
    const url=new URL(location.href);url.hash=location.hash || route;
    try{if(navigator.share&&matchMedia('(pointer:coarse)').matches){await navigator.share({title:document.title,url:url.href});return;}await navigator.clipboard.writeText(url.href);toast(t.copied);}
    catch(error){if(error.name!=='AbortError')toast(t.copyFail);}
  });
  window.addEventListener('hashchange',routeFromHash);
  window.addEventListener('resize',()=>{if(!matchMedia('(max-width:800px)').matches)closeDrawer();});
  applyLanguage();
  routeFromHash();
})();
