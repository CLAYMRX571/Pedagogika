document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".fade-up");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    }, { threshold: 0.2 });

    items.forEach(i => observer.observe(i));
});

document.addEventListener('DOMContentLoaded', function() {
    const starsContainer = document.getElementById('stars');
    const starCount = 80;
    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        const size = Math.random() * 2 + 1;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 3}s`; 
        starsContainer.appendChild(star);
    }
    
    const illustration = document.querySelector('.illustration');
    let rotation = 0;
    
    setInterval(() => {
        rotation = (rotation + 0.01) % 360;
        illustration.style.transform = `rotate(${rotation}deg)`;
    }, 50);
});