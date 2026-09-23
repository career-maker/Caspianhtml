import re

def create_page(filename, title, hero_title, hero_desc):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Caspian & Sun Food Trading LLC</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&family=Alex+Brush&display=swap" rel="stylesheet">
  <link href="components.css" rel="stylesheet">
  <style>
    :root {{
      --deep-teal: #1E4951;
      --rich-gold: #D7BB51;
      --charcoal: #171813;
      --cream: #fcfaf8;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Manrope', sans-serif;
      color: var(--charcoal);
      background-color: var(--cream);
      line-height: 1.6;
    }}
    
    /* HERO */
    .hero {{
      position: relative;
      height: 45vh;
      min-height: 300px;
      background: radial-gradient(circle, rgba(0,0,0,0) 0%, rgba(0,0,0,0.4) 100%), url('images/pdf_extracted/extracted_5_2000x1331.jpeg') center/cover;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(1.5rem, 4vw, 3.5rem);
      color: #fff;
      text-align: center;
    }}
    .hero-inner {{ max-width: 800px; margin: 0 auto; margin-top: 60px; }}
    .hero h1 {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.4rem, 5vw, 4rem);
      font-weight: 500;
      margin-bottom: 0.5rem;
    }}
    .hero p {{
      font-size: clamp(0.9rem, 1.5vw, 1.1rem);
      color: rgba(255,255,255,0.85);
    }}

    /* CONTENT SECTION */
    .page-content {{
      max-width: 900px;
      margin: 0 auto;
      padding: clamp(3rem, 5vw, 5rem) clamp(1.5rem, 5vw, 3rem);
      background: #fff;
      box-shadow: 0 10px 40px rgba(0,0,0,0.03);
      border-radius: 8px;
      transform: translateY(-40px);
      position: relative;
      z-index: 10;
    }}
    .page-content h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 29px;
      font-weight: 500;
      color: var(--charcoal);
      margin-top: 2.5rem;
      margin-bottom: 1rem;
    }}
    .page-content h2:first-child {{ margin-top: 0; }}
    .page-content p {{
      font-size: 16px;
      color: rgb(90, 90, 86);
      line-height: 27px;
      margin-bottom: 1.5rem;
    }}
    .page-content ul {{
      margin-bottom: 1.5rem;
      padding-left: 1.5rem;
      color: rgb(90, 90, 86);
      font-size: 16px;
      line-height: 27px;
    }}
    .page-content li {{ margin-bottom: 0.5rem; }}
  </style>
</head>
<body>

  <div id="header-placeholder"></div>

  <section class="hero">
    <div class="hero-inner">
      <h1>{hero_title}</h1>
      <p>{hero_desc}</p>
    </div>
  </section>

  <main class="page-content">
    <h2>1. Introduction</h2>
    <p>Welcome to Caspian & Sun Food Trading LLC. This document outlines our policies and terms. By accessing or using our services, you agree to comply with and be bound by these terms.</p>
    
    <h2>2. Information We Collect</h2>
    <p>We may collect personal information such as your name, contact details, and preferences when you interact with our website or services. This information is used to improve our offerings and provide you with a tailored experience.</p>
    
    <h2>3. Use of Information</h2>
    <p>Your information is used strictly for business purposes, including processing orders, responding to inquiries, and sending relevant updates. We do not sell or rent your personal information to third parties.</p>
    <ul>
      <li>To process your transactions and manage your account.</li>
      <li>To send administrative information, such as updates to our terms or policies.</li>
      <li>To respond to customer service requests and provide support.</li>
    </ul>

    <h2>4. Data Security</h2>
    <p>We implement appropriate technical and organizational measures to protect your personal data against unauthorized access, alteration, disclosure, or destruction.</p>

    <h2>5. Changes to This Policy</h2>
    <p>We reserve the right to update or modify this document at any time. Any changes will be effective immediately upon posting on our website. Your continued use of our services constitutes acceptance of the revised terms.</p>
  </main>

  <div id="footer-placeholder"></div>

  <script src="components.js"></script>
</body>
</html>'''
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

create_page('privacy-policy.html', 'Privacy Policy', 'Privacy Policy', 'Learn how we collect, use, and protect your information.')
create_page('terms.html', 'Terms of Use', 'Terms of Use', 'Read the terms and conditions governing the use of our services.')
