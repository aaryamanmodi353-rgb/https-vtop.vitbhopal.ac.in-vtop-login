import os

files = ['index.html', 'profile.html', 'credentials.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the broken syntax
        bad_syntax = r"onclick=\"window.location.href=\'index.html\'\""
        good_syntax = "onclick=\"window.location.href='index.html'\""
        
        content = content.replace(bad_syntax, good_syntax)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed {f}")
