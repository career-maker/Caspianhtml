import re
with open('products.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'\s*<select class="sort-select">.*?</select>', '', html, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(html)
