/**
 * CASPIAN & SUN FOOD TRADING LLC — MAIN JAVASCRIPT
 * Inner pages interactivity: Mobile menu drawer, Product filtering, Image gallery switchers
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- 1. Mobile Navigation Drawer ---
  const menuToggle = document.getElementById('menuToggle');
  const drawerClose = document.getElementById('drawerClose');
  const navDrawer = document.getElementById('navDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');

  function openDrawer() {
    if (navDrawer && drawerBackdrop) {
      navDrawer.classList.add('open');
      drawerBackdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawer() {
    if (navDrawer && drawerBackdrop) {
      navDrawer.classList.remove('open');
      drawerBackdrop.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  if (menuToggle) menuToggle.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeDrawer();
  });

  // --- 2. Product Category Filter (for products.html) ---
  const filterButtons = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card[data-category]');

  if (filterButtons.length > 0 && productCards.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        productCards.forEach(card => {
          const category = card.getAttribute('data-category');
          if (filterValue === 'all' || category === filterValue) {
            card.style.display = 'flex';
            setTimeout(() => {
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            }, 50);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(10px)';
            setTimeout(() => {
              card.style.display = 'none';
            }, 250);
          }
        });
      });
    });
  }

  // --- 3. Product Detail Image Gallery (for product-detail.html) ---
  const mainImage = document.getElementById('mainGalleryImage');
  const thumbButtons = document.querySelectorAll('.thumb-btn');

  if (mainImage && thumbButtons.length > 0) {
    thumbButtons.forEach(thumb => {
      thumb.addEventListener('click', () => {
        thumbButtons.forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');

        const targetSrc = thumb.getAttribute('data-full');
        if (targetSrc) {
          mainImage.style.opacity = '0';
          setTimeout(() => {
            mainImage.src = targetSrc;
            mainImage.style.opacity = '1';
          }, 200);
        }
      });
    });
  }

  // --- 4. Interactive Contact Form (for contact.html) ---
  const contactForm = document.getElementById('caspianContactForm');
  const formSuccess = document.getElementById('formSuccessMessage');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = `Sending Inquiry...`;
      }

      setTimeout(() => {
        if (formSuccess) {
          formSuccess.style.display = 'block';
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        contactForm.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = `Send Message <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>`;
        }
      }, 900);
    });
  }
});
