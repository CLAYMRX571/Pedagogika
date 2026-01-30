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

document.querySelectorAll('.icon').forEach(icon => { 
    icon.addEventListener('click', function(e) { 
        document.querySelectorAll('.icon').forEach(i => { 
            i.classList.remove('active'); 
        });  
        this.classList.add('active');  
        e.preventDefault(); 
    }); 
});  

window.addEventListener('load', function() { 
    const activePage = window.location.pathname.split('/').pop(); 
    if (activePage === '#') { 
        document.getElementById('brain-icon').classList.add('active'); 
    } 
    else if (activePage === '#') { 
        document.getElementById('heart-icon').classList.add('active'); 
    } 
    else if (activePage === '#') { 
        document.getElementById('handshake-icon').classList.add('active'); 
    } 
});

document.addEventListener("DOMContentLoaded", () => {
    const dropdown = document.querySelector(".lang-dropdown");
    const btn = dropdown.querySelector(".dropdown-btn");

    btn.addEventListener("click", () => {
        dropdown.classList.toggle("active");
    });

    // tashqariga bosilsa yopilsin
    document.addEventListener("click", (e) => {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove("active");
        }
    });
});