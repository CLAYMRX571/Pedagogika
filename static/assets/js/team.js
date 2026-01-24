document.addEventListener("DOMContentLoaded", function () {
    const wrapper = document.querySelector(".slides-wrapper");
    const slides = document.querySelectorAll(".slide");
    const nextBtn = document.querySelector(".arrow.right");
    const prevBtn = document.querySelector(".arrow.left");
    const downBtn = document.querySelector(".down-arrow");

    let index = 0;
    const total = slides.length;

    function updateSlide() {
        wrapper.style.transform = `translateX(-${index * 100}%)`;
    }

    nextBtn.addEventListener("click", () => {
        index = (index + 1) % total;
        updateSlide();
    });

    prevBtn.addEventListener("click", () => {
        index = (index - 1 + total) % total;
        updateSlide();
    });

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