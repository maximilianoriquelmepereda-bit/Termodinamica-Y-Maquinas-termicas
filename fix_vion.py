import re

# We will read Principal.html and manually reconstruct the slides and attachInteractiveEvents

with open('Principal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to extract slide 0 (Intro), 1 (Equilibrio), 2 (Dilatación), 3 (Mezcla) from the file
s0_match = re.search(r'\{\s*sub:\s*"Escuela Técnica N° 4-109".*?</div>\s*`\s*\}', content, re.DOTALL)
s1_match = re.search(r'\{\s*sub:\s*"Principio Fundamental".*?</div>\s*`\s*\}', content, re.DOTALL)
s2_match = re.search(r'\{\s*sub:\s*"Simulación Interactiva".*?</div>\s*`\s*\}', content, re.DOTALL)

s3 = """                {
                    sub: "Análisis Práctico",
                    title: "Ejercicio: Mezcla Vapor y Agua",
                    content: `
                <div class="bg-white rounded-3xl overflow-hidden shadow-lg border border-gray-100 w-full max-w-4xl flex flex-col md:flex-row slide-fade">
                    <div class="p-10 bordo-bg text-white md:w-2/5">
                        <h3 class="text-3xl font-black mb-6">El Escenario</h3>
                        <ul class="space-y-4 font-bold text-sm opacity-90">
                            <li><i class="fas fa-cloud mr-2"></i> 2 kg de Vapor (100°C)</li>
                            <li><i class="fas fa-tint mr-2"></i> 10 kg de Agua (15°C)</li>
                        </ul>
                    </div>
                    <div class="p-10 md:w-3/5">
                        <h4 class="text-xs font-black text-gray-400 uppercase mb-6 tracking-widest">Resultado del Cálculo</h4>
                        <div class="space-y-6">
                            <div class="flex items-center gap-4 border-b pb-4">
                                <span class="w-10 h-10 flex items-center justify-center rounded bg-gray-100 font-black">1</span>
                                <p class="text-sm">El vapor tiene energía de sobra para calentar toda el agua.</p>
                            </div>
                            <div class="flex items-center gap-4 border-b pb-4">
                                <span class="w-10 h-10 flex items-center justify-center rounded bg-gray-100 font-black">2</span>
                                <p class="text-sm">Solo se condensa una fracción del vapor.</p>
                            </div>
                            <div class="p-4 bg-green-50 text-green-700 rounded-xl font-black text-center text-lg">
                                Equilibrio Final: 100 °C
                            </div>
                        </div>
                    </div>
                </div>
            `
                }"""

s4 = """                {
                    sub: "Ejemplo Práctico",
                    title: "Conversión de Escalas",
                    content: `
                <div class="slide-fade w-full max-w-4xl">
                    <div class="card-soft p-8 border-t-8 border-[#F9C74F]">
                        <h3 class="text-2xl font-bold mb-6 text-center text-gray-800">Termómetro Digital Multi-Escala</h3>
                        <div class="flex flex-col md:flex-row items-center justify-center gap-6">
                            <div class="w-full md:w-1/3">
                                <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Celsius</label>
                                <input type="number" id="celsiusInput" value="100" class="w-full p-3 rounded-xl border-2 border-gray-200 text-center font-mono font-bold text-xl focus:border-[#C84B31] outline-none transition-colors">
                            </div>
                            <div class="text-2xl text-gray-300"><i class="fas fa-equals"></i></div>
                            <div class="w-full md:w-1/3 bg-[#3FB8AF] text-white p-4 rounded-xl text-center shadow-lg">
                                <div class="text-xs font-bold opacity-80 uppercase">Kelvin</div>
                                <div id="kelvinDisplay" class="text-2xl font-black font-mono">373.15</div>
                            </div>
                            <div class="w-full md:w-1/3 bg-[#F9C74F] text-gray-800 p-4 rounded-xl text-center shadow-lg">
                                <div class="text-xs font-bold opacity-80 uppercase">Fahrenheit</div>
                                <div id="fahrenheitDisplay" class="text-2xl font-black font-mono">212.00</div>
                            </div>
                        </div>
                        <p class="text-center text-sm text-gray-500 mt-6"><i class="fas fa-lightbulb text-[#F9C74F] mr-2"></i><strong>Dato:</strong> El cero absoluto es 0 K = -273.15 °C = -459.67 °F. No se puede alcanzar.</p>
                    </div>
                </div>
            `
                }"""

s5 = """                {
                    sub: "Ejemplo Práctico",
                    title: "Punto Triple del Agua",
                    content: `
                <div class="slide-fade w-full max-w-4xl">
                    <div class="grid md:grid-cols-2 gap-8 items-center">
                        <div class="card-soft p-8 border-l-8 border-[#3FB8AF]">
                            <h3 class="text-2xl font-bold mb-4 text-azul">Referencia Universal</h3>
                            <p class="text-gray-600 mb-4">El punto triple del agua es el estado donde coexisten hielo, agua líquida y vapor en equilibrio térmico.</p>
                            <div class="space-y-3">
                                <div class="flex items-center gap-3 bg-teal-50 p-3 rounded-lg">
                                    <i class="fas fa-temperature-low text-[#3FB8AF] text-xl"></i>
                                    <div>
                                        <div class="text-xs text-gray-500 font-bold uppercase">Temperatura</div>
                                        <div class="font-mono font-bold text-gray-800">273.16 K exactos</div>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3 bg-blue-50 p-3 rounded-lg">
                                    <i class="fas fa-tachometer-alt text-blue-500 text-xl"></i>
                                    <div>
                                        <div class="text-xs text-gray-500 font-bold uppercase">Presión</div>
                                        <div class="font-mono font-bold text-gray-800">611.657 Pa</div>
                                    </div>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">La Ley Cero garantiza que cualquier termómetro calibrado aquí dará lecturas consistentes en cualquier otro sistema en equilibrio.</p>
                        </div>
                        <div class="flex flex-col items-center gap-4">
                            <div class="relative w-48 h-48">
                                <svg viewBox="0 0 200 200" class="w-full h-full drop-shadow-xl">
                                    <circle cx="100" cy="100" r="80" fill="#E0F2FE" stroke="#3FB8AF" stroke-width="4"/>
                                    <text x="100" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#0E7490">H₂O</text>
                                    <text x="100" y="115" text-anchor="middle" font-size="10" fill="#0E7490">273.16 K</text>
                                    <g transform="translate(60,60)">
                                        <rect x="0" y="0" width="24" height="24" rx="4" fill="#BAE6FD" stroke="#3FB8AF" stroke-width="2"/>
                                        <text x="12" y="16" text-anchor="middle" font-size="8" fill="#0E7490">S</text>
                                    </g>
                                    <g transform="translate(116,60)">
                                        <circle cx="12" cy="12" r="10" fill="#BAE6FD" stroke="#3FB8AF" stroke-width="2"/>
                                        <text x="12" y="16" text-anchor="middle" font-size="8" fill="#0E7490">L</text>
                                    </g>
                                    <g transform="translate(88,116)">
                                        <path d="M2,12 L12,2 L22,12" fill="none" stroke="#3FB8AF" stroke-width="2"/>
                                        <text x="12" y="24" text-anchor="middle" font-size="8" fill="#0E7490">G</text>
                                    </g>
                                </svg>
                            </div>
                            <div class="bg-white px-4 py-2 rounded-full shadow text-xs font-bold text-gray-500">
                                <i class="fas fa-check-circle text-green-500 mr-1"></i> Base de la Escala ITS-90
                            </div>
                        </div>
                    </div>
                </div>
            `
                }"""

s_sims_match = re.search(r'(\{\s*sub:\s*"Aplicación Industrial 1".*?\}\s*\},)', content, re.DOTALL)
s_hist_match = re.search(r'(\{\s*sub:\s*"Nuestra Historia".*?</div>\s*`\s*\})', content, re.DOTALL)

# Reconstruct array
new_slides_array = f"const slides = [\n{s0_match.group(0)},\n{s1_match.group(0)},\n{s2_match.group(0)},\n{s3},\n{s4},\n{s5},\n{s_sims_match.group(1)}\n{s_hist_match.group(1)}\n];"

# Replace the slides array
content = re.sub(r'const slides = \[.*?\];', new_slides_array, content, flags=re.DOTALL)

# Now fix attachInteractiveEvents
new_attach = """function attachInteractiveEvents() {
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
                            document.getElementById('fahrenheitDisplay').innerText = ((c * 9 / 5) + 32).toFixed(2);
                        };
                        cInput.removeEventListener('input', cInput._handler);
                        cInput._handler = updateTemps;
                        cInput.addEventListener('input', updateTemps);
                        updateTemps();
                    }
                }

        if (mode === 'cascade' || current === 6) {
            const s1 = document.getElementById('sim1_slider');
            if (s1 && !s1.dataset.init) {
                s1.dataset.init = 'true';
                const handler = (e) => {
                    const val = parseFloat(e.target.value);
                    document.getElementById('sim1_valB').innerText = val.toFixed(1) + ' °C';
                    document.getElementById('sim1_screen').innerText = val.toFixed(1);
                    const status = document.getElementById('sim1_status');
                    const box = document.getElementById('sim1_box');
                    if (val >= 84.8 && val <= 85.2) {
                        status.innerHTML = '<i class="fas fa-check-circle"></i>';
                        status.className = 'text-2xl text-green-500';
                        box.className = 'flex justify-between items-center bg-green-50 p-4 rounded-xl border border-green-200 transition-colors';
                    } else {
                        status.innerHTML = '<i class="fas fa-times-circle"></i>';
                        status.className = 'text-2xl text-red-500';
                        box.className = 'flex justify-between items-center bg-yellow-50 p-4 rounded-xl border border-yellow-200 transition-colors';
                    }
                };
                s1.addEventListener('input', handler);
                s1.dispatchEvent(new Event('input'));
            }
        }

        if (mode === 'cascade' || current === 7) {
            const s2 = document.getElementById('sim2_slider');
            const failBtn = document.getElementById('sim2_failBtn');
            if (s2 && !s2.dataset.init) {
                s2.dataset.init = 'true';
                s2.failed = false;
                const update2 = () => {
                    const val = parseInt(s2.value);
                    document.getElementById('sim2_valA').innerText = val + '°C';
                    document.getElementById('sim2_valB').innerText = s2.failed ? Math.max(0, val - 120) + '°C' : val + '°C';
                    document.getElementById('sim2_lava').style.opacity = 0.5 + (val / 1500) * 0.5;
                    const alert = document.getElementById('sim2_alert');
                    if (s2.failed) {
                        alert.className = 'mt-4 p-3 rounded-lg text-xs font-bold text-center bg-red-100 text-red-700 transition-colors';
                        alert.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ¡Peligro! Pérdida de Equilibrio Detectada.';
                    } else {
                        alert.className = 'mt-4 p-3 rounded-lg text-xs font-bold text-center bg-green-100 text-green-700 transition-colors';
                        alert.innerHTML = '<i class="fas fa-shield-check"></i> Sensores en Equilibrio Térmico';
                    }
                };
                s2.addEventListener('input', update2);
                if (failBtn) {
                    failBtn.addEventListener('click', () => {
                        s2.failed = !s2.failed;
                        failBtn.innerText = s2.failed ? 'REPARAR' : 'ROMPER';
                        failBtn.className = s2.failed ? 'text-[8px] bg-green-600 text-white px-2 py-0.5 rounded ml-1 hover:bg-green-500 transition-colors' : 'text-[8px] bg-red-600 text-white px-2 py-0.5 rounded ml-1 hover:bg-red-500 transition-colors';
                        update2();
                    });
                }
            }
        }

        if (mode === 'cascade' || current === 8) {
            const sC = document.getElementById('sim3_sliderC');
            const sH = document.getElementById('sim3_sliderH');
            if (sC && sH && !sC.dataset.init) {
                sC.dataset.init = 'true';
                const update3 = () => {
                    const fc = parseInt(sC.value);
                    const fh = parseInt(sH.value);
                    document.getElementById('sim3_flowC').innerText = fc + '%';
                    document.getElementById('sim3_flowH').innerText = fh + '%';
                    const eq = ((fc * 20) + (fh * 90)) / (fc + fh);
                    document.getElementById('sim3_eq').innerText = eq.toFixed(1) + ' °C';
                    const r = Math.round(100 + (eq-20)*2.2);
                    const b = Math.round(255 - (eq-20)*2.2);
                    document.getElementById('sim3_outH').style.backgroundColor = `rgb(${r}, 100, ${b})`;
                    document.getElementById('sim3_outC').style.backgroundColor = `rgb(${r}, 100, ${b})`;
                };
                sC.addEventListener('input', update3);
                sH.addEventListener('input', update3);
                sC.dispatchEvent(new Event('input'));
            }
        }

        if (mode === 'cascade' || current === 9) {
            const btn = document.getElementById('sim4_btn');
            if (btn && !btn.dataset.init) {
                btn.dataset.init = 'true';
                btn.addEventListener('click', () => {
                    if (btn.isCooling) return;
                    btn.isCooling = true;
                    
                    const boxes = document.getElementById('sim4_boxes');
                    const temp = document.getElementById('sim4_prodTemp');
                    const boxColors = document.querySelectorAll('.box-color');
                    const prodBox = document.getElementById('sim4_prodBox');
                    const prodIcon = document.getElementById('sim4_prodIcon');
                    
                    btn.classList.add('opacity-50');
                    boxes.classList.remove('opacity-0', 'translate-y-10');
                    
                    temp.innerText = '25.0 °C';
                    temp.classList.replace('text-blue-700', 'text-orange-700');
                    prodBox.classList.replace('bg-blue-50', 'bg-orange-50');
                    prodBox.classList.replace('border-blue-100', 'border-orange-100');
                    prodIcon.classList.replace('text-blue-400', 'text-orange-400');
                    boxColors.forEach(b => {
                        b.classList.replace('bg-blue-300', 'bg-orange-300');
                        b.classList.replace('border-blue-400', 'border-orange-400');
                    });
                    
                    setTimeout(() => {
                        temp.innerText = '-18.0 °C';
                        temp.classList.replace('text-orange-700', 'text-blue-700');
                        prodBox.classList.replace('bg-orange-50', 'bg-blue-50');
                        prodBox.classList.replace('border-orange-100', 'border-blue-100');
                        prodIcon.classList.replace('text-orange-400', 'text-blue-400');
                        boxColors.forEach(b => {
                            b.classList.replace('bg-orange-300', 'bg-blue-300');
                            b.classList.replace('border-orange-400', 'border-blue-400');
                        });
                        
                        setTimeout(() => {
                            btn.classList.remove('opacity-50');
                            btn.innerHTML = '<i class="fas fa-redo"></i> Reiniciar Simulación';
                            btn.isCooling = false;
                        }, 3000);
                    }, 500);
                });
            }
        }

        if (mode === 'cascade' || current === 10) {
            const btn = document.getElementById('sim5_injectBtn');
            const slider = document.getElementById('sim5_slider');
            if (btn && slider && !btn.dataset.init) {
                btn.dataset.init = 'true';
                slider.addEventListener('input', (e) => {
                    document.getElementById('sim5_water').innerText = e.target.value + '°C';
                });
                
                btn.addEventListener('click', () => {
                    if (btn.coolingInterv) clearInterval(btn.coolingInterv);
                    const piece = document.getElementById('sim5_piece');
                    const prog = document.getElementById('sim5_progress');
                    const status = document.getElementById('sim5_status');
                    const waterTemp = parseInt(slider.value);
                    
                    piece.classList.replace('text-gray-200', 'text-orange-500');
                    piece.classList.replace('text-gray-500', 'text-orange-500');
                    prog.style.width = '0%';
                    status.innerText = 'Enfriando desde 200°C...';
                    
                    btn.disabled = true;
                    btn.classList.add('opacity-50');
                    
                    let currTemp = 200;
                    const coolRate = (50 - waterTemp) / 10 + 1; 
                    
                    btn.coolingInterv = setInterval(() => {
                        currTemp -= coolRate;
                        const pct = Math.max(0, Math.min(100, ((200 - currTemp) / (200 - waterTemp)) * 100));
                        prog.style.width = pct + '%';
                        
                        if (currTemp <= 60) {
                            clearInterval(btn.coolingInterv);
                            piece.classList.replace('text-orange-500', 'text-gray-500');
                            status.innerText = '¡Pieza Solidificada! Equilibrio térmico alcanzado.';
                            btn.disabled = false;
                            btn.classList.remove('opacity-50');
                        }
                    }, 100);
                });
            }
        }
    }"""

content = re.sub(r'function attachInteractiveEvents\(\) \{.*?(?=\n\s*function changeSlide)', new_attach, content, flags=re.DOTALL)

with open('Principal.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Principal.html fixed successfully.")
