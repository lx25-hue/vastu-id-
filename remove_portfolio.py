import os, glob, re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove from navbar
    content = re.sub(r'\s*<a href=\"portfolio\.html\">PORTFOLIO</a>', '', content)
    
    # Remove from footer links (e.g. <li><a href=\"portfolio.html\" ...>Portfolio</a></li>)
    content = re.sub(r'\s*<li><a href=\"portfolio\.html\"[^>]*>Portfolio</a></li>', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Removed portfolio link from {file}')
