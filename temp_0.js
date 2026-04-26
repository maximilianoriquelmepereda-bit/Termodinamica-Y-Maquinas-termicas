
            let current = 0;
            const slides = [
{
                    sub: "Escuela Técnica N° 4-109",
                    title: "Ley Cero de la Termodinámica",
                    content: `
                <div class="text-center slide-fade">
                    <div class="mb-8 inline-block p-6 rounded-full bg-gradient-to-br from-red-50 to-orange-50 text-bordo shadow-lg">
                        <i class="fas fa-temperature-low text-6xl"></i>
                    </div>
                    <h2 class="text-6xl font-black text-gradient mb-4 tracking-tighter">LEY CERO</h2>
                    <p class="text-xl text-gray-500 mb-12">Análisis de Equilibrio Térmico y Aplicaciones</p>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto">
                        <a href="maxi.html" class="p-4 bg-white rounded-xl shadow-md border-b-4 border-[#C84B31] font-bold text-sm hover:shadow-lg hover:scale-105 transition-all cursor-pointer text-gray-800 text-center no-underline">M. Riquelme</a>
                        <a href="cele.html" class="p-4 bg-white rounded-xl shadow-md border-b-4 border-[#3FB8AF] font-bold text-sm hover:shadow-lg hover:scale-105 transition-all cursor-pointer text-gray-800 text-center no-underline">C. Núñez</a>
                        <a href="dante.html" class="p-4 bg-white rounded-xl shadow-md border-b-4 border-[#F9C74F] font-bold text-sm hover:shadow-lg hover:scale-105 transition-all cursor-pointer text-gray-800 text-center no-underline">D. Cáceres</a>
                        <a href="juan.html" class="p-4 bg-white rounded-xl shadow-md border-b-4 border-[#9B5DE5] font-bold text-sm hover:shadow-lg hover:scale-105 transition-all cursor-pointer text-gray-800 text-center no-underline">J. Baigorria</a>
                    </div>
                    <div class="mt-12 flex justify-center gap-6 text-sm text-gray-400">
                        <span class="flex items-center gap-2"><i class="fas fa-calendar text-[#F8961E]"></i> 2026</span>
                        <span class="flex items-center gap-2"><i class="fas fa-graduation-cap text-[#3FB8AF]"></i> 5º Año</span>
                    </div>
                </div>
            `
                },
                {
                    sub: "Principio Fundamental",
                    title: "Equilibrio y Transitividad",
                    content: `
                <div class="slide-fade w-full max-w-6xl">
                    <div class="grid lg:grid-cols-3 gap-6 items-stretch">
                        <!-- Panel de controles -->
                        <div class="card-soft p-6 border-t-4 border-[#C84B31] flex flex-col justify-center">
                            <h3 class="text-xl font-bold mb-4 text-bordo">Ajusta las Temperaturas</h3>
                            <div class="space-y-5">
                                <div>
                                    <label class="flex justify-between text-sm font-bold text-gray-700 mb-1">
                                        <span>Cuerpo A</span>
                                        <span id="valA" class="text-[#C84B31]">50°C</span>
                                    </label>
                                    <input type="range" id="tempA" min="0" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#C84B31]">
                                </div>
                                <div>
                                    <label class="flex justify-between text-sm font-bold text-gray-700 mb-1">
                                        <span>Cuerpo B</span>
                                        <span id="valB" class="text-[#F9C74F]">50°C</span>
                                    </label>
                                    <input type="range" id="tempB" min="0" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#F9C74F]">
                                </div>
                                <div>
                                    <label class="flex justify-between text-sm font-bold text-gray-700 mb-1">
                                        <span>Cuerpo C (Referencia)</span>
                                        <span id="valC" class="text-[#3FB8AF]">50°C</span>
                                    </label>
                                    <input type="range" id="tempC" min="0" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#3FB8AF]">
                                </div>
                            </div>
                            <div id="statusMsg" class="mt-6 p-3 rounded-lg text-center text-sm font-bold transition-all duration-300 bg-gray-100 text-gray-600">
                                Ajusta los sliders para ver el equilibrio
                            </div>
                        </div>
                        <!-- Visualización -->
                        <div class="flex flex-col items-center justify-center gap-4 bg-white/50 rounded-xl p-4">
                            <div class="flex items-end justify-center gap-6 w-full">
                                <!-- Termómetro A -->
                                <div class="flex flex-col items-center gap-2">
                                    <div class="thermometer" style="height:160px; width:36px; border-width:3px;">
                                        <div id="fillA" class="thermometer-bulb" style="height:50%; background:linear-gradient(to top, #C84B31, #E85D4E);"></div>
                                    </div>
                                    <span class="text-xs font-black text-[#C84B31]">A</span>
                                </div>
                                <!-- Termómetro C -->
                                <div class="flex flex-col items-center gap-2">
                                    <div class="thermometer" style="height:180px; width:36px; border-width:3px;">
                                        <div id="fillC" class="thermometer-bulb" style="height:50%; background:linear-gradient(to top, #3FB8AF, #7FD1B9);"></div>
                                    </div>
                                    <span class="text-xs font-black text-[#3FB8AF]">C</span>
                                </div>
                                <!-- Termómetro B -->
                                <div class="flex flex-col items-center gap-2">
                                    <div class="thermometer" style="height:160px; width:36px; border-width:3px;">
                                        <div id="fillB" class="thermometer-bulb" style="height:50%; background:linear-gradient(to top, #F9C74F, #FDE68A);"></div>
                                    </div>
                                    <span class="text-xs font-black text-[#F9C74F]">B</span>
                                </div>
                            </div>
                            <svg width="300" height="80" viewBox="0 0 300 80" class="mt-2">
                                <line id="lineAC" x1="45" y1="40" x2="150" y2="40" stroke="#9CA3AF" stroke-width="4" stroke-linecap="round" />
                                <line id="lineBC" x1="255" y1="40" x2="150" y2="40" stroke="#9CA3AF" stroke-width="4" stroke-linecap="round" />
                                <text id="labelAC" x="97" y="32" text-anchor="middle" font-size="10" font-weight="bold" fill="#9CA3AF">A ↔ C</text>
                                <text id="labelBC" x="202" y="32" text-anchor="middle" font-size="10" font-weight="bold" fill="#9CA3AF">B ↔ C</text>
                            </svg>
                        </div>
                        <!-- Cuadro Como Funciona -->
                        <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Si el cuerpo <strong>A</strong> está en equilibrio térmico con el cuerpo <strong>C</strong> (la misma temperatura), y el cuerpo <strong>B</strong> también está en equilibrio térmico con <strong>C</strong>, entonces <strong>A y B</strong> estarán en equilibrio térmico entre sí. <br><br>Esta propiedad transitiva es la base fundamental de todos los termómetros.
                            </p>
                        </div>
                    </div>
                </div>
            `
                },
                {
                    sub: "Simulación Interactiva",
                    title: "Dilatación Térmica",
                    content: `
                <div class="slide-fade w-full max-w-6xl">
                    <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                        <div class="card-soft p-6 flex flex-col justify-center">
                            <h3 class="text-2xl font-bold mb-4 text-bordo">Simulador de Dilatación</h3>
                            <p class="text-gray-600 mb-6 text-sm">Ajusta la temperatura y observa cómo el mercúrio y la barra de metal responden al calor.</p>
                            <div class="mb-6">
                                <label class="block text-sm font-bold text-gray-700 mb-2">Temperatura: <span id="valDisplay" class="text-[#C84B31]">25°C</span></label>
                                <input type="range" id="tempInput" min="0" max="600" value="25" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#C84B31]">
                                <div class="flex justify-between text-[10px] text-gray-400 mt-1">
                                    <span>0°C</span>
                                    <span>300°C</span>
                                    <span>600°C</span>
                                </div>
                            </div>
                            <div class="bg-gray-50 p-4 rounded-lg font-mono text-center border-l-4 border-[#3FB8AF] shadow-inner">
                                <div id="lDisplay" class="text-lg font-bold text-gray-800">L = 10.0030 mm</div>
                                <div class="text-xs text-gray-500 mt-1">ΔL = α · L₀ · ΔT</div>
                            </div>
                        </div>
                        <div class="flex flex-col items-center justify-center gap-8 bg-white/50 rounded-xl p-4">
                            <div class="flex items-end gap-4">
                                <div class="thermometer">
                                    <div id="mercurioFill" class="thermometer-bulb" style="height: 18%"></div>
                                    <div class="thermometer-ticks">
                                        <div class="tick"></div><div class="tick"></div><div class="tick"></div>
                                        <div class="tick"></div><div class="tick"></div><div class="tick"></div>
                                        <div class="tick"></div><div class="tick"></div><div class="tick"></div>
                                    </div>
                                </div>
                                <div class="text-xs font-bold text-gray-400 mb-4">°C</div>
                            </div>
                            <div class="w-full max-w-xs">
                                <div class="text-xs font-bold text-gray-500 mb-1 text-center">Barra de Acero (L₀ = 10 mm)</div>
                                <div class="w-full bg-gray-200 rounded-full h-8 p-1 shadow-inner">
                                    <div id="metalBar" class="h-full rounded bg-gradient-to-b from-gray-300 via-gray-100 to-gray-300 border border-gray-500 transition-all duration-100" style="width: 50%"></div>
                                </div>
                            </div>
                        </div>
                        <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Al transferir calor a un material, sus partículas se mueven más rápido y se separan, aumentando su volumen. <br><br>
                                En los termómetros, el mercurio se dilata proporcionalmente a la temperatura, permitiendo medirla visualmente. La ecuación <strong>ΔL = α · L₀ · ΔT</strong> calcula cuánto crece un material sólido según su coeficiente <strong>α</strong>.
                            </p>
                        </div>
                    </div>
                </div>
            `
                },
                {
                    sub: "Análisis Práctico",
                    title: "Ejercicio: Mezcla Vapor y Agua",
                    content: `
                <div class="bg-white rounded-3xl overflow-hidden shadow-lg border border-gray-100 w-full max-w-6xl flex flex-col md:flex-row slide-fade">
                    <div class="p-10 bordo-bg text-white md:w-1/3 flex flex-col justify-center">
                        <h3 class="text-3xl font-black mb-6">El Escenario</h3>
                        <ul class="space-y-4 font-bold text-sm opacity-90">
                            <li><i class="fas fa-cloud mr-2"></i> 2 kg de Vapor (100°C)</li>
                            <li><i class="fas fa-tint mr-2"></i> 10 kg de Agua (15°C)</li>
                        </ul>
                    </div>
                    <div class="p-10 md:w-1/3 flex flex-col justify-center bg-gray-50 border-r border-gray-200">
                        <h4 class="text-xs font-black text-gray-400 uppercase mb-6 tracking-widest">Resultado del Cálculo</h4>
                        <div class="space-y-6">
                            <div class="flex items-center gap-4 border-b pb-4">
                                <span class="w-10 h-10 flex items-center justify-center rounded bg-gray-100 font-black">1</span>
                                <p class="text-sm">El vapor tiene energía de sobra para calentar el agua.</p>
                            </div>
                            <div class="flex items-center gap-4 border-b pb-4">
                                <span class="w-10 h-10 flex items-center justify-center rounded bg-gray-100 font-black">2</span>
                                <p class="text-sm">Solo se condensa una fracción del vapor.</p>
                            </div>
                            <div class="p-4 bg-green-50 text-green-700 rounded-xl font-black text-center text-lg shadow-sm border border-green-200">
                                Equilibrio: 100 °C
                            </div>
                        </div>
                    </div>
                    <div class="p-10 md:w-1/3 bg-indigo-50 flex flex-col justify-center">
                        <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                        <p class="text-xs text-gray-700 leading-relaxed font-medium">
                            El <strong>calor latente de vaporización</strong> del agua es gigantesco en comparación con su calor específico. Al mezclarse, el vapor cede tanto calor al condensarse que logra calentar toda el agua fría hasta los 100°C antes de condensarse por completo. El equilibrio final es una mezcla de agua líquida y vapor a 100°C.
                        </p>
                    </div>
                </div>
            `
                },
                {
                    sub: "Ejemplo Práctico",
                    title: "Conversión de Escalas",
                    content: `
                <div class="slide-fade w-full max-w-6xl">
                    <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                        <div class="card-soft p-6 border-t-8 border-[#F9C74F] lg:col-span-2 flex flex-col justify-center">
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
                            <p class="text-center text-sm text-gray-500 mt-6"><i class="fas fa-lightbulb text-[#F9C74F] mr-2"></i><strong>Dato:</strong> El cero absoluto es 0 K = -273.15 °C = -459.67 °F.</p>
                        </div>
                        <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Para estandarizar mediciones, usamos escalas. <strong>Celsius y Kelvin</strong> comparten el mismo tamaño de grado, pero Kelvin arranca desde el cero absoluto (ausencia total de calor). <strong>Fahrenheit</strong> usa otro tamaño de grado y punto cero. La Ley Cero asegura que sin importar la escala, el estado térmico es el mismo.
                            </p>
                        </div>
                    </div>
                </div>
            `
                },
                {
                    sub: "Ejemplo Práctico",
                    title: "Punto Triple del Agua",
                    content: `
                <div class="slide-fade w-full max-w-6xl">
                    <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                        <div class="card-soft p-6 border-l-8 border-[#3FB8AF] flex flex-col justify-center">
                            <h3 class="text-2xl font-bold mb-4 text-azul">Referencia Universal</h3>
                            <p class="text-gray-600 mb-4 text-sm">El estado donde coexisten hielo, agua líquida y vapor en equilibrio.</p>
                            <div class="space-y-3">
                                <div class="flex items-center gap-3 bg-teal-50 p-3 rounded-lg border border-teal-100">
                                    <i class="fas fa-temperature-low text-[#3FB8AF] text-xl"></i>
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase">Temperatura</div>
                                        <div class="font-mono font-bold text-gray-800 text-sm">273.16 K exactos</div>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3 bg-blue-50 p-3 rounded-lg border border-blue-100">
                                    <i class="fas fa-tachometer-alt text-blue-500 text-xl"></i>
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase">Presión</div>
                                        <div class="font-mono font-bold text-gray-800 text-sm">611.657 Pa</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-col items-center justify-center gap-4 bg-white/50 rounded-xl p-4">
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
                            <div class="bg-white px-4 py-2 rounded-full shadow text-[10px] font-bold text-gray-500 uppercase">
                                <i class="fas fa-check-circle text-green-500 mr-1"></i> Base ITS-90
                            </div>
                        </div>
                        <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Por la Regla de las Fases de Gibbs, las tres fases de una sustancia pura (sólido, líquido, gas) solo pueden coexistir en equilibrio a una presión y temperatura exactas y únicas. <br><br>
                                Al ser inalterable en todo el universo, se utiliza como la calibración maestra de donde parten todos los termómetros del mundo gracias a la Ley Cero.
                            </p>
                        </div>
                    </div>
                </div>
            `
                },
                {
                    sub: "Aplicación Industrial 1",
                    title: "Calibración en Baño Térmico",
                    content: `
        <div class="slide-fade w-full max-w-6xl">
            <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                <div class="card-soft p-6 border-l-8 border-[#F9C74F] flex flex-col justify-center">
                    <h3 class="text-2xl font-bold mb-4 text-amarillo">Alineación de Termómetros</h3>
                    <p class="text-gray-600 mb-6 text-sm">Se sumerge un sensor (B) junto a un termómetro patrón de alta precisión (A) en un baño térmico (C).</p>
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
                        <label class="block text-[10px] font-bold text-gray-500 uppercase mb-2">Perilla de Calibración (B)</label>
                        <input type="range" id="sim1_slider" min="60" max="100" value="70" step="0.1" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#F9C74F]">
                    </div>
                </div>
                <div class="flex flex-col justify-center bg-white/50 rounded-xl p-4 items-center">
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
                <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Esta es la aplicación más pura de la Ley Cero. El termómetro A (calibrado) está en equilibrio con el baño C. El sensor industrial B se sumerge en C. 
                                <br><br>Cuando B alcanza el equilibrio con C, debería marcar la misma temperatura que A. Si no lo hace, manipulamos su circuito hasta igualarlo, sabiendo matemáticamente que ambos cuerpos están a la misma temperatura.
                            </p>
                        </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 2",
                    title: "Control de Hornos",
                    content: `
        <div class="slide-fade w-full max-w-6xl">
            <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                <div class="card-soft p-6 border-l-8 border-[#C84B31] flex flex-col justify-center">
                    <h3 class="text-2xl font-bold mb-4 text-bordo">Redundancia de Sensores</h3>
                    <p class="text-gray-600 mb-6 text-sm">Se usan dos termopares (A y B) en el mismo metal fundido (C) para evitar accidentes por sensores degradados.</p>
                    <div class="space-y-4 mb-6">
                        <label class="block text-[10px] font-bold text-gray-500 uppercase">Potencia del Horno</label>
                        <input type="range" id="sim2_slider" min="500" max="1500" value="500" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#C84B31]">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-gray-800 p-4 rounded-xl text-center shadow-inner border border-gray-700">
                            <div class="text-[10px] text-gray-400 font-bold uppercase mb-1">Termopar A</div>
                            <div id="sim2_valA" class="text-2xl font-mono font-black text-red-500">500°C</div>
                        </div>
                        <div class="bg-gray-800 p-4 rounded-xl text-center shadow-inner border border-gray-700 relative group">
                            <div class="text-[10px] text-gray-400 font-bold uppercase mb-1">Termopar B <button id="sim2_failBtn" class="text-[8px] bg-red-600 text-white px-2 py-0.5 rounded ml-1 hover:bg-red-500 transition-colors absolute top-2 right-2">ROMPER</button></div>
                            <div id="sim2_valB" class="text-2xl font-mono font-black text-red-500">500°C</div>
                        </div>
                    </div>
                    <div id="sim2_alert" class="mt-4 p-3 rounded-lg text-xs font-bold text-center bg-green-100 text-green-700 transition-colors">
                        <i class="fas fa-shield-check"></i> Sensores en Equilibrio Térmico
                    </div>
                </div>
                <div class="flex flex-col justify-center items-center bg-white/50 rounded-xl p-4 relative">
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
                <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                Por transitividad, si los termopares A y B están inmersos en el mismo horno C, ambos deben marcar siempre la misma temperatura (equilibrio térmico). <br><br>
                                Si la lectura de A difiere de B, el sistema de control (PLC) sabe inmediatamente que un sensor falló y detiene el quemador, previniendo sobrecalentamientos peligrosos.
                            </p>
                        </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 3",
                    title: "Intercambiadores de Calor",
                    content: `
        <div class="slide-fade w-full max-w-6xl">
            <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                <div class="card-soft p-6 border-l-8 border-[#3FB8AF] flex flex-col justify-center">
                    <h3 class="text-2xl font-bold mb-4 text-azul">Búsqueda del Equilibrio</h3>
                    <p class="text-gray-600 mb-6 text-sm">Fluidos fríos y calientes intercambian calor buscando la misma temperatura final.</p>
                    
                    <div class="space-y-6">
                        <div>
                            <label class="flex justify-between text-[10px] font-bold text-gray-500 uppercase mb-2">
                                <span>Caudal Agua Fría (20°C)</span>
                                <span id="sim3_flowC" class="text-blue-500">50%</span>
                            </label>
                            <input type="range" id="sim3_sliderC" min="10" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500">
                        </div>
                        <div>
                            <label class="flex justify-between text-[10px] font-bold text-gray-500 uppercase mb-2">
                                <span>Caudal Agua Caliente (90°C)</span>
                                <span id="sim3_flowH" class="text-red-500">50%</span>
                            </label>
                            <input type="range" id="sim3_sliderH" min="10" max="100" value="50" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-red-500">
                        </div>
                    </div>
                    
                    <div class="mt-8 bg-gray-50 p-4 rounded-xl border border-gray-200 text-center shadow-inner">
                        <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Temperatura a la Salida</div>
                        <div id="sim3_eq" class="text-4xl font-black font-mono text-purple-600 transition-all duration-300">55.0 °C</div>
                    </div>
                </div>
                <div class="flex flex-col items-center justify-center bg-white/50 rounded-xl p-4">
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
                    <div class="mt-4 text-[10px] font-bold text-gray-400 text-center uppercase tracking-wider">Intercambiador de Contraflujo</div>
                </div>
                <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                El fluido caliente cede calor a través de la pared de metal, que a su vez lo cede al fluido frío. La Ley Cero dicta que si permanecieran en contacto indefinidamente, ambos fluidos y el metal alcanzarían el equilibrio térmico total.<br><br>
                                Variando el caudal de los fluidos, los ingenieros controlan la temperatura final de la mezcla sin tener que mezclar físicamente los líquidos.
                            </p>
                        </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 4",
                    title: "Cámaras Frigoríficas",
                    content: `
        <div class="slide-fade w-full max-w-6xl">
            <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                <div class="card-soft p-6 border-l-8 border-[#9B5DE5] flex flex-col justify-center">
                    <h3 class="text-2xl font-bold mb-4 text-lavanda">Maduración Térmica</h3>
                    <p class="text-gray-600 mb-6 text-sm">Productos (A) entran a cámara fría (C) y transfieren su calor hasta el equilibrio térmico.</p>
                    
                    <div class="flex justify-center mb-6">
                        <button id="sim4_btn" class="bg-gradient-to-r from-purple-500 to-indigo-500 text-white font-bold py-3 px-6 rounded-xl shadow-lg hover:shadow-xl hover:scale-105 transition-all w-full flex items-center justify-center gap-2 text-sm">
                            <i class="fas fa-box"></i> Ingresar Productos (25°C)
                        </button>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-blue-50 p-4 rounded-xl border border-blue-100 text-center shadow-inner">
                            <i class="fas fa-snowflake text-blue-400 text-xl mb-2"></i>
                            <div class="text-[10px] font-bold text-gray-500 uppercase">Cámara (C)</div>
                            <div class="text-xl font-mono font-black text-blue-700">-18.0 °C</div>
                        </div>
                        <div class="bg-orange-50 p-4 rounded-xl border border-orange-100 text-center transition-colors duration-[3000ms] shadow-inner" id="sim4_prodBox">
                            <i class="fas fa-apple-alt text-orange-400 text-xl mb-2 transition-colors duration-[3000ms]" id="sim4_prodIcon"></i>
                            <div class="text-[10px] font-bold text-gray-500 uppercase">Producto (A)</div>
                            <div id="sim4_prodTemp" class="text-xl font-mono font-black text-orange-700 transition-colors duration-[3000ms]">--.- °C</div>
                        </div>
                    </div>
                </div>
                <div class="flex justify-center items-center bg-white/50 rounded-xl p-4">
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
                <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                El aire frío de la cámara (C) rodea las cajas de producto (A). Como el aire y el producto no están en equilibrio térmico, el calor fluye desde los productos calientes hacia el aire frío continuo. <br><br>
                                Al pasar el tiempo necesario, la Ley Cero determina que la temperatura final del producto en el centro será idéntica a la del aire configurado.
                            </p>
                        </div>
            </div>
        </div>
    `
                },
                {
                    sub: "Aplicación Industrial 5",
                    title: "Refrigeración de Moldes",
                    content: `
        <div class="slide-fade w-full max-w-6xl">
            <div class="grid lg:grid-cols-3 gap-8 items-stretch">
                <div class="card-soft p-6 border-l-8 border-[#F8961E] flex flex-col justify-center">
                    <h3 class="text-2xl font-bold mb-4 text-naranja">Moldeo por Inyección</h3>
                    <p class="text-gray-600 mb-4 text-sm">Plástico a 200°C entra al molde. Agua refrigerante enfría la matriz sólida logrando el equilibrio.</p>
                    
                    <div class="mb-6">
                        <label class="flex justify-between text-[10px] font-bold text-gray-500 uppercase mb-2">
                            <span>Temperatura del Agua</span>
                            <span id="sim5_water" class="text-blue-500">20°C</span>
                        </label>
                        <input type="range" id="sim5_slider" min="10" max="50" value="20" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500">
                    </div>
                    
                    <button id="sim5_injectBtn" class="bg-orange-500 text-white font-bold py-3 px-6 rounded-xl shadow-lg hover:bg-orange-600 transition-all w-full mb-4 text-sm">
                        <i class="fas fa-fill-drip"></i> Inyectar Plástico
                    </button>
                    
                    <div class="w-full bg-gray-200 rounded-full h-4 overflow-hidden relative border border-gray-300">
                        <div id="sim5_progress" class="bg-green-500 h-full w-0 transition-all duration-75"></div>
                    </div>
                    <div id="sim5_status" class="text-[10px] text-center font-bold text-gray-500 uppercase mt-2">Esperando Inyección...</div>
                </div>
                <div class="flex justify-center items-center bg-white/50 rounded-xl p-4">
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
                <div class="card-soft p-6 border-l-4 border-indigo-400 bg-indigo-50/50 flex flex-col justify-center">
                            <h4 class="text-sm font-black text-indigo-800 uppercase tracking-wider mb-3"><i class="fas fa-lightbulb text-yellow-500 mr-2 text-lg"></i> ¿Cómo Funciona?</h4>
                            <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                El plástico inyectado tiene mucha energía térmica. Para que mantenga la forma y se solidifique, debe ceder calor rápidamente a la matriz de acero. <br><br>
                                El agua absorbe el calor del acero y evita que toda la matriz alcance el equilibrio térmico con el plástico, creando un delta térmico constante y forzando la solidificación del producto.
                            </p>
                        </div>
            </div>
        </div>
    `
                },
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
];
            // mode is presentation only
            function renderSlide() {
                const container = document.getElementById('container');
                container.className = 'flex-grow flex items-center justify-center p-4 sm:p-6 md:p-8 w-full';
                const slide = slides[current];
                container.innerHTML = `
                <div class="w-full flex flex-col items-center">
                    <div class="mb-6 md:mb-10 text-center">
                        <p class="text-[10px] md:text-xs font-black text-blue-500 uppercase tracking-[0.3em] md:tracking-[0.4em] mb-2">${slide.sub}</p>
                        <h2 class="text-3xl md:text-4xl font-black text-gray-900 tracking-tight leading-tight">${slide.title}</h2>
                    </div>
                    <div class="w-full max-w-full overflow-x-hidden flex justify-center">
                        ${slide.content}
                    </div>
                </div>
            `;

                const counter = document.getElementById('counter');
                if (counter) counter.innerText = `${String(current + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
                const progressBar = document.getElementById('progress-bar');
                if (progressBar) progressBar.style.width = `${((current + 1) / slides.length) * 100}%`;
                
                attachInteractiveEvents();
            }

            function attachInteractiveEvents() {


                if (current === 1) {
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

                if (current === 2) {
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

                if (current === 4) {
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

        if (current === 6) {
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

        if (current === 7) {
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

        if (current === 8) {
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

        if (current === 9) {
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

        if (current === 10) {
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

            }


            function changeSlide(dir) {
                if (current + dir >= 0 && current + dir < slides.length) {
                    current += dir;
                    renderSlide();
                }
            }

            function goToSlide(index) {
                if (index >= 0 && index < slides.length) {
                    current = index;
                    renderSlide();
                }
            }

            // Lógica de Impresión Masiva (PDF)
            window.onbeforeprint = () => {
                const buffer = document.getElementById('print-buffer');
                buffer.innerHTML = slides.map((s, i) => `
            <div class="print-page">
                <div style="text-align: center; margin-bottom: 40px;">
                    <p style="color: #4682B4; font-weight: 900; font-size: 10px; text-transform: uppercase; letter-spacing: 2px;">${s.sub}</p>
                    <h2 style="font-size: 32px; font-weight: 900; color: #111; margin-top: 5px;">${s.title}</h2>
                </div>
                <div style="width: 100%; display: flex; justify-content: center; transform: scale(0.95);">
                    ${s.content}
                </div>
                <div style="position: absolute; bottom: 30px; width: 100%; text-align: center; border-top: 1px solid #eee; padding-top: 20px; font-size: 10px; color: #aaa;">
                    E.E.S.T. "Ing. Álvarez Condarco" | 5º4 Electromecánica | Diapositiva ${i + 1}
                </div>
            </div>
        `).join('');
                buffer.classList.remove('hidden');
            };

            window.onafterprint = () => {
                document.getElementById('print-buffer').classList.add('hidden');
            };

            // Teclado
            document.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight') changeSlide(1);
                if (e.key === 'ArrowLeft') changeSlide(-1);
            });

            // Inicio
            window.onload = renderSlide;
        