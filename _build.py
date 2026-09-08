# -*- coding: utf-8 -*-
"""
THE 좋은식판 유아 사이트 — 정적 HTML 생성기
실행:  python -X utf8 _build.py
결과:  같은 폴더에 index.html 등 6개 페이지 + sitemap.xml + robots.txt

헤더·푸터·메타태그를 한 곳에서 관리해 페이지 간 어긋남을 막는다.
문구를 고칠 때는 이 파일을 고치고 다시 실행한다 (HTML 직접 수정 금지).
"""
import os, datetime, json

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.xn--the-vq6no9oz5bx06a.com"   # www.the좋은식판.com (punycode)
TEL = "1668-5243"
TEL_HREF = "tel:16685243"
KAKAO = "https://pf.kakao.com/_xixgxkdT/chat"
EMAIL = "thejoeun_gm@naver.com"
FAX = "0504-273-5443"
ADDR = "경기도 광명시 일직로99번안길 20, 1층"
MAP = "https://map.naver.com/p/search/%EA%B4%91%EB%AA%85%EC%8B%9C%20%EC%9D%BC%EC%A7%81%EB%A1%9C99%EB%B2%88%EC%95%88%EA%B8%B8%2020"
# 오시는 길 = 본사 사무실(기업부설연구소 소재지, 회사정보 정본 2026-07-03 확인). 등기상 본사(광명)는 푸터·회사 페이지에 유지
OFFICE_ADDR = "경기도 화성시 동탄첨단산업1로 27, B동 1728호 (영천동)"
OFFICE_MAP = "https://map.naver.com/p/search/" + "%ED%99%94%EC%84%B1%EC%8B%9C%20%EB%8F%99%ED%83%84%EC%B2%A8%EB%8B%A8%EC%82%B0%EC%97%851%EB%A1%9C%2027"
APPLY_URL = ""   # 학부모 신청 웹앱 공개 주소가 확정되면 여기에 넣는다 (비어 있으면 '준비 중' 표시)
YEAR = "2026"

# ---------- 아이콘 ----------
I_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 4C7 4 3 7.2 3 11c0 2.4 1.6 4.5 4 5.7L6 21l4.3-2.4c.6.1 1.1.1 1.7.1 5 0 9-3.2 9-7s-4-7-9-7z"/></svg>'
I_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>'
I_LEAF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20c0-9 6-15 16-16-1 10-7 16-16 16z"/><path d="M4 20c4-5 8-8 12-10"/></svg>'
I_DROP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>'
I_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>'
I_CYCLE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.3-5.7"/><path d="M20 4v5h-5"/></svg>'

NAV = [
    ("service.html", "서비스"),
    ("report.html", "위생 리포트"),
    ("partnership.html", "교육기관 도입"),
    ("about.html", "회사"),
]

def header(active):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a class="item" href="{h}">{t}</a>' for h, t in NAV)
    return f'''
<header class="site-header" id="siteHeader">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="THE 좋은식판 홈">
      <img class="lg-color" src="assets/logo/logo-h.png" alt="THE 좋은식판 식기케어서비스" width="1200" height="421">
      <img class="lg-white" src="assets/logo/logo-h-white.png" alt="" width="1200" height="421">
    </a>
    <nav class="nav" aria-label="주 메뉴">{links}</nav>
    <div class="hd-cta">
      <a class="hd-tel" href="{TEL_HREF}">{TEL}</a>
      <a class="btn btn-fill btn-sm" href="contact.html">서비스 신청</a>
      <button class="nav-toggle" id="navToggle" aria-label="메뉴 열기" aria-expanded="false" aria-controls="mnav"><span></span></button>
    </div>
  </div>
</header>
<div class="mnav" id="mnav">
  <a class="item" href="index.html">홈</a>
  {mlinks}
  <a class="item" href="contact.html">신청·문의</a>
  <div class="mnav-cta">
    <a class="btn btn-fill btn-lg" href="contact.html">서비스 신청하기</a>
    <a class="btn btn-line btn-lg" href="{KAKAO}" target="_blank" rel="noopener">{I_CHAT}카카오톡 상담</a>
    <a class="btn btn-line btn-lg" href="{TEL_HREF}">{I_TEL}{TEL}</a>
  </div>
</div>'''

FOOTER = f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="ft-grid">
      <div class="ft-brand">
        <img src="assets/logo/logo-h-white.png" alt="THE 좋은식판" width="1200" height="421">
        <p>어린이집·유치원 식기를 매일 살균 세척해<br>진공 포장으로 배송하는 영유아 식기 케어 서비스입니다.</p>
      </div>
      <div>
        <h5>서비스</h5>
        <ul>
          <li><a href="service.html">서비스 소개</a></li>
          <li><a href="service.html#process">6단계 세척 공정</a></li>
          <li><a href="report.html">안심 위생 리포트</a></li>
        </ul>
      </div>
      <div>
        <h5>도입</h5>
        <ul>
          <li><a href="partnership.html">교육기관 도입 안내</a></li>
          <li><a href="partnership.html#area">서비스 지역</a></li>
          <li><a href="contact.html">신청·문의</a></li>
        </ul>
      </div>
      <div>
        <h5>연락처</h5>
        <ul>
          <li><a href="{TEL_HREF}">전화 {TEL}</a></li>
          <li>팩스 {FAX}</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>평일 09:00 – 18:00</li>
        </ul>
      </div>
    </div>
    <div class="ft-bot">
      <span>© {YEAR} 주식회사 더좋은. All rights reserved.</span>
      <span>대표 신동석 &nbsp;|&nbsp; 사업자등록번호 634-87-01123 &nbsp;|&nbsp; {ADDR}</span>
    </div>
  </div>
</footer>'''

LD_BUSINESS = json.dumps({
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "THE 좋은식판",
    "legalName": "주식회사 더좋은",
    "description": "어린이집·유치원 식기를 매일 살균 세척해 진공 포장으로 배송하는 영유아 식기 케어 서비스",
    "url": SITE + "/",
    "telephone": "+82-1668-5243",
    "email": EMAIL,
    "image": SITE + "/assets/img/kid.jpg",
    "address": {"@type": "PostalAddress", "streetAddress": "일직로99번안길 20, 1층", "addressLocality": "광명시",
                "addressRegion": "경기도", "addressCountry": "KR"},
    "openingHours": "Mo-Fr 09:00-18:00",
    "areaServed": ["광명시", "화성시", "인천광역시", "시흥시", "천안시"],
    "sameAs": [KAKAO],
}, ensure_ascii=False)

def shell(fname, title, desc, body, has_hero=False, extra_ld=None):
    canon = f"{SITE}/" if fname == "index.html" else f"{SITE}/{fname}"
    body_cls = ' class="has-hero"' if has_hero else ""
    ld = f'<script type="application/ld+json">{LD_BUSINESS}</script>'
    if extra_ld:
        ld += f'\n<script type="application/ld+json">{extra_ld}</script>'
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="THE 좋은식판">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/kid.jpg">
<meta name="theme-color" content="#00244C">
<link rel="icon" type="image/png" sizes="64x64" href="assets/logo/favicon-64.png">
<link rel="apple-touch-icon" href="assets/logo/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="assets/css/kids.css">
{ld}
</head>
<body{body_cls}>
<a class="sr-only" href="#main">본문 바로가기</a>
{header(fname)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="assets/js/kids.js"></script>
</body>
</html>
'''

# ---------- 공용 블록 ----------
STEPS = [
    ("01", "고온수 세척", "모든 세척과 헹굼을 80℃ 이상 고온수에서 진행합니다.", "80℃ 이상"),
    ("02", "수류 불림 세척", "수류 펌핑 세척기의 고온수에 불려 굳은 오염을 떼어냅니다.", "1차 불림 세척"),
    ("03", "초음파 버블 세척", "손이 닿지 않는 미세한 틈까지 초음파 버블로 씻어냅니다.", "미세 오염 제거"),
    ("04", "고온·고압 헹굼", "대형 세척기에서 3차에 걸친 고온 고압 헹굼을 추가로 진행합니다.", "3차 헹굼"),
    ("05", "고온 살균 건조", "120℃ 이상 고온 건조로 식중독균까지 사멸시킵니다.", "120℃ 이상"),
    ("06", "위생 점검·진공 포장", "고온 살균과 전수 위생 점검을 마친 식기를 진공 포장해 당일 배송합니다.", "당일 배송"),
]

def steps_block():
    cards = "".join(
        f'<div class="step"><span class="no">{n}</span><h3>{t}</h3><p>{d}</p><span class="cond">{c}</span></div>'
        for n, t, d, c in STEPS)
    return f'<div class="steps">{cards}</div>'

SHEET = '''
<div class="sheet" aria-label="안심 위생 리포트 예시">
  <div class="sheet-top"><b>안심 위생 리포트</b><span>정기 위생검사 결과지 (예시)</span></div>
  <div class="sheet-row"><span>일반세균</span><b>기준 이내</b></div>
  <div class="sheet-row"><span>대장균군</span><b>불검출</b></div>
  <div class="sheet-row"><span>잔류세제</span><b>불검출</b></div>
  <div class="sheet-row"><span>ATP 표면오염도</span><span class="ok">적합</span></div>
  <p class="sheet-note">검사 항목과 결과는 실제 결과지를 기준으로 원에 전달됩니다.</p>
</div>'''

def cta_block(title, sub, primary=("우리 아이 식판 신청", "contact.html"), hint=True):
    hint_html = '<p class="cta-hint">키즈노트 스마트주문으로도 신청하실 수 있습니다.</p>' if hint else ""
    return f'''
<section class="band-white" id="cta">
  <div class="wrap cta-grid">
    <div>
      <h2>{title}</h2>
      <p class="lead mt-16">{sub}</p>
      <div class="cta-btns">
        <a class="btn btn-fill btn-lg" href="{primary[1]}">{primary[0]}</a>
        <a class="btn btn-line btn-lg" href="{KAKAO}" target="_blank" rel="noopener">{I_CHAT}카카오톡 상담</a>
        <a class="btn btn-line btn-lg" href="{TEL_HREF}">{I_TEL}{TEL}</a>
      </div>
      {hint_html}
    </div>
    <div class="cta-photo"><img src="assets/img/kid.jpg" alt="진공 포장된 THE 좋은식판 식판을 들고 웃는 아이" width="1400" height="788"></div>
  </div>
</section>'''

# ---------- 홈 ----------
HOME = f'''
<div class="hero" id="hero">
  <div class="hero-media">
    <video id="bgv" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-poster.jpg" aria-hidden="true" tabindex="-1">
      <source src="assets/hero.mp4" type="video/mp4">
    </video>
    <img class="fallback" src="assets/img/vacuum-pack.jpg" alt="" width="1400" height="788">
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-inner">
    <p class="kicker">어린이집·유치원 식판 살균 세척 · 진공 포장 배송</p>
    <h1>아이가 매일 쓰는 식판,<br>세제 한 방울도 남기지 않습니다.</h1>
    <p class="lead">어린이집 식판을 매일 가져와 80℃ 고온수부터 120℃ 살균 건조까지 6단계 살균 세척을 거친 뒤, 진공 포장해 원으로 다시 보내드립니다.</p>
    <div class="hero-btns on-dark">
      <a class="btn btn-fill btn-lg" href="contact.html">우리 아이 식판 신청</a>
      <a class="btn btn-line btn-lg" href="partnership.html">원 도입 상담</a>
    </div>
  </div>
  <div class="cycle" aria-label="하루의 순환">
    <div class="wrap">
      <div class="cycle-item"><div class="when">회수</div><b>사용한 식기를 원에서 가져옵니다</b><span>설거지도, 보관도 원에서 하실 일이 없습니다</span></div>
      <div class="cycle-item"><div class="when">세척</div><b>6단계 살균 세척 후 진공 포장</b><span>고온수 · 초음파 · 고압 헹굼 · 120℃ 건조</span></div>
      <div class="cycle-item"><div class="when">배송</div><b>매일 진공 포장 식기 배송</b><span>포장을 뜯어 바로 식탁에 올리면 됩니다</span></div>
    </div>
  </div>
</div>

<section id="who">
  <div class="wrap">
    <div class="sec-head">
      <h2>원이 도입을 정하면,<br>신청과 결제는 학부모님이 아이별로</h2>
      <p>어린이집·유치원이 THE 좋은식판을 도입하면, 학부모님이 우리 아이 몫을 신청하고 결제합니다. 세척 공정도, 위생검사도 같습니다.</p>
    </div>
    <div class="who-grid">
      <div class="who">
        <span class="tag">학부모님께</span>
        <h3>원이 도입한 뒤, 우리 아이 몫만 신청하고 결제해요</h3>
        <p>원에서 THE 좋은식판을 도입했다면 아이가 다니는 원을 검색해 신청하면 됩니다. 우리 아이 몫의 식기가 매일 진공 포장으로 원에 도착합니다.</p>
        <ul>
          <li>원 이름 검색 후 3분이면 신청 완료</li>
          <li>식판, 수저·포크, 간식기까지 한 세트</li>
          <li>키즈노트 스마트주문으로도 신청 가능</li>
          <li>아직 도입 전인 원이라면 선생님께 저희를 알려주세요</li>
        </ul>
        <a class="btn btn-fill" href="contact.html">우리 아이 식판 신청</a>
      </div>
      <div class="who">
        <span class="tag">선생님 · 원장님께</span>
        <h3>설거지와 소독, 보관 부담을 통째로 덜어드립니다</h3>
        <p>식기는 저희가 준비하고, 살균 세척과 진공 포장, 매일 배송까지 맡습니다. 도입을 정하시면 학부모님 안내와 개별 신청 접수까지 함께 합니다.</p>
        <ul>
          <li>급식 후 설거지·소독·건조 업무 해소</li>
          <li>정기 위생검사 결과지 제공</li>
          <li>광명 · 화성 · 인천·시흥 · 천안 서비스</li>
        </ul>
        <a class="btn btn-line" href="partnership.html">원 도입 상담</a>
      </div>
    </div>
  </div>
</section>

<section class="band-white" id="why">
  <div class="wrap problem-grid">
    <div>
      <h2>설거지가 끝나도<br>세제는 식판에 남습니다.</h2>
      <p class="lead mt-16">가정에서든 원에서든 손 설거지로는 세제를 완전히 씻어내기 어렵습니다. 아이는 그 식판으로 하루 세 번 밥을 먹습니다.</p>
      <p class="mt-16">THE 좋은식판은 세제에 기대지 않습니다. 80℃ 고온수, 초음파, 고압 헹굼, 120℃ 건조가 세제의 자리를 대신합니다.</p>
    </div>
    <div class="stat-card">
      <div class="num">2컵<small>한 해 동안</small></div>
      <p class="desc">아이 한 명이 1년간 삼키게 되는 세제의 양 (소주잔 50ml 기준)</p>
      <p class="src">출처: 충남대학교 환경공학과 서동일 교수 연구</p>
    </div>
  </div>
</section>

<section id="process">
  <div class="wrap">
    <div class="sec-head">
      <h2>6단계 살균 세척 공정</h2>
      <p>사람 손으로는 할 수 없는 온도와 압력으로, 눈에 보이지 않는 잔류물까지 걷어냅니다.</p>
    </div>
    {steps_block()}
  </div>
</section>

<section class="band-sky" id="report">
  <div class="wrap report-grid">
    {SHEET}
    <div>
      <h2>말이 아니라<br>검사지로 증명합니다.</h2>
      <p class="lead mt-16">교육·보육기관 안전 기준에 맞춘 정기 위생검사를 시행하고, 그 결과를 원에 그대로 전달합니다. 학부모 문의에 원에서 결과지로 바로 답하실 수 있습니다.</p>
      <ul class="check">
        <li>정기 위생검사 결과지 제공</li>
        <li>교육·보육기관 안전 기준 적용</li>
        <li>검사 항목과 수치 그대로 공개</li>
      </ul>
      <a class="btn btn-line mt-32" href="report.html">위생 리포트 자세히 보기</a>
    </div>
  </div>
</section>

<section class="band-leaf" id="eco">
  <div class="wrap">
    <div class="sec-head">
      <h2>아이에게 좋은 방법이<br>지구에도 좋아야 합니다.</h2>
      <p>일회용을 쓰지 않고, 세제에 기대지 않고, 환경경영 기준으로 운영합니다.</p>
    </div>
    <div class="eco-grid">
      <div class="eco"><div class="ic">{I_CYCLE}</div><h3>다시 쓰는 식판</h3><p>일회용 식기를 쓰지 않습니다. 스테인리스 식판을 살균 세척해 매일 다시 씁니다.</p><p class="fact">일회용 쓰레기 0</p></div>
      <div class="eco"><div class="ic">{I_DROP}</div><h3>세제 대신 물과 온도</h3><p>고온수와 초음파, 고압 헹굼이 세제의 역할을 대신합니다. 아이 몸에도, 물에도 부담을 줄입니다.</p><p class="fact">80℃ 고온수 · 초음파 세척</p></div>
      <div class="eco"><div class="ic">{I_LEAF}</div><h3>환경경영 인증 사업장</h3><p>식기 케어 서비스 전 과정이 ISO 14001 환경경영시스템 인증을 받았습니다. 세척 상황을 분석해 분사량을 제어하는 AI 식기세척 장치 특허도 2건 등록했습니다.</p><p class="fact">ISO 14001 · 특허 2건</p></div>
    </div>
  </div>
</section>

{cta_block("우리 아이 식판부터 바꿔주세요", "신청은 3분이면 충분합니다. 궁금한 점은 카카오톡으로 편하게 물어보세요.")}
'''

# ---------- 서비스 ----------
SERVICE = f'''
<div class="page-head">
  <div class="wrap">
    <h1>매일 살균 세척을 마친 식기가<br>원으로 갑니다.</h1>
    <p class="lead">회수부터 세척, 포장, 배송까지 식기 관리의 전 과정을 THE 좋은식판이 맡습니다. 원에서는 포장을 뜯어 식탁에 올리기만 하면 됩니다.</p>
    <div class="page-photo mt-48"><img src="assets/img/hero-still.jpg" alt="세척기 랙에 정렬된 스테인리스 유아 식판" width="1600" height="900"></div>
  </div>
</div>

<section class="band-white" id="cycle">
  <div class="wrap">
    <div class="sec-head">
      <h2>하루의 순환</h2>
      <p>식기는 원과 세척 공장 사이를 매일 오갑니다. 원에 남는 일은 없습니다.</p>
    </div>
    <div class="how">
      <div class="how-item"><span class="k">1. 회수</span><h3>사용한 식기를 원에서 가져옵니다</h3><p>급식 후 남은 식기는 전용 박스에 담아 두시면 됩니다. 설거지도, 헹굼도, 보관도 필요 없습니다.</p></div>
      <div class="how-item"><span class="k">2. 세척 · 포장</span><h3>6단계 살균 세척 후 진공 포장</h3><p>80℃ 고온수 세척부터 120℃ 살균 건조까지 거친 뒤 전수 위생 점검을 하고 진공 포장합니다.</p></div>
      <div class="how-item"><span class="k">3. 배송</span><h3>매일 진공 포장 식기 배송</h3><p>진공 포장된 식기가 매일 원에 도착합니다. 포장을 뜯는 순간까지 살균 상태가 유지됩니다.</p></div>
    </div>
  </div>
</section>

<section id="process">
  <div class="wrap">
    <div class="sec-head">
      <h2>6단계 살균 세척 공정</h2>
      <p>사람 손으로는 할 수 없는 온도와 압력으로, 눈에 보이지 않는 잔류물까지 걷어냅니다.</p>
    </div>
    {steps_block()}
  </div>
</section>

<section class="band-white" id="set">
  <div class="wrap">
    <div class="sec-head">
      <h2>아이 한 명에게 가는 한 세트</h2>
      <p>아이가 한 끼에 쓰는 식기를 한 세트로 묶어 진공 포장합니다.</p>
    </div>
    <div class="set-grid">
      <div class="photo"><img src="assets/img/vacuum-pack.jpg" alt="THE 좋은식판 로고가 보이는 진공 포장 식판" width="1400" height="788" loading="lazy"></div>
      <div class="items">
        <div class="step"><h3>식판</h3><p>스테인리스 유아용 식판입니다. 코팅이 벗겨질 걱정 없이 고온 살균이 가능합니다.</p></div>
        <div class="step"><h3>수저 · 포크</h3><p>아이 손에 맞는 크기의 수저와 포크를 식판과 함께 포장합니다.</p></div>
        <div class="step"><h3>간식기</h3><p>오전·오후 간식 시간에 쓰는 간식기까지 같은 기준으로 세척합니다.</p></div>
      </div>
    </div>
    <p class="mt-24" style="font-size:15px;color:var(--ink-3)">식기 구성은 원의 급식 방식에 맞춰 조정할 수 있습니다. 도입 상담 때 말씀해 주세요.</p>
  </div>
</section>

<section id="vs">
  <div class="wrap">
    <div class="sec-head">
      <h2>가정에서 쓰는 개인 식판과<br>무엇이 다른가요</h2>
      <p>같은 스테인리스 식판이라도 씻는 온도와 방법, 그리고 확인하는 방식이 다릅니다.</p>
    </div>
    <div class="vs">
      <div class="vs-row head"><div>비교</div><div>가정 설거지</div><div>THE 좋은식판</div></div>
      <div class="vs-row"><div>세척 온도</div><div>손이 견디는 온도의 물</div><div>80℃ 이상 고온수</div></div>
      <div class="vs-row"><div>세제와 헹굼</div><div>세제로 씻고 손으로 헹굼</div><div>초음파 버블 세척과 3차 고온 고압 헹굼</div></div>
      <div class="vs-row"><div>건조와 살균</div><div>자연 건조 또는 행주</div><div>120℃ 이상 고온 살균 건조</div></div>
      <div class="vs-row"><div>보관</div><div>가방이나 원 선반에 보관</div><div>진공 포장 상태로 매일 도착</div></div>
      <div class="vs-row"><div>확인 방법</div><div>눈으로 보는 것 외에 없음</div><div>정기 위생검사 결과지</div></div>
    </div>
  </div>
</section>

<section class="band-sky" id="report">
  <div class="wrap report-grid">
    {SHEET}
    <div>
      <h2>세척했다는 말 대신<br>검사 결과지를 드립니다.</h2>
      <p class="lead mt-16">정기 위생검사 결과를 원에 그대로 전달합니다.<br>학부모 문의에 결과지로 답하실 수 있습니다.</p>
      <a class="btn btn-line mt-32" href="report.html">안심 위생 리포트 보기</a>
    </div>
  </div>
</section>

{cta_block("도입 상담부터 시작해 보세요", "원 규모와 급식 방식을 알려주시면 맞는 구성으로 안내해 드립니다.")}
'''

# ---------- 위생 리포트 ----------
REPORT = f'''
<div class="page-head">
  <div class="wrap">
    <h1>말이 아니라 검사지로 증명합니다.</h1>
    <p class="lead">"깨끗하게 씻었습니다"라는 말은 누구나 할 수 있습니다. THE 좋은식판은 교육·보육기관 안전 기준에 맞춘 정기 위생검사를 시행하고, 검사 항목과 수치를 그대로 원에 전달합니다.</p>
    <div class="page-photo mt-48"><img src="assets/img/atp-test.jpg" alt="세척을 마친 식판 표면의 ATP 오염도를 측정하는 모습" width="1400" height="788"></div>
  </div>
</div>

<section class="band-white">
  <div class="wrap report-grid">
    {SHEET}
    <div>
      <h2>선생님과 원장님께 드리는<br>가장 확실한 답</h2>
      <p class="lead mt-16">"식판은 어떻게 관리하세요?"라는 학부모 질문에 결과지 한 장으로 답하실 수 있습니다. 원 게시판이나 학부모 알림에 그대로 공유하셔도 됩니다.</p>
      <ul class="check">
        <li>정기 위생검사 시행 후 결과지 전달</li>
        <li>교육·보육기관 안전 기준 적용</li>
        <li>검사 항목과 수치 그대로 공개</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <h2>무엇을 검사하나요</h2>
      <p>식기 위생에서 학부모가 가장 걱정하는 네 가지를 봅니다.</p>
    </div>
    <div class="info-grid">
      <div class="info"><h3>일반세균</h3><p>세척 후 식기 표면에 남은 세균 수를 측정합니다. 고온 살균 건조가 제대로 됐는지 보여주는 기본 지표입니다.</p></div>
      <div class="info"><h3>대장균군</h3><p>분변 오염의 지표균입니다. 식중독 예방의 기준선이며, 불검출이 원칙입니다.</p></div>
      <div class="info"><h3>잔류세제</h3><p>헹굼이 끝난 뒤 식기에 남은 세제 성분을 확인합니다. 아이가 매일 삼키게 되는 양과 직결되는 항목입니다.</p></div>
      <div class="info"><h3>ATP 표면오염도</h3><p>눈에 보이지 않는 유기물 오염을 수치로 즉시 확인하는 검사입니다. 급식 현장 위생 점검에 널리 쓰입니다.</p></div>
    </div>
  </div>
</section>

{cta_block("결과지를 직접 보고 결정하세요", "도입 상담을 신청하시면 최근 위생검사 결과지를 함께 보내드립니다.", primary=("도입 상담 신청", "contact.html"), hint=False)}
'''

# ---------- 교육기관 도입 안내 (선생님·원장님) ----------
# 사장님 확정(2026-09-08): 업체 결정은 원(선생님·원장님), 결제는 학부모 개개인. 원의 도입 결정 없이 학부모 단독 신청은 불가.
# FAQ는 HTML과 검색엔진용 FAQPage 구조화 데이터 두 곳에 같이 쓰인다
FAQ = [
    ("비용은 어떻게 되나요?",
     "원아 수와 식기 구성, 배송 지역에 따라 달라집니다. 이용료는 원에서 도입을 정한 뒤 학부모님이 아이별로 신청·결제하며, 상담 때 원 규모를 알려주시면 월 기준으로 안내해 드립니다."),
    ("학부모가 개별로 신청할 수도 있나요?",
     "원에서 THE 좋은식판 도입을 결정한 뒤에는 학부모님께서 아이 한 명 몫을 개별로 신청하고 결제하실 수 있습니다. 원의 결정 없이 학부모님 단독으로 신청하실 수는 없으니, 아직 도입 전인 원이라면 먼저 선생님께 도입을 요청해 주세요. 도입된 원에서는 키즈노트 스마트주문으로도 신청하실 수 있습니다."),
    ("학부모인데 우리 원에 도입을 요청하고 싶어요. 어떻게 하나요?",
     "원 선생님이나 원장님께 THE 좋은식판을 알려주시고 저희 연락처(1668-5243, 카카오톡 채널)를 전달해 주세요. 원과 직접 상담해 도입을 도와드립니다."),
    ("식기는 누가 준비하나요?",
     "식판, 수저·포크, 간식기 모두 저희가 준비해 드립니다. 원에서 따로 구매하실 것은 없습니다."),
    ("우리 원 식기와 아이별 식기는 어떻게 구분하나요?",
     "원별로 구분해 포장하고 배송합니다. 반별·아이별 구분 방식은 원의 운영 방식에 맞춰 상담 때 함께 정합니다."),
    ("식판을 분실하거나 파손하면 어떻게 되나요?",
     "분실·파손 처리 기준은 도입 상담 때 안내해 드리고, 계약 전에 문서로 확인하실 수 있습니다."),
    ("언제부터 시작하고, 중단은 어떻게 하나요?",
     "시작일은 상담에서 원 일정에 맞춰 정합니다. 이용 기간과 중단 절차는 계약 전에 안내해 드립니다."),
    ("방학이나 휴원 기간에는 어떻게 되나요?",
     "방학 중 등원하는 아이 수에 맞춰 세트 수를 조정합니다. 일정을 미리 알려주시면 배송량을 함께 맞춥니다."),
    ("위생검사는 얼마나 자주 하나요?",
     "정기적으로 시행하며, 결과지는 검사 때마다 원에 전달합니다. 최근 결과지는 도입 상담 때 미리 보실 수 있습니다."),
]

def faq_html():
    return "".join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in FAQ)

LD_FAQ = json.dumps({
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ],
}, ensure_ascii=False)

PARTNER = f'''
<div class="page-head">
  <div class="wrap">
    <h1>선생님, 원장님,<br>식판 걱정은 저희가 맡겠습니다.</h1>
    <p class="lead">급식이 끝난 뒤 설거지, 소독, 건조, 보관까지. 매일 반복되는 식기 관리를 원 밖으로 내보내면 선생님들의 시간이 아이에게 돌아갑니다. 원이 도입을 정하면 이용료는 학부모님이 아이별로 신청·결제합니다.</p>
  </div>
</div>

<section class="band-white">
  <div class="wrap">
    <div class="sec-head">
      <h2>도입하면 달라지는 것</h2>
    </div>
    <div class="who-grid">
      <div class="who">
        <h3>식기 관리 업무가 원에서 사라집니다</h3>
        <p>식기는 저희가 준비합니다. 회수, 살균 세척, 진공 포장, 매일 배송까지 한 번에 맡습니다.</p>
        <ul>
          <li>급식 후 설거지·소독·건조 업무 해소</li>
          <li>식기 보관 공간과 소독기 관리 부담 해소</li>
          <li>아이 수가 바뀌면 세트 수만 조정</li>
        </ul>
      </div>
      <div class="who">
        <h3>학부모 신뢰의 근거가 생깁니다</h3>
        <p>정기 위생검사 결과지를 원에 전달합니다. 식판 위생을 묻는 학부모께 말이 아니라 검사지로 답하실 수 있습니다.</p>
        <ul>
          <li>정기 위생검사 결과지 제공</li>
          <li>6단계 살균 세척 공정 안내 자료 제공</li>
          <li>ISO 14001 환경경영 · ISO 45001 안전보건 인증 사업장</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="sec-head">
      <h2>도입 절차</h2>
      <p>상담에서 원 상황을 먼저 확인한 뒤, 첫 배송까지 보통 영업일 3일 정도가 걸립니다.</p>
    </div>
    <div class="precheck">
      <h3>도입 전에 함께 확인합니다</h3>
      <p>원마다 급식 방식과 공간이 달라, 아래 다섯 가지를 상담에서 먼저 맞춥니다.</p>
      <ul class="check">
        <li>원아 수와 반 구성</li>
        <li>급식·간식 시간과 배식 방식</li>
        <li>식기를 내놓고 받는 위치</li>
        <li>식기 보관 공간</li>
        <li>반별·아이별 구분 기준</li>
      </ul>
    </div>
    <div class="how">
      <div class="how-item"><span class="k">1. 상담</span><h3>원 규모와 급식 방식 확인</h3><p>원아 수, 급식·간식 시간, 식기 구성을 함께 정합니다. 전화나 카카오톡으로 시작하시면 됩니다.</p></div>
      <div class="how-item"><span class="k">2. 준비</span><h3>배송 일정과 식기 세트 준비</h3><p>배송 시간과 회수 방식을 원 일정에 맞춰 정하고, 아이 수만큼 식기 세트를 준비합니다.</p></div>
      <div class="how-item"><span class="k">3. 첫 배송</span><h3>매일 진공 포장 식기 도착</h3><p>첫날부터 진공 포장된 식기가 원에 도착합니다. 이후로는 매일 정해진 시간에 반복됩니다.</p></div>
    </div>
  </div>
</section>

<section class="band-white" id="faq">
  <div class="wrap-narrow">
    <div class="sec-head">
      <h2>자주 묻는 질문</h2>
    </div>
    <div class="faq">
      {faq_html()}
    </div>
  </div>
</section>

<section id="area">
  <div class="wrap">
    <div class="sec-head">
      <h2>서비스 지역</h2>
      <p>네 곳의 거점에서 매일 배송합니다. 인근 지역은 문의해 주세요.</p>
    </div>
    <div class="area-grid">
      <div class="area"><b>광명</b><p>본사 · 광명시와 인근 지역</p></div>
      <div class="area"><b>화성</b><p>화성 세척 공장 · 화성시와 인근 지역</p></div>
      <div class="area"><b>인천 · 시흥</b><p>인천점 · 인천시와 시흥시 인근 지역</p></div>
      <div class="area"><b>천안</b><p>천안점 · 천안시와 인근 지역</p></div>
    </div>
  </div>
</section>

{cta_block("도입 상담을 신청해 주세요", "원 규모만 알려주시면 하루 안에 구성과 일정을 안내해 드립니다.", primary=("도입 상담 신청", "contact.html"), hint=False)}
'''

# ---------- 회사 ----------
ABOUT = f'''
<div class="page-head">
  <div class="wrap">
    <h1>내 아이가 쓰는 식판을 관리한다는 마음으로</h1>
    <p class="lead">THE 좋은식판은 2019년 광명에서 시작한 영유아 식기 케어 서비스입니다. 아이들의 깨끗하고 건강한 식사 시간을 위해 식기 관리의 전 과정을 맡고 있습니다.</p>
  </div>
</div>

<section class="band-white">
  <div class="wrap prose">
    <h2>왜 시작했나</h2>
    <p class="mt-16">면역력이 낮은 아이들에게 식기 위생은 식단만큼 중요합니다. 그런데 원에서 매일 수십 장의 식판을 손으로 씻고 소독하는 일은 선생님들에게 큰 부담이고, 세제가 완전히 씻겼는지는 눈으로 확인할 수 없습니다.</p>
    <p>그래서 식기 관리를 원 밖으로 가져왔습니다. 전용 세척 공장에서 80℃ 고온수, 초음파, 고압 헹굼, 120℃ 살균 건조를 거쳐 진공 포장한 식기를 매일 원으로 배송합니다. 더 이상 아이들의 위생을 걱정하지 않는 세상이 저희의 목표입니다.</p>
    <h3>하는 일</h3>
    <p>어린이집과 유치원의 식판, 수저·포크, 간식기를 회수해 살균 세척하고 진공 포장해 배송합니다. 정기 위생검사를 시행해 결과지를 원에 전달하고, 세척 상황을 분석해 분사량을 제어하는 AI 식기세척 장치를 직접 연구·개발합니다.</p>
  </div>
</section>

<section id="cert">
  <div class="wrap">
    <div class="sec-head">
      <h2>인증과 특허</h2>
      <p>말이 아니라 인증서와 등록증으로 확인하실 수 있습니다.</p>
    </div>
    <div class="cert-list">
      <div class="cert"><span class="no">ISO 14001</span><div><b>환경경영시스템 인증</b><span>인증범위 식기케어 서비스 · GMS Certification Services · E250366</span></div></div>
      <div class="cert"><span class="no">ISO 45001</span><div><b>안전보건경영시스템 인증</b><span>인증범위 식기케어 서비스 · GMS Certification Services · OH250367</span></div></div>
      <div class="cert"><span class="no">특허</span><div><b>인공지능 분석에 따라 제어하는 식기세척 장치</b><span>특허청 등록 제10-2966388호 (2026-05-13)</span></div></div>
      <div class="cert"><span class="no">특허</span><div><b>운용 환경 변화에 따른 인공지능 식기 세척 장치</b><span>특허청 등록 제10-2984565호 (2026-06-26)</span></div></div>
      <div class="cert"><span class="no">이노비즈</span><div><b>기술혁신형 중소기업 (등급 A)</b><span>중소벤처기업부 · 제250602-01406호</span></div></div>
      <div class="cert"><span class="no">메인비즈</span><div><b>경영혁신형 중소기업</b><span>중소벤처기업부 · 제260602-02032호</span></div></div>
      <div class="cert"><span class="no">벤처기업</span><div><b>벤처기업확인 (혁신성장유형)</b><span>벤처기업협회 · 제20241127030011호</span></div></div>
      <div class="cert"><span class="no">연구소</span><div><b>기업부설연구소 인정</b><span>한국산업기술진흥협회 · 제2025113301호</span></div></div>
      <div class="cert"><span class="no">상표</span><div><b>THE 좋은식판 상표등록 2건</b><span>특허청 제40-2327195호 · 제40-2327196호</span></div></div>
    </div>
  </div>
</section>

<section class="band-white" id="branch">
  <div class="wrap">
    <div class="sec-head">
      <h2>거점</h2>
      <p>광명 본사와 화성 세척 공장, 인천·시흥과 천안의 지점에서 매일 배송합니다.</p>
    </div>
    <div class="area-grid">
      <div class="area"><b>광명 본사</b><p>경기도 광명시 일직로99번안길 20</p></div>
      <div class="area"><b>화성 공장</b><p>경기도 화성시 반월길 48-16</p></div>
      <div class="area"><b>인천 · 시흥점</b><p>인천시와 시흥시 인근 지역 서비스</p></div>
      <div class="area"><b>천안점</b><p>천안시와 인근 지역 서비스</p></div>
    </div>
  </div>
</section>

<section class="band-leaf">
  <div class="wrap prose">
    <h2>환경경영</h2>
    <p class="mt-16">일회용 식기를 쓰지 않는 것이 이 서비스의 출발점입니다. 여기에 더해 세척 전 과정을 ISO 14001 환경경영시스템 기준으로 운영하고, 물과 에너지를 상황에 맞게 쓰는 AI 식기세척 기술을 연구하고 있습니다. 아이에게 좋은 방법이 지구에도 좋아야 한다고 믿습니다.</p>
  </div>
</section>

{cta_block("궁금한 점은 편하게 물어보세요", "서비스, 도입, 제휴 어떤 문의든 하루 안에 답변드립니다.", primary=("신청 · 문의", "contact.html"), hint=False)}
'''

# ---------- 신청·문의 ----------
if APPLY_URL:
    APPLY_CARD = f'''<div class="info"><h3>온라인 신청</h3><p>원 이름을 검색하고 아이 정보를 입력하면 3분 안에 신청이 끝납니다.</p><a class="btn btn-fill" href="{APPLY_URL}">온라인 신청하기</a></div>'''
else:
    APPLY_CARD = '''<div class="info"><h3>온라인 신청</h3><p>원이 도입한 뒤 학부모님이 아이별로 신청하는 온라인 페이지를 준비하고 있습니다. 지금은 카카오톡이나 전화로 신청해 주시면 바로 접수해 드립니다.</p><p class="mt-8" style="font-size:14px;color:var(--ink-3)">키즈노트를 쓰는 원이라면 스마트주문에서도 신청하실 수 있습니다.</p></div>'''

CONTACT = f'''
<div class="page-head">
  <div class="wrap">
    <h1>신청과 문의, 편한 방법으로 하세요.</h1>
    <p class="lead">학부모님의 개별 신청도, 어린이집·유치원 선생님과 원장님의 도입 상담도 같은 창구에서 받습니다. 카카오톡이 가장 빠르고, 전화는 평일 09:00부터 18:00까지 연결됩니다.</p>
  </div>
</div>

<section class="band-white">
  <div class="wrap info-grid">
    <div class="info"><h3>카카오톡 상담</h3><p>가장 빠른 방법입니다. 신청, 도입 상담, 서비스 문의 모두 받습니다.</p><a class="btn btn-fill" href="{KAKAO}" target="_blank" rel="noopener">{I_CHAT}카카오톡으로 문의하기</a></div>
    <div class="info"><h3>전화</h3><div class="big"><a href="{TEL_HREF}">{TEL}</a></div><p>평일 09:00 – 18:00</p><a class="btn btn-line" href="{TEL_HREF}">{I_TEL}전화 걸기</a></div>
    {APPLY_CARD}
    <div class="info"><h3>이메일 · 팩스</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a><br>팩스 {FAX}</p><p class="mt-8" style="font-size:14px;color:var(--ink-3)">도입 제안서나 위생검사 결과지가 필요하시면 이메일로 요청해 주세요.</p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <h2>오시는 길</h2>
    </div>
    <div class="info-grid">
      <div class="info"><h3>본사 사무실</h3><p>{OFFICE_ADDR}</p><a class="btn btn-line btn-sm" href="{OFFICE_MAP}" target="_blank" rel="noopener">네이버 지도에서 보기</a></div>
      <div class="notice"><b>상담 전에 준비해 주시면 빠릅니다</b><br>원 이름과 지역, 대략의 원아 수, 급식·간식 시간.<br>이 세 가지면 하루 안에 구성과 일정을 안내해 드릴 수 있습니다.</div>
    </div>
  </div>
</section>
'''

PAGES = [
    ("index.html", "THE 좋은식판 | 어린이집·유치원 식기 살균 세척 · 진공 포장 배송",
     "아이가 매일 쓰는 식판, 세제 한 방울도 남기지 않습니다. 6단계 살균 세척을 거쳐 진공 포장한 식기를 매일 어린이집·유치원으로 배송하는 영유아 식기 케어 서비스.", HOME, True),
    ("service.html", "서비스 소개 | THE 좋은식판",
     "회수, 6단계 살균 세척, 진공 포장, 매일 배송까지. 어린이집·유치원 식기 관리의 전 과정을 THE 좋은식판이 맡습니다.", SERVICE, False),
    ("report.html", "안심 위생 리포트 | THE 좋은식판",
     "교육·보육기관 안전 기준에 맞춘 정기 위생검사 결과지를 원에 그대로 전달합니다. 일반세균, 대장균군, 잔류세제, ATP 표면오염도.", REPORT, False),
    ("partnership.html", "교육기관 도입 안내 | THE 좋은식판",
     "어린이집·유치원 선생님과 원장님을 위한 식기 케어 도입 안내. 설거지·소독·보관 부담 해소, 위생검사 결과지 제공, 도입 절차, 자주 묻는 질문과 서비스 지역.", PARTNER, False, LD_FAQ),
    ("about.html", "회사 소개 | THE 좋은식판",
     "2019년 광명에서 시작한 영유아 식기 케어 서비스. ISO 14001·45001 인증, AI 식기세척 장치 특허 2건, 이노비즈·메인비즈·벤처기업 확인.", ABOUT, False),
    ("contact.html", "신청 · 문의 | THE 좋은식판",
     "카카오톡 상담, 전화 1668-5243, 이메일로 서비스 신청과 도입 상담을 받습니다. 평일 09:00–18:00.", CONTACT, False),
]

def main():
    for fname, title, desc, body, has_hero, *rest in PAGES:
        html = shell(fname, title, desc, body, has_hero, rest[0] if rest else None)
        with open(os.path.join(HERE, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote", fname, len(html.encode("utf-8")), "bytes")

    today = datetime.date.today().isoformat()
    urls = "".join(
        f"  <url><loc>{SITE}/{'' if p[0]=='index.html' else p[0]}</loc><lastmod>{today}</lastmod></url>\n" for p in PAGES)
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(HERE, "CNAME"), "w", encoding="utf-8", newline="\n") as f:
        f.write("www.xn--the-vq6no9oz5bx06a.com\n")
    print("wrote sitemap.xml, robots.txt, CNAME")

if __name__ == "__main__":
    main()
