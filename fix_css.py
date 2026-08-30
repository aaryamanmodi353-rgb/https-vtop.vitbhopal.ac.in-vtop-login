import os

with open("styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find start and end of drawer-item-header related rules
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith(".drawer-item-header, .drawer-item-link {"):
        start_idx = i
    if line.startswith(".drawer-chevron {"):
        end_idx = i

if start_idx != -1 and end_idx != -1:
    css_content = """.drawer-item-header, .drawer-item-link {
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
"""
    new_lines = lines[:start_idx] + [css_content] + lines[end_idx:]
    with open("styles.css", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Fixed styles.css successfully!")
else:
    print("Could not find boundaries.")
