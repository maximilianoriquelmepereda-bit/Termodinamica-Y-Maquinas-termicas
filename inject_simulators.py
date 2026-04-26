import re
import json

with open("Principal.html", "r", encoding="utf-8") as f:
    content = f.read()

slides_to_inject = """                {
                    sub: "Aplicación Industrial 1",
                    title: "Calibración en Baño Térmico",
                    content: `
        <div class="slide-fade w-full max-w-4xl">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="card-soft p-8 border-l-8 border-[#F9C74F]">
                    <h3 class="text-2xl font-bold mb-4 text-amarillo">Alineación de Termómetros</h3>
                    <p class="text-gray-600 mb-6">En la industria, para asegurar que un termómetro (B) es preciso, se sumerge junto con un termómetro patrón de alta precisión (A) en un baño térmico (C).</p>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center bg-gray-50 p-4 rounded-xl border border-gray-200">
                            <div>
                                <div class="text-[10px] font-bold text-gray-400 uppercase">Patrón (A)</div>
                                <div class="text-xl font-mono font-black text-gray-800">85.0 °C</div>
                            </div>
                            <div class="text-2xl text-green-500"><i class="fas fa-check-circle"></i></div>
                        </div>
                        <div class="flex justify-between items-center bg-yellow-50 p-4 rounded-xl border border-yellow-200 transition-colors" id="sim1_box">
                            <div>
                                <div class="text-[10px] font-bold text-gray-400 uppercase">Industrial (B)</div>
                                <div id="sim1_valB" class="text-xl font-mono font-black text-gray-800">70.0 °C</div>
                            </div>
                            <div id="sim1_status" class="text-2xl text-red-500"><i class="fas fa-times-circle"></i></div>
                        </div>
                    </div>
                    <div class="mt-6">
                        <label class="block text-xs font-bold text-gray-500 uppercase mb-2">Perilla de Calibración (B)</label>
                        <input type="range" id="sim1_slider" min="60" max="100" value="70" step="0.1" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#F9C74F]">
                    </div>
                </div>
                <div class="flex justify-center">
                    <div class="relative w-64 h-64 bg-gray-100 rounded-3xl overflow-hidden shadow-inner border-4 border-gray-300 flex items-end justify-center pb-4">
                        <div class="absolute bottom-0 w-full h-3/4 bg-yellow-400/20 backdrop-blur-sm border-t-2 border-yellow-500/50"></div>
                        <div class="absolute inset-0 flex justify-center items-center gap-8 mt-10">
                            <div class="flex flex-col items-center z-10">
                                <div class="w-6 h-32 bg-white/80 rounded-full border-2 border-gray-400 flex items-end p-1 shadow-md">
                                    <div class="w-full h-[85%] bg-red-500 rounded-full"></div>
                                </div>
                                <div class="mt-2 font-bold text-sm text-gray-600">A</div>
                            </div>
                            <div class="flex flex-col items-center z-10">
                                <div class="w-8 h-32 bg-gray-800 rounded flex items-center justify-center border-2 border-gray-600 shadow-xl relative">
                                    <div id="sim1_screen" class="w-6 h-10 bg-green-200 rounded-sm font-mono text-[8px] flex items-center justify-center font-bold absolute top-2 text-green-900">70.0</div>
                                    <div class="w-2 h-16 bg-gray-300 absolute bottom-0 rounded-b"></div>
                                </div>
                                <div class="mt-2 font-bold text-sm text-gray-600">B</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 2",
                    title: "Control de Hornos de Fundición",
                    content: `
        <div class="slide-fade w-full max-w-4xl">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="card-soft p-8 border-l-8 border-[#C84B31]">
                    <h3 class="text-2xl font-bold mb-4 text-bordo">Redundancia de Sensores</h3>
                    <p class="text-gray-600 mb-6">En altas temperaturas, los sensores se degradan. Usamos la Ley Cero colocando dos termopares (A y B) en el mismo metal fundido (C).</p>
                    <div class="space-y-4 mb-6">
                        <label class="block text-xs font-bold text-gray-500 uppercase">Potencia del Horno</label>
                        <input type="range" id="sim2_slider" min="500" max="1500" value="500" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#C84B31]">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-gray-800 p-4 rounded-xl text-center shadow-inner border border-gray-700">
                            <div class="text-[10px] text-gray-400 font-bold uppercase mb-1">Termopar A</div>
                            <div id="sim2_valA" class="text-2xl font-mono font-black text-red-500">500°C</div>
                        </div>
                        <div class="bg-gray-800 p-4 rounded-xl text-center shadow-inner border border-gray-700">
                            <div class="text-[10px] text-gray-400 font-bold uppercase mb-1">Termopar B <button id="sim2_failBtn" class="text-[8px] bg-red-600 text-white px-2 py-0.5 rounded ml-1 hover:bg-red-500 transition-colors">ROMPER</button></div>
                            <div id="sim2_valB" class="text-2xl font-mono font-black text-red-500">500°C</div>
                        </div>
                    </div>
                    <div id="sim2_alert" class="mt-4 p-3 rounded-lg text-xs font-bold text-center bg-green-100 text-green-700 transition-colors">
                        <i class="fas fa-shield-check"></i> Sensores en Equilibrio Térmico
                    </div>
                </div>
                <div class="flex justify-center relative">
                    <div class="w-64 h-64 bg-gray-300 rounded-b-full border-8 border-gray-600 overflow-hidden relative shadow-2xl flex items-end">
                        <div id="sim2_lava" class="w-full h-1/2 bg-gradient-to-t from-orange-600 to-yellow-500 transition-all duration-300 opacity-50 shadow-[0_0_30px_rgba(234,88,12,0.8)]"></div>
                        <div class="absolute top-0 left-16 w-3 h-48 bg-gray-800 rounded-b border border-gray-600 flex flex-col items-center">
                            <span class="text-white text-[10px] font-bold mt-2">A</span>
                        </div>
                        <div class="absolute top-0 right-16 w-3 h-48 bg-gray-800 rounded-b border border-gray-600 flex flex-col items-center">
                            <span class="text-white text-[10px] font-bold mt-2">B</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 3",
                    title: "Intercambiadores de Calor",
                    content: `
        <div class="slide-fade w-full max-w-4xl">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="card-soft p-8 border-l-8 border-[#3FB8AF]">
                    <h3 class="text-2xl font-bold mb-4 text-azul">Búsqueda del Equilibrio</h3>
                    <p class="text-gray-600 mb-6">Dos fluidos (frío y caliente) intercambian calor a través de una pared metálica. Su objetivo termodinámico es alcanzar una temperatura final de equilibrio.</p>
                    
                    <div class="space-y-6">
                        <div>
                            <label class="flex justify-between text-xs font-bold text-gray-500 uppercase mb-2">
                                <span>Caudal Agua Fría (20°C)</span>
                                <span id="sim3_flowC" class="text-blue-500">50%</span>
                            </label>
                            <input type="range" id="sim3_sliderC" min="10" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500">
                        </div>
                        <div>
                            <label class="flex justify-between text-xs font-bold text-gray-500 uppercase mb-2">
                                <span>Caudal Agua Caliente (90°C)</span>
                                <span id="sim3_flowH" class="text-red-500">50%</span>
                            </label>
                            <input type="range" id="sim3_sliderH" min="10" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-red-500">
                        </div>
                    </div>
                    
                    <div class="mt-8 bg-gray-50 p-4 rounded-xl border border-gray-200 text-center shadow-inner">
                        <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Temperatura de Equilibrio a la Salida</div>
                        <div id="sim3_eq" class="text-4xl font-black font-mono text-purple-600 transition-all duration-300">55.0 °C</div>
                    </div>
                </div>
                <div class="flex flex-col items-center">
                    <div class="w-full max-w-sm h-48 bg-gray-200 rounded-xl border-4 border-gray-400 relative overflow-hidden flex flex-col justify-center">
                        <div class="w-full h-1/2 flex relative border-b-2 border-gray-400">
                            <div class="w-1/2 h-full bg-red-500 opacity-80 flex items-center px-2 text-white text-[10px] font-bold">HOT IN</div>
                            <div id="sim3_outH" class="w-1/2 h-full bg-purple-500 transition-colors duration-500 flex items-center justify-end px-2 text-white text-[10px] font-bold">OUT</div>
                            <div class="absolute inset-0 flex items-center justify-center opacity-50"><i class="fas fa-chevron-right text-white text-2xl"></i></div>
                        </div>
                        <div class="w-full h-1/2 flex relative">
                            <div id="sim3_outC" class="w-1/2 h-full bg-purple-500 transition-colors duration-500 flex items-center px-2 text-white text-[10px] font-bold">OUT</div>
                            <div class="w-1/2 h-full bg-blue-500 opacity-80 flex items-center justify-end px-2 text-white text-[10px] font-bold">COLD IN</div>
                            <div class="absolute inset-0 flex items-center justify-center opacity-50"><i class="fas fa-chevron-left text-white text-2xl"></i></div>
                        </div>
                    </div>
                    <div class="mt-4 text-xs font-bold text-gray-400 text-center">Intercambiador de Contraflujo</div>
                </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 4",
                    title: "Cámaras Frigoríficas",
                    content: `
        <div class="slide-fade w-full max-w-4xl">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="card-soft p-8 border-l-8 border-[#9B5DE5]">
                    <h3 class="text-2xl font-bold mb-4 text-lavanda">Maduración Térmica</h3>
                    <p class="text-gray-600 mb-6">Los productos (A) se introducen en una cámara fría (C). Con el tiempo, transfieren su calor al aire hasta alcanzar el equilibrio térmico.</p>
                    
                    <div class="flex justify-center mb-8">
                        <button id="sim4_btn" class="bg-gradient-to-r from-purple-500 to-indigo-500 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:shadow-xl hover:scale-105 transition-all w-full flex items-center justify-center gap-2">
                            <i class="fas fa-box"></i> Ingresar Lote de Productos (25°C)
                        </button>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-blue-50 p-4 rounded-xl border border-blue-100 text-center">
                            <i class="fas fa-snowflake text-blue-400 text-xl mb-2"></i>
                            <div class="text-[10px] font-bold text-gray-500 uppercase">Cámara (C)</div>
                            <div class="text-xl font-mono font-black text-blue-700">-18.0 °C</div>
                        </div>
                        <div class="bg-orange-50 p-4 rounded-xl border border-orange-100 text-center transition-colors duration-[3000ms]" id="sim4_prodBox">
                            <i class="fas fa-apple-alt text-orange-400 text-xl mb-2 transition-colors duration-[3000ms]" id="sim4_prodIcon"></i>
                            <div class="text-[10px] font-bold text-gray-500 uppercase">Producto (A)</div>
                            <div id="sim4_prodTemp" class="text-xl font-mono font-black text-orange-700 transition-colors duration-[3000ms]">--.- °C</div>
                        </div>
                    </div>
                </div>
                <div class="flex justify-center">
                    <div class="w-64 h-64 bg-blue-100 rounded-xl border-4 border-blue-300 shadow-inner relative overflow-hidden flex flex-col p-4">
                        <div class="text-blue-400 font-bold text-xs mb-2 flex items-center gap-1"><i class="fas fa-wind"></i> Aire a -18°C</div>
                        <div id="sim4_boxes" class="flex-grow grid grid-cols-2 gap-2 opacity-0 transform translate-y-10 transition-all duration-500">
                            <div class="bg-orange-300 rounded shadow-sm border border-orange-400 transition-colors duration-[3000ms] box-color"></div>
                            <div class="bg-orange-300 rounded shadow-sm border border-orange-400 transition-colors duration-[3000ms] box-color"></div>
                            <div class="bg-orange-300 rounded shadow-sm border border-orange-400 transition-colors duration-[3000ms] box-color"></div>
                            <div class="bg-orange-300 rounded shadow-sm border border-orange-400 transition-colors duration-[3000ms] box-color"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 5",
                    title: "Refrigeración de Moldes",
                    content: `
        <div class="slide-fade w-full max-w-4xl">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="card-soft p-8 border-l-8 border-[#F8961E]">
                    <h3 class="text-2xl font-bold mb-4 text-naranja">Moldeo por Inyección</h3>
                    <p class="text-gray-600 mb-6">Plástico a 200°C (A) llena un molde (C). Canales de agua (B) enfrían el molde. Solidifica al llegar al equilibrio (< 60°C).</p>
                    
                    <div class="mb-6">
                        <label class="flex justify-between text-xs font-bold text-gray-500 uppercase mb-2">
                            <span>Temperatura del Agua</span>
                            <span id="sim5_water" class="text-blue-500">20°C</span>
                        </label>
                        <input type="range" id="sim5_slider" min="10" max="50" value="20" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500">
                    </div>
                    
                    <button id="sim5_injectBtn" class="bg-orange-500 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-orange-600 transition-all w-full mb-4">
                        <i class="fas fa-fill-drip"></i> Inyectar Plástico
                    </button>
                    
                    <div class="w-full bg-gray-200 rounded-full h-4 overflow-hidden relative border border-gray-300">
                        <div id="sim5_progress" class="bg-green-500 h-full w-0 transition-all duration-75"></div>
                    </div>
                    <div id="sim5_status" class="text-[10px] text-center font-bold text-gray-500 uppercase mt-2">Esperando Inyección...</div>
                </div>
                <div class="flex justify-center">
                    <div class="w-64 h-64 bg-gray-300 rounded-lg border-4 border-gray-500 shadow-xl relative p-4 flex items-center justify-center">
                        <div class="absolute inset-0 flex flex-col justify-between p-4 opacity-50 pointer-events-none">
                            <div class="w-full h-2 bg-blue-500 rounded-full"></div>
                            <div class="w-full h-2 bg-blue-500 rounded-full"></div>
                            <div class="w-full h-2 bg-blue-500 rounded-full"></div>
                            <div class="w-full h-2 bg-blue-500 rounded-full"></div>
                        </div>
                        <div class="relative z-10 w-32 h-32 flex items-center justify-center">
                            <i id="sim5_piece" class="fas fa-cog text-8xl text-gray-200 drop-shadow-md transition-colors duration-100"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
                },
"""

js_inject = """
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
"""

# Insert slides before "Nuestra Historia" slide
historia_re = r'(\{\s*sub:\s*"Nuestra Historia",)'
content = re.sub(historia_re, slides_to_inject + r'\1', content)

# Insert JS at the end of attachInteractiveEvents
js_re = r'(cInput\.addEventListener\(\'input\', updateTemps\);\s*updateTemps\(\);\s*\}\s*\})'
content = re.sub(js_re, r'\1\n' + js_inject, content)

with open("Principal.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Injected 5 simulators successfully")
