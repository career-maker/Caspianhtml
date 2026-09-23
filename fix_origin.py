import re

with open('product-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacement = '''          <div class="info-group">
            <div class="info-label">Origin</div>
            <div class="origin-box">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 500" width="28" height="28" style="border-radius: 50%; border: 1px solid #ddd; object-fit: cover; display: block;">
                <rect width="750" height="500" fill="#c60b1e"/>
                <rect y="125" width="750" height="250" fill="#ffc400"/>
                <circle cx="250" cy="250" r="45" fill="#c60b1e" opacity="0.8"/>
              </svg>
              Spain
            </div>
          </div>'''

html = re.sub(r'          <div class="info-group">\s*<div class="info-label">Origin</div>\s*<div class="origin-box">.*?</div>\s*</div>', replacement, html, flags=re.DOTALL)

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)
