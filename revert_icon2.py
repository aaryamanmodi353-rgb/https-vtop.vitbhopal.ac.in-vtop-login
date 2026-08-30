import os

files = ["index.html", "profile.html", "credentials.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # replace fa-plane with fa-space-shuttle
    new_content = content.replace("fa-solid fa-plane", "fa-solid fa-space-shuttle")
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {file}")
