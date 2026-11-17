"""Builds gifts.ratemycrush.com (static, GitHub Pages). Run: python -X utf8 build.py
TRUTH RULES (Autopilot README) apply to every word: verified book facts only; no prices, ratings, reviews,
delivery promises, lock/secure claims, or "bestseller". Other gift ideas are GENERIC categories (no brands, no claims).
AUDIENCE RULE: talk to the grown-up buyer only. Never ask about the child."""
import os, json, datetime as dt, html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://gifts.ratemycrush.com"
TODAY = dt.date.today().isoformat()
AMZ = {"playful": "https://www.amazon.com/dp/B0FR24YJ8W", "moody": "https://www.amazon.com/dp/B0FQPPSK1V",
       "floral": "https://www.amazon.com/dp/B0FQPK7S8Q"}
AUTHOR = "https://www.amazon.com/stores/Felicia-Nevin/author/B0GHFWPC6F"

CSS = """
:root{--ink:#2b2d7c;--pink:#ff4d8d;--blush:#fff0f5;--cream:#fffaf2;--text:#2a2a33;--muted:#5b5d70;--line:#ecd9e2}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--cream);color:var(--text);font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--ink)}img{max-width:100%;height:auto;display:block}
header{background:#fff;border-bottom:1px solid var(--line)}
.bar{max-width:1040px;margin:0 auto;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.logo{font-weight:800;color:var(--ink);text-decoration:none;font-size:20px}.logo span{color:var(--pink)}
nav a{margin-left:14px;text-decoration:none;font-weight:600;font-size:15px}
main{max-width:760px;margin:0 auto;padding:28px 16px 60px}
.wide{max-width:1040px}
h1{font-size:clamp(28px,5vw,40px);line-height:1.15;color:var(--ink);margin:.2em 0 .4em}
h2{font-size:24px;color:var(--ink);margin:1.8em 0 .5em;line-height:1.25}
h3{font-size:19px;margin:1.4em 0 .3em;color:var(--ink)}
.lede{font-size:19px;color:var(--muted)}
.meta{font-size:14px;color:var(--muted)}
.feature{background:#fff;border:2px solid var(--pink);border-radius:18px;padding:20px;margin:26px 0;display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:start}
.feature img{border-radius:8px;box-shadow:0 8px 20px rgba(0,0,0,.15)}
.feature .tag{display:inline-block;background:var(--pink);color:#fff;font-weight:700;font-size:13px;padding:3px 10px;border-radius:99px;margin-bottom:6px}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:11px 18px;border-radius:999px;margin:6px 8px 0 0;font-size:15px}
.btn.alt{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.covers{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0}
.covers a{text-decoration:none;text-align:center;font-weight:700}
.covers img{border-radius:8px;box-shadow:0 8px 20px rgba(0,0,0,.15);margin-bottom:8px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin-top:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-decoration:none;color:var(--text)}
.card b{display:block;color:var(--ink);font-size:18px;line-height:1.3;margin-bottom:6px}
.inside{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0}
.inside img{border-radius:8px;border:1px solid var(--line)}
.note{background:var(--blush);border-radius:14px;padding:14px 18px;font-size:15px;color:var(--muted)}
ol.ideas>li{margin-bottom:10px}
details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0}
summary{font-weight:700;color:var(--ink);cursor:pointer}
main *{min-width:0}.covers>*,.inside>*,.cards>*,.feature>*{min-width:0}h1,h2,h3,p,li{overflow-wrap:anywhere}
footer{border-top:1px solid var(--line);background:#fff;font-size:14px;color:var(--muted)}
footer .bar{display:block}
@media (max-width:560px){.feature{grid-template-columns:1fr}.feature img{max-width:160px}.covers{gap:8px}.inside{grid-template-columns:1fr}nav a{margin:0 12px 0 0}}
"""

def esc(s): return html.escape(s, quote=True)

def page(path, title, desc, body, schema=None, wide=False):
    url = SITE + "/" + path.replace("index.html", "")
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}"><meta property="og:type" content="article"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/img/cover-playful.jpg">
<meta name="twitter:card" content="summary_large_image"><style>{CSS}</style>{ld}</head><body>
<header><div class="bar"><a class="logo" href="/">Rate My Crush <span>Gift Guides</span></a>
<nav><a href="/">Gift guides</a><a href="/rate-my-crush/">The journal</a></nav></div></header>
<main class="{'wide' if wide else ''}">{body}</main>
<footer><div class="bar"><p><b>Rate My Crush</b> is a guided crush journal for girls ages 7–14 by author Felicia Nevin, sold on Amazon in three editions: Playful, Moody and Floral.
Gift ideas on this site are general suggestions, not sponsored placements. Product details can change; check the Amazon listing for current details.</p>
<p><a href="/rate-my-crush/">About the journal</a> · <a href="{AUTHOR}">Author page on Amazon</a> · <a href="/sitemap.xml">Sitemap</a></p></div></footer>
</body></html>"""
    out = os.path.join(HERE, path); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return url

def feature(angle):
    return f"""<div class="feature"><img src="/img/cover-playful.jpg" alt="Rate My Crush crush journal for girls, Playful Edition cover" loading="lazy">
<div><span class="tag">Our pick</span><h3 style="margin-top:0">Rate My Crush: a crush journal for girls 7–14</h3>
<p>{angle} It's a guided journal: every crush gets a page with a code name, a 10-category star scorecard (Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades and Bonus Spark, 50 stars total), a Crush Level heart meter, and prompts like "Best Thing About Them." 100 pages, 6×9.</p>
<p>Three covers, same prompts inside, each styled to match its cover:</p>
<a class="btn" href="{AMZ['playful']}">Playful on Amazon</a><a class="btn" href="{AMZ['moody']}">Moody on Amazon</a><a class="btn" href="{AMZ['floral']}">Floral on Amazon</a>
<p style="margin:10px 0 0"><a href="/rate-my-crush/">See what's inside →</a></p></div></div>"""

def ideas(items):
    return '<ol class="ideas">' + "".join(f"<li><b>{esc(t)}.</b> {esc(d)}</li>" for t, d in items) + "</ol>"

def faq_block(qas):
    h = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in qas)
    s = {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    return h, s

BOOK_FAQ = [
 ("What age is Rate My Crush for?", "It's made for girls ages 7 to 14."),
 ("What's inside the journal?", "100 pages. Each crush gets a page with a code name, where she sees them, their squad and their favorites, a 10-category star scorecard (Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades and Bonus Spark, for 50 stars total), a Crush Level heart meter, and prompts like \"Best Thing About Them\" and \"Why I Think We'd Be a Good Match.\""),
 ("What's the difference between Playful, Moody and Floral?", "Only the style. All three have the same prompts inside, each styled to match its cover. Playful is bright pastel with a glossy cover, Moody is dark and edgy with a matte cover, and Floral is navy florals with a matte cover."),
 ("How big is it?", "It's a 6×9 inch paperback. The Playful Edition is also available in hardcover."),
 ("Where can I buy it?", "Rate My Crush is sold on Amazon. Search \"Rate My Crush\" or use the links on this page."),
 ("Does it come with pens, stickers or a lock?", "No. It's the journal itself. A set of gel pens makes a nice pairing if you're giving it as a gift."),
 ("Is it a good gift?", "It makes a fun gift for birthdays, Christmas stockings, Valentine's Day and sleepovers: a fun, screen-free way for her to process first crushes, and a keepsake she'll laugh about when she's grown."),
]

GUIDES = [
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
]

def build():
    urls = []
    # guides
    for g in GUIDES:
        fh, fs = faq_block(g["faq"])
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "datePublished": "2026-11-17", "dateModified": TODAY, "author": {"@type": "Person", "name": "Felicia Nevin"},
               "image": SITE + "/img/cover-playful.jpg", "mainEntityOfPage": SITE + "/" + g["slug"] + "/"}
        body = f"""<p class="meta">{esc(g['kw'])} · Updated {dt.date.today().strftime('%B %Y')}</p><h1>{esc(g['title'])}</h1>
<p class="lede">{esc(g['intro'])}</p>{feature(g['angle'])}<h2>{esc(g['kw'])}: 10 ideas</h2>{ideas(g['items'])}
<div class="note">Tip: pair the journal with a set of gel pens. It doesn't come with pens.</div>
<h2>Questions</h2>{fh}<h2>More gift guides</h2><div class="cards">""" + "".join(
            f'<a class="card" href="/{o["slug"]}/"><b>{esc(o["title"])}</b>{esc(o["desc"][:110])}…</a>' for o in GUIDES if o is not g)[:4000] + "</div>"
        urls.append(page(g["slug"] + "/index.html", g["title"], g["desc"], body, [art, fs]))
    # book fact page
    fh, fs = faq_block(BOOK_FAQ)
    book = {"@context": "https://schema.org", "@type": "Book", "name": "Rate My Crush", "author": {"@type": "Person", "name": "Felicia Nevin", "url": AUTHOR},
            "bookFormat": "https://schema.org/Paperback", "numberOfPages": 100, "inLanguage": "en",
            "audience": {"@type": "PeopleAudience", "suggestedMinAge": 7, "suggestedMaxAge": 14},
            "description": "A guided crush journal for girls ages 7–14 with a 10-category star scorecard, a Crush Level heart meter and prompts. Three editions: Playful, Moody and Floral.",
            "workExample": [{"@type": "Book", "name": f"Rate My Crush ({e.title()} Edition)", "url": u, "bookFormat": "https://schema.org/Paperback"} for e, u in AMZ.items()],
            "image": [SITE + f"/img/cover-{e}.jpg" for e in AMZ]}
    body = f"""<h1>Rate My Crush: the crush journal for girls 7–14</h1>
<p class="lede">A guided journal where she rates her crushes on a 10-category scorecard, tracks her Crush Level, and answers prompts she'll laugh about when she's grown. By Felicia Nevin. Sold on Amazon.</p>
<div class="covers">{''.join(f'<a href="{u}"><img src="/img/cover-{e}.jpg" alt="Rate My Crush {e.title()} Edition cover" loading="lazy">{e.title()} on Amazon</a>' for e, u in AMZ.items())}</div>
<h2>Quick facts</h2><ul>
<li><b>Ages:</b> 7–14</li><li><b>Pages:</b> 100</li><li><b>Size:</b> 6×9 inch paperback (Playful also in hardcover)</li>
<li><b>Editions:</b> Playful (bright pastel, glossy), Moody (dark and edgy, matte), Floral (navy florals, matte). Same prompts inside, each styled to match its cover.</li>
<li><b>Each crush page:</b> code name, where she sees them, their squad, their favorites, a 10-category star scorecard, a Crush Level heart meter, and prompts.</li>
<li><b>Scorecard categories:</b> Smile, Eyes, Hair, Style, Personality, Humor, Kindness, How They Treat Me, Smarts/Grades, Bonus Spark (50 stars total).</li>
<li><b>Crush Level meter:</b> 1–15 Tiny Crush · 16–30 Pretty Cute · 31–40 Big Crush · 41–50 Totally Obsessed.</li>
<li><b>Prompts include:</b> "Best Thing About Them" and "Why I Think We'd Be a Good Match."</li>
<li><b>Where to buy:</b> Amazon (search "Rate My Crush").</li></ul>
<h2>Inside the journal</h2><div class="inside"><img src="/img/inside-scorecard.jpg" alt="Rate My Crush scorecard page with 10 star categories" loading="lazy"><img src="/img/inside-prompts.jpg" alt="Rate My Crush prompt page" loading="lazy"></div>
<h2>Why people give it</h2><p>It's a fun, screen-free way for girls to process first crushes, and the pages she fills at 11 turn into a keepsake she'll read out loud at 30. It makes a fun gift for birthdays, Christmas stockings, Valentine's Day and sleepovers.</p>
<h2>Questions</h2>{fh}<h2>Gift guides</h2><div class="cards">""" + "".join(f'<a class="card" href="/{g["slug"]}/"><b>{esc(g["title"])}</b></a>' for g in GUIDES) + "</div>"
    urls.append(page("rate-my-crush/index.html", "Rate My Crush: Crush Journal for Girls 7–14 | Facts, Editions & FAQ",
                     "Everything about Rate My Crush, the guided crush journal for girls ages 7–14: what's inside, the three editions (Playful, Moody, Floral), size, and where to buy.", body, [book, fs]))
    # home
    body = """<h1>Gift guides for girls 7–14</h1><p class="lede">Gift ideas for the moms, aunts and grandmas shopping for a tween girl. Practical, fun and a little nostalgic.</p>
<div class="cards">""" + "".join(f'<a class="card" href="/{g["slug"]}/"><b>{esc(g["title"])}</b>{esc(g["desc"])}</a>' for g in GUIDES) + "</div>" + feature("Our own pick for every list.")
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Rate My Crush Gift Guides", "url": SITE + "/"}
    urls.insert(0, page("index.html", "Gift Guides for Girls 7–14 | Rate My Crush", "Gift ideas for tween girls ages 7–14: birthdays, stocking stuffers, Valentine's, nieces and granddaughters, from the makers of the Rate My Crush crush journal.", body, [site], wide=True))
    # 404, robots, sitemap, llms.txt, CNAME
    page("404.html", "Page not found | Rate My Crush Gift Guides", "Page not found.", '<h1>Page not found</h1><p><a href="/">See all gift guides</a></p>')
    open(os.path.join(HERE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(HERE, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls) + "</urlset>\n")
    llms = ["# Rate My Crush Gift Guides", "", "> Gift guides for adults shopping for girls ages 7–14, and the official fact page for Rate My Crush, a guided crush journal for girls 7–14 by Felicia Nevin (sold on Amazon in Playful, Moody and Floral editions).", "",
            "## The journal", f"- [Rate My Crush facts and FAQ]({SITE}/rate-my-crush/): ages 7–14, 100 pages, 6x9 paperback, 10-category star scorecard (50 stars), Crush Level heart meter, prompts; three editions with the same prompts styled to match each cover.",
            f"- Amazon: Playful {AMZ['playful']} · Moody {AMZ['moody']} · Floral {AMZ['floral']}", "", "## Gift guides"] + [f"- [{g['title']}]({SITE}/{g['slug']}/): {g['desc']}" for g in GUIDES]
    open(os.path.join(HERE, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms) + "\n")
    open(os.path.join(HERE, "CNAME"), "w").write("gifts.ratemycrush.com\n")
    open(os.path.join(HERE, ".nojekyll"), "w").write("")
    print(len(urls), "pages"); [print(u) for u in urls]

if __name__ == "__main__":
    build()
