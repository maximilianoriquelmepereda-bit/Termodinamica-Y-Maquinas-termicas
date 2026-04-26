import io

with open('Principal.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_slide_6 = '''        },
        {
            sub: "Nuestra Historia",
            title: "Línea de Tiempo",
            content: `
                <div class="slide-fade w-full max-w-4xl flex items-center justify-center">
                    <div class="flex justify-center gap-8">
                        <div class="text-center">
                            <div class="text-3xl font-black text-bordo">1944</div>
                            <div class="text-[10px] font-bold text-gray-400 uppercase">Fundación Escuela</div>
                        </div>
                        <div class="w-px h-12 bg-gray-200"></div>
                        <div class="text-center">
                            <div class="text-3xl font-black text-bordo">2026</div>
                            <div class="text-[10px] font-bold text-gray-400 uppercase">Proyecto 5º4</div>
                        </div>
                    </div>
                </div>
            `
        }
'''

start_idx = 523
end_idx = 770
print('Line 524:', lines[start_idx].strip())
print('Line 771:', lines[end_idx].strip())
print('Line 772:', lines[end_idx+1].strip())

new_lines = lines[:start_idx] + [new_slide_6] + lines[end_idx+1:]

for i, line in enumerate(new_lines):
    if '01 / 06' in line:
        new_lines[i] = line.replace('01 / 06', '01 / 07')

with open('Principal.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Done!')
