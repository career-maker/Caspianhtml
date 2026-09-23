import re

with open('product-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove force-sticky-header from body
html = html.replace('<body class="force-sticky-header">', '<body>')

# Add small hero CSS
hero_css = '''
    /* SMALL HERO BANNER */
    .hero-small {
      position: relative;
      height: 35vh;
      min-height: 250px;
      background: radial-gradient(circle, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.6) 100%), url('images/hero-seafood.jpg') center/cover;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(1.5rem, 4vw, 3.5rem);
      color: #fff;
      text-align: center;
    }
    .hero-small .hero-inner {
      max-width: 800px;
      margin: 0 auto;
      margin-top: 40px;
    }
    .hero-small h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.4rem, 5vw, 4rem);
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
'''
html = html.replace('  </style>', hero_css + '  </style>')

# Add hero section HTML just after header placeholder
hero_html = '''  <div id="header-placeholder"></div>

  <section class="hero-small">
    <div class="hero-inner">
      <h1>Carabinaro Shrimp</h1>
    </div>
  </section>'''
html = html.replace('  <div id="header-placeholder"></div>', hero_html)

# Remove the h1 from the product-info grid since it's now in the banner
html = html.replace('        <h1>Carabinaro Shrimp</h1>\n', '')
# Alternatively, I can leave the product-desc, etc.

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)
