import re
import os

crumbs_css = '''
/* BREADCRUMB */
.crumbs { max-width: 1500px; margin: 0 auto; padding: clamp(1.2rem, 2.5vw, 1.8rem) var(--gutter) 0; font-size: clamp(.74rem, 1.2vw, .85rem); color: #7a7a74; display: flex; flex-wrap: wrap; align-items: center; gap: .5rem; font-family: 'Manrope', sans-serif; }
.crumbs a { color: #7a7a74; text-decoration: none; transition: color .3s ease; }
.crumbs a:hover { color: var(--deep-teal); }
.crumbs .sep { width: 5px; height: 5px; border-top: 1.2px solid #b5b5ad; border-right: 1.2px solid #b5b5ad; transform: rotate(45deg); }
.crumbs .current { color: var(--charcoal); font-weight: 600; }
'''

# 1. Add crumbs CSS to components.css
with open('components.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '/* BREADCRUMB */' not in css:
    with open('components.css', 'a', encoding='utf-8') as f:
        f.write('\n' + crumbs_css)

# 2. Delete crumbs CSS from product-detail.html
with open('product-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'\s*/\* BREADCRUMB \*/.*?\.current\{.*?\}', '', html, flags=re.DOTALL)
with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add crumbs HTML to other pages
pages = {
    'about.html': 'About Us',
    'products.html': 'Products',
    'blog.html': 'Blog',
    'contact.html': 'Contact Us',
    'privacy-policy.html': 'Privacy Policy',
    'terms.html': 'Terms of Service'
}

for page, title in pages.items():
    if not os.path.exists(page): continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<div class="crumbs"' in content:
        continue # Already has crumbs
        
    crumbs_html = f'''</section>

  <div class="crumbs" role="navigation" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span class="sep"></span>
    <span class="current">{title}</span>
  </div>'''

    # Insert crumbs right after the hero section
    content = re.sub(r'</section>', crumbs_html, content, count=1)
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

print("Breadcrumbs added to all pages.")
