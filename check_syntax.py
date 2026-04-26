import re
import subprocess

with open('Principal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract script blocks
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)

for i, script in enumerate(scripts):
    with open(f'temp_{i}.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print(f"Checking script {i}...")
    res = subprocess.run(['node', '-c', f'temp_{i}.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error in script {i}:\n{res.stderr}")
    else:
        print("Syntax OK")
