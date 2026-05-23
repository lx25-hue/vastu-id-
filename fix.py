import os, re

files = ['about.html', 'services.html', 'portfolio.html', 'studio.html', 'contact.html', 'blog.html']

for file in files:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update fonts link if Orbitron is missing
    if 'Orbitron' not in content:
        content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Montserrat[^"]*" rel="stylesheet">',
                         '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Lora:ital,wght@0,400;1,400&family=Yeseva+One&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">',
                         content)

    # 2. Update .logo css
    content = re.sub(r'\.logo\s*\{\s*font-family:\s*\'[^\']+\',\s*serif;\s*font-size:\s*[0-9.]+rem;\s*font-weight:\s*\d+;',
                     '.logo { font-family: \'Yeseva One\', serif; font-size: 2.2rem; font-weight: 400;',
                     content)

    # 3. Update .nav-links a css
    content = re.sub(r'\.nav-links a\s*\{\s*(font-family:[^;]+;)?\s*text-decoration:\s*none;\s*color:\s*var\(--white\);\s*margin-left:\s*40px;\s*font-weight:\s*600;',
                     '.nav-links a { font-family: \'Orbitron\', sans-serif; text-decoration: none; color: var(--white); margin-left: 40px; font-weight: 600;',
                     content)
                     
    # 4. Update the nav-links block
    nav_links_block = '''<div class="nav-links" id="nav-links">
            <a href="index.html">HOME</a>
            <a href="about.html">ABOUT US</a>
            <div class="dropdown">
                <a href="services.html">SERVICES</a>
                <div class="dropdown-menu">
                    <a href="services.html">Building Planing</a>
                    <a href="services.html">Structural Design</a>
                    <a href="services.html">Architectural Design</a>
                    <a href="services.html">Soil Testing</a>
                    <a href="services.html">Piling Works</a>
                    <a href="services.html">Surveying</a>
                    <a href="services.html">Construction</a>
                </div>
            </div>
            <a href="portfolio.html">PORTFOLIO</a>
            <a href="blog.html">BLOG</a>
            <a href="contact.html">CONTACT</a>
        </div>'''
        
    content = re.sub(r'<div class="nav-links" id="nav-links">.*?</div>\s*</nav>', nav_links_block + '\n    </nav>', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')
