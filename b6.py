p = []
p.append("""    <section id="view-sales" class="hidden space-y-4">
      <div class="glass p-3.5 rounded-2xl border border-slate-800 flex justify-between items-center">
        <div><h2 class="text-sm font-extrabold uppercase text-cyan-400">Live Brand Sales &amp; Drops</h2><p class="text-[10px] text-slate-400">Tap heart to add to Wants. Tap card to view store.</p></div>
        <button onclick="switchTab('wants')" class="px-3 py-1.5 rounded-xl bg-purple-900 border border-purple-400 text-purple-200 text-xs font-bold">Wants (<span id="wants-badge">0</span>)</button>
      </div>
      <div id="sales-feed-container" class="space-y-4"></div>
    </section>
    <section id="view-wants" class="hidden space-y-4">
      <div class="glass p-4 rounded-3xl border border-purple-400/40 space-y-1">
        <h2 class="text-sm font-black text-purple-300 uppercase tracking-wider"><i class="fa-solid fa-heart text-purple-400 mr-1.5"></i> My Saved Wants</h2>
        <p class="text-xs text-slate-300">Items favorited from your sales feed live here.</p>
      </div>
      <div id="wants-container" class="grid grid-cols-2 gap-3"></div>
    </section>
    <section id="view-outfits" class="hidden space-y-4">
      <div class="glass p-4 rounded-3xl border border-cyan-400/40 space-y-2">
        <div class="flex justify-between items-center"><span class="text-[10px] font-mono text-cyan-400 font-bold bg-cyan-950 px-2 py-0.5 rounded">SUNDAY SYNC ACTIVE</span><span class="text-xs text-slate-300 font-bold">Fall/Winter • 62°F Forecast</span></div>
        <h2 class="text-sm font-black text-white uppercase">Your 7-Day Stylist Schedule</h2>
        <p class="text-xs text-slate-300">Auto-assembled from your closet vault. Tap to inspect; double-tap to wear in 360° room.</p>
      </div>
      <div id="weekly-outfits-list" class="space-y-3"></div>
    </section>
    <section id="view-pinterest" class="hidden space-y-4">
      <h2 class="text-sm font-extrabold uppercase text-cyan-400">Pinterest Inspiration Vault</h2>
      <div class="glass p-4 rounded-2xl border border-slate-800 space-y-2">
        <span class="text-xs font-bold text-cyan-400 uppercase">Board 1: Fall/Winter Tailored Layers</span>
        <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-bold"><div class="p-3 bg-black/60 rounded-xl border border-slate-800">Velvet Trench</div><div class="p-3 bg-black/60 rounded-xl border border-slate-800">Cashmere Knit</div><div class="p-3 bg-black/60 rounded-xl border border-slate-800">Tailored Leather</div></div>
      </div>
    </section>
  </main>
""")
with open("p6.txt", "w") as f: f.write("".join(p))
