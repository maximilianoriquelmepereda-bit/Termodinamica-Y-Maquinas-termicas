import io
import re

with open('Principal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace header
header_old = '''<header class="bg-white/90 backdrop-blur border-b p-4 flex justify-between items-center no-print shadow-sm">
    <div class="flex items-center gap-3">
        <div class="p-2 bordo-bg rounded-lg text-white shadow-lg"><i class="fas fa-microchip"></i></div>
        <div>
            <h1 class="text-xs font-bold text-gray-500 uppercase tracking-wider">E.E.S.T. "Ing. Álvarez Condarco"</h1>
            <p class="text-sm font-black text-gray-800 tracking-tight">5º4 ELECTROMECÁNICA</p>
        </div>
    </div>
    <button onclick="window.print()" class="btn-primary px-5 py-2.5 rounded-xl text-xs font-bold flex items-center gap-2 shadow-md">
        <i class="fas fa-file-pdf"></i> DESCARGAR PDF
    </button>
</header>'''

header_new = '''<header class="bg-white/90 backdrop-blur border-b p-4 flex justify-between items-center no-print shadow-sm relative z-50">
    <div class="flex items-center gap-3">
        <div class="p-2 bordo-bg rounded-lg text-white shadow-lg"><i class="fas fa-microchip"></i></div>
        <div>
            <h1 class="text-xs font-bold text-gray-500 uppercase tracking-wider">E.E.S.T. "Ing. Álvarez Condarco"</h1>
            <p class="text-sm font-black text-gray-800 tracking-tight">5º4 ELECTROMECÁNICA</p>
        </div>
    </div>
    <div class="flex items-center gap-2">
        <button id="modeToggleBtn" onclick="toggleMode()" class="btn-secondary px-5 py-2.5 rounded-xl text-xs font-bold shadow-md flex items-center gap-2">
            <i class="fas fa-layer-group"></i> CASCADA
        </button>
        <button onclick="window.print()" class="btn-primary px-5 py-2.5 rounded-xl text-xs font-bold flex items-center gap-2 shadow-md hidden sm:flex">
            <i class="fas fa-file-pdf"></i> PDF
        </button>
    </div>
</header>'''

content = content.replace(header_old, header_new)

# 2. Replace Javascript logic from `function renderSlide() {` up to `function changeSlide(dir) {`
# We will use regex for this

js_new = '''    let mode = 'presentation';

    function toggleMode() {
        mode = mode === 'presentation' ? 'cascade' : 'presentation';
        const toggleBtn = document.getElementById('modeToggleBtn');
        const footer = document.querySelector('footer');
        const progressContainer = document.querySelector('.fixed.top-0');
        
        if (mode === 'cascade') {
            toggleBtn.innerHTML = '<i class="fas fa-desktop"></i> PRESENTACIÓN';
            toggleBtn.classList.replace('btn-secondary', 'btn-primary');
            if (footer) footer.classList.add('hidden');
            if (progressContainer) progressContainer.classList.add('hidden');
        } else {
            toggleBtn.innerHTML = '<i class="fas fa-layer-group"></i> CASCADA';
            toggleBtn.classList.replace('btn-primary', 'btn-secondary');
            if (footer) footer.classList.remove('hidden');
            if (progressContainer) progressContainer.classList.remove('hidden');
        }
        renderSlide();
    }

    function renderSlide() {
        const container = document.getElementById('container');
        
        if (mode === 'presentation') {
            container.className = 'flex-grow flex items-center justify-center p-6';
            const slide = slides[current];
            container.innerHTML = `
                <div class="w-full flex flex-col items-center">
                    <div class="mb-10 text-center">
                        <p class="text-xs font-black text-blue-500 uppercase tracking-[0.4em] mb-2">${slide.sub}</p>
                        <h2 class="text-4xl font-black text-gray-900 tracking-tight">${slide.title}</h2>
                    </div>
                    ${slide.content}
                </div>
            `;
            
            const counter = document.getElementById('counter');
            if (counter) counter.innerText = `${String(current + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
            const progressBar = document.getElementById('progress-bar');
            if (progressBar) progressBar.style.width = `${((current + 1) / slides.length) * 100}%`;
            
        } else {
            container.className = 'flex-grow flex flex-col items-center p-6 gap-12 py-12';
            container.innerHTML = slides.map((slide, i) => `
                <div class="w-full max-w-5xl bg-white/50 backdrop-blur rounded-3xl p-8 shadow-xl border border-gray-200 slide-fade" style="animation-delay: ${i * 0.1}s">
                    <div class="mb-8 text-center border-b pb-4">
                        <p class="text-xs font-black text-blue-500 uppercase tracking-[0.4em] mb-2">Diapositiva 0${i + 1} • ${slide.sub}</p>
                        <h2 class="text-3xl font-black text-gray-900 tracking-tight">${slide.title}</h2>
                    </div>
                    <div class="flex flex-col items-center">
                        ${slide.content}
                    </div>
                </div>
            `).join('');
        }

        attachInteractiveEvents();
    }

    function attachInteractiveEvents() {
        if (mode === 'cascade' || current === 1) {
            const tA = document.getElementById('tempA');
            const tB = document.getElementById('tempB');
            const tC = document.getElementById('tempC');
            if (tA && tB && tC) {
                const updateEquilibrio = () => {
                    const valA = parseInt(tA.value);
                    const valB = parseInt(tB.value);
                    const valC = parseInt(tC.value);
                    document.getElementById('valA').innerText = `${valA}°C`;
                    document.getElementById('valB').innerText = `${valB}°C`;
                    document.getElementById('valC').innerText = `${valC}°C`;
                    document.getElementById('fillA').style.height = `${valA}%`;
                    document.getElementById('fillB').style.height = `${valB}%`;
                    document.getElementById('fillC').style.height = `${valC}%`;

                    const eqAC = Math.abs(valA - valC) <= 2;
                    const eqBC = Math.abs(valB - valC) <= 2;
                    const lineAC = document.getElementById('lineAC');
                    const lineBC = document.getElementById('lineBC');
                    const labelAC = document.getElementById('labelAC');
                    const labelBC = document.getElementById('labelBC');
                    const status = document.getElementById('statusMsg');

                    if (eqAC) {
                        lineAC.setAttribute('stroke', '#3FB8AF');
                        labelAC.setAttribute('fill', '#3FB8AF');
                        labelAC.textContent = 'A = C ✓';
                    } else {
                        lineAC.setAttribute('stroke', '#9CA3AF');
                        labelAC.setAttribute('fill', '#9CA3AF');
                        labelAC.textContent = 'A ↔ C';
                    }

                    if (eqBC) {
                        lineBC.setAttribute('stroke', '#3FB8AF');
                        labelBC.setAttribute('fill', '#3FB8AF');
                        labelBC.textContent = 'B = C ✓';
                    } else {
                        lineBC.setAttribute('stroke', '#9CA3AF');
                        labelBC.setAttribute('fill', '#9CA3AF');
                        labelBC.textContent = 'B ↔ C';
                    }

                    if (eqAC && eqBC) {
                        status.className = 'mt-6 p-3 rounded-lg text-center text-sm font-bold transition-all duration-300 bg-green-100 text-green-700';
                        status.innerHTML = '<i class="fas fa-check-circle mr-1"></i> ¡A, B y C están en equilibrio! T<sub>A</sub> = T<sub>B</sub> = T<sub>C</sub>';
                    } else if (eqAC || eqBC) {
                        status.className = 'mt-6 p-3 rounded-lg text-center text-sm font-bold transition-all duration-300 bg-blue-50 text-blue-600';
                        status.innerHTML = 'Equilibrio parcial detectado. Ajusta para igualar todas las temperaturas.';
                    } else {
                        status.className = 'mt-6 p-3 rounded-lg text-center text-sm font-bold transition-all duration-300 bg-gray-100 text-gray-600';
                        status.innerHTML = 'Ajusta los sliders para ver el equilibrio';
                    }
                };
                tA.removeEventListener('input', tA._handler);
                tB.removeEventListener('input', tB._handler);
                tC.removeEventListener('input', tC._handler);
                tA._handler = updateEquilibrio;
                tB._handler = updateEquilibrio;
                tC._handler = updateEquilibrio;
                tA.addEventListener('input', updateEquilibrio);
                tB.addEventListener('input', updateEquilibrio);
                tC.addEventListener('input', updateEquilibrio);
                updateEquilibrio();
            }
        }

        if (mode === 'cascade' || current === 2) {
            const input = document.getElementById('tempInput');
            if (input) {
                const handler = (e) => {
                    const temp = parseInt(e.target.value);
                    document.getElementById('valDisplay').innerText = `${temp}°C`;
                    document.getElementById('mercurioFill').style.height = `${(temp / 600) * 85 + 15}%`;
                    const expansion = (temp / 600) * 45;
                    document.getElementById('metalBar').style.width = `${50 + expansion}%`;
                    document.getElementById('lDisplay').innerText = `L = ${(10 + (temp * 0.00012)).toFixed(4)} mm`;
                };
                input.removeEventListener('input', input._handler);
                input._handler = handler;
                input.addEventListener('input', handler);
                input.dispatchEvent(new Event('input'));
            }
        }

        if (mode === 'cascade' || current === 4) {
            const cInput = document.getElementById('celsiusInput');
            if (cInput) {
                const updateTemps = () => {
                    const c = parseFloat(cInput.value);
                    if (isNaN(c)) return;
                    document.getElementById('kelvinDisplay').innerText = (c + 273.15).toFixed(2);
                    document.getElementById('fahrenheitDisplay').innerText = ((c * 9/5) + 32).toFixed(2);
                };
                cInput.removeEventListener('input', cInput._handler);
                cInput._handler = updateTemps;
                cInput.addEventListener('input', updateTemps);
                updateTemps();
            }
        }
    }

    function changeSlide'''

match = re.search(r'function renderSlide\(\) \{.*?(?=function changeSlide)', content, re.DOTALL)
if match:
    content = content[:match.start()] + js_new + content[match.end() + 22:]
else:
    print("Could not find renderSlide function")

with open('Principal.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected cascade mode")
