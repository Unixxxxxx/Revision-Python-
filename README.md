<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🐍 Python Revision — README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;800&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0e14;
    --surface: #0f1620;
    --card: #131c2b;
    --border: #1e2d42;
    --accent: #00d4ff;
    --accent2: #7bed9f;
    --accent3: #ffd32a;
    --accent4: #ff6b9d;
    --text: #c9d8ef;
    --muted: #4a6080;
    --snake: #3ddc84;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    overflow-x: hidden;
    cursor: none;
  }

  /* Custom cursor */
  .cursor {
    width: 12px; height: 12px;
    background: var(--accent);
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 9999;
    transition: transform 0.15s ease;
    mix-blend-mode: screen;
  }
  .cursor-trail {
    width: 32px; height: 32px;
    border: 1.5px solid var(--accent);
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 9998;
    transition: all 0.25s ease;
    opacity: 0.4;
  }

  /* Grid bg */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: 0;
  }

  /* ---- HERO ---- */
  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 40px 20px;
    overflow: hidden;
    z-index: 1;
  }

  .snake-canvas {
    position: absolute;
    inset: 0;
    opacity: 0.18;
    z-index: 0;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: 1px solid var(--border);
    background: rgba(0,212,255,0.06);
    padding: 6px 16px;
    border-radius: 999px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--accent);
    letter-spacing: 0.08em;
    margin-bottom: 28px;
    animation: fadeDown 0.8s ease both;
  }
  .hero-badge span { animation: blink 1.2s step-end infinite; }

  .hero-title {
    font-size: clamp(52px, 10vw, 120px);
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #fff 0%, var(--accent) 50%, var(--snake) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeUp 0.9s ease both 0.2s;
    position: relative;
    z-index: 1;
  }

  .hero-subtitle {
    font-size: clamp(16px, 3vw, 22px);
    font-weight: 400;
    color: var(--muted);
    margin-top: 20px;
    max-width: 560px;
    line-height: 1.6;
    animation: fadeUp 0.9s ease both 0.4s;
    position: relative;
    z-index: 1;
  }

  .hero-buttons {
    display: flex;
    gap: 14px;
    margin-top: 36px;
    flex-wrap: wrap;
    justify-content: center;
    animation: fadeUp 0.9s ease both 0.6s;
    position: relative;
    z-index: 1;
  }

  .btn {
    padding: 12px 28px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    border: none;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .btn:hover { transform: translateY(-2px); }
  .btn-primary {
    background: var(--accent);
    color: var(--bg);
    box-shadow: 0 0 30px rgba(0,212,255,0.35);
  }
  .btn-primary:hover { box-shadow: 0 0 50px rgba(0,212,255,0.6); }
  .btn-outline {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
  }
  .btn-outline:hover { border-color: var(--accent); color: var(--accent); }

  /* stats row */
  .stats-row {
    display: flex;
    gap: 0;
    margin-top: 60px;
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    animation: fadeUp 1s ease both 0.8s;
    position: relative;
    z-index: 1;
    backdrop-filter: blur(6px);
    background: rgba(15,22,32,0.7);
  }
  .stat-item {
    padding: 20px 36px;
    text-align: center;
    border-right: 1px solid var(--border);
    flex: 1;
  }
  .stat-item:last-child { border-right: none; }
  .stat-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px;
    font-weight: 800;
    color: #fff;
  }
  .stat-label { font-size: 11px; color: var(--muted); margin-top: 4px; letter-spacing: 0.1em; text-transform: uppercase; }

  /* scroll indicator */
  .scroll-hint {
    position: absolute;
    bottom: 36px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    color: var(--muted);
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    animation: fadeIn 1.5s ease both 1.5s;
    z-index: 1;
  }
  .scroll-dot {
    width: 1px;
    height: 50px;
    background: linear-gradient(to bottom, var(--accent), transparent);
    animation: scrollLine 1.5s ease-in-out infinite;
  }

  /* ---- SECTIONS ---- */
  .section {
    max-width: 1100px;
    margin: 0 auto;
    padding: 100px 24px;
    position: relative;
    z-index: 1;
  }

  .section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 14px;
  }

  .section-title {
    font-size: clamp(32px, 5vw, 56px);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.02em;
    color: #fff;
    margin-bottom: 16px;
  }

  .section-desc {
    color: var(--muted);
    font-size: 16px;
    max-width: 560px;
    line-height: 1.7;
    margin-bottom: 60px;
  }

  /* Topic cards */
  .topics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }

  .topic-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, transform 0.3s;
    cursor: default;
  }
  .topic-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--card-accent, var(--accent));
    opacity: 0;
    transition: opacity 0.3s;
  }
  .topic-card:hover { border-color: var(--card-accent, var(--accent)); transform: translateY(-4px); }
  .topic-card:hover::before { opacity: 1; }

  .topic-icon {
    width: 48px; height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 20px;
    background: rgba(255,255,255,0.05);
  }
  .topic-title {
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 10px;
  }
  .topic-desc {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.6;
  }
  .topic-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 18px;
  }
  .tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 999px;
    background: rgba(0,212,255,0.08);
    color: var(--accent);
    border: 1px solid rgba(0,212,255,0.15);
  }

  /* CODE SNIPPET */
  .code-section {
    background: var(--surface);
    border-left: 4px solid var(--accent);
    border-radius: 0 16px 16px 0;
    overflow: hidden;
    margin: 60px 0;
  }
  .code-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    background: rgba(255,255,255,0.02);
  }
  .code-dots { display: flex; gap: 7px; }
  .code-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
  }
  .code-title { font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--muted); }
  pre {
    padding: 24px 28px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    line-height: 1.8;
    overflow-x: auto;
    color: var(--text);
  }
  .kw { color: var(--accent4); font-weight: 600; }
  .fn { color: var(--accent); }
  .str { color: var(--accent2); }
  .num { color: var(--accent3); }
  .cmt { color: var(--muted); font-style: italic; }
  .var { color: #e0b3ff; }

  /* LEARNING PATH */
  .path-steps {
    display: flex;
    flex-direction: column;
    gap: 0;
    position: relative;
  }
  .path-steps::before {
    content: '';
    position: absolute;
    left: 27px;
    top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, var(--accent), var(--snake), transparent);
    z-index: 0;
  }
  .path-step {
    display: flex;
    gap: 24px;
    align-items: flex-start;
    padding: 28px 0;
    position: relative;
    z-index: 1;
    opacity: 0;
    transform: translateX(-20px);
    transition: all 0.6s ease;
  }
  .path-step.visible { opacity: 1; transform: translateX(0); }
  .step-num {
    width: 56px; height: 56px;
    border-radius: 50%;
    background: var(--card);
    border: 2px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
    font-weight: 800;
    flex-shrink: 0;
    transition: border-color 0.3s;
    color: #fff;
  }
  .path-step:hover .step-num { border-color: var(--accent); color: var(--accent); }
  .step-content h3 { font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 8px; }
  .step-content p { font-size: 14px; color: var(--muted); line-height: 1.6; }
  .step-content code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    background: rgba(0,212,255,0.08);
    color: var(--accent);
    padding: 2px 8px;
    border-radius: 4px;
  }

  /* MISTAKES TABLE */
  .mistakes-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  @media(max-width: 700px) { .mistakes-grid { grid-template-columns: 1fr; } }
  .mistake-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    transition: border-color 0.3s;
  }
  .mistake-card:hover { border-color: var(--accent4); }
  .mistake-bad {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--accent4);
    background: rgba(255,107,157,0.08);
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }
  .mistake-good {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--accent2);
    background: rgba(123,237,159,0.08);
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }
  .mistake-label { font-size: 12px; font-weight: 700; margin-bottom: 6px; }
  .mistake-explain { font-size: 13px; color: var(--muted); line-height: 1.5; }

  /* DIVIDER */
  .divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 0 24px;
  }

  /* FOOTER */
  footer {
    text-align: center;
    padding: 60px 24px 80px;
    position: relative;
    z-index: 1;
  }
  .footer-logo {
    font-size: 48px;
    margin-bottom: 16px;
    animation: spin 8s linear infinite;
    display: inline-block;
  }
  .footer-text { color: var(--muted); font-size: 14px; line-height: 1.8; }
  .footer-text a { color: var(--accent); text-decoration: none; }

  /* GLOW BLOBS */
  .blob {
    position: fixed;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.06;
    pointer-events: none;
    z-index: 0;
  }
  .blob1 { width: 600px; height: 600px; background: var(--accent); top: -200px; left: -200px; }
  .blob2 { width: 400px; height: 400px; background: var(--snake); bottom: 10%; right: -100px; }

  /* ---- ANIMATIONS ---- */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; } to { opacity: 1; }
  }
  @keyframes blink {
    50% { opacity: 0; }
  }
  @keyframes scrollLine {
    0%   { transform: scaleY(0); transform-origin: top; }
    50%  { transform: scaleY(1); transform-origin: top; }
    51%  { transform: scaleY(1); transform-origin: bottom; }
    100% { transform: scaleY(0); transform-origin: bottom; }
  }
  @keyframes spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
  }
  @keyframes typewriter {
    from { width: 0; }
    to { width: 100%; }
  }
  @keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }

  .float { animation: float 3s ease-in-out infinite; }

  /* Typewriter text */
  .typewriter {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 2px solid var(--accent);
    animation: typewriter 2.5s steps(30) both 1s, blink 0.8s step-end infinite;
    max-width: 100%;
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(14px, 2vw, 18px);
    color: var(--accent);
    margin-top: 18px;
  }

  /* Highlight reel */
  .highlight-bar {
    display: inline-block;
    position: relative;
  }
  .highlight-bar::after {
    content: '';
    position: absolute;
    bottom: 2px; left: 0; right: 0;
    height: 8px;
    background: var(--accent);
    opacity: 0.2;
    border-radius: 4px;
    z-index: -1;
  }
</style>
</head>
<body>

<!-- Blobs -->
<div class="blob blob1"></div>
<div class="blob blob2"></div>

<!-- Custom cursor -->
<div class="cursor" id="cursor"></div>
<div class="cursor-trail" id="cursorTrail"></div>

<!-- ===== HERO ===== -->
<section class="hero">
  <canvas class="snake-canvas" id="snakeCanvas"></canvas>

  <div class="hero-badge">
    <span>●</span> Python 3 · Revision Notes · Open Source
  </div>

  <h1 class="hero-title">
    Revision<br>Python 🐍
  </h1>

  <p class="hero-subtitle">
    A clean, hands-on Python 3 learning repo covering variables, data types, and the most common beginner mistakes — built to level up your skills fast.
  </p>

  <div class="typewriter">$ python3 revision.py  # Let's begin!</div>

  <div class="hero-buttons">
    <a class="btn btn-primary" href="https://github.com/Unixxxxxx/Revision-Python-" target="_blank">⭐ View on GitHub</a>
    <a class="btn btn-outline" href="#topics">Explore Topics ↓</a>
  </div>

  <div class="stats-row">
    <div class="stat-item">
      <div class="stat-num">3</div>
      <div class="stat-label">Core Files</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">100%</div>
      <div class="stat-label">Python 3</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">∞</div>
      <div class="stat-label">Things to Learn</div>
    </div>
  </div>

  <div class="scroll-hint">
    <div class="scroll-dot"></div>
    scroll
  </div>
</section>

<div class="divider"></div>

<!-- ===== TOPICS ===== -->
<section class="section" id="topics">
  <div class="section-label">// What's inside</div>
  <h2 class="section-title">Core <span class="highlight-bar">Topics</span></h2>
  <p class="section-desc">Everything covered in this revision repo, explained clearly with examples and real code.</p>

  <div class="topics-grid">
    <div class="topic-card" style="--card-accent: #00d4ff;">
      <div class="topic-icon">📦</div>
      <div class="topic-title">Variables & Assignment</div>
      <div class="topic-desc">How Python stores data using dynamic typing. Learn how to name, assign, and reassign variables — including multiple assignment in one line.</div>
      <div class="topic-tags">
        <span class="tag">variables.py</span>
        <span class="tag">int</span>
        <span class="tag">str</span>
        <span class="tag">float</span>
        <span class="tag">bool</span>
      </div>
    </div>

    <div class="topic-card" style="--card-accent: #7bed9f;">
      <div class="topic-icon">🔢</div>
      <div class="topic-title">Data Types</div>
      <div class="topic-desc">Python's built-in types: integers, floats, strings, booleans, lists, tuples, dicts, and sets. Type checking with <code>type()</code> and conversion with <code>int()</code>, <code>str()</code>, etc.</div>
      <div class="topic-tags">
        <span class="tag" style="color: var(--accent2); border-color: rgba(123,237,159,0.3); background: rgba(123,237,159,0.08)">list</span>
        <span class="tag" style="color: var(--accent2); border-color: rgba(123,237,159,0.3); background: rgba(123,237,159,0.08)">dict</span>
        <span class="tag" style="color: var(--accent2); border-color: rgba(123,237,159,0.3); background: rgba(123,237,159,0.08)">tuple</span>
        <span class="tag" style="color: var(--accent2); border-color: rgba(123,237,159,0.3); background: rgba(123,237,159,0.08)">set</span>
      </div>
    </div>

    <div class="topic-card" style="--card-accent: #ffd32a;">
      <div class="topic-icon">⚠️</div>
      <div class="topic-title">Common Mistakes</div>
      <div class="topic-desc">The exact pitfalls that trip up every beginner: mixing types, using <code>=</code> vs <code>==</code>, mutable defaults, and off-by-one errors.</div>
      <div class="topic-tags">
        <span class="tag" style="color: var(--accent3); border-color: rgba(255,211,42,0.3); background: rgba(255,211,42,0.08)">v_common_mistakes.py</span>
        <span class="tag" style="color: var(--accent3); border-color: rgba(255,211,42,0.3); background: rgba(255,211,42,0.08)">bugs</span>
        <span class="tag" style="color: var(--accent3); border-color: rgba(255,211,42,0.3); background: rgba(255,211,42,0.08)">fixes</span>
      </div>
    </div>

    <div class="topic-card" style="--card-accent: #ff6b9d;">
      <div class="topic-icon">📝</div>
      <div class="topic-title">Python Notes</div>
      <div class="topic-desc">Quick-reference notes covering Python 3 syntax, best practices, indentation rules, and code style tips — perfect for rapid revision before a test or project.</div>
      <div class="topic-tags">
        <span class="tag" style="color: var(--accent4); border-color: rgba(255,107,157,0.3); background: rgba(255,107,157,0.08)">python.txt</span>
        <span class="tag" style="color: var(--accent4); border-color: rgba(255,107,157,0.3); background: rgba(255,107,157,0.08)">cheatsheet</span>
      </div>
    </div>
  </div>
</section>

<!-- ===== CODE SNIPPET ===== -->
<section class="section">
  <div class="section-label">// Sample code</div>
  <h2 class="section-title">See It In <span class="highlight-bar">Action</span></h2>

  <div class="code-section">
    <div class="code-header">
      <div class="code-dots">
        <div class="code-dot" style="background:#ff5f57"></div>
        <div class="code-dot" style="background:#febc2e"></div>
        <div class="code-dot" style="background:#28c840"></div>
      </div>
      <div class="code-title">variables.py</div>
      <div></div>
    </div>
    <pre><span class="cmt"># ── Python 3 Variable Revision ───────────────────────</span>

<span class="cmt"># Basic data types</span>
<span class="var">name</span>     = <span class="str">"Unixxxxxx"</span>        <span class="cmt"># str</span>
<span class="var">age</span>      = <span class="num">21</span>               <span class="cmt"># int</span>
<span class="var">height</span>   = <span class="num">5.9</span>              <span class="cmt"># float</span>
<span class="var">is_cool</span>  = <span class="kw">True</span>             <span class="cmt"># bool</span>

<span class="cmt"># Multiple assignment</span>
<span class="var">x</span>, <span class="var">y</span>, <span class="var">z</span> = <span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>

<span class="cmt"># Type checking</span>
<span class="fn">print</span>(<span class="fn">type</span>(<span class="var">name</span>))           <span class="cmt"># &lt;class 'str'&gt;</span>
<span class="fn">print</span>(<span class="fn">type</span>(<span class="var">age</span>))            <span class="cmt"># &lt;class 'int'&gt;</span>

<span class="cmt"># Type conversion</span>
<span class="var">age_str</span> = <span class="fn">str</span>(<span class="var">age</span>)          <span class="cmt"># "21"</span>
<span class="var">score</span>   = <span class="fn">int</span>(<span class="str">"42"</span>)         <span class="cmt"># 42</span>

<span class="cmt"># f-strings (Python 3.6+)</span>
<span class="fn">print</span>(<span class="str">f"Hello, </span><span class="var">{name}</span><span class="str">! You are </span><span class="var">{age}</span><span class="str"> years old."</span>)</pre>
  </div>

  <div class="code-section" style="border-left-color: var(--accent4);">
    <div class="code-header">
      <div class="code-dots">
        <div class="code-dot" style="background:#ff5f57"></div>
        <div class="code-dot" style="background:#febc2e"></div>
        <div class="code-dot" style="background:#28c840"></div>
      </div>
      <div class="code-title">v_common_mistakes.py</div>
      <div></div>
    </div>
    <pre><span class="cmt"># ── Common Beginner Mistakes ──────────────────────────</span>

<span class="cmt"># ❌ MISTAKE 1: = vs ==</span>
<span class="kw">if</span> <span class="var">x</span> == <span class="num">5</span>:           <span class="cmt"># ✅ comparison</span>
    <span class="fn">print</span>(<span class="str">"five!"</span>)
<span class="cmt"># if x = 5:          # ❌ SyntaxError!</span>

<span class="cmt"># ❌ MISTAKE 2: String + Number</span>
<span class="var">age</span> = <span class="num">20</span>
<span class="cmt"># print("Age: " + age)       ❌ TypeError</span>
<span class="fn">print</span>(<span class="str">"Age: "</span> + <span class="fn">str</span>(<span class="var">age</span>))   <span class="cmt"># ✅ cast first</span>

<span class="cmt"># ❌ MISTAKE 3: Mutable default argument</span>
<span class="kw">def</span> <span class="fn">add_item</span>(<span class="var">item</span>, <span class="var">lst</span>=<span class="kw">None</span>):
    <span class="kw">if</span> <span class="var">lst</span> <span class="kw">is</span> <span class="kw">None</span>:
        <span class="var">lst</span> = []        <span class="cmt"># ✅ safe default</span>
    <span class="var">lst</span>.<span class="fn">append</span>(<span class="var">item</span>)
    <span class="kw">return</span> <span class="var">lst</span>

<span class="cmt"># ❌ MISTAKE 4: Off-by-one in range</span>
<span class="kw">for</span> <span class="var">i</span> <span class="kw">in</span> <span class="fn">range</span>(<span class="num">1</span>, <span class="num">6</span>):  <span class="cmt"># ✅ prints 1,2,3,4,5</span>
    <span class="fn">print</span>(<span class="var">i</span>)</pre>
  </div>
</section>

<div class="divider"></div>

<!-- ===== LEARNING PATH ===== -->
<section class="section">
  <div class="section-label">// How to use this repo</div>
  <h2 class="section-title">Learning <span class="highlight-bar">Path</span></h2>
  <p class="section-desc">Follow these steps to get the most out of this revision repo.</p>

  <div class="path-steps">
    <div class="path-step">
      <div class="step-num">01</div>
      <div class="step-content">
        <h3>Clone the Repo</h3>
        <p>Start by cloning the repo to your local machine.<br><code>git clone https://github.com/Unixxxxxx/Revision-Python-.git</code></p>
      </div>
    </div>
    <div class="path-step">
      <div class="step-num">02</div>
      <div class="step-content">
        <h3>Read <code>python.txt</code></h3>
        <p>Open the notes file first. It gives you a quick mental map of all Python 3 concepts covered — ideal for warming up before diving into code.</p>
      </div>
    </div>
    <div class="path-step">
      <div class="step-num">03</div>
      <div class="step-content">
        <h3>Run <code>variables.py</code></h3>
        <p>Run the variables script and observe the output. Try changing values, adding new types, and printing them to reinforce your understanding of Python's type system.</p>
      </div>
    </div>
    <div class="path-step">
      <div class="step-num">04</div>
      <div class="step-content">
        <h3>Study <code>v_common_mistakes.py</code></h3>
        <p>Go through every mistake example. For each one, break the code intentionally, read the error, then fix it. This is the fastest way to learn Python error messages.</p>
      </div>
    </div>
    <div class="path-step">
      <div class="step-num">05</div>
      <div class="step-content">
        <h3>Extend & Experiment 🚀</h3>
        <p>Add your own examples, write new mistake patterns, or try converting the notes into interactive exercises. Make the repo yours!</p>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ===== COMMON MISTAKES ===== -->
<section class="section">
  <div class="section-label">// Quick reference</div>
  <h2 class="section-title">Mistakes <span class="highlight-bar">Cheatsheet</span></h2>
  <p class="section-desc">The most common Python beginner errors and how to fix them — at a glance.</p>

  <div class="mistakes-grid">
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">if x = 5:</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">if x == 5:</div>
      <div class="mistake-explain">= is assignment. == is comparison. Using = inside an if statement causes a SyntaxError.</div>
    </div>
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">"Age: " + 25</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">"Age: " + str(25)</div>
      <div class="mistake-explain">You can't concatenate a string and an integer directly. Convert with str() first.</div>
    </div>
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">def fn(lst=[]):</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">def fn(lst=None):</div>
      <div class="mistake-explain">Mutable default arguments are shared across all calls. Use None and create inside the function.</div>
    </div>
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">for i in range(5): # 1-5?</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">for i in range(1, 6):</div>
      <div class="mistake-explain">range(5) gives 0–4. Use range(1,6) to get 1–5. Always check start and stop values.</div>
    </div>
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">print(type = "hello")</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">print(type("hello"))</div>
      <div class="mistake-explain">type is a built-in function, not a keyword argument of print(). Don't shadow built-ins.</div>
    </div>
    <div class="mistake-card">
      <div class="mistake-label" style="color: var(--accent4)">❌ Wrong</div>
      <div class="mistake-bad">my_list[len(my_list)]</div>
      <div class="mistake-label" style="color: var(--accent2)">✅ Correct</div>
      <div class="mistake-good">my_list[-1]  # last item</div>
      <div class="mistake-explain">Lists are zero-indexed. The last valid index is len-1. Use -1 for the last element.</div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- FOOTER -->
<footer>
  <div class="footer-logo float">🐍</div>
  <div class="footer-text">
    Made with ❤️ by <a href="https://github.com/Unixxxxxx" target="_blank">Unixxxxxx</a><br>
    Python 3 Revision Repo · Open Source<br><br>
    <span style="color: var(--muted); font-size: 12px;">
      <a href="https://github.com/Unixxxxxx/Revision-Python-" target="_blank" style="color: var(--accent)">github.com/Unixxxxxx/Revision-Python-</a>
    </span>
  </div>
</footer>

<script>
  // ---- CUSTOM CURSOR ----
  const cursor = document.getElementById('cursor');
  const trail = document.getElementById('cursorTrail');
  document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX - 6 + 'px';
    cursor.style.top = e.clientY - 6 + 'px';
    setTimeout(() => {
      trail.style.left = e.clientX - 16 + 'px';
      trail.style.top = e.clientY - 16 + 'px';
    }, 80);
  });

  // ---- SNAKE BACKGROUND CANVAS ----
  const canvas = document.getElementById('snakeCanvas');
  const ctx = canvas.getContext('2d');
  function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  const snakes = Array.from({length: 5}, (_, i) => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    angle: Math.random() * Math.PI * 2,
    speed: 0.8 + Math.random() * 0.6,
    trail: [],
    hue: [180, 150, 200, 60, 330][i]
  }));

  function animateSnakes() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    snakes.forEach(s => {
      s.angle += (Math.random() - 0.5) * 0.15;
      s.x += Math.cos(s.angle) * s.speed;
      s.y += Math.sin(s.angle) * s.speed;
      if (s.x < 0) s.x = canvas.width;
      if (s.x > canvas.width) s.x = 0;
      if (s.y < 0) s.y = canvas.height;
      if (s.y > canvas.height) s.y = 0;
      s.trail.push({x: s.x, y: s.y});
      if (s.trail.length > 80) s.trail.shift();
      if (s.trail.length < 2) return;
      ctx.beginPath();
      ctx.moveTo(s.trail[0].x, s.trail[0].y);
      for (let j = 1; j < s.trail.length; j++) {
        ctx.lineTo(s.trail[j].x, s.trail[j].y);
      }
      ctx.strokeStyle = `hsla(${s.hue}, 80%, 60%, 0.6)`;
      ctx.lineWidth = 1.5;
      ctx.lineCap = 'round';
      ctx.stroke();
    });
    requestAnimationFrame(animateSnakes);
  }
  animateSnakes();

  // ---- SCROLL REVEAL ----
  const steps = document.querySelectorAll('.path-step');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 120);
      }
    });
  }, { threshold: 0.2 });
  steps.forEach(s => observer.observe(s));
</script>

</body>
</html>
