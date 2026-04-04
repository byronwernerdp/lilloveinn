// Nav scroll effect
const nav = document.querySelector('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
});

// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (toggle) {
  toggle.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// Fade-up on scroll
const fadeEls = document.querySelectorAll('.fade-up');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) { el.target.classList.add('visible'); observer.unobserve(el.target); }
  });
}, { threshold: 0.1 });
fadeEls.forEach(el => observer.observe(el));

// Contact form (Web3Forms)
const form = document.getElementById('contact-form');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const btn = form.querySelector('button');
    btn.textContent = 'Sending...';
    btn.disabled = true;
    try {
      const res = await fetch('https://api.web3forms.com/submit', { method: 'POST', body: data });
      const json = await res.json();
      if (json.success) {
        form.style.display = 'none';
        document.getElementById('form-success').style.display = 'block';
      } else {
        btn.textContent = 'Send'; btn.disabled = false;
        alert('Something went wrong. Please email us directly.');
      }
    } catch {
      btn.textContent = 'Send'; btn.disabled = false;
    }
  });
}

// Lightbox for property gallery images
(function() {
  // Create lightbox elements
  const overlay = document.createElement('div');
  overlay.id = 'lightbox-overlay';
  overlay.style.cssText = `
    display:none; position:fixed; inset:0; background:rgba(0,0,0,0.92);
    z-index:9999; cursor:pointer; align-items:center; justify-content:center;
  `;

  const img = document.createElement('img');
  img.style.cssText = `
    max-width:92vw; max-height:90vh; object-fit:contain;
    border-radius:6px; box-shadow:0 8px 40px rgba(0,0,0,0.6);
    pointer-events:none;
  `;

  const close = document.createElement('div');
  close.innerHTML = '&times;';
  close.style.cssText = `
    position:fixed; top:20px; right:28px; color:#fff; font-size:2.8rem;
    cursor:pointer; line-height:1; font-weight:300; text-shadow:0 2px 8px rgba(0,0,0,0.5);
  `;

  overlay.appendChild(img);
  overlay.appendChild(close);
  document.body.appendChild(overlay);

  // Open lightbox on gallery image click
  document.addEventListener('click', function(e) {
    const target = e.target;
    if (target.tagName === 'IMG' && target.closest('.prop-gallery-grid')) {
      img.src = target.src;
      overlay.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }
  });

  // Close on overlay click or X
  function closeLightbox() {
    overlay.style.display = 'none';
    img.src = '';
    document.body.style.overflow = '';
  }
  overlay.addEventListener('click', closeLightbox);
  close.addEventListener('click', function(e) { e.stopPropagation(); closeLightbox(); });

  // Close on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeLightbox();
  });

  // Pointer cursor on gallery images
  document.querySelectorAll('.prop-gallery-grid img').forEach(function(el) {
    el.style.cursor = 'pointer';
  });
})();
