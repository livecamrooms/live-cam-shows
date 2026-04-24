import json, os

API_SAMPLE = [
 {"username":"HotModel","image_url":"https://via.placeholder.com/300","num_users":1234,"url":"https://chaturbate.com/?wm=T2CSW"},
 {"username":"SexyGirl","image_url":"https://via.placeholder.com/300","num_users":845,"url":"https://chaturbate.com/?wm=T2CSW"}
]

def render_cards():
 return "".join([f'''
 <div class="card">
  <a href="{r['url']}" target="_blank">
   <img src="{r['image_url']}">
   <div class="overlay">🔴 LIVE</div>
  </a>
  <div class="info">
   <b>{r['username']}</b><br>
   🔥 {r['num_users']} watching
   <a class="btn" href="{r['url']}" target="_blank">JOIN NOW</a>
  </div>
 </div>''' for r in API_SAMPLE])

template = '''<html>
<head>
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header>{title}</header>
<div class="grid">
{cards}
</div>
<section>
<h2>{title}</h2>
<p>{desc}</p>
</section>
<footer>18+ Affiliate site</footer>
</body>
</html>'''

os.makedirs("country", exist_ok=True)
os.makedirs("tags", exist_ok=True)

countries=json.load(open("data/countries.json"))

for c in countries:
 html=template.format(
  title=f"{c['name']} Live Cam Shows",
  desc=f"Watch {c['name']} live cam girls streaming now.",
  cards=render_cards()
 )
 open(f"country/{c['slug']}.html","w").write(html)

tags=["milf","teen","asian","latina","ebony","couple","blonde"]

for t in tags:
 html=template.format(
  title=f"{t.upper()} Live Cam Shows",
  desc=f"Watch the hottest {t} cam girls live now.",
  cards=render_cards()
 )
 open(f"tags/{t}.html","w").write(html)

print("Generated 100+ SEO pages")
