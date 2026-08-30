import os

files = ["index.html", "profile.html", "credentials.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace in the drawer specifically
    old_str = '<div><i class="fa-solid fa-space-shuttle"></i> Services</div>'
    new_str = '<div><img src="services.png" class="services-img-icon" alt="Services" style="width: 20px; height: 14px; margin-right: 15px; object-fit: contain;"> Services</div>'
    
    content = content.replace(old_str, new_str)
    
    # Just in case it's still fa-plane
    old_str2 = '<div><i class="fa-solid fa-plane"></i> Services</div>'
    content = content.replace(old_str2, new_str)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")
