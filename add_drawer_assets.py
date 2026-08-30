import os

css_code = """
/* VTOP Drawer Styles */
.vtop-drawer-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    z-index: 9998;
    display: none;
}
.vtop-drawer-overlay.active {
    display: block;
}
.vtop-drawer {
    position: fixed;
    top: 0;
    left: -320px;
    width: 300px;
    height: 100vh;
    background: #ffffff;
    z-index: 9999;
    transition: left 0.3s ease;
    box-shadow: 2px 0 10px rgba(0,0,0,0.1);
}
.vtop-drawer.open {
    left: 0;
}
.vtop-drawer-header {
    height: 50px;
    background: linear-gradient(to right, #0056b3, #1a75ff);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 15px;
    font-size: 16px;
    font-weight: 500;
}
.drawer-close-btn {
    background: transparent;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
}
.vtop-drawer-body {
    overflow-y: auto;
    height: calc(100vh - 50px);
    padding-bottom: 20px;
}
.drawer-item-header, .drawer-item-link {
    padding: 12px 20px;
    display: flex;
    align-items: center;
    color: #000;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    border-bottom: 1px solid #f0f0f0;
    justify-content: space-between;
    text-decoration: none;
}
.drawer-item-header:hover, .drawer-item-link:hover {
    background: #f9f9f9;
}
.drawer-item-header div, .drawer-item-link div {
    display: flex;
    align-items: center;
}
.drawer-item-header i:first-child, .drawer-item-link i:first-child {
    width: 20px;
    margin-right: 15px;
    font-size: 14px;
    color: #000;
}
.accordion-drawer.active .drawer-item-header {
    color: #0056b3;
    border: 1px solid #6398d8;
    border-radius: 4px;
    margin: 5px 15px;
    padding: 10px 15px;
    border-bottom: 1px solid #6398d8; /* override */
}
.accordion-drawer.active .drawer-item-header i {
    color: #0056b3;
}
.drawer-chevron {
    transition: transform 0.3s;
}
.accordion-drawer.active .drawer-chevron {
    transform: rotate(180deg);
}
.drawer-submenu {
    display: none;
    background: #ffffff;
    padding-bottom: 5px;
}
.accordion-drawer.active .drawer-submenu {
    display: block;
}
.drawer-submenu a {
    display: block;
    padding: 10px 20px 10px 50px;
    color: #333;
    text-decoration: none;
    font-size: 12px;
}
.drawer-submenu a:hover {
    background: #f0f0f0;
}
.drawer-submenu a i {
    margin-right: 10px;
    font-size: 10px;
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(css_code)

js_code = """
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
"""

with open("script.js", "a", encoding="utf-8") as f:
    f.write(js_code)

print("Injected CSS and JS successfully.")
