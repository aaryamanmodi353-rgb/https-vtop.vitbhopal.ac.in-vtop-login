import os

files = ["index.html", "profile.html", "credentials.html", "drawer.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # replace img in narrow sidebar
    content = content.replace('<img src="services.png" class="services-img-icon" alt="Services">', '<i class="fa-solid fa-space-shuttle shuttle-icon"></i>')
    
    # replace img in drawer
    content = content.replace('<div><img src="services.png" class="services-img-icon" alt="Services"> Services</div>', '<div><i class="fa-solid fa-space-shuttle shuttle-icon"></i> Services</div>')
    
    # also handle any leftovers from my previous scripts just in case
    content = content.replace('<div><img src="services.png" class="services-img-icon" alt="Services" style="width: 20px; height: 14px; margin-right: 15px; object-fit: contain;"> Services</div>', '<div><i class="fa-solid fa-space-shuttle shuttle-icon"></i> Services</div>')
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")

# Now add .shuttle-icon to styles.css
with open("styles.css", "a", encoding="utf-8") as f:
    f.write("\n.shuttle-icon {\n    transform: scale(1.25);\n    display: inline-block;\n}\n")
print("Updated styles.css with .shuttle-icon")
