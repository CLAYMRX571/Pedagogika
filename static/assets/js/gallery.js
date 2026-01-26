document.addEventListener("DOMContentLoaded", function () {
    const wrapper = document.querySelector(".slides-wrapper");
    const slides = document.querySelectorAll(".slide");

    let index = 0;
    const total = slides.length;

    function updateSlide() {
        wrapper.style.transform = `translateX(-${index * 100}%)`;
    }

    // Auto slide every 5 seconds
    setInterval(() => {
        index = (index + 1) % total;
        updateSlide();
    }, 5000);

    // Scroll down
    downBtn.addEventListener("click", () => {
        window.scrollBy({
            top: window.innerHeight,
            behavior: "smooth"
        });
    });

    // SEE MORE button
    const btn = document.getElementById("seeMoreBtn");
    const info = document.getElementById("moreInfo");

    btn.addEventListener("click", () => {
        info.style.display = info.style.display === "block" ? "none" : "block";
        btn.textContent = info.style.display === "block" ? "HIDE INFO" : "SEE MORE ABOUT US";
    });
});

document.getElementById('newsletterForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('nameInput').value.trim();
    const email = document.getElementById('emailInput').value.trim();

    if (!name || !email) {
        alert("Iltimos, barcha maydonlarni to'ldiring!");
        return;
    }

    alert(`Rahmat, ${name}! Sizning "${email}" pochtangiz ro'yxatdan o'tdi.`);

    document.getElementById('nameInput').value = '';
    document.getElementById('emailInput').value = '';
});

const faders = document.querySelectorAll('.fade-up');
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
}, { threshold: 0.2 });

faders.forEach(el => observer.observe(el));

// MODAL IMAGE
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modalImg');
const closeBtn = document.querySelector('.close');

document.querySelectorAll('.gallery-card img').forEach(img => {
    img.addEventListener('click', () => {
        modal.style.display = 'flex';
        modalImg.src = img.src;
    });
});

closeBtn.onclick = () => modal.style.display = 'none';
modal.onclick = e => {
    if (e.target === modal) modal.style.display = 'none';
};

document.querySelectorAll('.img-box img').forEach(img => {
    img.addEventListener('click', () => {
        modal.style.display = 'flex';
        modalImg.src = img.src;
    });
});

document.querySelectorAll('.overlay-text').forEach(text => {
    text.addEventListener('click', (e) => {
        e.stopPropagation(); 
        modal.style.display = 'flex';
        modalImg.src = text.getAttribute('data-img');
    });
});
