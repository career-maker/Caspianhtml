import os

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carabinaro Shrimp | Caspian & Sun Food Trading LLC</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="components.css" rel="stylesheet">
  <style>
    :root {
      --deep-teal: #1E4951;
      --rich-gold: #D7BB51;
      --charcoal: #171813;
      --cream: #fcfaf8;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Manrope', sans-serif;
      color: var(--charcoal);
      background-color: var(--cream);
      line-height: 1.6;
    }
    
    .detail-section {
      padding: clamp(6rem, 8vw, 8rem) clamp(1.5rem, 5vw, 3rem) clamp(3rem, 5vw, 4rem);
      max-width: 1400px;
      margin: 0 auto;
    }
    .detail-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(2rem, 5vw, 4rem);
      align-items: center;
    }
    
    .product-img-box {
      background: #fff;
      padding: 2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 400px;
    }
    .product-img-box img {
      max-width: 100%;
      height: auto;
      object-fit: contain;
    }
    
    .product-info {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }
    .product-info h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.4rem, 4vw, 3.2rem);
      font-weight: 500;
      color: var(--charcoal);
      text-transform: uppercase;
      line-height: 1.1;
    }
    .product-desc {
      font-size: 16px;
      color: rgb(90, 90, 86);
      line-height: 27px;
    }
    
    .info-label {
      font-size: 0.85rem;
      text-transform: uppercase;
      color: var(--deep-teal);
      margin-bottom: 0.5rem;
      letter-spacing: 1px;
    }
    
    .origin-box {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 500;
      font-size: 1.1rem;
    }
    .origin-box img {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      object-fit: cover;
    }
    
    .sizes-grid {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .size-box {
      border: 1px solid #ddd;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100px;
      height: 100px;
      background: #fff;
      transition: border-color 0.3s;
    }
    .size-box:hover {
      border-color: var(--deep-teal);
    }
    .size-box img {
      width: 48px;
      height: auto;
      margin-bottom: 0.5rem;
    }
    .size-box span {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--charcoal);
    }
    
    /* RELATED PRODUCTS */
    .related-section {
      padding: clamp(2rem, 5vw, 4rem) clamp(1.5rem, 5vw, 3rem) clamp(4rem, 8vw, 6rem);
      max-width: 1400px;
      margin: 0 auto;
    }
    .related-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2rem, 3.5vw, 2.8rem);
      font-weight: 500;
      color: var(--charcoal);
      margin-bottom: 2.5rem;
      text-transform: uppercase;
    }
    .related-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2rem;
    }
    .related-card {
      background: #fff;
      padding: 2rem 1.5rem 1.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      text-decoration: none;
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .related-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.06);
    }
    .related-img-box {
      height: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 1.5rem;
    }
    .related-img-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    .related-card h3 {
      font-family: 'Manrope', sans-serif;
      font-size: 1rem;
      font-weight: 600;
      color: var(--charcoal);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      width: 100%;
      border-top: 1px solid #eee;
      padding-top: 1.2rem;
    }
    
    @media (max-width: 900px) {
      .detail-grid {
        grid-template-columns: 1fr;
      }
      .related-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 500px) {
      .related-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <div id="header-placeholder"></div>

  <section class="detail-section">
    <div class="detail-grid">
      <div class="product-img-box">
        <img src="https://images.unsplash.com/photo-1565680018434-b513d5e5fd47?auto=format&fit=crop&w=800&q=80" alt="Carabinaro Shrimp">
      </div>
      <div class="product-info">
        <h1>Carabinaro Shrimp</h1>
        <p class="product-desc">Premium Carabinero Shrimp selected for its distinctive flavour, vibrant colour, and superior quality, responsibly sourced and carefully handled to meet the highest standards of global seafood markets.</p>
        
        <div class="info-group">
          <div class="info-label">Origin</div>
          <div class="origin-box">
            <!-- Using an emoji or flag icon for Spain -->
            <span style="font-size: 1.5rem;">🇪🇸</span> Spain
          </div>
        </div>
        
        <div class="info-group">
          <div class="info-label">Sizes Available</div>
          <div class="sizes-grid">
            <div class="size-box">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--deep-teal)" stroke-width="1.5"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/><path d="M11 7h2v6h-2zm0 8h2v2h-2z"/></svg>
              <span>5-7</span>
            </div>
            <div class="size-box">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--deep-teal)" stroke-width="1.5"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/><path d="M11 7h2v6h-2zm0 8h2v2h-2z"/></svg>
              <span>8-10</span>
            </div>
            <div class="size-box">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--deep-teal)" stroke-width="1.5"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/><path d="M11 7h2v6h-2zm0 8h2v2h-2z"/></svg>
              <span>18-24 SZ</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="related-section">
    <h2 class="related-title">Related Products</h2>
    <div class="related-grid">
      <a href="product-detail.html" class="related-card">
        <div class="related-img-box">
          <img src="https://images.unsplash.com/photo-1629851605335-502a5c54817a?auto=format&fit=crop&w=400&q=80" alt="Osetra Caviar">
        </div>
        <h3>Osetra Caviar</h3>
      </a>
      <a href="product-detail.html" class="related-card">
        <div class="related-img-box">
          <img src="https://images.unsplash.com/photo-1629851605335-502a5c54817a?auto=format&fit=crop&w=400&q=80" alt="Calluga Hybrid Caviar">
        </div>
        <h3>Calluga Hybrid Caviar</h3>
      </a>
      <a href="product-detail.html" class="related-card">
        <div class="related-img-box">
          <img src="https://images.unsplash.com/photo-1599839619722-39751411ea63?auto=format&fit=crop&w=400&q=80" alt="King Crab Legs">
        </div>
        <h3>King Crab Legs</h3>
      </a>
      <a href="product-detail.html" class="related-card">
        <div class="related-img-box">
          <img src="https://images.unsplash.com/photo-1599839619722-39751411ea63?auto=format&fit=crop&w=400&q=80" alt="Lobster Tail">
        </div>
        <h3>Lobster Tail</h3>
      </a>
    </div>
  </section>

  <div id="footer-placeholder"></div>

  <script src="components.js"></script>
</body>
</html>
"""

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated product-detail.html")
