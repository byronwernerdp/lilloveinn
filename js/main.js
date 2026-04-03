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
