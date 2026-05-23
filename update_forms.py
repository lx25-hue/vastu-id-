import os, re

files = ['index.html', 'contact.html']

new_inputs = '''<input type="email" id="email" placeholder="Email Address" required>
                <input type="text" id="cities" placeholder="City" required>
                <select id="price-range" required>
                    <option value="" disabled selected>Price Range</option>
                    <option value="1 Lakh - 5 Lakh">1 Lakh - 5 Lakh</option>
                    <option value="5 Lakh - 10 Lakh">5 Lakh - 10 Lakh</option>
                    <option value="10 Lakh - 15 Lakh">10 Lakh - 15 Lakh</option>
                    <option value="more then 20 Lakh">more then 20 Lakh</option>
                </select>'''

for file in files:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    content = content.replace('.contact input, .contact textarea {', '.contact input, .contact textarea, .contact select {')
    content = content.replace('.contact input:focus, .contact textarea:focus {', '.contact input:focus, .contact textarea:focus, .contact select:focus {')

    # 2. Add City and Price Range fields
    content = re.sub(r'<input type=\"email\" id=\"email\" placeholder=\"Email Address\" required>', new_inputs, content)

    # 3. Add styling for select options to make them look good, but standard select mostly works. 
    # Just to be safe, maybe we don't need additional styling since it inherits from .contact select

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')
