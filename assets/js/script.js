// Theme Toggle Functionality
// This script handles the dark/light mode toggle and other interactive features

// Wait for the DOM to be fully loaded before running any scripts
document.addEventListener('DOMContentLoaded', function() {
    
    // Theme Toggle Elements
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    
    // Check if user has a saved theme preference, otherwise default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the saved theme on page load
    if (currentTheme === 'dark') {
        document.documentElement.classList.add('dark');
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
    } else {
        document.documentElement.classList.remove('dark');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
    }
    
    // Theme toggle button click handler
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            // Toggle the dark class on the html element
            document.documentElement.classList.toggle('dark');
            
            // Check if dark mode is currently active
            const isDark = document.documentElement.classList.contains('dark');
            
            // Update the theme icons
            if (isDark) {
                sunIcon.classList.remove('hidden');
                moonIcon.classList.add('hidden');
                localStorage.setItem('theme', 'dark');
            } else {
                sunIcon.classList.add('hidden');
                moonIcon.classList.remove('hidden');
                localStorage.setItem('theme', 'light');
            }
        });
    }
    
    // Active Navigation Link Highlighting
    // This function highlights the current page in the navigation
    function highlightActiveNavLink() {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const navLinks = document.querySelectorAll('nav a');
        
        navLinks.forEach(link => {
            // Remove any existing active classes
            link.classList.remove('bg-blue-50', 'dark:bg-gray-700', 'text-blue-600', 'dark:text-blue-400');
            
            // Check if this link matches the current page
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('bg-blue-50', 'dark:bg-gray-700', 'text-blue-600', 'dark:text-blue-400');
            }
        });
    }
    
    // Call the function to highlight the active link
    highlightActiveNavLink();
    
    // Smooth Scrolling for Anchor Links
    // This provides smooth scrolling when clicking on anchor links within the page
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Mobile Navigation Toggle (for future responsive design)
    // This is prepared for when we add mobile navigation functionality
    const mobileNavToggle = document.getElementById('mobile-nav-toggle');
    const mobileNav = document.getElementById('mobile-nav');
    
    if (mobileNavToggle && mobileNav) {
        mobileNavToggle.addEventListener('click', function() {
            mobileNav.classList.toggle('hidden');
        });
    }
    
    // Form Validation Helper (for contact form)
    // This function validates email format
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // Contact Form Handler (for future contact form)
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const email = formData.get('email');
            const message = formData.get('message');
            
            // Basic validation
            if (!email || !isValidEmail(email)) {
                alert('Please enter a valid email address.');
                return;
            }
            
            if (!message || message.trim().length < 10) {
                alert('Please enter a message with at least 10 characters.');
                return;
            }
            
            // Here you would typically send the form data to your server
            // For now, we'll just show a success message
            alert('Thank you for your message! I\'ll get back to you soon.');
            this.reset();
        });
    }
    
    // Lazy Loading for Images (for future optimization)
    // This helps with performance when we add images to the site
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // Console welcome message for developers
    console.log('Harvey Rendall Personal Website - JavaScript loaded successfully!');
    console.log('Theme:', localStorage.getItem('theme') || 'light');
    
});

// Utility Functions
// These are helper functions that can be used throughout the site

// Debounce function for performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Format date function for blog posts
function formatDate(dateString) {
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Truncate text function for previews
function truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substr(0, maxLength) + '...';
} 