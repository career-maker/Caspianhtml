import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Replacements
css_old = """
.product-card{background:#fff;border:1px solid #eee;padding:clamp(1.8rem,3vw,2.5rem) 1.2rem 1.6rem;display:flex;flex-direction:column;align-items:center;transition:box-shadow .35s ease,transform .35s ease;}
.product-card:hover{box-shadow:0 18px 40px rgba(0,0,0,.08);transform:translateY(-4px);}
.product-icon{width:100%;aspect-ratio:1/1;overflow:hidden;margin-bottom:1.4rem;}
.product-icon img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.16,1,.3,1);}
.product-card:hover .product-icon img{transform:scale(1.08);}
.product-divider{width:36px;height:1px;background:var(--rich-gold);margin-bottom:min(1rem, 2vh);}
.product-name{font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--charcoal);text-align:center;}
""".strip()

css_new = """
.product-card{background:transparent;border:none;padding:0;display:flex;flex-direction:column;cursor:pointer;}
.product-card:hover .product-info { opacity: 0; }
.product-card:hover .product-overlay { opacity: 1; visibility: visible; }
.product-icon{position:relative;width:100%;aspect-ratio:1/1;overflow:hidden;}
.product-icon img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.16,1,.3,1);}
.product-card:hover .product-icon img{transform:scale(1.08);}
.product-overlay{position:absolute;top:8%;bottom:8%;left:8%;right:8%;background:rgba(255,255,255,0.95);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:1.5rem;opacity:0;visibility:hidden;transition:opacity .4s ease,visibility .4s ease;}
.product-overlay h3{font-family:'Manrope',sans-serif;font-size:1.1rem;font-weight:700;margin-bottom:1rem;color:var(--charcoal);text-transform:uppercase;}
.product-overlay p{font-family:'Manrope',sans-serif;font-size:12px;line-height:20px;color:#5a5a56;margin-bottom:1.5rem;}
.view-link{font-family:'Manrope',sans-serif;font-size:12px;color:var(--deep-teal);text-decoration:none;display:flex;align-items:center;gap:0.4rem;transition:color .3s ease;}
.view-link:hover{color:var(--charcoal);}
.view-link svg{width:16px;height:16px;stroke:currentColor;fill:none;}
.product-info{display:flex;justify-content:space-between;align-items:center;padding-top:1rem;transition:opacity .3s ease;}
.product-name{font-family:'Manrope',sans-serif;font-size:1rem;font-weight:700;text-transform:uppercase;color:var(--charcoal);}
""".strip()

content = content.replace(css_old, css_new)

def replacer(match):
    img_src = match.group(1)
    img_alt = match.group(2)
    name = match.group(3)
    
    svg_arrow = '<svg viewBox="0 0 24 24" stroke-width="1.5"><path d="M2 12h14"/><circle cx="18" cy="12" r="2"/></svg>'

    return f'''      <div class="product-card reveal">
        <div class="product-icon">
          <img src="{img_src}" alt="{img_alt}">
          <div class="product-overlay">
            <h3>{name}</h3>
            <p>Sustainably sourced and handled with the highest quality standards, our products deliver premium taste, consistency, and freshness for global food service and retail industries.</p>
            <a href="#" class="view-link">View More {svg_arrow}</a>
          </div>
        </div>
        <div class="product-info">
          <div class="product-name">{name}</div>
          <a href="#" class="view-link">View More {svg_arrow}</a>
        </div>
      </div>'''

pattern = re.compile(
    r'<div class="product-card reveal">\s*<div class="product-icon"><img src="([^"]+)" alt="([^"]+)"></div>\s*<div class="product-divider"></div>\s*<div class="product-name">([^<]+)</div>\s*</div>'
)

content = pattern.sub(replacer, content)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated product cards CSS and HTML')
