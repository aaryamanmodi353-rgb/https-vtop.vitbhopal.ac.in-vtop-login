document.addEventListener('DOMContentLoaded', () => {
    // 1. Sidebar Toggle Logic
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const sidebar = document.getElementById('sidebar');

    hamburgerBtn.addEventListener('click', () => {
        if (window.innerWidth <= 640) {
            // Mobile: toggle mobile-open class
            sidebar.classList.toggle('mobile-open');
        } else {
            // Desktop: toggle hidden class
            sidebar.classList.toggle('hidden');
            // Adjust main content margin
            const contentArea = document.querySelector('.content-area');
            contentArea.classList.toggle('expanded');
        }
    });

    // Close sidebar if clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 640) {
            if (!sidebar.contains(e.target) && !hamburgerBtn.contains(e.target)) {
                sidebar.classList.remove('mobile-open');
            }
        }
        
        // Close all popups
        document.querySelectorAll('.popup-menu').forEach(p => p.classList.remove('show-popup'));
        document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active'));
    });

    // Sidebar Popups Logic
    const sidebarItems = document.querySelectorAll('.sidebar-item');
    sidebarItems.forEach(item => {
        const btn = item.querySelector('.sidebar-icon');
        const popup = item.querySelector('.popup-menu');
        
        if (btn && popup) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const isCurrentlyOpen = popup.classList.contains('show-popup');
                
                // Close all other popups
                document.querySelectorAll('.popup-menu').forEach(p => p.classList.remove('show-popup'));
                document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active'));
                
                if (!isCurrentlyOpen) {
                    popup.classList.add('show-popup');
                    item.classList.add('active');
                }
            });
            
            // Prevent clicks inside popup from closing it
            popup.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        }
    });

    // 2. Accordion Logic
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const currentAccordion = header.parentElement;
            const content = currentAccordion.querySelector('.accordion-content');
            
            // Toggle active class on current accordion
            const isActive = currentAccordion.classList.contains('active');
            
            // Optional: close other accordions
            /*
            document.querySelectorAll('.accordion').forEach(acc => {
                acc.classList.remove('active');
                acc.querySelector('.accordion-content').style.display = 'none';
            });
            */
            
            if (isActive) {
                currentAccordion.classList.remove('active');
                content.style.display = 'none';
            } else {
                currentAccordion.classList.add('active');
                content.style.display = 'block';
            }
        });
    });

    // 3. Fake Session Timer
    let minutes = 15;
    let seconds = 43;
    const timerDisplay = document.getElementById('session-timer');

    setInterval(() => {
        if (seconds > 0) {
            seconds--;
        } else {
            if (minutes > 0) {
                minutes--;
                seconds = 59;
            } else {
                // Timer reached 0
                return;
            }
        }
        
        timerDisplay.textContent = `${minutes}m ${seconds}s`;
    }, 1000);

    // 4. Dropdown Change Logic (Optional: For styling if needed, but native works fine here)
    const messSelect = document.getElementById('mess-select');
    messSelect.addEventListener('change', (e) => {
        // The value updates instantly and native styling takes over
        // We can just blur it so the arrow goes away after selection
        e.target.blur();
    });
});

// VTOP Drawer Logic
document.addEventListener("DOMContentLoaded", function() {
    const hamburgerBtn = document.getElementById("hamburger-btn");
    const drawerCloseBtn = document.getElementById("drawerCloseBtn");
    const vtopDrawer = document.getElementById("vtopDrawer");
    const vtopDrawerOverlay = document.getElementById("vtopDrawerOverlay");
    
    if (hamburgerBtn && drawerCloseBtn && vtopDrawer && vtopDrawerOverlay) {
        function openDrawer() {
            vtopDrawer.classList.add("open");
            vtopDrawerOverlay.classList.add("active");
        }
        
        function closeDrawer() {
            vtopDrawer.classList.remove("open");
            vtopDrawerOverlay.classList.remove("active");
        }
        
        hamburgerBtn.addEventListener("click", openDrawer);
        drawerCloseBtn.addEventListener("click", closeDrawer);
        vtopDrawerOverlay.addEventListener("click", closeDrawer);
        
        // Drawer Accordions
        const drawerAccordions = document.querySelectorAll(".accordion-drawer .drawer-item-header");
        drawerAccordions.forEach(header => {
            header.addEventListener("click", function() {
                const parent = this.parentElement;
                
                // Toggle active class
                if (parent.classList.contains("active")) {
                    parent.classList.remove("active");
                } else {
                    // Close others (optional, but standard for accordions)
                    document.querySelectorAll(".accordion-drawer").forEach(acc => {
                        acc.classList.remove("active");
                    });
                    parent.classList.add("active");
                }
            });
        });
    }
});
