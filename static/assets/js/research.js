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
    const cards = document.querySelectorAll('.card');  
    const observer = new IntersectionObserver((entries) => { 
        entries.forEach(entry => { 
            if (entry.isIntersecting) { 
                entry.target.classList.add('fade-in'); 
                observer.unobserve(entry.target); 
            } 
        }); 
    }, 
    { threshold: 0.1 }); 
    cards.forEach(card => { 
        observer.observe(card); 
    }); 
});