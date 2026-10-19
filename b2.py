p = []
p.append("""  <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800 px-4 py-3">
    <div class="flex justify-between items-center mb-2">
      <div onclick="switchTab('home')" class="cursor-pointer">
        <h1 class="text-xl font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-white to-purple-400">TOY'S CLOSET</h1>
        <p class="text-[10px] text-cyan-400 font-bold tracking-widest uppercase">The Private Glamour Vault</p>
      </div>
      <button onclick="openModal()" class="px-4 py-2 rounded-full bg-cyan-400 text-slate-950 font-extrabold text-xs flex items-center gap-2 shadow-lg active:scale-95">
        <i class="fa-solid fa-camera"></i> <span>+ Upload</span>
      </button>
    </div>
    <nav class="flex gap-2 overflow-x-auto hide-scrollbar pt-1 text-xs whitespace-nowrap">
      <button onclick="switchTab('home')" id="tb-home" class="px-3.5 py-1.5 rounded-xl font-bold bg-cyan-400 text-slate-950">Vault Hub</button>
      <button onclick="openDrawerModal()" id="tb-closet" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">Closet Drawers</button>
      <button onclick="openDressingRoom()" id="tb-dressing" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">360° Dressing Room</button>
      <button onclick="switchTab('outfits')" id="tb-outfits" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">Weekly Fits</button>
      <button onclick="switchTab('sales')" id="tb-sales" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">Sales Feed</button>
      <button onclick="switchTab('wants')" id="tb-wants" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">My Wants (<span id="wants-count">0</span>)</button>
      <button onclick="switchTab('pinterest')" id="tb-pinterest" class="px-3.5 py-1.5 rounded-xl font-semibold glass text-slate-300">Mood Boards</button>
    </nav>
  </header>
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-md hidden flex flex-col justify-between p-4" onclick="closeLightbox()">
    <div class="flex justify-between items-center py-2">
      <span id="lightbox-title" class="text-sm font-bold text-cyan-400"></span>
      <button class="w-10 h-10 rounded-full glass text-white text-lg"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="flex-1 flex items-center justify-center p-2">
      <img id="lightbox-img" class="max-h-[75vh] max-w-full rounded-2xl object-contain drop-shadow-[0_20px_35px_rgba(0,240,255,0.25)]">
    </div>
    <p class="text-center text-xs text-slate-400 pb-4">Tap anywhere to close</p>
  </div>
""")
with open("p2.txt", "w") as f: f.write("".join(p))
