p = []
p.append("""  <main class="p-4 space-y-4">
    <section id="view-home" class="space-y-4 text-center">
      <p class="text-[11px] text-cyan-400 font-bold uppercase tracking-wider">Tap a Wedge to Unlock Drawer • Tap Center to Upload</p>
      <div class="relative w-80 h-80 mx-auto rounded-full bg-slate-950 border-4 border-cyan-400 shadow-[0_0_35px_rgba(0,240,255,0.35)] flex items-center justify-center overflow-hidden">
        <div onclick="enterDrawer('Skirts')" class="pie-wedge bg-gradient-to-br from-cyan-600/60 to-purple-800/80 border border-white/20" style="transform: rotate(0deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Skirts</span></div>
        <div onclick="enterDrawer('Shirts')" class="pie-wedge bg-gradient-to-br from-purple-800/80 to-pink-600/60 border border-white/20" style="transform: rotate(45deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Shirts</span></div>
        <div onclick="enterDrawer('Pants')" class="pie-wedge bg-gradient-to-br from-pink-600/60 to-cyan-600/60 border border-white/20" style="transform: rotate(90deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Pants</span></div>
        <div onclick="enterDrawer('Shorts')" class="pie-wedge bg-gradient-to-br from-cyan-700/60 to-teal-600/60 border border-white/20" style="transform: rotate(135deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Shorts</span></div>
        <div onclick="enterDrawer('Jackets')" class="pie-wedge bg-gradient-to-br from-teal-600/60 to-purple-900/80 border border-white/20" style="transform: rotate(180deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Jackets</span></div>
        <div onclick="enterDrawer('Shoes')" class="pie-wedge bg-gradient-to-br from-purple-900/80 to-indigo-700/60 border border-white/20" style="transform: rotate(225deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Shoes</span></div>
        <div onclick="enterDrawer('Purses')" class="pie-wedge bg-gradient-to-br from-indigo-700/60 to-pink-700/60 border border-white/20" style="transform: rotate(270deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Purses</span></div>
        <div onclick="enterDrawer('Jewelry')" class="pie-wedge bg-gradient-to-br from-pink-700/60 to-cyan-600/60 border border-white/20" style="transform: rotate(315deg);"><span class="absolute top-5 left-1/2 -translate-x-1/2 text-[10px] font-black text-white drop-shadow">Jewelry</span></div>
        <button onclick="openModal()" class="relative z-10 w-28 h-28 rounded-full bg-gradient-to-tr from-[#1b0736] via-[#050b14] to-[#00221c] border-4 border-cyan-400 shadow-[0_0_25px_rgba(0,240,255,0.7)] flex flex-col items-center justify-center p-2 group active:scale-95">
          <i class="fa-solid fa-cloud-arrow-up text-2xl text-cyan-400"></i>
          <span class="text-xs font-black text-white uppercase mt-0.5">+ UPLOAD</span>
          <span class="text-[8px] text-purple-300 font-mono">DRAWER PICK</span>
        </button>
      </div>
      <div class="pt-2">
        <span id="total-vault-pieces" class="text-xs font-mono font-bold text-cyan-400 bg-cyan-950/80 px-4 py-1.5 rounded-full border border-cyan-400/30">0 Pieces Stored</span>
      </div>
    </section>
""")
with open("p3.txt", "w") as f: f.write("".join(p))
