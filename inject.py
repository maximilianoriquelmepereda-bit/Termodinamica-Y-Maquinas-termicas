import os
import re

files = {
    'maxi.html': { 'id': 'maxi', 'color': '#C84B31', 'btn': 'btn-primary', 'text_class': 'text-bordo' },
    'cele.html': { 'id': 'cele', 'color': '#3FB8AF', 'btn': 'btn-secondary', 'text_class': 'text-azul' },
    'dante.html': { 'id': 'dante', 'color': '#F9C74F', 'btn': 'btn-primary', 'text_class': 'text-amarillo' },  # wait, I'll use inline styles or just btn-primary if not sure
    'juan.html': { 'id': 'juan', 'color': '#9B5DE5', 'btn': 'btn-primary', 'text_class': 'text-lavanda' }
}

html_to_inject = """
        <!-- Mi Cuaderno de Notas -->
        <div class="mt-8 p-6 bg-white rounded-2xl shadow-lg border-t-4" style="border-color: {color};">
            <h4 class="text-xl font-bold mb-4 flex items-center gap-2" style="color: {color};">
                <i class="fas fa-book"></i> Mi Cuaderno de Notas
            </h4>
            <textarea id="studentNote" class="w-full h-32 p-4 border border-gray-200 rounded-xl outline-none resize-none transition-all" style="outline-color: {color};" placeholder="Escribe tus apuntes aquí..."></textarea>
            
            <div class="mt-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg text-sm font-bold text-gray-600 transition-colors flex items-center gap-2 border border-gray-300">
                    <i class="fas fa-image"></i> Adjuntar Imagen
                    <input type="file" id="imageUpload" accept="image/*" class="hidden">
                </label>
                <button id="saveBtn" class="px-6 py-2 rounded-lg text-sm font-bold shadow-md flex items-center gap-2 text-white" style="background-color: {color};">
                    <i class="fas fa-save"></i> Guardar Notas
                </button>
            </div>
            
            <div id="imagePreviewContainer" class="mt-4 hidden">
                <p class="text-xs font-bold text-gray-500 mb-2 uppercase">Imagen Adjunta:</p>
                <div class="relative inline-block">
                    <img id="noteImage" src="" alt="Imagen adjunta" class="max-h-48 rounded-lg border border-gray-200 shadow-sm">
                    <button id="removeImageBtn" class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 shadow-md">
                        <i class="fas fa-times text-xs"></i>
                    </button>
                </div>
            </div>
        </div>
"""

js_to_inject = """
    // Cuaderno de notas logic
    const studentId = '{id}';
    const noteEl = document.getElementById('studentNote');
    const imgUpload = document.getElementById('imageUpload');
    const noteImage = document.getElementById('noteImage');
    const imgContainer = document.getElementById('imagePreviewContainer');
    const removeImgBtn = document.getElementById('removeImageBtn');
    const saveBtn = document.getElementById('saveBtn');

    // Load saved data
    window.addEventListener('DOMContentLoaded', () => {{
        const savedNote = localStorage.getItem(`nota_${{studentId}}`);
        const savedImage = localStorage.getItem(`img_${{studentId}}`);
        
        if (savedNote) noteEl.value = savedNote;
        if (savedImage) {{
            noteImage.src = savedImage;
            imgContainer.classList.remove('hidden');
        }}
    }});

    // Handle image upload
    imgUpload.addEventListener('change', function(e) {{
        const file = e.target.files[0];
        if (file) {{
            const reader = new FileReader();
            reader.onload = function(event) {{
                noteImage.src = event.target.result;
                imgContainer.classList.remove('hidden');
            }};
            reader.readAsDataURL(file);
        }}
    }});

    // Remove image
    removeImgBtn.addEventListener('click', () => {{
        noteImage.src = '';
        imgContainer.classList.add('hidden');
        imgUpload.value = '';
    }});

    // Save functionality
    saveBtn.addEventListener('click', () => {{
        localStorage.setItem(`nota_${{studentId}}`, noteEl.value);
        if (!imgContainer.classList.contains('hidden')) {{
            localStorage.setItem(`img_${{studentId}}`, noteImage.src);
        }} else {{
            localStorage.removeItem(`img_${{studentId}}`);
        }}
        
        // Show success feedback
        const originalText = saveBtn.innerHTML;
        saveBtn.innerHTML = '<i class="fas fa-check"></i> ¡Guardado!';
        saveBtn.style.backgroundColor = '#10B981'; // Tailwind green-500
        setTimeout(() => {{
            saveBtn.innerHTML = originalText;
            saveBtn.style.backgroundColor = '{color}';
        }}, 2000);
    }});
"""

for fname, config in files.items():
    if not os.path.exists(fname):
        print(f"Skipping {fname}, does not exist")
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already injected
    if 'Mi Cuaderno de Notas' in content:
        print(f"Already injected into {fname}")
        continue
    
    # 1. Insert HTML right before <div class="text-center mt-6"> 
    # Usually it's after <div class="w-full"> ... </div>
    # Using regex to find the end of the w-full div
    
    match = re.search(r'</div>\s*<div class="text-center mt-6">', content)
    if match:
        html_content = html_to_inject.format(color=config['color'])
        content = content[:match.start()] + '</div>' + html_content + '\n        <div class="text-center mt-6">' + content[match.end():]
        
    # 2. Insert JS right before </script>
    match_js = re.search(r'</script>', content)
    if match_js:
        js_content = js_to_inject.format(id=config['id'], color=config['color'])
        content = content[:match_js.start()] + js_content + content[match_js.start():]
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Injected into {fname}")

print("Done with all files")
