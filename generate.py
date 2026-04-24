import json, os

with open('data/countries.json') as f:
    countries = json.load(f)

template = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{name} Live Cam Shows</title>
<link rel="stylesheet" href="../style.css">
</head>
<body onload="initPage('{code}','{name}')">
<header>{name} Live Cam Shows</header>
<nav id="nav"></nav>
<div id="rooms" class="grid"></div>
<footer>
<p>18+ ONLY. ADULT CONTENT.</p>
<p>Affiliate links included.</p>
</footer>
<script src="../script.js"></script>
</body>
</html>'''

os.makedirs('country', exist_ok=True)

for c in countries:
    with open(f"country/{c['slug']}.html","w") as f:
        f.write(template.format(code=c['code'], name=c['name']))

print("Country pages generated!")
