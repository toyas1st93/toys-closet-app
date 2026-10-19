p = []
p.append("""    <div id="corner-mini-mannequin" ondragover="allowDrop(event)" ondrop="handleMiniDrop(event)" onclick="onMiniModelClick()" class="fixed bottom-4 right-4 z-40 w-20 h-28 rounded-2xl bg-gradient-to-b from-[#22073d] via-[#09111e] to-black border-2 border-cyan-400 shadow-2xl flex flex-col items-center justify-between p-1.5 cursor-pointer active:scale-95 group">
      <div class="text-[8px] font-mono text-cyan-400 font-bold bg-black/80 px-1.5 py-0.5 rounded">3D FIT</div>
      <div class="w-full flex-1 flex flex-col justify-center items-center gap-1 py-1">
        <div id="mini-slot-top" class="w-8 h-6 rounded border border-dashed border-cyan-400/60 overflow-hidden bg-black/40 flex items-center justify-center"><i class="fa-solid fa-shirt text-[9px] text-slate-500"></i></div>
        <div id="mini-slot-bottom" class="w-8 h-7 rounded border border-dashed border-purple-400/60 overflow-hidden bg-black/40 flex items-center justify-center"><i class="fa-solid fa-person-dress text-[9px] text-slate-500"></i></div>
        <div id="mini-slot-shoes" class="w-8 h-5 rounded border border-dashed border-pink-400/60 overflow-hidden bg-black/40 flex items-center justify-center"><i class="fa-solid fa-shoe-prints text-[8px] text-slate-500"></i></div>
      </div>
    </div>
    <div id="dressing-room-modal" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-md hidden flex flex-col justify-between p-4">
      <div class="flex justify-between items-center pb-2 border-b border-slate-800">
        <div>
          <h2 class="text-sm font-black text-cyan-400 uppercase tracking-wider"><i class="fa-solid fa-arrows-spin mr-1"></i> 360° Dressing Room</h2>
          <span id="likeness-badge" class="text-[10px] text-purple-300 font-mono">Toya • Cocoa Radiance &amp; Waist Knotless Braids</span>
        </div>
        <div class="flex items-center gap-2">
          <select onchange="returnToDrawer(this.value)" class="bg-slate-900 border border-cyan-400 text-cyan-400 rounded-xl px-2.5 py-1 text-xs font-bold focus:outline-none">
            <option value="" disabled selected>Go to Drawer...</option>
            <option value="Skirts">Skirts</option>
            <option value="Shirts">Shirts</option>
            <option value="Pants">Pants</option>
            <option value="Jackets">Jackets</option>
            <option value="Shoes">Shoes</option>
            <option value="Purses">Purses</option>
            <option value="Jewelry">Jewelry</option>
          </select>
          <button onclick="closeDressingRoom()" class="w-8 h-8 rounded-full glass text-white"><i class="fa-solid fa-xmark"></i></button>
        </div>
      </div>
      <div class="flex-1 flex flex-col items-center justify-center relative py-2">
        <div id="mannequin-3d-stage" class="relative w-56 h-96 rounded-3xl bg-gradient-to-b from-[#2a0845] via-[#09111e] to-black border-2 border-cyan-400 p-3 shadow-2xl flex flex-col items-center justify-between transition-transform duration-75">
          <div class="w-full flex justify-between items-center text-[10px] font-mono text-cyan-400"><span>360° VIEW</span><span id="rotation-angle-label">0°</span></div>
          <div class="w-full flex-1 flex flex-col justify-between py-2 space-y-2">
            <div id="stage-slot-top" class="h-28 rounded-2xl border-2 border-dashed border-cyan-400/60 overflow-hidden bg-black/40 flex items-center justify-center relative"><span class="text-xs text-slate-500"><i class="fa-solid fa-shirt mr-1"></i> Empty Top</span></div>
            <div id="stage-slot-bottom" class="h-28 rounded-2xl border-2 border-dashed border-purple-400/60 overflow-hidden bg-black/40 flex items-center justify-center relative"><span class="text-xs text-slate-500"><i class="fa-solid fa-person-dress mr-1"></i> Empty Bottom</span></div>
            <div id="stage-slot-shoes" class="h-16 rounded-2xl border-2 border-dashed border-pink-400/60 overflow-hidden bg-black/40 flex items-center justify-center relative"><span class="text-xs text-slate-500"><i class="fa-solid fa-shoe-prints mr-1"></i> Empty Shoes</span></div>
          </div>
          <button onclick="resetDressedFit()" class="text-[10px] text-slate-400 underline hover:text-white">Clear Fit</button>
        </div>
      </div>
      <div class="space-y-2 pb-2">
        <div class="flex justify-between items-center text-xs px-2"><span class="text-slate-300 font-bold">Spin 360° Silhouette:</span><button onclick="toggleAutoSpin()" id="auto-spin-btn" class="px-3 py-1 bg-cyan-400 text-slate-950 rounded-xl font-bold text-[11px]">Auto Spin: OFF</button></div>
        <input type="range" id="rotation-slider" min="0" max="360" value="0" oninput="rotateModel(this.value)" class="w-full accent-cyan-400 cursor-pointer">
      </div>
    </div>
""")
with open("p5.txt", "w") as f: f.write("".join(p))
