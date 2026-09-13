import re
import os

files = ['index.html', 'profile.html', 'credentials.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the opening button tag for the house chimney icon
        pattern = r'<button class="icon-btn">(\s*<i class="fa-solid fa-house-chimney")'
        replacement = r'<button class="icon-btn" onclick="window.location.href=\'index.html\'">\1'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
