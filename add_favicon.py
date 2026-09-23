import os

files = ['index.html', 'about.html', 'products.html', 'product-detail.html', 'blog.html', 'blog-detail.html', 'contact.html', 'privacy-policy.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</title>', '</title>\n  <link rel="icon" type="image/png" href="images/logo.png">')
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print('Favicon added')
