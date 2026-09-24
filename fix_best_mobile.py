import re

with open('about.html', 'r', encoding='utf-8') as f:
    css = f.read()

# I will update the media query at max-width: 1024px for best-section
# and also update the header for best-card (removing the sunglasses text and putting something about production)
# Actually, they just said "on mobile the background photo of this section ... is not properly responsive"

replacement = '''
  /* @media (max-width:1024px) overrides for best-section */
    .best-section { min-height: auto; }
    .best-bg { position: static; height: 400px; }
    .best-card { position: static; width: 100%; margin-top: 0; min-height: auto; }
'''

# Find the @media (max-width:1024px) block and replace the best-card part
css = re.sub(
    r'\.best-card\s*\{\s*position:\s*static;\s*width:\s*100%;\s*margin-top:\s*0;\s*min-height:\s*auto;\s*\}',
    r'.best-section { min-height: auto; }\n    .best-bg { position: static; height: 400px; }\n    .best-card{position:static;width:100%;margin-top:0;min-height:auto;}',
    css
)

# And on smaller mobile (max-width: 768px), adjust height
# I'll just add it to max-width: 768px if needed, but 400px is fine for both. Maybe 300px for 768px.
css = re.sub(
    r'(\@media \(max-width:768px\)\{.*?)\}',
    r'\1    .best-bg { height: 250px; }\n  }',
    css,
    flags=re.DOTALL
)

# Also fix the title from "BEST SUNGLASSES STORE..." to "SUSTAINABLE PRODUCTION PROCESS" just to be safe
css = css.replace('<h2>BEST SUNGLASSES STORE FOR YOUR STYLISH &amp; CLASSY LOOK</h2>', '<h2>SUSTAINABLE PRODUCTION PROCESS</h2>')
css = css.replace('<h2>BEST SUNGLASSES STORE FOR YOUR STYLISH & CLASSY LOOK</h2>', '<h2>SUSTAINABLE PRODUCTION PROCESS</h2>')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(css)
