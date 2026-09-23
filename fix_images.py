import re

with open('product-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Carabinaro Shrimp image
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-1565680018434-b513d5e5fd47[^"]*" alt="Carabinaro Shrimp">',
    r'<img src="images/pdf_extracted/extracted_5_2000x1331.jpeg" alt="Carabinaro Shrimp">',
    content
)

# Replace Osetra Caviar image
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-1629851605335-502a5c54817a[^"]*" alt="Osetra Caviar">',
    r'<img src="images/sturgeon-caviar.jpg" alt="Osetra Caviar">',
    content
)

# Replace Calluga Hybrid Caviar image
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-1629851605335-502a5c54817a[^"]*" alt="Calluga Hybrid Caviar">',
    r'<img src="images/pdf_extracted/extracted_3_2208x3936.jpeg" alt="Calluga Hybrid Caviar">',
    content
)

# Replace King Crab Legs image
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-1599839619722-39751411ea63[^"]*" alt="King Crab Legs">',
    r'<img src="images/pdf_extracted/extracted_4_2000x1499.jpeg" alt="King Crab Legs">',
    content
)

# Replace Lobster Tail image
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-1599839619722-39751411ea63[^"]*" alt="Lobster Tail">',
    r'<img src="images/pdf_extracted/extracted_1_2000x2500.jpeg" alt="Lobster Tail">',
    content
)

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced.")
