import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change aspect ratio to 4/5
content = content.replace('aspect-ratio:1/1;', 'aspect-ratio:4/5;')

# Replace href="#" with href="product-detail.html" for product links
content = re.sub(r'href="#" class="view-link"', 'href="product-detail.html" class="view-link"', content)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated products.html')
