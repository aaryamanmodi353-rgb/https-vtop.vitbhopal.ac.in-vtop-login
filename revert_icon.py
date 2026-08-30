import os
import re

files = ["index.html", "profile.html", "credentials.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # replace fa-space-shuttle with fa-plane
    new_content = content.replace("fa-solid fa-space-shuttle", "fa-solid fa-plane")
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {file}")
