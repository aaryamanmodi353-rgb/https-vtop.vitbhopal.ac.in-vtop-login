import re

files = ["index.html", "profile.html", "credentials.html"]

with open("drawer.html", "r", encoding="utf-8") as f:
    drawer_html = f.read()

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if already injected
    if "vtop-drawer" not in content:
        # insert before </body>
        new_content = content.replace("</body>", f"{drawer_html}\n</body>")
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"{file} already has the drawer.")
