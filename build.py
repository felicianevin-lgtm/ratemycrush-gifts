"""Builds gifts.ratemycrush.com (static, GitHub Pages). Run: python -X utf8 build.py
TRUTH RULES (Autopilot README) apply to every word: verified book facts only; no prices, ratings, reviews,
delivery promises, lock/secure claims, or "bestseller". Other gift ideas are GENERIC categories (no brands, no claims).
AUDIENCE RULE: talk to the grown-up buyer only. Never ask about the child.
Design v2 (11/17/2026, Felicia: "next level", "dynamic", "make people want it"): pastel brand look, real covers and
interior pages, sample scorecard demo (labeled), edition picker, social links. Sample content is always labeled."""
import os, json, datetime as dt, html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://gifts.ratemycrush.com"
TODAY = dt.date.today().isoformat()
AMZ = {"playful": "https://www.amazon.com/dp/B0FR24YJ8W", "moody": "https://www.amazon.com/dp/B0FQPPSK1V",
       "floral": "https://www.amazon.com/dp/B0FQPK7S8Q"}
AUTHOR = "https://www.amazon.com/stores/Felicia-Nevin/author/B0GHFWPC6F"
INDEXNOW = "4f7c2a9e1b6d48e3a5c0f2d9e8b7a6c1"

# BLACK FRIDAY 2026 (brief 11/17): the sale banner + sale FAQ show ONLY when today is 2026-11-22..2026-11-30 AND
# Autopilot/sale_bf2026.json status.drop_live_verified is true (set by the daily task after it sees $9.99 on Amazon).
# Outside that window they disappear on the next build (the daily task rebuilds + pushes on 11/24 and 12/1).
def _sale():
    try:
        j = json.load(open(os.path.join(os.path.dirname(HERE), "Autopilot", "sale_bf2026.json"), encoding="utf-8"))
    except Exception:
        return None
    t = dt.date.today()
    if not (dt.date(2026, 11, 22) <= t <= dt.date(2026, 11, 30) and j.get("status", {}).get("drop_live_verified")): return None
    d = next((dt.date.fromisoformat(str(x.get("date"))[:10]) for x in j.get("log", []) if isinstance(x, dict) and x.get("date") and x.get("prices")), None)
    d = max(d or dt.date(2026, 11, 22), dt.date(2026, 11, 22))
    return d.strftime("%b %-d, %Y") if os.name != "nt" else d.strftime("%b %#d, %Y")
SALE_ASOF = _sale()
BF_SEASON = dt.date.today() <= dt.date(2026, 11, 30)
SALEBAR = (f'<div class="salebar">🎉 <b>Black Friday price drop:</b> all 3 paperback covers $9.99 on Amazon (as of {SALE_ASOF}, through Cyber Monday 11/30) '
           f'<a href="/rate-my-crush/#editions">Pick a cover →</a></div>') if SALE_ASOF else ""

# Verified edition facts (Amazon listings + KDP, 11/17/2026). No prices here on purpose.
EDITIONS = [
 dict(key="playful", name="Playful", vibe="Bright & sparkly", look="Glossy pastel cover with hearts and stars",
      best="For the glitter-pen kid", extra="Paperback · also in hardcover", color="#ff7eb6"),
 dict(key="moody", name="Moody", vibe="Dark & edgy", look="Matte cover, gothic lettering, low-key look",
      best="For the low-key, too-cool tween", extra="Paperback · matte finish", color="#2a2233"),
 dict(key="floral", name="Floral", vibe="Soft & floral", look="Matte navy cover with painted florals",
      best="For the keepsake lover", extra="Paperback · matte finish", color="#1d2b4f"),
]

SOCIAL = [
 ("Instagram", "https://www.instagram.com/ratemycrushbook/", "@ratemycrushbook",
  '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="currentColor"/>'),
 ("TikTok", "https://www.tiktok.com/@ratemycrushbook", "@ratemycrushbook",
  '<path d="M14 3v11.2a3.6 3.6 0 1 1-3.1-3.6V7.4A6.9 6.9 0 1 0 17.3 14V8.6a7.7 7.7 0 0 0 3.7 1V6.3A4.6 4.6 0 0 1 17.3 3z" fill="currentColor"/>'),
 ("YouTube", "https://www.youtube.com/@ratemycrushbook", "@ratemycrushbook",
  '<rect x="2" y="5" width="20" height="14" rx="4.5" fill="currentColor"/><path d="M10 9v6l5.2-3z" fill="#fff"/>'),
 ("Facebook", "https://www.facebook.com/profile.php?id=61596674310069", "Rate My Crush",
  '<path d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.9.3-1.5 1.5-1.5h1.6V4.3a21 21 0 0 0-2.3-.1c-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z" fill="currentColor"/>'),
 ("Threads", "https://www.threads.com/@ratemycrushbook", "@ratemycrushbook",
  '<path d="M16.6 11.3c-.1 0-.2-.1-.3-.1-.2-3-1.8-4.7-4.6-4.7-1.7 0-3.1.7-4 2l1.6 1.1c.6-1 1.6-1.2 2.4-1.2 1 0 1.7.3 2.2.8.3.4.6 1 .7 1.7a12 12 0 0 0-2.8-.1c-2.8.2-4.6 1.8-4.5 4.1.1 1.2.6 2.2 1.6 2.8.8.5 1.9.8 3 .7 1.4-.1 2.6-.6 3.4-1.6.6-.8 1-1.8 1.2-3 .7.4 1.1.9 1.4 1.6.5 1.1.5 2.9-1 4.4-1.3 1.3-2.9 1.9-5.3 1.9-2.7 0-4.7-.9-6-2.6C6.4 17.5 5.8 15.2 5.8 12.3s.6-5.2 1.8-6.8C8.9 3.8 10.9 3 13.6 3c2.7 0 4.8.9 6.1 2.6.7.8 1.2 1.9 1.5 3.1l1.9-.5c-.4-1.5-1-2.8-1.9-3.9C19.4 2.1 16.9 1 13.6 1h-.1C10.3 1 7.8 2.1 6.1 4.2 4.6 6.1 3.8 8.8 3.8 12.3s.8 6.1 2.3 8c1.7 2.1 4.2 3.2 7.5 3.2h.1c2.9 0 4.9-.8 6.6-2.5 2.2-2.2 2.1-4.9 1.4-6.6-.5-1.2-1.5-2.2-2.9-2.9zm-4.9 4.6c-1.2.1-2.4-.5-2.5-1.5 0-.8.6-1.6 2.4-1.7h.6c.7 0 1.3.1 1.9.2-.2 2.4-1.4 2.9-2.4 3z" fill="currentColor"/>'),
 ("Pinterest", "https://www.pinterest.com/thefelicianevin/", "Gift idea boards",
  '<path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 0-2.9l1.3-5.4s-.3-.7-.3-1.6c0-1.5.9-2.7 2-2.7.9 0 1.4.7 1.4 1.6 0 1-.6 2.4-.9 3.7-.3 1.1.6 2 1.7 2 2 0 3.5-2.1 3.5-5.2 0-2.7-2-4.6-4.8-4.6-3.3 0-5.2 2.5-5.2 5 0 1 .4 2.1.9 2.7.1.1.1.2.1.3l-.3 1.3c-.1.2-.2.3-.4.2-1.5-.7-2.4-2.8-2.4-4.6 0-3.7 2.7-7.2 7.9-7.2 4.1 0 7.3 3 7.3 6.9 0 4.1-2.6 7.4-6.2 7.4-1.2 0-2.4-.6-2.7-1.4l-.8 2.8c-.3 1-1 2.3-1.5 3.1A10 10 0 1 0 12 2z" fill="currentColor"/>'),
]

def icon(svg, size=22):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{svg}</svg>'

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&family=Caveat:wght@600;700&display=swap" rel="stylesheet">'

CSS = """
:root{--ink:#2b2d7c;--pink:#ff4d8d;--pink2:#ff86b3;--lilac:#b7a4ff;--sky:#8fd6ff;--butter:#ffd86b;--mint:#9be7c4;
--cream:#fffaf6;--blush:#fff0f6;--text:#2a2740;--muted:#625e7a;--line:#f1dbe7;--moody:#231d2e;--navy:#18244a;
--r:22px;--shadow:0 18px 40px -18px rgba(70,30,90,.35)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--text);font:17px/1.65 Nunito,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow-x:hidden}
a{color:var(--ink)}img{max-width:100%;height:auto;display:block}
h1,h2,h3,.logo,.btn,.tag{font-family:"Baloo 2",Nunito,sans-serif}
h1{font-size:clamp(34px,6vw,62px);line-height:1.02;color:var(--ink);margin:.15em 0 .3em;letter-spacing:-.5px}
h2{font-size:clamp(28px,4.4vw,44px);line-height:1.08;color:var(--ink);margin:0 0 .35em;letter-spacing:-.3px}
h3{font-size:22px;line-height:1.2;margin:.2em 0 .3em;color:var(--ink)}
p{margin:.5em 0 1em}
.hand{font-family:Caveat,cursive;font-weight:700;color:var(--pink);font-size:1.25em;line-height:1}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.narrow{max-width:780px;margin:0 auto;padding:0 20px}
section{padding:72px 0;position:relative}
.center{text-align:center}
.kicker{display:inline-flex;align-items:center;gap:8px;background:#fff;border:2px solid var(--line);color:var(--pink);font-weight:800;font-size:14px;padding:6px 14px;border-radius:999px;letter-spacing:.3px;text-transform:uppercase}
.lede{font-size:clamp(18px,2.2vw,21px);color:var(--muted);max-width:640px}
.center .lede{margin-left:auto;margin-right:auto}
/* header */
header.top{position:sticky;top:0;z-index:50;background:rgba(255,250,246,.82);backdrop-filter:saturate(1.4) blur(12px);-webkit-backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid rgba(241,219,231,.8)}
.bar{max-width:1120px;margin:0 auto;padding:10px 20px;display:flex;align-items:center;gap:18px}
.logo{display:flex;align-items:center;gap:8px;font-weight:800;color:var(--ink);text-decoration:none;font-size:23px;white-space:nowrap}
.logo .h{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:12px;background:linear-gradient(135deg,var(--pink),var(--lilac));color:#fff;font-size:18px;transform:rotate(-8deg)}
nav.main{display:flex;gap:4px;margin-left:auto;align-items:center}
nav.main a{text-decoration:none;font-weight:800;font-size:15px;color:var(--ink);padding:8px 12px;border-radius:999px}
nav.main a:hover{background:var(--blush)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--pink);color:#fff;text-decoration:none;font-weight:800;font-size:17px;padding:13px 24px;border-radius:999px;border:0;cursor:pointer;box-shadow:0 10px 22px -10px rgba(255,77,141,.8);transition:transform .2s,box-shadow .2s;line-height:1.1}
.btn:hover{transform:translateY(-2px) scale(1.02);box-shadow:0 16px 28px -12px rgba(255,77,141,.9)}
.btn.ink{background:var(--ink);box-shadow:0 10px 22px -10px rgba(43,45,124,.8)}
.btn.ghost{background:#fff;color:var(--ink);border:2px solid var(--ink);box-shadow:none}
.btn.sm{font-size:15px;padding:9px 16px}
nav.main .btn{color:#fff;padding:9px 16px}nav.main .btn:hover{background:var(--pink)}
/* hero */
.hero{padding:56px 0 80px;overflow:hidden;background:radial-gradient(1200px 500px at 85% 10%,#ffe0ef 0,transparent 60%),radial-gradient(900px 500px at 0% 90%,#e7e0ff 0,transparent 60%),linear-gradient(180deg,#fff5fa,#fffaf6)}
.hero .wrap{display:grid;grid-template-columns:1.05fr 1fr;gap:40px;align-items:center}
.hero h1 .pop{background:linear-gradient(90deg,var(--pink),#a774ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero .ctas{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0 18px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.chip{background:#fff;border:1.5px solid var(--line);border-radius:999px;padding:5px 12px;font-weight:700;font-size:14px;color:var(--muted)}
.stack{position:relative;height:500px}
.stack a{position:absolute;width:48%;top:50%;left:50%;border-radius:10px;transition:transform .45s cubic-bezier(.2,.8,.2,1),z-index 0s;box-shadow:0 30px 50px -20px rgba(40,10,60,.55)}
.stack img{border-radius:10px}
.stack a:nth-child(1){transform:translate(-118%,-50%) rotate(-12deg);z-index:1}
.stack a:nth-child(2){transform:translate(-50%,-56%) rotate(1deg);z-index:3}
.stack a:nth-child(3){transform:translate(18%,-50%) rotate(11deg);z-index:2}
.stack a:hover{z-index:5}
.stack a:nth-child(1):hover{transform:translate(-118%,-56%) rotate(-8deg) scale(1.04)}
.stack a:nth-child(2):hover{transform:translate(-50%,-62%) rotate(0) scale(1.04)}
.stack a:nth-child(3):hover{transform:translate(18%,-56%) rotate(7deg) scale(1.04)}
.stack .lbl{position:absolute;left:50%;bottom:-16px;transform:translateX(-50%);background:#fff;color:var(--ink);font:800 14px "Baloo 2";padding:4px 12px;border-radius:999px;box-shadow:var(--shadow);white-space:nowrap}
.float{position:absolute;pointer-events:none;font-size:28px;animation:bob 6s ease-in-out infinite;opacity:.9}
@keyframes bob{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-16px) rotate(8deg)}}
.sticker{position:absolute;z-index:6;right:4%;top:6%;width:118px;height:118px;border-radius:50%;background:var(--butter);color:var(--ink);display:grid;place-items:center;text-align:center;font:800 17px/1.05 "Baloo 2";transform:rotate(12deg);box-shadow:var(--shadow);border:3px dashed #fff;padding:10px}
/* marquee */
.ticker{background:var(--ink);color:#fff;overflow:hidden;padding:14px 0;transform:rotate(-1.2deg);margin:-14px -10px 0;position:relative;z-index:3}
.ticker .t{display:flex;gap:38px;width:max-content;animation:scroll 32s linear infinite;font:800 19px "Baloo 2";white-space:nowrap}
.ticker .t span::after{content:"✦";color:var(--pink2);margin-left:38px}
@keyframes scroll{to{transform:translateX(-50%)}}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:34px}
.step{background:#fff;border-radius:var(--r);padding:28px 24px;box-shadow:var(--shadow);position:relative;border:2px solid #fff}
.step .n{position:absolute;top:-18px;left:22px;width:44px;height:44px;border-radius:14px;display:grid;place-items:center;color:#fff;font:800 22px "Baloo 2";transform:rotate(-6deg)}
.step:nth-child(1) .n{background:var(--pink)}.step:nth-child(2) .n{background:#9b7bff}.step:nth-child(3) .n{background:#3fb7f0}
.step .e{font-size:38px;margin:6px 0 4px}
/* demo scorecard */
.demo{background:linear-gradient(160deg,#fff0f7,#efeaff);border-radius:34px;padding:48px 36px;display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:center}
.card-page{background:#fff;border-radius:18px;padding:24px 24px 20px;box-shadow:0 30px 60px -28px rgba(60,20,90,.45);position:relative;transform:rotate(-1.2deg)}
.card-page:before{content:"";position:absolute;inset:10px;border:2px dashed #f3d3e2;border-radius:12px;pointer-events:none}
.card-page .hd{font:800 22px "Baloo 2";color:var(--ink);display:flex;justify-content:space-between;align-items:baseline;gap:8px;position:relative}
.card-page .cn{font-family:Caveat,cursive;font-size:26px;color:var(--pink);position:relative}
.rows{margin:10px 0 6px;position:relative}
.row{display:grid;grid-template-columns:1fr auto;align-items:center;gap:10px;padding:3px 0;font-weight:700;font-size:15px;color:var(--muted)}
.stars{display:flex;gap:3px}
.stars i{width:20px;height:20px;display:block;background:#e9e3f3;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);transition:background .25s,transform .25s}
.stars i.on{background:var(--butter);transform:scale(1.12)}
.total{display:flex;justify-content:space-between;align-items:center;border-top:2px dashed var(--line);padding-top:10px;margin-top:6px;font:800 20px "Baloo 2";color:var(--ink);position:relative}
.meter{height:16px;border-radius:99px;background:#f0eaf7;overflow:hidden;margin-top:10px;position:relative}
.meter b{display:block;height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#ffd36b,#7fd38f,#6cb7ef,#a58be6);transition:width 1s cubic-bezier(.2,.8,.2,1)}
.level{margin-top:8px;font:800 22px "Baloo 2";color:var(--pink);min-height:30px;position:relative}
.sample{font-size:13px;color:var(--muted);font-style:italic;position:relative}
.levels{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:18px 0}
.lv{background:#fff;border-radius:14px;padding:10px 14px;font-weight:800;color:var(--ink);display:flex;gap:10px;align-items:center;font-size:15px}
.lv small{display:block;font-weight:700;color:var(--muted);font-size:13px}
/* editions */
.eds{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:36px}
.ed{border-radius:28px;padding:26px 22px 24px;text-align:center;color:#fff;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .3s}
.ed:hover{transform:translateY(-6px) rotate(-.5deg)}
.ed.playful{background:linear-gradient(160deg,#ff9ac6,#b9a2ff 60%,#8fd6ff)}
.ed.moody{background:linear-gradient(160deg,#3a2f48,#1b1622)}
.ed.floral{background:linear-gradient(160deg,#25386a,#14203f)}
.ed .cover{width:62%;margin:6px auto 18px;border-radius:8px;box-shadow:0 24px 40px -16px rgba(0,0,0,.6);transform:rotate(-3deg);transition:transform .35s}
.ed:hover .cover{transform:rotate(0) scale(1.04)}
.ed h3{color:#fff;font-size:30px;margin:0}
.ed .vibe{font:800 15px Nunito;text-transform:uppercase;letter-spacing:1.5px;opacity:.9}
.ed p{margin:.4em 0;opacity:.95;font-size:15.5px}
.ed .best{display:inline-block;background:rgba(255,255,255,.18);border-radius:999px;padding:4px 12px;font-weight:800;font-size:14px;margin:6px 0 14px}
.ed .btn{background:#fff;color:var(--ink);width:100%;box-shadow:none}
.ed .btn:hover{background:var(--butter)}
.same{margin-top:22px;text-align:center;color:var(--muted);font-weight:700}
/* gallery */
.tabs{display:inline-flex;background:#fff;border-radius:999px;padding:6px;gap:4px;box-shadow:var(--shadow);margin:20px 0 26px;flex-wrap:wrap;justify-content:center}
.tabs button{border:0;background:none;font:800 16px "Baloo 2";color:var(--ink);padding:9px 20px;border-radius:999px;cursor:pointer}
.tabs button[aria-selected=true]{background:var(--ink);color:#fff}
.pages{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}
.pages figure{margin:0;background:#fff;border-radius:18px;padding:10px;box-shadow:var(--shadow);cursor:zoom-in;transition:transform .3s}
.pages figure:hover{transform:translateY(-6px)}
.pages figure:nth-child(1){transform:rotate(-1.5deg)}.pages figure:nth-child(3){transform:rotate(1.5deg)}
.pages img{border-radius:10px}
.pages figcaption{font-weight:800;color:var(--ink);text-align:center;padding:10px 4px 4px;font-size:15px}
/* reasons */
.reasons{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:36px}
.rs{background:#fff;border-radius:var(--r);padding:24px 20px;border:2px solid var(--line);transition:transform .25s,border-color .25s}
.rs:hover{transform:translateY(-5px);border-color:var(--pink2)}
.rs .e{width:56px;height:56px;border-radius:18px;display:grid;place-items:center;font-size:28px;margin-bottom:10px}
.rs:nth-child(4n+1) .e{background:#ffe1ee}.rs:nth-child(4n+2) .e{background:#e9e2ff}.rs:nth-child(4n+3) .e{background:#dcf3ff}.rs:nth-child(4n+4) .e{background:#fff1c9}
.rs h3{font-size:20px}.rs p{font-size:15.5px;color:var(--muted);margin:0}
/* occasions */
.occ{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:26px}
.occ a,.occ span{display:inline-flex;gap:8px;align-items:center;background:#fff;border:2px solid var(--line);border-radius:999px;padding:10px 18px;font-weight:800;color:var(--ink);text-decoration:none;transition:all .2s}
.occ a:hover{background:var(--ink);color:#fff;border-color:var(--ink)}
/* author */
.author{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center;background:#fff;border-radius:30px;padding:34px;box-shadow:var(--shadow)}
.author .av{width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--lilac));display:grid;place-items:center;font-size:52px;transform:rotate(-6deg)}
/* social */
.social{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:30px}
.so{display:flex;flex-direction:column;align-items:center;gap:8px;background:#fff;border-radius:20px;padding:20px 10px;text-decoration:none;color:var(--ink);font-weight:800;border:2px solid var(--line);transition:transform .2s,background .2s,color .2s}
.so small{font-weight:700;color:var(--muted);font-size:12.5px}
.so:hover{transform:translateY(-5px) rotate(-2deg);background:var(--ink);color:#fff}.so:hover small{color:#dcd8ff}
.so .ic{width:48px;height:48px;border-radius:15px;display:grid;place-items:center;color:#fff}
/* faq + cards */
details{background:#fff;border:2px solid var(--line);border-radius:18px;padding:14px 20px;margin:12px 0;transition:border-color .2s}
details[open]{border-color:var(--pink2)}
summary{font:800 18px "Baloo 2";color:var(--ink);cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:12px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:26px;line-height:1;color:var(--pink);transition:transform .2s}
details[open] summary::after{transform:rotate(45deg)}
details p{color:var(--muted);margin:.6em 0 .2em}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;margin-top:26px}
.gcard{background:#fff;border-radius:22px;padding:22px;text-decoration:none;color:var(--text);border:2px solid var(--line);display:flex;flex-direction:column;gap:6px;transition:transform .25s,box-shadow .25s,border-color .25s}
.gcard:hover{transform:translateY(-6px);box-shadow:var(--shadow);border-color:#fff}
.gcard .e{font-size:34px}
.gcard b{font:800 20px/1.2 "Baloo 2";color:var(--ink)}
.gcard span{font-size:15px;color:var(--muted)}
.gcard em{font-style:normal;font-weight:800;color:var(--pink);margin-top:auto;font-size:15px}
/* CTA band */
.band{background:linear-gradient(120deg,var(--pink),#a774ff 55%,#56b7f2);color:#fff;border-radius:36px;padding:52px 30px;text-align:center;position:relative;overflow:hidden}
.band h2{color:#fff}.band p{opacity:.95;font-size:19px}
.band .row3{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:20px}
.band .btn{background:#fff;color:var(--ink);box-shadow:0 12px 24px -12px rgba(0,0,0,.4)}
.band .btn:hover{background:var(--butter)}
/* guide pages */
.ghero{padding:48px 0 40px;background:radial-gradient(900px 400px at 90% 0,#ffe0ef 0,transparent 60%),radial-gradient(700px 400px at 0 100%,#e7e0ff 0,transparent 60%),#fff7fb}
.crumb{font-size:14px;font-weight:700;color:var(--muted)}.crumb a{color:var(--muted)}
.pick{background:#fff;border-radius:28px;padding:26px;box-shadow:var(--shadow);display:grid;grid-template-columns:200px 1fr;gap:26px;align-items:center;margin:34px 0;border:3px solid var(--pink2);position:relative}
.pick .tag{position:absolute;top:-16px;left:24px;background:var(--pink);color:#fff;font-weight:800;padding:5px 16px;border-radius:999px;transform:rotate(-3deg)}
.pick .mini{display:flex;gap:8px;margin:10px 0 4px;flex-wrap:wrap}
.pick .mini a{display:flex;align-items:center;gap:8px;background:var(--blush);border-radius:999px;padding:5px 12px 5px 5px;text-decoration:none;font-weight:800;font-size:14px}
.pick .mini img{width:28px;border-radius:4px}
ol.ideas{list-style:none;padding:0;counter-reset:i;display:grid;gap:12px}
ol.ideas li{counter-increment:i;background:#fff;border-radius:18px;padding:16px 18px 16px 70px;position:relative;border:2px solid var(--line)}
ol.ideas li::before{content:counter(i);position:absolute;left:16px;top:14px;width:38px;height:38px;border-radius:12px;background:var(--blush);color:var(--pink);display:grid;place-items:center;font:800 19px "Baloo 2"}
ol.ideas li.star{border-color:var(--pink2);background:#fff7fb}
ol.ideas li.star::before{content:"♥";background:var(--pink);color:#fff}
.salebar{background:linear-gradient(90deg,#ff4f9a,#ff8a5c);color:#fff;text-align:center;font-weight:700;font-size:15px;padding:10px 14px;line-height:1.4}.salebar a{color:#fff;text-decoration:underline;margin-left:6px;white-space:nowrap}
.film{display:grid;grid-template-columns:minmax(0,360px) 1fr;gap:40px;align-items:center}.film .vid{position:relative;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(40,10,40,.55);background:#1c110a;aspect-ratio:9/16}.film video{width:100%;height:100%;object-fit:cover;display:block}.film .snd{position:absolute;left:50%;bottom:16px;transform:translateX(-50%);border:0;border-radius:999px;background:rgba(255,255,255,.92);color:#3b1d2e;font:800 15px Nunito,sans-serif;padding:10px 18px;cursor:pointer;white-space:nowrap}
@media (max-width:720px){.film{grid-template-columns:1fr}.film .vid{max-width:320px;margin:0 auto}}
.note{background:#fff7d6;border-radius:18px;padding:14px 18px;font-weight:700;color:#6b5a1d;margin:18px 0}
.art h2{font-size:clamp(26px,3.6vw,34px);margin-top:1.6em}
/* footer */
footer{background:var(--ink);color:#d9d6f5;padding:50px 0 90px;margin-top:40px;font-size:15px}
footer .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:30px}
footer a{color:#fff}footer h4{font:800 18px "Baloo 2";color:#fff;margin:0 0 8px}
footer .icons{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}
footer .icons a{width:42px;height:42px;border-radius:13px;background:rgba(255,255,255,.12);display:grid;place-items:center;transition:background .2s,transform .2s}
footer .icons a:hover{background:var(--pink);transform:translateY(-3px)}
footer ul{list-style:none;padding:0;margin:0}footer li{margin:5px 0}
footer .fine{border-top:1px solid rgba(255,255,255,.15);margin-top:30px;padding-top:18px;font-size:13.5px;color:#b9b5e0}
/* mobile buy bar */
.buybar{position:fixed;left:12px;right:12px;bottom:12px;z-index:60;display:none;background:var(--ink);color:#fff;border-radius:999px;padding:8px 8px 8px 20px;align-items:center;justify-content:space-between;gap:10px;box-shadow:0 16px 30px -10px rgba(20,10,60,.6);transform:translateY(120%);transition:transform .35s}
.buybar.show{transform:none}
.buybar b{font:800 16px "Baloo 2"}
/* lightbox */
.lb{position:fixed;inset:0;background:rgba(25,15,40,.85);display:none;place-items:center;z-index:100;padding:20px;cursor:zoom-out}
.lb.open{display:grid}.lb img{max-height:92vh;width:auto;border-radius:12px;box-shadow:0 30px 60px rgba(0,0,0,.5)}
/* reveal */
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.js .rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.js .rv{opacity:1;transform:none}.float,.ticker .t{animation:none}*{transition:none!important}}
.wavy{display:block;width:100%;height:40px}
main *{min-width:0}h1,h2,h3,p,li{overflow-wrap:break-word}
@media (max-width:960px){.hero .wrap{grid-template-columns:1fr}.stack{height:400px;max-width:520px;margin:0 auto;width:100%}.reasons{grid-template-columns:repeat(2,1fr)}.social{grid-template-columns:repeat(3,1fr)}.demo{grid-template-columns:1fr;padding:34px 20px}footer .cols{grid-template-columns:1fr 1fr}}
@media (max-width:720px){nav.main a:not(.btn){display:none}.eds,.steps,.pages{grid-template-columns:1fr}.eds{max-width:400px;margin-left:auto;margin-right:auto}.pages{max-width:380px;margin:0 auto}.pages figure:nth-child(n){transform:none}.steps{gap:34px}.pick{grid-template-columns:1fr}.pick>img{max-width:170px;margin:0 auto}.author{grid-template-columns:1fr;text-align:center}.author .av{margin:0 auto}.buybar{display:flex}section{padding:56px 0}.sticker{width:94px;height:94px;font-size:14px;right:0}.stack{height:340px}footer .cols{grid-template-columns:1fr}}
@media (max-width:420px){.reasons{grid-template-columns:1fr}.social{grid-template-columns:repeat(2,1fr)}.levels{grid-template-columns:1fr}.stars i{width:17px;height:17px}.stack{height:290px}.logo{font-size:20px}}
"""

JS = r"""
(()=>{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));setTimeout(()=>document.querySelectorAll('.rv').forEach(e=>e.classList.add('in')),6000);
// sample scorecard (fictional sample, filled in by us)
const card=document.querySelector('[data-demo]');
if(card){const rows=[...card.querySelectorAll('.stars')],tot=card.querySelector('[data-total]'),bar=card.querySelector('.meter b'),lv=card.querySelector('[data-level]'),cn=card.querySelector('[data-cn]');
const names=['Mr. Pancakes','Skater Boy #2','The Quiet One','Locker 214','Mystery Drummer','Captain Hoodie','Sir Laughs-a-Lot','Front Row Kid'];
const levels=[[15,'Tiny Crush 💛'],[30,'Pretty Cute 💚'],[40,'Big Crush 💙'],[50,'Totally Obsessed 💜']];
function deal(){const target=[12+Math.floor(Math.random()*38)][0];let v=rows.map(()=>1),left=target-rows.length;while(left>0){const i=Math.floor(Math.random()*rows.length);if(v[i]<5){v[i]++;left--}}
cn.textContent=names[Math.floor(Math.random()*names.length)];let sum=0;
rows.forEach((r,i)=>{[...r.children].forEach((s,j)=>{s.classList.remove('on');setTimeout(()=>s.classList.toggle('on',j<v[i]),80*i+40*j)})});
let n=0;const step=()=>{n=Math.min(target,n+1);tot.textContent=n;if(n<target)requestAnimationFrame(step)};setTimeout(step,200);
bar.style.width=(target/50*100)+'%';const L=levels.find(l=>target<=l[0]);setTimeout(()=>lv.textContent=L[1],900)}
const o=new IntersectionObserver(es=>{if(es[0].isIntersecting){deal();o.disconnect()}},{threshold:.35});o.observe(card);
document.querySelector('[data-shuffle]')?.addEventListener('click',deal)}
// edition tabs
document.querySelectorAll('[data-tabs] button').forEach(b=>b.addEventListener('click',()=>{const k=b.dataset.k;
b.parentNode.querySelectorAll('button').forEach(x=>x.setAttribute('aria-selected',x===b));
document.querySelectorAll('[data-page]').forEach(img=>{img.src='/img/page-'+k+'-'+img.dataset.page+'.jpg';img.alt='Rate My Crush '+k+' edition '+(img.dataset.page=='score'?'scorecard':'prompts')+' page'});
const c=document.querySelector('[data-cover-img]');if(c){c.src='/img/cover-'+k+'.jpg'}}));
// lightbox
const lb=document.createElement('div');lb.className='lb';lb.innerHTML='<img alt="">';document.body.appendChild(lb);
document.querySelectorAll('[data-zoom] img').forEach(i=>i.addEventListener('click',()=>{lb.firstChild.src=i.src;lb.firstChild.alt=i.alt;lb.classList.add('open')}));
lb.addEventListener('click',()=>lb.classList.remove('open'));addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('open')});
// count Amazon clicks (GoatCounter events; no cookies)
document.addEventListener('click',e=>{const a=e.target.closest('a[href*="amazon.com"]');if(!a||!window.goatcounter||!goatcounter.count)return;
const ed={'B0FR24YJ8W':'playful','B0FQPPSK1V':'moody','B0FQPK7S8Q':'floral'}[(a.href.match(/dp\/(\w+)/)||[])[1]]||'author';
goatcounter.count({path:'amazon-'+ed+location.pathname.replace(/\/$/,'').replace(/\//g,'-'),title:'Amazon click: '+ed,event:true})});
// mobile buy bar
const bb=document.querySelector('.buybar');if(bb){const f=()=>bb.classList.toggle('show',scrollY>500);addEventListener('scroll',f,{passive:true});f()}
})();
"""

def esc(s): return html.escape(s, quote=True)

def socials_footer():
    return "".join(f'<a href="{u}" aria-label="Rate My Crush on {n}" target="_blank" rel="noopener">{icon(svg,20)}</a>' for n, u, h, svg in SOCIAL)

SOCIAL_COLORS = {"Instagram": "linear-gradient(135deg,#feda75,#d62976 50%,#4f5bd5)", "TikTok": "#111", "YouTube": "#ff0033",
                 "Facebook": "#1877f2", "Threads": "#000", "Pinterest": "#e60023"}

def socials_grid():
    return '<div class="social">' + "".join(
        f'<a class="so rv" href="{u}" target="_blank" rel="noopener"><span class="ic" style="background:{SOCIAL_COLORS[n]}">{icon(svg,26)}</span>{n}<small>{esc(h)}</small></a>'
        for n, u, h, svg in SOCIAL) + "</div>"

SAME_AS = [u for n, u, h, sv in SOCIAL] + list(AMZ.values())
ORG = {"@context": "https://schema.org", "@type": "Brand", "@id": SITE + "/#brand", "name": "Rate My Crush", "url": SITE + "/rate-my-crush/",
       "logo": SITE + "/img/cover-playful.jpg", "description": "Rate My Crush is a guided crush journal for ages 7–14 by Felicia Nevin, sold on Amazon in Playful, Moody and Floral editions.",
       "sameAs": SAME_AS}
PERSON = {"@context": "https://schema.org", "@type": "Person", "@id": SITE + "/#felicia", "name": "Felicia Nevin", "jobTitle": "Author",
          "description": "Author of the Rate My Crush crush journal series, writing from East Tennessee.", "url": AUTHOR, "sameAs": [AUTHOR]}

def crumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

GC = '<script data-goatcounter="https://ratemycrush.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'

def page(path, title, desc, body, schema=None, buybar=True, og="og.jpg"):
    url = SITE + "/" + path.replace("index.html", "")
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    guides_links = "".join(f'<li><a href="/{g["slug"]}/">{esc(g["kw"])}</a></li>' for g in GUIDES)
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/img/{og}">
<meta property="og:site_name" content="Rate My Crush"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Rate My Crush crush journal: Playful, Moody and Floral covers"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}/img/{og}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1"><meta name="theme-color" content="#fff5fa"><meta name="p:domain_verify" content="2bf34be4f8d0c0ea909f29abf56b6f69">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%92%97%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.add('js')</script>{FONTS}<style>{CSS}</style>{ld}<script type="application/ld+json">{json.dumps([ORG, PERSON], ensure_ascii=False)}</script>{GC}</head><body>{SALEBAR}
<header class="top"><div class="bar"><a class="logo" href="/rate-my-crush/"><span class="h">♥</span>Rate My Crush</a>
<nav class="main"><a href="/rate-my-crush/#inside">Peek inside</a><a href="/rate-my-crush/#why">Why it works</a><a href="/">Gift guides</a><a class="btn sm" href="/rate-my-crush/#editions">Shop on Amazon</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="cols">
<div><a class="logo" href="/rate-my-crush/" style="color:#fff"><span class="h">♥</span>Rate My Crush</a>
<p>A guided crush journal for ages 7–14 by author Felicia Nevin. Three covers (Playful, Moody and Floral), same prompts inside, each styled to match its cover. Sold on Amazon.</p>
<div class="icons">{socials_footer()}</div></div>
<div><h4>The journal</h4><ul><li><a href="/rate-my-crush/#editions">Pick a cover</a></li><li><a href="/rate-my-crush/#inside">Peek inside</a></li><li><a href="/rate-my-crush/#faq">FAQ</a></li><li><a href="/sleepover-game/">Free sleepover game</a></li>
<li><a href="{AMZ['playful']}">Playful on Amazon</a></li><li><a href="{AMZ['moody']}">Moody on Amazon</a></li><li><a href="{AMZ['floral']}">Floral on Amazon</a></li><li><a href="{AUTHOR}">Author page on Amazon</a></li></ul></div>
<div><h4>Gift guides</h4><ul>{guides_links}</ul></div></div>
<p class="fine">Gift ideas on this site are general suggestions, not sponsored placements. Product details can change; check the Amazon listing for current details. Sample scorecards on this site are filled in by us for fun. Questions: <a href="mailto:hello@ratemycrush.com">hello@ratemycrush.com</a> · <a href="/sitemap.xml">Sitemap</a></p></div></footer>
{'<div class="buybar"><b>Rate My Crush ♥</b><a class="btn sm" href="/rate-my-crush/#editions">Pick a cover</a></div>' if buybar else ''}
<script>{JS}</script></body></html>"""
    out = os.path.join(HERE, path); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return url

def pick(angle):
    mini = "".join(f'<a href="{AMZ[e["key"]]}"><img src="/img/cover-{e["key"]}.jpg" alt="" loading="lazy">{e["name"]} on Amazon</a>' for e in EDITIONS)
    return f"""<div class="pick rv"><span class="tag">♥ Our pick</span><img src="/img/cover-playful.jpg" alt="Rate My Crush crush journal, Playful Edition cover" loading="lazy" style="border-radius:8px;box-shadow:0 20px 30px -14px rgba(0,0,0,.5);transform:rotate(-3deg)">
<div><h3 style="font-size:26px">Rate My Crush: the crush journal for ages 7–14</h3>
<p>{angle} Every crush gets a page with a code name, a 10-category star scorecard (Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades and Bonus Spark, 50 stars total), a Crush Level heart meter, and prompts like "Best Thing About Them." 100 pages, 6×9.</p>
<p style="margin-bottom:4px"><b>Three covers, same prompts inside, each styled to match:</b></p><div class="mini">{mini}</div>
<p style="margin:12px 0 0"><a class="btn sm ink" href="/rate-my-crush/">See inside the journal →</a></p></div></div>"""

def ideas(items):
    return '<ol class="ideas">' + "".join(f'<li class="{"star" if "crush journal" in t.lower() else ""}"><b>{esc(t)}.</b> {esc(d)}</li>' for t, d in items) + "</ol>"

def faq_block(qas):
    h = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in qas)
    s = {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    return h, s

GUIDE_EMOJI = {"gifts-for-10-year-old-girls": "🎂", "stocking-stuffers-for-tween-girls": "🧦", "gifts-for-niece": "💅",
               "valentines-gifts-for-girls": "💌", "screen-free-gifts-for-tween-girls": "📵", "gifts-for-granddaughter": "🧶",
               "sleepover-ideas-for-tween-girls": "🍕",
               "christmas-gifts-for-tween-girls": "🎄", "birthday-gifts-for-tween-girls": "🎈", "gifts-for-8-year-old-girls": "🧸",
               "gifts-for-9-year-old-girls": "🎨", "gifts-for-11-year-old-girls": "💖", "gifts-for-12-year-old-girls": "🖤",
               "galentines-day-gift-ideas-for-tweens": "👯", "best-journals-for-tween-girls": "📓", "easter-basket-ideas-for-tweens": "🐣",
               "gifts-for-girls-who-have-everything": "✨",
               "black-friday-gift-ideas-for-tween-girls": "🛍️", "cyber-monday-gift-ideas-for-tweens": "💻"}

def guide_cards(gs, short=False):
    return '<div class="cards">' + "".join(
        f'<a class="gcard rv" href="/{g["slug"]}/"><span class="e">{GUIDE_EMOJI.get(g["slug"], "🎁")}</span><b>{esc(g["title"])}</b>'
        + ("" if short else f'<span>{esc(g["desc"])}</span>') + '<em>Read the guide →</em></a>' for g in gs) + "</div>"

BOOK_FAQ = [
 ("What age is Rate My Crush for?", "It's made for girls ages 7 to 14."),
 ("What's inside the journal?", "100 pages. Each crush gets a page with a code name, where she sees them, their squad and their favorites, a 10-category star scorecard (Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades and Bonus Spark, for 50 stars total), a Crush Level heart meter, and prompts like \"Best Thing About Them\" and \"Why I Think We'd Be a Good Match.\""),
 ("What's the difference between Playful, Moody and Floral?", "Only the style. All three have the same prompts inside, each styled to match its cover. Playful is bright pastel with a glossy cover, Moody is dark and edgy with a matte cover, and Floral is navy florals with a matte cover."),
 ("How big is it?", "It's a 6×9 inch paperback. The Playful Edition is also available in hardcover."),
 ("Where can I buy it?", "Rate My Crush is sold on Amazon. Search \"Rate My Crush\" or use the links on this page."),
 ("Does it come with pens, stickers or a lock?", "No. It's the journal itself. A set of gel pens makes a nice pairing if you're giving it as a gift."),
 ("What is a crush journal?", "A crush journal is a guided journal for writing about crushes. In Rate My Crush, each crush gets a page with a code name, a 10-category star scorecard (50 stars total), a Crush Level heart meter and prompts like \"Why I Think We'd Be a Good Match.\""),
 ("Is Rate My Crush a good stocking stuffer?", "Yes. It's a 6×9 inch paperback, so it fits in most standard stockings, and it's a screen-free gift that gets used long after Christmas morning."),
 ("Is Rate My Crush a good birthday gift for a 9, 10, 11 or 12 year old?", "Yes. It's made for ages 7–14, so it fits any of those birthdays, and the scorecard makes a fun group activity at a birthday sleepover."),
 ("Is Rate My Crush a good Valentine's Day or Galentine's Day gift?", "Yes. It's a lighthearted, on-theme alternative to candy, and it makes a funny group activity for a Galentine's sleepover."),
 ("Is Rate My Crush age-appropriate?", "Yes. It's designed for ages 7–14 and keeps things lighthearted. The scorecard even rates Kindness and How They Treat Me alongside Smile and Hair."),
 ("Who wrote Rate My Crush?", "Rate My Crush is by Felicia Nevin, an independent author writing from East Tennessee. It's published in three editions (Playful, Moody and Floral) and sold on Amazon."),
 ("Is Rate My Crush a good gift for a daughter, niece, granddaughter or little sister?", "Yes. It's made for ages 7–14, so it works for a daughter, niece, granddaughter, goddaughter or little sister in that range. Moms, aunts, grandmas and big sisters give it as a fun, screen-free gift and a keepsake she'll laugh about when she's grown."),
 ("Is it a good gift?", "It makes a fun gift for birthdays, Christmas stockings, Valentine's Day and sleepovers: a fun, screen-free way for her to process first crushes, and a keepsake she'll laugh about when she's grown."),
]

GUIDES = [
 dict(slug="black-friday-gift-ideas-for-tween-girls", kw="Black Friday gifts for tween girls",
  title="Black Friday Gift Ideas for Tween Girls (2026): Stocking Stuffers & Gifts Ages 7–14",
  desc="Black Friday gift ideas for tween girls ages 7–14: stocking stuffers, screen-free gifts, and picks for your daughter, niece or granddaughter, starting with a crush journal she'll laugh about when she's grown.",
  intro="Black Friday is when the list gets real: the niece, the granddaughter, your own daughter, the little sister who's suddenly too cool for everything. These ideas work for girls ages 7 to 14, from stocking stuffers to the gift she'll open first.",
  angle="It's the fun-aunt, cool-grandma, mom-who-gets-it gift, and at 6×9 it fits in most stockings.",
  items=[("A crush journal", "Rate My Crush: every crush gets a code name, a 10-category scorecard and a Crush Level. A keepsake she'll laugh about at 30."),
   ("A big set of gel pens", "The perfect pairing for any journal. Glitter, scented or pastel."),
   ("Cozy pajamas or fuzzy pants", "For movie nights all winter."),
   ("A friendship bracelet kit", "Something to make and trade with friends over the break."),
   ("Room decor", "String lights, a fun pillow or a small mirror for her space."),
   ("A card or party game", "For sleepovers and family game night."),
   ("A first book in a new series", "A long winter read."),
   ("A beginner craft kit", "Embroidery, sewing, clay or painting."),
   ("A cute water bottle and stickers", "She'll decorate it the same day."),
   ("An experience with you", "Ice skating, a holiday show or a baking day.")],
  faq=[("What are good Black Friday gifts for tween girls?", "Gifts she'll actually use: journals, gel pens, cozy pajamas, craft kits, room decor, card games and books. A crush journal like Rate My Crush is a screen-free, funny gift for ages 7–14 that doubles as a stocking stuffer."),
       ("What's a good Black Friday gift for my niece, granddaughter or daughter (ages 7–14)?", "Something personal and a little grown-up: a journal, a craft kit, room decor or an experience together. Rate My Crush is a crush journal made for ages 7–14 with code names, a 10-category star scorecard and a Crush Level meter."),
       ("Are there stocking stuffers for tweens that aren't candy?", "Yes: gel pens, hair accessories, lip balm, card games, stickers and small journals. Rate My Crush is a 6×9 paperback, so it fits in most standard stockings."),
       ("Does Rate My Crush come with pens?", "No. It's the journal itself (no pens, stickers or lock included). A pack of gel pens makes a great pairing.")],
  sale_faq=[("Is Rate My Crush on sale for Black Friday?", f"Yes. As of {SALE_ASOF}, all three paperback covers (Playful, Moody and Floral) are $9.99 on Amazon, through Cyber Monday, November 30, 2026. Prices can change, so check the Amazon listing for the current price. The Playful hardcover isn't part of the price drop.")]),
 dict(slug="cyber-monday-gift-ideas-for-tweens", kw="Cyber Monday gifts for girls",
  title="Cyber Monday Gift Ideas for Tweens (2026): Gifts for Girls 7–14",
  desc="Cyber Monday gift ideas for tween girls ages 7–14: easy online picks for your daughter, niece or granddaughter, plus stocking stuffers and a crush journal that gets a gasp.",
  intro="Cyber Monday is made for finishing the list from the couch. Here are online-friendly gift ideas for girls ages 7 to 14 that feel thoughtful, not last-minute.",
  angle="It's an easy add-to-cart gift that still feels personal: she fills it in with her own crushes, code names and star ratings.",
  items=[("A crush journal", "Rate My Crush: a guided crush journal for ages 7–14 with a 50-star scorecard and a Crush Level heart meter."),
   ("Gel pens or fine-tip markers", "A journal kid's must-have."),
   ("A cozy throw blanket", "For reading, movies and sleepovers."),
   ("A jewelry-making kit", "Beads, charms and a reason to make gifts for friends."),
   ("A fun alarm clock or lamp", "A grown-up touch for her room."),
   ("A graphic novel or chapter book", "Something new for winter break."),
   ("A sketchbook and colored pencils", "For the doodler."),
   ("A game for the whole family", "Something for after Christmas dinner."),
   ("Hair accessories", "Claw clips, scrunchies and headbands."),
   ("A puzzle book", "Word searches, logic puzzles and brain teasers.")],
  faq=[("What are good Cyber Monday gifts for girls ages 7–14?", "Journals, gel pens, craft and jewelry kits, books, room decor, cozy blankets and family games. Rate My Crush is a crush journal for ages 7–14 sold on Amazon in three covers: Playful, Moody and Floral."),
       ("Which Rate My Crush cover should I pick?", "Same prompts inside, each styled to match its cover: Playful is bright pastel and glossy, Moody is dark and matte, and Floral is navy florals and matte. Pick the one that matches her style.")],
  sale_faq=[("Is Rate My Crush on sale for Black Friday?", f"Yes. As of {SALE_ASOF}, all three paperback covers (Playful, Moody and Floral) are $9.99 on Amazon, through Cyber Monday, November 30, 2026. Prices can change, so check the Amazon listing for the current price. The Playful hardcover isn't part of the price drop.")]),
 dict(slug="gifts-for-10-year-old-girls", kw="Gifts for a 10 year old girl",
  title="Gift Ideas for a 10-Year-Old Girl (That She'll Actually Use)",
  desc="Thoughtful, fun gift ideas for a 10-year-old girl: screen-free, creative and age-appropriate picks, plus a crush journal she'll laugh about when she's grown.",
  intro="Ten is a funny age to shop for. She's too old for a lot of toys, not quite into teen stuff, and she has opinions. The best gifts at this age let her feel a little more grown-up while still being fun. Here are ideas that tend to land.",
  angle="Ten is right around when crushes start becoming a Whole Thing, and this gives her a fun place to put them.",
  items=[("A crush journal", "A guided journal where she rates her crushes on a scorecard. Funny now, priceless later."),
   ("A big set of gel pens or fine-tip markers", "Every journal kid needs the good pens."),
   ("A friendship bracelet kit", "Something to make, trade and wear."),
   ("A cozy blanket or oversized hoodie", "Comfort gifts never miss at this age."),
   ("A room upgrade", "String lights, a small mirror, a fun pillow: anything that makes her room feel like hers."),
   ("A beginner craft or sewing kit", "Hands-on projects that take an afternoon."),
   ("Card games for sleepovers", "Easy group games she can bring to a friend's house."),
   ("A chapter-book series", "The first book of a series she can keep reading."),
   ("A mini instant camera or photo album", "For the friend-group photo wall."),
   ("An experience", "Tickets, a class, or a one-on-one day out with you.")],
  faq=[("What do 10-year-old girls like?", "At 10, many girls are into friendships, crafts, journaling, room decor, sleepovers and anything that feels a little more grown-up. Gifts that let her express herself tend to be the biggest hits."),
       ("What's a good screen-free gift for a 10-year-old girl?", "Journals, craft kits, books, card games and room decor are all screen-free favorites. A guided crush journal like Rate My Crush is a fun one because she'll want to fill it out.")]),
 dict(slug="stocking-stuffers-for-tween-girls", kw="Stocking stuffers for tween girls",
  title="Stocking Stuffers for Tween Girls (Ages 8–14) That Aren't Just Candy",
  desc="Small, fun stocking stuffer ideas for tween girls ages 8 to 14, from gel pens to a crush journal she'll keep for years.",
  intro="The best stocking stuffers are small, a little silly, and actually get used after Christmas morning. Here's a list for the tween in your life.",
  angle="It fits in a stocking (6×9) and gets way more use than candy.",
  items=[("A crush journal", "The one that gets a gasp, then gets hidden from her little brother."),
   ("Gel pens", "Bonus points for glitter or scented."), ("Lip balm or a fun lip gloss", "A tween classic."),
   ("Hair clips and scrunchies", "You can never have too many."), ("Fuzzy socks", "Required by stocking law."),
   ("A small card game", "Something for the car ride to Grandma's."), ("Stickers for her water bottle", "She'll decorate everything."),
   ("A keychain or bag charm", "For her backpack."), ("A mini notebook or sketchbook", "For doodles and lists."),
   ("A small puzzle or brain teaser", "Quiet entertainment for the afternoon.")],
  faq=[("What are good stocking stuffers for tween girls?", "Small things she'll actually use: gel pens, hair accessories, lip balm, fuzzy socks, card games, stickers and journals. A crush journal like Rate My Crush fits in most stockings and lasts well beyond Christmas morning."),
       ("Is Rate My Crush small enough for a stocking?", "It's a 6×9 inch paperback, so it fits in most standard stockings.")]),
 dict(slug="gifts-for-niece", kw="Gifts for your niece",
  title="Fun Aunt Gift Guide: Gifts for Your Niece (Ages 7–14)",
  desc="Gift ideas for your niece ages 7 to 14 from the fun aunt: things her parents wouldn't think of, including a crush journal she'll love.",
  intro="Being the fun aunt is a responsibility. Your gift doesn't need to be the biggest, it needs to be the one she talks about. These ideas are built for that.",
  angle="It's the gift her parents wouldn't think to buy, which is exactly why it should come from you.",
  items=[("A crush journal", "Peak fun-aunt energy. She'll love that you get it."),
   ("A matching aunt-and-niece activity", "A craft you do together, or a cookie-decorating day."),
   ("Nail polish and a mini manicure set", "Paint nights are a fun-aunt staple."),
   ("A day out, just you two", "Lunch, a movie, a bookstore trip."),
   ("Cute room decor", "Something that makes her room feel like hers."),
   ("A big set of markers or gel pens", "Pairs perfectly with a journal."),
   ("A friendship bracelet kit", "Make one for her, one for you."),
   ("A fun mug and hot cocoa", "Cozy and easy to wrap."),
   ("A book you loved at her age", "Add a note about why."),
   ("A group game for the next family get-together", "So you're the fun one there too.")],
  faq=[("What should I get my niece who's 10, 11 or 12?", "Gifts that feel a little grown-up and a little fun: a guided journal, craft kits, room decor, or an outing just the two of you. Rate My Crush is a fun-aunt pick made for girls 7–14."),
       ("What's a unique gift for a niece?", "Something her parents wouldn't buy. A crush journal is a good example: harmless, funny and very on-brand for an aunt.")]),
 dict(slug="valentines-gifts-for-girls", kw="Valentine's gifts for girls (not candy)",
  title="Valentine's Day Gifts for Girls That Aren't Candy (Ages 7–14)",
  desc="Non-candy Valentine's Day gift ideas for daughters, nieces and granddaughters ages 7 to 14, including a crush journal made for the season.",
  intro="Candy is gone by February 15th. If you want a Valentine's gift for the girl in your life that lasts a little longer, here are ideas that still feel festive.",
  angle="It's practically made for Valentine's Day, and unlike candy hearts, she'll still have it next year.",
  items=[("A crush journal", "About as on-theme as Valentine's gifts get."),
   ("Heart-shaped or pink stationery", "Cards to hand out to friends."),
   ("A cozy pair of pajamas", "For a Valentine's movie night at home."),
   ("Friendship bracelet supplies", "Galentine's gifts for her friends."),
   ("A Valentine's craft kit", "Make cards, garlands or decorations together."),
   ("A pink or red hair accessory set", "For a festive school day."),
   ("A book about friendship", "Something sweet to read."),
   ("A fun mug with a note", "Fill it with something small."),
   ("A baking kit", "Heart cookies, together."),
   ("A handwritten letter from you", "The one she'll keep.")],
  faq=[("What's a good Valentine's gift for a daughter that isn't candy?", "Something she'll keep: a journal, pajamas, a craft kit or a handwritten letter. Rate My Crush is a crush journal for girls 7–14, so it's about as on-theme as Valentine's gifts get."),
       ("Is Rate My Crush appropriate for Valentine's Day?", "Yes. It's a lighthearted, age-appropriate journal for girls 7–14 to rate their crushes with stars and a heart meter.")]),
 dict(slug="screen-free-gifts-for-tween-girls", kw="Screen-free gifts for tween girls",
  title="Screen-Free Gifts for Tween Girls She'll Actually Want",
  desc="Screen-free gift ideas for tween girls ages 8 to 14 that compete with a phone: journals, crafts, games and a crush journal she'll want to fill out.",
  intro="It's hard to compete with a screen. The screen-free gifts that work are the ones that feel personal, creative or social. Here are ideas that get picked up again and again.",
  angle="It's screen-free, and it's one she'll actually want to fill out because it's all about her.",
  items=[("A guided crush journal", "Prompts make journaling feel fun instead of like homework."),
   ("A craft kit she can finish in a weekend", "Quick wins keep it fun."), ("A big puzzle", "Good for a cozy weekend."),
   ("A friendship bracelet or bead kit", "Social and creative."), ("Card and board games", "Especially ones for 3+ players."),
   ("A sketchbook and good pencils", "For the doodler."), ("A book series", "Book one plus a note to ask for book two."),
   ("Outdoor gear", "A new bike helmet, a jump rope, a scooter."), ("A baking or cooking kit", "Something you make together."),
   ("A disposable or instant camera", "Photos without the phone.")],
  faq=[("What are good screen-free gifts for tweens?", "Journals with prompts, craft kits, puzzles, card games, books and outdoor gear. The most-used ones feel personal or social."),
       ("Is a journal a good screen-free gift for a tween?", "Yes, especially a guided one. Rate My Crush gives her prompts and a scorecard, so it's fun to fill out instead of a blank page.")]),
 dict(slug="gifts-for-granddaughter", kw="Gifts for your granddaughter",
  title="Gifts for Your Granddaughter (Ages 7–14) From a Cool Grandma",
  desc="Gift ideas for a granddaughter ages 7 to 14: fun, thoughtful picks that make Grandma the cool one, including a crush journal.",
  intro="Shopping for a granddaughter between 7 and 14 can feel like a moving target. These ideas are easy to pick, easy to wrap, and they'll make you the cool grandparent.",
  angle="It's the kind of gift that gets a reaction, and it's a keepsake she'll laugh about when she's grown.",
  items=[("A crush journal", "The gift that makes Grandma the cool one."),
   ("A keepsake box", "For notes, tickets and treasures."), ("A cozy robe or blanket", "Warm and personal."),
   ("A recipe card set from your kitchen", "Handwritten family recipes to keep."),
   ("A craft you do together", "Knitting, baking or a paint-by-number."), ("A book you loved as a girl", "With a note inside."),
   ("A photo book of the two of you", "She'll treasure it later."), ("Gel pens and stationery", "For writing letters to you."),
   ("A day trip together", "Lunch and a shopping trip."), ("A small piece of jewelry", "A simple charm or necklace.")],
  faq=[("What do you get a granddaughter who's 10 to 12?", "Gifts that feel personal and a little grown-up: a guided journal, a keepsake box, a craft to do together, or a photo book of you two."),
       ("Is Rate My Crush appropriate for a granddaughter?", "Yes. It's a lighthearted, age-appropriate crush journal designed for girls 7–14.")]),
 dict(slug="sleepover-ideas-for-tween-girls", kw="Sleepover ideas for tween girls",
  title="Sleepover Ideas for Tween Girls: Activities, Snacks and Games",
  desc="Easy sleepover ideas for tween girls ages 8 to 14: activities, games and snack ideas, plus a crush journal that makes a fun group activity.",
  intro="A good sleepover needs a plan that doesn't feel like a plan. Here's a mix of activities, games and snacks that keep a group of tweens happy until (way past) bedtime.",
  angle="It works as a sleepover activity: everyone takes turns with the scorecard, and the giggling takes care of itself.",
  items=[("Make-your-own pizza", "Everyone builds their own."), ("A crush journal", "A guaranteed giggle session."),
   ("Friendship bracelets", "Everyone leaves with one."), ("A movie marathon", "Let them vote on the lineup."),
   ("DIY face masks and nail painting", "A spa night classic."), ("A blanket fort", "Bonus points for string lights."),
   ("Truth-or-dare-style card games", "Pick an age-appropriate deck."), ("A hot cocoa bar", "Marshmallows and toppings."),
   ("A dance-off", "Somebody always wins."), ("Polaroid photo wall", "Take pictures, pin them up.")],
  faq=[("What do tween girls do at sleepovers?", "Movies, crafts like friendship bracelets, spa nights, card games, snacks and a lot of talking. Activities that get everyone laughing together work best."),
       ("Is Rate My Crush a good sleepover activity?", "Yes. The Amazon listing describes it as a sleepover activity, and its scorecard format is easy to share and laugh about with friends.")]),
 dict(slug="christmas-gifts-for-tween-girls", kw="Christmas gifts for tween girls",
  title="Christmas Gifts for Tween Girls (Ages 8–14) She'll Actually Use",
  desc="Christmas gift ideas for tween girls ages 8 to 14: cozy, creative and screen-free picks, plus a crush journal that makes a perfect stocking stuffer.",
  intro="Tweens are tricky to shop for at Christmas: too old for toys, too young for a lot of teen stuff, and very clear about what's cringe. These ideas land in that sweet spot, from big gifts to stocking stuffers.",
  angle="It's a Christmas morning gasp-then-giggle gift, and at 6×9 it fits in most stockings.",
  items=[("A crush journal", "Peak stocking-stuffer energy: she rates her crushes on a 10-category scorecard."),
   ("Cozy Christmas pajamas", "For the Christmas Eve photo and every movie night after."),
   ("A room makeover kit", "String lights, a fun throw pillow and a small mirror."),
   ("A friendship bracelet kit", "Something to make over winter break and trade with friends."),
   ("A big set of gel pens", "The journal kid's must-have."),
   ("A beginner sewing or embroidery kit", "A project for the slow days after Christmas."),
   ("Card games for family game night", "Something everyone can play on Christmas afternoon."),
   ("A first book in a new series", "A long winter-break read."),
   ("A fuzzy blanket", "Gifts you can snuggle never miss."),
   ("An experience", "Ice skating, a holiday show or a cookie-decorating day with you.")],
  faq=[("What do tween girls want for Christmas?", "Many tweens want things that feel a little grown-up and very personal: room decor, cozy clothes, craft kits, journals, books and experiences with family or friends. Gifts that let her express herself tend to be hits."),
       ("What's a good stocking stuffer for a tween girl?", "Small things she'll use after Christmas morning: gel pens, hair accessories, lip balm, card games and journals. Rate My Crush is a 6×9 crush journal that fits in most stockings.")]),
 dict(slug="birthday-gifts-for-tween-girls", kw="Birthday gifts for tween girls",
  title="Birthday Gifts for Tween Girls (Ages 8–14): Fun Ideas She'll Love",
  desc="Birthday gift ideas for tween girls ages 8 to 14, from party-favorite crafts to a crush journal that gets passed around the whole sleepover.",
  intro="A tween birthday gift has two jobs: get a reaction when she opens it, and still be in use a month later. Here are ideas that do both, whether it's your daughter, niece, granddaughter or her best friend.",
  angle="It's a birthday gift that gets a reaction at the party and keeps getting filled in after.",
  items=[("A crush journal", "Opens with a squeal, gets passed around the birthday sleepover."),
   ("A DIY spa night kit", "Face masks and nail polish for the party."),
   ("A mini instant camera or photo album", "For party pictures with her friends."),
   ("A friendship bracelet kit", "Everyone at the party can make one."),
   ("Room decor in her favorite color", "Lights, pillows, a cute storage box."),
   ("A big art or sketch set", "For the creative birthday girl."),
   ("A cozy hoodie or robe", "Comfort gifts always land."),
   ("A book series she hasn't started", "Something to read after the party."),
   ("A group card game", "So the party has a built-in activity."),
   ("A birthday outing", "A class, a show or lunch with you.")],
  faq=[("What's a good birthday gift for a tween girl?", "Gifts that are personal and a little grown-up: journals, room decor, craft kits, cozy clothes and experiences. Rate My Crush is a guided crush journal for ages 7–14 that doubles as a party activity."),
       ("What can I give a tween girl for her birthday that isn't a gift card?", "A guided journal, a craft kit, a spa night kit or an outing together all feel more personal than a gift card.")]),
 dict(slug="gifts-for-8-year-old-girls", kw="Gifts for an 8 year old girl",
  title="Gift Ideas for an 8-Year-Old Girl: Fun, Creative and Screen-Free",
  desc="Gift ideas for an 8-year-old girl: craft kits, books, games and a fun crush journal she can grow into.",
  intro="At 8, she's reading on her own, making things with her hands and starting to have big opinions about her friends. These gift ideas lean into all of that.",
  angle="Eight is often when the first 'he's kind of cute' moments show up, and this turns them into giggles.",
  items=[("A crush journal", "Something fun to grow into, with prompts and a star scorecard."),
   ("A big craft kit", "Slime, beads, painting or clay."), ("A chapter-book series", "The first book plus a note to ask for book two."),
   ("A fun card game", "Easy to learn, good for playdates."), ("Gel pens and stickers", "For decorating everything."),
   ("A science or discovery kit", "Hands-on experiments for a rainy day."), ("A plush or cozy blanket", "Still a favorite at 8."),
   ("A jump rope or outdoor toy", "For recess and backyard afternoons."), ("Hair accessories", "Clips, scrunchies and headbands."),
   ("A day out with you", "The zoo, a museum or the bookstore.")],
  faq=[("What does an 8-year-old girl like?", "Many 8-year-olds love crafts, chapter books, card games, stickers and anything they can make or collect. Screen-free gifts that let her create are a great bet."),
       ("Is Rate My Crush OK for an 8-year-old?", "Rate My Crush is made for ages 7–14 and is lighthearted and age-appropriate, with a scorecard that includes Kindness and How They Treat Me.")]),
 dict(slug="gifts-for-9-year-old-girls", kw="Gifts for a 9 year old girl",
  title="Gift Ideas for a 9-Year-Old Girl She'll Be Excited About",
  desc="Gift ideas for a 9-year-old girl: creative kits, books, room decor and a crush journal that makes her feel a little grown-up.",
  intro="Nine is the start of the tween years: she wants to feel older, but she still loves to play. The best gifts at this age give her a little independence and a lot of fun.",
  angle="Nine-year-olds love feeling a little grown-up, and a journal with a scorecard and a Crush Level does exactly that.",
  items=[("A crush journal", "A little grown-up, a lot of fun."), ("A friendship bracelet kit", "Make, trade, repeat."),
   ("A diary or sketchbook", "Her own space for ideas."), ("A room decor upgrade", "Lights or a cute pillow."),
   ("A beginner cooking or baking kit", "Make something together."), ("A book series", "Something to binge-read."),
   ("Card and board games", "For sleepovers and family nights."), ("Gel pens", "Pairs perfectly with any journal."),
   ("An art set", "Markers, paints or colored pencils."), ("An experience", "A class or an outing with you.")],
  faq=[("What should I get a 9-year-old girl?", "Journals, craft kits, books, games and room decor are favorites at 9. Gifts that make her feel a little more grown-up are usually a hit."),
       ("Is a journal a good gift for a 9-year-old?", "Yes, especially a guided one with prompts, so it's fun instead of a blank page. Rate My Crush is made for ages 7–14.")]),
 dict(slug="gifts-for-11-year-old-girls", kw="Gifts for an 11 year old girl",
  title="Gift Ideas for an 11-Year-Old Girl (Tween-Approved)",
  desc="Gift ideas for an 11-year-old girl: room decor, cozy clothes, creative kits and a crush journal she'll laugh about for years.",
  intro="Eleven is full-on tween: friends are everything, crushes are a topic, and her room is her kingdom. These ideas speak her language.",
  angle="At 11, crushes are a Whole Topic, and this gives them a code name, a scorecard and a Crush Level.",
  items=[("A crush journal", "Rate the crush, track the Crush Level, laugh about it later."), ("Room decor", "Lights, a mirror, a cute storage box."),
   ("A cozy oversized hoodie", "The unofficial tween uniform."), ("A DIY jewelry kit", "Make her own accessories."),
   ("A mini instant camera", "For the friend-group photo wall."), ("A big set of gel pens or markers", "For journaling and doodling."),
   ("A book series", "Something her friends are reading too."), ("A self-care kit", "Face masks and lip balm."),
   ("A sleepover game", "For the next slumber party."), ("Tickets to something", "A show, a game or a concert with you.")],
  faq=[("What do 11-year-old girls like?", "Many 11-year-olds are into friendships, room decor, cozy clothes, journaling, crafts and sleepovers. Gifts that feel personal and a little grown-up tend to win."),
       ("Is Rate My Crush a good gift for an 11-year-old?", "Yes. It's a guided crush journal for ages 7–14 with a 10-category star scorecard and a Crush Level heart meter.")]),
 dict(slug="gifts-for-12-year-old-girls", kw="Gifts for a 12 year old girl",
  title="Gift Ideas for a 12-Year-Old Girl She Won't Think Are Cringe",
  desc="Gift ideas for a 12-year-old girl: cozy, creative and personal picks, plus a crush journal with a 10-category scorecard.",
  intro="Shopping for a 12-year-old means avoiding anything that feels 'for little kids.' These ideas feel grown-up enough for middle school and fun enough to actually use.",
  angle="It has the perfect amount of drama for 12, and the Moody cover is made for the 'I'm too cool for pink' crowd.",
  items=[("A crush journal", "Pick the Moody cover for the too-cool-for-pink crowd."), ("A cozy hoodie or pajama set", "Comfort is everything."),
   ("Room decor", "Something that makes her room feel like hers."), ("A journal or planner", "For school and everything else."),
   ("A self-care set", "Face masks, lip balm, a scrunchie."), ("A creative kit", "Embroidery, painting or jewelry making."),
   ("A book series", "Something to talk about with friends."), ("A mini instant camera", "Photos without the phone."),
   ("A group game", "For sleepovers."), ("An experience", "A concert, a class or a day trip.")],
  faq=[("What do 12-year-old girls want?", "Many 12-year-olds want things that feel grown-up: room decor, cozy clothes, self-care items, journals and experiences with friends."),
       ("Which Rate My Crush cover is best for a 12-year-old?", "All three have the same prompts inside, each styled to match its cover. Moody (dark and edgy) suits older tweens who've outgrown pink, but Playful and Floral work too. It's about her style.")]),
 dict(slug="galentines-day-gift-ideas-for-tweens", kw="Galentine's Day gift ideas for tweens",
  title="Galentine's Day Gift Ideas for Tweens and Their Besties",
  desc="Galentine's Day gift ideas for tweens and their best friends, plus party activities and a crush journal that makes the perfect group giggle.",
  intro="Galentine's Day (February 13th) is all about celebrating friends. For tweens, that means matching gifts, a sleepover and a lot of laughing. Here's how to make it fun.",
  angle="It's the ultimate Galentine's activity: everyone takes turns with the scorecard, and the giggling takes care of itself.",
  items=[("A crush journal", "Group giggles guaranteed."), ("Matching friendship bracelets", "Make them together."),
   ("Mini self-care kits", "Face masks and lip balm for each friend."), ("A pink-and-red snack board", "Strawberries, cookies and candy hearts."),
   ("Heart-shaped stationery", "For writing notes to each other."), ("A friendship book", "Fill-in pages about each other."),
   ("A Galentine's movie night", "Blankets, popcorn and a friendship movie."), ("A cookie-decorating kit", "Hearts and sprinkles."),
   ("Matching scrunchies or socks", "Twinning is the point."), ("A photo booth corner", "Props and a camera.")],
  faq=[("When is Galentine's Day?", "Galentine's Day is celebrated on February 13th, the day before Valentine's Day, to celebrate friendships."),
       ("What's a good Galentine's gift for a tween?", "Matching friendship items, self-care kits, stationery and fun group activities. Rate My Crush is a crush journal for ages 7–14 that makes a funny group activity.")]),
 dict(slug="best-journals-for-tween-girls", kw="Best journals for tween girls",
  title="The Best Kinds of Journals for Tween Girls (and Which One to Pick)",
  desc="A guide to journals for tween girls ages 8 to 14: guided journals, diaries, gratitude journals, crush journals and more, and how to pick the right one.",
  intro="A journal is one of the best screen-free gifts for a tween, but a blank notebook can be intimidating. Here's a guide to the main kinds of journals and who each one is for.",
  angle="If she's into crushes and gossip-level drama, a guided crush journal is the one she'll actually want to fill in.",
  items=[("A guided crush journal", "Prompts and a star scorecard make it fun instead of homework."),
   ("A classic diary", "Lined pages for the girl who loves to write."), ("A gratitude journal", "A few happy things a day."),
   ("A friendship journal", "Fill-in pages about her and her besties."), ("A sketch journal", "For the artist who doodles more than writes."),
   ("A mood or feelings journal", "Simple check-ins for big feelings."), ("A reading journal", "For the bookworm to log every book."),
   ("A mother-daughter journal", "A shared notebook to pass back and forth."), ("A goals or vision journal", "Dreams, plans and lists."),
   ("A travel or summer journal", "For trips, camp and summer break.")],
  faq=[("What kind of journal is best for a tween girl?", "Guided journals with prompts are often easiest for tweens to stick with, because they don't start with a blank page. Pick a theme she's into: crushes, friends, books, art or feelings."),
       ("What is a crush journal?", "A crush journal is a guided journal for writing about crushes. Rate My Crush, for example, gives each crush a page with a code name, a 10-category star scorecard, a Crush Level meter and prompts.")]),
 dict(slug="easter-basket-ideas-for-tweens", kw="Easter basket ideas for tweens",
  title="Easter Basket Ideas for Tweens (That Aren't Just Candy)",
  desc="Non-candy Easter basket ideas for tweens ages 8 to 14: small, fun fillers including a crush journal that fits right in the basket.",
  intro="Tweens still love an Easter basket, they just want it to feel a little more grown-up. These fillers mix a few treats with things she'll actually use.",
  angle="It slides right into an Easter basket (6×9) and lasts a lot longer than the chocolate.",
  items=[("A crush journal", "A basket filler that outlasts the candy."), ("Gel pens", "Pastel ones for spring."),
   ("Lip balm and a scrunchie", "Small, useful, cute."), ("A spring craft kit", "Flowers, beads or painting."),
   ("Sunglasses", "Ready for spring break."), ("A small card game", "For family time on Easter afternoon."),
   ("A paperback book", "The first in a series."), ("Bath bombs or a face mask", "A little self-care."),
   ("Stickers for her water bottle", "She'll decorate everything."), ("A few favorite treats", "It's still Easter.")],
  faq=[("What do you put in a tween's Easter basket?", "A mix of small treats and things she'll use: gel pens, lip balm, hair accessories, a book, a craft kit or a journal."),
       ("Does Rate My Crush fit in an Easter basket?", "It's a 6×9 inch paperback, so it fits in most Easter baskets.")]),
 dict(slug="gifts-for-girls-who-have-everything", kw="Gifts for a tween girl who has everything",
  title="Gifts for a Tween Girl Who Has Everything (Ages 8–14)",
  desc="Unique gift ideas for a tween girl who has everything: experiences, personal gifts and a crush journal she definitely doesn't have yet.",
  intro="When she already has every gadget and craft kit, the best gifts are personal, funny or something to do together. Here are ideas that stand out.",
  angle="It's the gift she definitely doesn't already have, and it gets a laugh the second she opens it.",
  items=[("A crush journal", "Funny, personal and definitely not already in her room."), ("An experience", "Tickets, a class or a trip."),
   ("A personalized item", "Her name or initial on a bag or blanket."), ("A letter from you", "Written to be opened later."),
   ("A subscription box", "Something new arrives every month."), ("A skill class", "Cooking, art, dance or sewing."),
   ("A photo book", "Her year in pictures."), ("A donation in her name", "To a cause she cares about."),
   ("A cozy upgrade", "A really good blanket or robe."), ("A family tradition starter", "An ornament or a game you play every year.")],
  faq=[("What do you get a tween who has everything?", "Experiences, personalized gifts and funny, personal items she wouldn't buy herself. A guided crush journal like Rate My Crush is a good example."),
       ("What's a unique gift for a tween girl?", "Something personal and a little unexpected: an experience, a handwritten letter or a crush journal she'll laugh about when she's grown.")]),
]


TICKER = ["Code names", "10-category scorecard", "50 stars per crush", "Crush Level meter", "Screen-free",
          "Fits in a stocking", "Sleepover-ready", "Playful · Moody · Floral", "100 guided pages", "Tomorrow's keepsake"]

STEPS = [("🕵️", "Give them a code name", "Every crush gets a page: code name, where they're seen most, their squad, what they're into and their faves."),
         ("⭐", "Rate them in 10 categories", "Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades and Bonus Spark. Up to 5 stars each."),
         ("💜", "Find the Crush Level", "Add up the stars (50 max) for Tiny Crush, Pretty Cute, Big Crush or Totally Obsessed. Then the prompts: best thing about them, funniest memory, why we'd be a good match.")]

REASONS = [("📵", "Screen-free fun", "Paper, pen and a lot of giggling. No app, no account, no feed."),
           ("✍️", "Writing that isn't homework", "Fill-in prompts and star ratings beat a scary blank page."),
           ("💗", "Kindness counts", "The scorecard rates Kindness and How They Treat Me right next to Smile and Hair."),
           ("🌟", "Room for big feelings", "A lighthearted place to sort out first-crush feelings in their own words."),
           ("🛌", "Sleepover gold", "A scorecard is made for group giggles at the next sleepover."),
           ("🎁", "So easy to give", "A 6×9 paperback that slides into a stocking or a gift bag."),
           ("🎨", "A cover for every personality", "Bright and sparkly, dark and edgy, or soft and floral."),
           ("📸", "Tomorrow's keepsake", "The pages filled in at 11 are the ones read out loud at 30.")]

OCCASIONS = [("🎂", "Birthdays", "/gifts-for-10-year-old-girls/"), ("🧦", "Stocking stuffers", "/stocking-stuffers-for-tween-girls/"),
             ("💌", "Valentine's & Galentine's", "/valentines-gifts-for-girls/"), ("🍕", "Sleepovers", "/sleepover-ideas-for-tween-girls/"),
             ("💅", "From the fun aunt", "/gifts-for-niece/"), ("🧶", "From Grandma", "/gifts-for-granddaughter/"), ("📵", "Screen-free gifts", "/screen-free-gifts-for-tween-girls/"), ("🎄", "Christmas", "/christmas-gifts-for-tween-girls/"), ("👯", "Galentine's", "/galentines-day-gift-ideas-for-tweens/"), ("🐣", "Easter baskets", "/easter-basket-ideas-for-tweens/")]

CATS = ["Smile", "Eyes", "Hair", "Style", "Personality", "Humor", "Kindness", "How They Treat Me", "Smarts/Grades", "Bonus Spark"]

def hero_stack():
    order = ["moody", "playful", "floral"]
    return '<div class="stack">' + "".join(
        f'<a href="{AMZ[k]}" aria-label="{k.title()} Edition on Amazon"><img src="/img/cover-{k}.jpg" alt="Rate My Crush {k.title()} Edition cover" width="801" height="1200"><span class="lbl">{k.title()}</span></a>'
        for k in order) + '<div class="sticker">Fits in a stocking!</div><span class="float" style="left:2%;top:8%">💗</span><span class="float" style="right:10%;bottom:4%;animation-delay:-2s">⭐</span><span class="float" style="left:12%;bottom:10%;animation-delay:-4s">💌</span></div>'

def ticker():
    items = "".join(f"<span>{esc(t)}</span>" for t in TICKER) * 2
    return f'<div class="ticker" aria-hidden="true"><div class="t">{items}</div></div>'

def demo():
    rows = "".join(f'<div class="row"><span>{c}</span><span class="stars">{"<i></i>"*5}</span></div>' for c in CATS)
    levels = "".join(f'<div class="lv">{h}<div>{n}<small>{r} stars</small></div></div>' for h, n, r in
                     [("💛", "Tiny Crush", "1–15"), ("💚", "Pretty Cute", "16–30"), ("💙", "Big Crush", "31–40"), ("💜", "Totally Obsessed", "41–50")])
    return f"""<section id="demo"><div class="wrap"><div class="demo rv">
<div><span class="kicker">⭐ Try the scorecard</span><h2>50 stars. 10 categories. <span class="hand">One very serious</span>&nbsp;Crush Level.</h2>
<p class="lede">Here's how a page works, with a sample filled in by us. Hit shuffle and watch the Crush Level change.</p>
<div class="levels">{levels}</div><button class="btn" data-shuffle type="button">🔀 Shuffle the sample</button></div>
<div class="card-page" data-demo><div class="hd"><span>Crush #1</span><span class="cn" data-cn>Mr. Pancakes</span></div>
<div class="sample">Code name only. Sample page, filled in by us.</div>
<div class="rows">{rows}</div><div class="total"><span>Total score</span><span><span data-total>0</span> / 50 ⭐</span></div>
<div class="meter"><b></b></div><div class="level" data-level></div></div></div></div></section>"""

def editions():
    cards = "".join(f"""<div class="ed {e['key']} rv"><img class="cover" src="/img/cover-{e['key']}.jpg" alt="Rate My Crush {e['name']} Edition cover" loading="lazy" width="801" height="1200">
<div class="vibe">{e['vibe']}</div><h3>{e['name']} Edition</h3><p>{e['look']}</p><span class="best">{e['best']}</span>
<p style="font-size:14px;opacity:.85">{e['extra']}</p><a class="btn" href="{AMZ[e['key']]}">View {e['name']} on Amazon →</a></div>""" for e in EDITIONS)
    return f"""<section id="editions" style="background:linear-gradient(180deg,#fffaf6,#fff0f7)"><div class="wrap center">
<span class="kicker">🎨 Pick a cover</span><h2>Three vibes. <span class="hand">Same fun inside.</span></h2>
<p class="lede">Every edition has the same prompts inside, each styled to match its cover. Just pick the one that feels like them.</p>
<div class="eds">{cards}</div><p class="same">Not sure? Playful is the crowd-pleaser, Moody is for the "I'm too cool for pink" crowd, and Floral is the keepsake.</p></div></section>"""

def gallery():
    return f"""<section id="inside"><div class="wrap center"><span class="kicker">👀 Peek inside</span><h2>Real pages from the journal</h2>
<p class="lede">The scorecard, the prompts and the Crush Level meter. Tap a cover style to see its pages, and tap any page to zoom in.</p>
<div class="tabs" role="tablist" data-tabs><button type="button" role="tab" aria-selected="true" data-k="playful">Playful</button><button type="button" role="tab" aria-selected="false" data-k="moody">Moody</button><button type="button" role="tab" aria-selected="false" data-k="floral">Floral</button></div>
<div class="pages" data-zoom>
<figure class="rv"><img data-page="score" src="/img/page-playful-score.jpg" alt="Rate My Crush playful edition scorecard page" loading="lazy" width="576" height="864"><figcaption>The crush profile + scorecard</figcaption></figure>
<figure class="rv"><img data-page="prompts" src="/img/page-playful-prompts.jpg" alt="Rate My Crush playful edition prompts page" loading="lazy" width="576" height="864"><figcaption>Prompts + Crush Level meter</figcaption></figure>
<figure class="rv"><img data-cover-img src="/img/cover-playful.jpg" alt="Rate My Crush cover" loading="lazy" width="801" height="1200"><figcaption>The cover</figcaption></figure></div></div></section>"""

def reasons():
    rs = "".join(f'<div class="rs rv"><div class="e">{e}</div><h3>{t}</h3><p>{d}</p></div>' for e, t, d in REASONS)
    return f"""<section id="why" style="background:#fff"><div class="wrap center"><span class="kicker">💡 Why grown-ups love giving it</span>
<h2>It's silly. <span class="hand">That's the point.</span></h2><p class="lede">Crushes are a big deal at 10 and hilarious at 30. This gives them a home.</p>
<div class="reasons" style="text-align:left">{rs}</div>
<div class="occ">{''.join(f'<a href="{u}">{e} {t}</a>' for e, t, u in OCCASIONS)}</div></div></section>"""

OCC_TEXT = [
 ("🎄", "Christmas & stocking stuffers", "A 6×9 paperback that fits in most stockings and gets used long after Christmas morning.", "/christmas-gifts-for-tween-girls/"),
 ("🎈", "Birthdays (ages 7–14)", "Opens with a squeal, then turns into the birthday-sleepover activity.", "/birthday-gifts-for-tween-girls/"),
 ("💌", "Valentine's Day", "The on-theme gift that isn't candy, and still there next February.", "/valentines-gifts-for-girls/"),
 ("👯", "Galentine's Day", "Everyone takes a turn with the scorecard. Instant group giggles.", "/galentines-day-gift-ideas-for-tweens/"),
 ("🐣", "Easter baskets", "Slides into the basket and outlasts the chocolate.", "/easter-basket-ideas-for-tweens/"),
 ("🍕", "Sleepovers & camp", "A slumber-party activity and a fun camp care-package pick.", "/sleepover-ideas-for-tween-girls/"),
]

def occasions():
    cards = "".join(f'<a class="gcard rv" href="{u}"><span class="e">{e}</span><b>{t}</b><span>{d}</span><em>Gift ideas →</em></a>' for e, t, d, u in OCC_TEXT)
    return f"""<section id="occasions" style="background:linear-gradient(180deg,#fff,#fff6fb)"><div class="wrap center"><span class="kicker">🎁 A gift for every occasion</span>
<h2>Stocking stuffer, birthday gift, <span class="hand">Valentine's pick.</span></h2>
<p class="lede">Rate My Crush is a go-to gift idea for tweens ages 7–14 all year long.</p><div class="cards" style="text-align:left">{cards}</div></div></section>"""

def author():
    return f"""<section><div class="narrow"><div class="author rv"><div class="av">✍️</div><div><span class="hand">Hi, I'm Felicia!</span>
<h3 style="font-size:28px;margin-top:6px">From the author</h3>
<p>I'm Felicia Nevin, an author writing from East Tennessee. I make books that give kids and tweens a place to be exactly who they are. Rate My Crush is my love letter to that very specific feeling of liking someone at 11: it deserves a code name, a scorecard and a Crush Level.</p>
<a class="btn sm ghost" href="{AUTHOR}">More from Felicia on Amazon</a></div></div></div></section>"""

def social_section():
    return f"""<section style="background:linear-gradient(180deg,#fff,#f4efff)"><div class="wrap center"><span class="kicker">📲 Come hang out</span>
<h2>Follow Rate My Crush</h2><p class="lede">Gift ideas, funny skits and peeks inside the journal, for the grown-ups doing the shopping.</p>{socials_grid()}</div></section>"""

def film_section():
    """'Not Lost to Time' short film (evergreen cut, no price). Muted autoplay loop when on screen, lazy loaded, play-with-sound button."""
    if not os.path.exists(os.path.join(HERE, "video", "not-lost-to-time.mp4")): return ""
    return """<section id="film"><div class="wrap film"><div class="vid rv"><video muted loop playsinline preload="none" poster="/video/not-lost-to-time.jpg" data-src="/video/not-lost-to-time.mp4" aria-label="Not Lost to Time, a short film (a dramatization)"></video>
<button class="snd" type="button">▶ Play with sound</button></div>
<div class="rv"><span class="kicker">🎬 A short film · a dramatization</span><h2>Not Lost to Time</h2>
<p class="lede">Every generation has a first crush. Grandma's was a folded note in a lunchbox in 1962. Mom's was a mixtape label in 1991. Yours might have been a flip-phone text. Most of those moments were lost to time.</p>
<p>Rate My Crush gives hers a place to live: a code name, a 10-category scorecard, and prompts like "Funniest/Best Memory I Have" and "Why I Think We'd Be a Good Match."</p>
<p><a class="btn" href="#editions">Pick a cover →</a></p></div></div></section>
<script>(function(){var v=document.querySelector('#film video'),b=document.querySelector('#film .snd');if(!v)return;
function load(){if(!v.src){v.src=v.dataset.src}}
if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){load();if(v.muted)v.play().catch(function(){})}else{v.pause()}})},{threshold:.35}).observe(v)}else{load()}
b.addEventListener('click',function(){load();v.muted=!v.muted;if(!v.muted){v.currentTime=0;v.loop=false}else{v.loop=true}v.play().catch(function(){});b.textContent=v.muted?'▶ Play with sound':'🔇 Mute'});
v.addEventListener('ended',function(){v.muted=true;v.loop=true;v.play().catch(function(){});b.textContent='▶ Play with sound'});})();</script>"""

def band(title, sub):
    btns = "".join(f'<a class="btn" href="{AMZ[e["key"]]}">{e["name"]} on Amazon</a>' for e in EDITIONS)
    return f"""<section><div class="wrap"><div class="band rv"><span class="float" style="left:5%;top:14%">💗</span><span class="float" style="right:6%;top:20%;animation-delay:-3s">⭐</span>
<h2>{title}</h2><p>{sub}</p><div class="row3">{btns}</div></div></div></section>"""

GAME_YT = "ZwCLW1o27yQ"
GAME_NOTE = '<div class="note">💘 <b>Free sleepover game:</b> <a href="/sleepover-game/">Who\'s My Mystery Crush?</a> Everyone picks a secret crush, then takes turns asking questions and guessing. Free printable and a how-to video.</div>'
GAME_PDF = "/printables/whos-my-mystery-crush-sleepover-game.pdf"
GAME_QS = ["What's their favorite snack?", "What color do they wear the most?", "Are they real or made-up?", "Where would you find them on a Saturday?",
           "What animal are they most like?", "What song plays when they walk in?", "What's their superpower?", "What would they order at a drive-thru?",
           "Where would they go on vacation?", "Would they share their fries?", "What's one word that describes them?", "What would they do at THIS sleepover?",
           "Do their laugh! (no words)", "Do their walk! (no words)"]
GAME_FAQ = [("What ages is the game for?", "It's made for girls about 7 to 14, and it's easy enough for younger siblings to join in."),
            ("What do we need to play?", "Nothing but a few friends. The free printable has the rules, a question list and a heart tracker, but once you know the rules you can play anywhere, even in the car."),
            ("How many players?", "Three or more. It's even more fun with a big sleepover group."),
            ("Does anyone have to share a real crush?", "No. Players can pick anyone everybody in the room would know, like a cartoon character, a singer or an athlete. A real crush is only if they want to."),
            ("Is the printable free?", "Yes, it's free to print for personal use.")]

def game_page():
    fh, fs = faq_block(GAME_FAQ)
    vid = {"@context": "https://schema.org", "@type": "VideoObject", "name": "Who's My Mystery Crush? Free Sleepover Game for Girls (How to Play)",
           "description": "How to play Who's My Mystery Crush?, a free guessing game for sleepovers: pick a secret crush, take turns asking questions, guess right to win a heart.",
           "thumbnailUrl": f"https://i.ytimg.com/vi/{GAME_YT}/hqdefault.jpg", "uploadDate": "2026-11-20", "embedUrl": f"https://www.youtube-nocookie.com/embed/{GAME_YT}",
           "contentUrl": f"https://www.youtube.com/watch?v={GAME_YT}", "duration": "PT1M44S"}
    qs = "".join(f"<li>{esc(q)}</li>" for q in GAME_QS)
    body = f"""<div class="ghero"><div class="narrow"><p class="crumb"><a href="/">Gift guides</a> › Free sleepover game</p>
<span class="kicker">💘 Free printable · sleepover game</span><h1 style="font-size:clamp(32px,5.4vw,52px)">Who's My Mystery Crush? A Free Sleepover Game for Girls</h1>
<p class="lede">Hosting a sleepover? Here's an easy guessing game girls 7–14 can learn in a minute: everyone picks a secret crush, takes turns asking questions, and tries to guess who it is. No supplies needed.</p>
<div class="ctas"><a class="btn" href="{GAME_PDF}" download>Download the free printable (PDF)</a><a class="btn ghost" href="#watch">Watch how to play</a></div></div></div>
<div class="narrow art">
<h2 id="watch">Watch how to play (1:44)</h2>
<div style="position:relative;padding-top:56.25%;border-radius:18px;overflow:hidden;box-shadow:0 20px 40px -20px rgba(90,35,80,.5)"><iframe src="https://www.youtube-nocookie.com/embed/{GAME_YT}" title="How to play Who's My Mystery Crush?" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe></div>
<h2>How to play</h2>
<ol class="ideas">
<li><b>Pick a secret crush.</b> Think of anyone everybody in the room would know: a cartoon character, a movie or book character, a singer, an athlete, a YouTuber, even a famous animal. A real crush is okay too, but only if you want. Keep it in your head, and no switching! Two rules: nobody who is in the room, and keep it kind.</li>
<li><b>Take turns asking.</b> On your turn, pick any player and ask them one question from the list below (or make up your own). They answer about their secret crush, honestly and without saying the name. Then you get one guess.</li>
<li><b>Guess right? Win a heart!</b> They say "You got me!" and pick a brand-new secret crush. Wrong guess? No big deal. It's the next player's turn.</li>
</ol>
<div class="note">🏆 <b>How to win:</b> the first player to 5 hearts wins. Short on time? Play until lights out, and whoever has the most hearts wins. 🤔 <b>Stuck?</b> If 3 guesses in a row miss your crush, give a hint: the first letter of their name.</div>
<h2>The question list</h2>
<ol class="ideas">{qs}</ol>
<p><a class="btn" href="{GAME_PDF}" download>Print the game free (2 pages)</a></p>
{pick("Want the real thing for the sleepover bag? Once the game's over, she can rate her actual crush in her own journal.")}
<h2>Questions</h2>{fh}</div>
<section style="padding-top:40px"><div class="wrap"><h2 class="center">More sleepover &amp; gift ideas</h2>{guide_cards([g for g in GUIDES if 'sleepover' in g['slug']] + [g for g in GUIDES if 'sleepover' not in g['slug']][:5], short=True)}</div></section>
{band("Three covers. One very funny journal.", "Rate My Crush: the crush journal for ages 7–14.")}"""
    return page("sleepover-game/index.html", "Who's My Mystery Crush? Free Printable Sleepover Game for Girls 7–14 | Rate My Crush",
                 "A free printable sleepover game for girls 7–14: everyone picks a secret crush, takes turns asking questions and guessing. Easy rules, a question list and a how-to video. No supplies needed.",
                 body, [vid, fs, crumbs([("Gift guides", "/"), ("Free sleepover game", "/sleepover-game/")])])

def build():
    urls = []
    # ---------- guides ----------
    for g in GUIDES:
        fh, fs = faq_block(g["faq"] + (g.get("sale_faq", []) if SALE_ASOF else []))
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "datePublished": "2026-11-17", "dateModified": TODAY, "author": {"@type": "Person", "name": "Felicia Nevin"},
               "image": SITE + "/img/cover-playful.jpg", "mainEntityOfPage": SITE + "/" + g["slug"] + "/"}
        others = [o for o in GUIDES if o is not g][:6]
        body = f"""<div class="ghero"><div class="narrow"><p class="crumb"><a href="/">Gift guides</a> › {esc(g['kw'])}</p>
<span class="kicker">{GUIDE_EMOJI.get(g['slug'], '🎁')} {esc(g['kw'])} · Updated {dt.date.today().strftime('%B %Y')}</span><h1 style="font-size:clamp(32px,5.4vw,52px)">{esc(g['title'])}</h1>
<p class="lede">{esc(g['intro'])}</p></div></div>
<div class="narrow art">{pick(g['angle'])}<h2>{esc(g['kw'])}: 10 ideas</h2>{ideas(g['items'])}
<div class="note">💡 Tip: pair the journal with a set of gel pens. It doesn't come with pens.</div>{GAME_NOTE if ("sleepover" in g["slug"] or "camp" in g["slug"]) else ""}
<h2>Questions</h2>{fh}</div>
<section style="padding-top:40px"><div class="wrap"><h2 class="center">More gift guides</h2>{guide_cards(others, short=True)}</div></section>
{band("Three covers. One very funny journal.", "Rate My Crush: the crush journal for ages 7–14.")}"""
        art["about"] = {"@type": "Book", "name": "Rate My Crush", "url": SITE + "/rate-my-crush/"}
        art["keywords"] = g["kw"] + ", gift ideas, tween gifts, stocking stuffers, crush journal"
        urls.append(page(g["slug"] + "/index.html", g["title"], g["desc"], body, [art, fs, crumbs([("Gift guides", "/"), (g["kw"], "/" + g["slug"] + "/")])]))
    # ---------- the journal (main landing page) ----------
    fh, fs = faq_block(BOOK_FAQ)
    book = {"@context": "https://schema.org", "@type": "Book", "name": "Rate My Crush", "author": {"@type": "Person", "name": "Felicia Nevin", "url": AUTHOR},
            "bookFormat": "https://schema.org/Paperback", "numberOfPages": 100, "inLanguage": "en", "genre": ["Guided journal", "Children's diary"],
            "brand": {"@id": SITE + "/#brand"}, "isFamilyFriendly": True, "typicalAgeRange": "7-14", "sameAs": list(AMZ.values()), "url": SITE + "/rate-my-crush/",
            "keywords": "crush journal, gift for tween girls, stocking stuffer for tweens, birthday gift for girls 7-14, Valentine's gift for girls, Galentine's gift, journal for girls, screen-free gift",
            "audience": {"@type": "PeopleAudience", "suggestedMinAge": 7, "suggestedMaxAge": 14},
            "description": "A guided crush journal for ages 7–14 with a 10-category star scorecard, a Crush Level heart meter and prompts. Three editions: Playful, Moody and Floral.",
            "workExample": [{"@type": "Book", "name": f"Rate My Crush ({e.title()} Edition)", "url": u, "bookFormat": "https://schema.org/Paperback"} for e, u in AMZ.items()],
            "image": [SITE + f"/img/cover-{e}.jpg" for e in AMZ]}
    body = f"""<section class="hero"><div class="wrap"><div class="rv in">
<span class="kicker">♥ The crush journal for ages 7–14</span>
<h1>Rate the crush. <span class="pop">Track the feels.</span> Laugh about it forever.</h1>
<p class="lede">Rate My Crush is a guided journal where every crush gets a code name, a 10-category star scorecard and a Crush Level. It's screen-free, silly in the best way, and made to be filled in, not left on a shelf.</p>
<div class="ctas"><a class="btn" href="#editions">Pick a cover →</a><a class="btn ghost" href="#inside">Peek inside</a></div>
<div class="chips"><span class="chip">📖 100 guided pages</span><span class="chip">📏 6×9 paperback</span><span class="chip">🎨 3 covers</span><span class="chip">📵 Screen-free</span></div></div>
{hero_stack()}</div></section>{ticker()}
<section id="how"><div class="wrap center"><span class="kicker">📝 How it works</span><h2>One crush. One page. <span class="hand">Zero chill.</span></h2>
<div class="steps" style="text-align:left">{''.join(f'<div class="step rv"><span class="n">{i+1}</span><div class="e">{e}</div><h3>{t}</h3><p style="color:var(--muted);margin:0">{d}</p></div>' for i, (e, t, d) in enumerate(STEPS))}</div></div></section>
{demo()}{film_section()}{editions()}{gallery()}{reasons()}{occasions()}{author()}{social_section()}
<section id="faq"><div class="narrow"><h2 class="center">Questions grown-ups ask</h2>{fh}</div></section>
<section style="padding-top:20px"><div class="wrap"><h2 class="center">Gift guides</h2>{guide_cards(GUIDES, short=True)}</div></section>
{band("Ready to make someone giggle?", "Pick their cover. Same prompts inside, each styled to match.")}"""
    urls.append(page("rate-my-crush/index.html", "Rate My Crush: The Crush Journal Gift for Ages 7–14 | Stocking Stuffer & Birthday Gift",
                     "Rate My Crush is a guided crush journal for ages 7–14 and a fun, screen-free gift: stocking stuffer, birthday, Valentine's or Galentine's. Code names, a 10-category star scorecard and a Crush Level. Playful, Moody and Floral covers on Amazon.", body, [book, fs]))
    # ---------- free sleepover game (Felicia 11/20: simple, no dice; how-to video on YouTube) ----------
    urls.append(game_page())
    # ---------- home ----------
    body = f"""<section class="hero"><div class="wrap"><div class="rv in"><span class="kicker">🎁 Gift guides for ages 7–14</span>
<h1>Gifts that get a <span class="pop">gasp</span>, a giggle and actually get used.</h1>
<p class="lede">Gift ideas for the moms, aunts, grandmas and big sisters shopping for a tween. Practical, fun and a little nostalgic, from the makers of Rate My Crush.</p>
<div class="ctas"><a class="btn" href="#guides">Browse gift guides →</a><a class="btn ghost" href="/rate-my-crush/">Meet Rate My Crush</a></div></div>
{hero_stack()}</div></section>{ticker()}
<section id="guides"><div class="wrap center"><span class="kicker">📚 Gift guides</span><h2>Find the perfect gift, <span class="hand">fast.</span></h2>{guide_cards(GUIDES)}</div></section>
<section style="padding-top:10px"><div class="narrow">{pick("Our own pick for every list: the gift that gets a gasp, then gets filled in.")}</div></section>
{social_section()}{band("Three covers. One very funny journal.", "Rate My Crush: the crush journal for ages 7–14.")}"""
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Rate My Crush", "url": SITE + "/", "publisher": {"@id": SITE + "/#brand"}}
    il = {"@context": "https://schema.org", "@type": "ItemList", "name": "Gift guides for tweens ages 7–14", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + "/" + g["slug"] + "/", "name": g["title"]} for i, g in enumerate(GUIDES)]}
    urls.insert(0, page("index.html", ("Gift Ideas for Tween Girls 7–14: Black Friday, Christmas & Stocking Stuffers | Rate My Crush" if BF_SEASON else "Gift Ideas for Tween Girls 7–14: Christmas, Birthday & Valentine's | Rate My Crush"), ("Black Friday and Cyber Monday gift ideas for tween girls 7–14, plus g" if BF_SEASON else "G") + "ift ideas for tween girls ages 7–14: Christmas gifts, stocking stuffers, birthday gifts, Valentine's and Galentine's ideas, plus gifts for nieces and granddaughters, from the makers of the Rate My Crush crush journal.", body, [site, il]))
    # ---------- 404, robots, sitemap, llms.txt, CNAME ----------
    page("404.html", "Page not found | Rate My Crush", "Page not found.",
         '<section class="hero"><div class="narrow center"><h1>Oops, that page ghosted us 👻</h1><p class="lede" style="margin:0 auto 20px">It happens to the best crushes.</p><a class="btn" href="/rate-my-crush/">Meet Rate My Crush</a> <a class="btn ghost" href="/">See gift guides</a></div></section>')
    bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckDuckBot", "CCBot"]
    open(os.path.join(HERE, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(HERE, INDEXNOW + ".txt"), "w").write(INDEXNOW)
    full = ["# Rate My Crush: full facts for AI assistants", "", "Rate My Crush is a guided crush journal for ages 7–14 by Felicia Nevin, an independent author writing from East Tennessee. It is sold on Amazon.", "",
            "## Product facts", "- Ages: 7–14", "- 100 pages, 6x9 inch paperback (Playful Edition also in hardcover)",
            "- Editions (same prompts inside, each styled to match its cover): " + "; ".join(f"{e['name']} ({e['vibe']}, {e['look']}) {AMZ[e['key']]}" for e in EDITIONS),
            "- Each crush page: code name, where they're seen most, their squad, what they're into, favorites, a 10-category star scorecard (Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades, Bonus Spark; 50 stars total), Crush Level meter (1–15 Tiny Crush, 16–30 Pretty Cute, 31–40 Big Crush, 41–50 Totally Obsessed), prompts (Best Thing About Them; Funniest/Best Memory I Have; Why I Think We'd Be a Good Match).",
            "- Does not include pens, stickers or a lock.", "",
            "## Good gift for", "- Christmas gifts and stocking stuffers for tweens (fits most stockings)", "- Birthday gifts for girls ages 7–14", "- Valentine's Day (non-candy) and Galentine's Day", "- Easter baskets", "- Sleepovers, slumber parties and camp care packages", "- Gifts from aunts, grandmothers and big sisters", "",
            "## FAQ"] + [f"Q: {q}\nA: {a}" for q, a in BOOK_FAQ] + ["", "## Gift guides"] + [f"- {g['title']}: {SITE}/{g['slug']}/" for g in GUIDES] + ["", "## Official links", f"- Website: {SITE}/rate-my-crush/ (also ratemycrush.com)"] + [f"- {n}: {u}" for n, u, h, sv in SOCIAL]
    open(os.path.join(HERE, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full) + "\n")
    open(os.path.join(HERE, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
        + "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod>" + ("".join(f"<image:image><image:loc>{SITE}/img/{im}</image:loc></image:image>" for im in ["cover-playful.jpg", "cover-moody.jpg", "cover-floral.jpg", "page-playful-score.jpg", "page-playful-prompts.jpg", "page-moody-score.jpg", "page-floral-score.jpg"]) if u.endswith("/rate-my-crush/") else "") + "</url>" for u in urls) + "</urlset>\n")
    llms = ["# Rate My Crush", "", "> Official site for Rate My Crush, a guided crush journal for ages 7–14 by Felicia Nevin (sold on Amazon in Playful, Moody and Floral editions), plus gift guides for adults shopping for tweens.", "",
            "## The journal", f"- [Rate My Crush facts, pages and FAQ]({SITE}/rate-my-crush/): ages 7–14, 100 pages, 6x9 paperback (Playful also in hardcover), 10-category star scorecard (50 stars), Crush Level heart meter (Tiny Crush, Pretty Cute, Big Crush, Totally Obsessed), prompts; three editions with the same prompts styled to match each cover.",
            f"- Amazon: Playful {AMZ['playful']} · Moody {AMZ['moody']} · Floral {AMZ['floral']}",
            "- Social: " + " · ".join(f"{n} {u}" for n, u, h, s in SOCIAL), "", "## Gift guides"] + [f"- [{g['title']}]({SITE}/{g['slug']}/): {g['desc']}" for g in GUIDES] + ["", "## More", f"- [Full facts]({SITE}/llms-full.txt)"]
    open(os.path.join(HERE, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms) + "\n")
    open(os.path.join(HERE, "CNAME"), "w").write("gifts.ratemycrush.com\n")
    open(os.path.join(HERE, ".nojekyll"), "w").write("")
    print(len(urls), "pages"); [print(u) for u in urls]

if __name__ == "__main__":
    build()
