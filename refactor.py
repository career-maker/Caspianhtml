import os
import re

files = [
    'index.html',
    'about.html',
    'products.html',
    'product-detail.html',
    'blog.html',
    'blog-detail.html',
    'contact.html',
    'privacy-policy.html'
]

for filename in files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert components.css
    if 'components.css' not in content:
        content = content.replace('</head>', '  <link href="components.css" rel="stylesheet">\n</head>')
        
    # 2. Insert components.js
    if 'components.js' not in content:
        content = content.replace('</body>', '<script src="components.js"></script>\n</body>')

    # 3. Replace <header> with placeholder
    header_pattern = re.compile(r'<header>.*?</header>', re.DOTALL)
    if header_pattern.search(content):
        content = header_pattern.sub('<div id="header-placeholder"></div>', content)
        
    # 4. Remove drawer-backdrop and mobile-drawer
    drawer_backdrop = re.compile(r'<div class="drawer-backdrop"[^>]*></div>', re.DOTALL)
    content = drawer_backdrop.sub('', content)
    
    drawer_pattern = re.compile(r'<aside class="mobile-drawer"[^>]*>.*?</aside>', re.DOTALL)
    content = drawer_pattern.sub('', content)

    # 5. Replace <footer> with placeholder
    footer_pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub('<div id="footer-placeholder"></div>', content)

    # 6. Remove specific scripts
    # Script 1: header scroll
    script1 = re.compile(r'<script>\s*\(function\(\)\{\s*var header=document\.querySelector\(\'header\'\);.*?</script>', re.DOTALL)
    content = script1.sub('', content)
    
    # Script 2: hamburger (sometimes it's a separate script block, sometimes merged)
    script2 = re.compile(r'\(function\(\)\{\s*var btn=document\.getElementById\(\'hamburgerBtn\'\);.*?\n\}\)\(\);\n', re.DOTALL)
    content = script2.sub('', content)
    
    # Script 3: footer accordion
    script3 = re.compile(r'<script>\s*\(function\(\)\{\s*document\.querySelectorAll\(\'\.footer-accordion h3\'\).*?</script>', re.DOTALL)
    content = script3.sub('', content)

    # Clean up empty script tags left behind
    content = re.compile(r'<script>\s*</script>', re.DOTALL).sub('', content)

    # 7. Remove CSS blocks using regex
    # We will remove the exact css blocks that we extracted.
    css_patterns = [
        r'/\* HEADER.*?\nheader\.scrolled \.cta-btn:hover\{.*?\}',
        r'/\* HAMBURGER.*?\nheader\.scrolled \.hamburger span\{.*?\}',
        r'/\* MOBILE DRAWER.*?\nbody\.drawer-open\{overflow:hidden;\}',
        r'/\* FOOTER —.*?\n\.footer-bottom strong\{color:#fff;\}',
        r'/\* FOOTER MOBILE ACCORDION.*?\n\.footer-content\{overflow:hidden;\}',
    ]
    for p in css_patterns:
        content = re.sub(p, '', content, flags=re.DOTALL)

    # Remove media query specific content for header/footer
    # This is a bit trickier, but we can do string replacements for known exact lines
    media_queries_to_remove = [
        "nav{display:none;}",
        ".phone-cta{display:none;}",
        ".hamburger{display:flex;}",
        ".footer-grid{grid-template-columns:1fr 1fr;}",
        ".footer-grid{grid-template-columns:1fr 1fr;text-align:left;}",
        "header{padding:1rem 1.25rem;}",
        "header.scrolled{padding:.7rem 1.25rem;}",
        ".cta-btn{display:none;}",
        ".footer-grid{grid-template-columns:1fr;text-align:center;}",
        ".social-links{justify-content:center;}",
        ".footer-contact-item{justify-content:center;}",
        ".footer-bottom{flex-direction:column;text-align:center;}",
        ".logo img{height:52px;}",
        ".drawer-logo{height:42px;}",
        ".mobile-drawer{width:88vw;padding:1.3rem 1.4rem 1.6rem;}",
        ".footer-logo-badge{width:80px;height:80px;}",
        ".footer-grid{grid-template-columns:1fr;text-align:left;}",
        ".footer-section:first-child{text-align:center;margin-bottom:.5rem;}",
        ".footer-section:first-child .footer-logo-badge{margin-left:auto;margin-right:auto;}",
        ".footer-section:first-child .social-links{justify-content:center;}",
        ".footer-accordion{border-bottom:1px solid rgba(255,255,255,.15);padding-bottom:.9rem;}",
        ".footer-accordion h3{cursor:pointer;margin-bottom:0;padding:.4rem 0;}",
        ".footer-toggle-icon{display:block;}",
        ".footer-accordion .footer-content{max-height:0;transition:max-height .4s ease;}",
        ".footer-accordion.open .footer-content{max-height:400px;padding-top:.8rem;}",
    ]
    for mq in media_queries_to_remove:
        content = content.replace("  " + mq + "\n", "")
        content = content.replace(mq + "\n", "")

    # Clean up any empty media queries
    content = re.sub(r'@media[^{]+\{\s*\}', '', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refactored {filename}")
