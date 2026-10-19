p = []
p.append("""  <div id="cam-modal" class="fixed inset-0 bg-black/85 z-50 flex items-end sm:items-center justify-center p-4 hidden">
    <div class="glass w-full max-w-sm rounded-3xl p-5 border border-cyan-400/50 space-y-4">
      <div class="flex justify-between items-center">
        <div><h3 class="font-bold text-white text-sm">Upload to Vault</h3><p class="text-[10px] text-cyan-400 font-bold">Manual Drawer Select &amp; Background Removal</p></div>
        <button onclick="closeModal()" class="text-slate-400 text-lg"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div>
        <label class="text-[11px] text-slate-300 block mb-1 font-bold">Select Target Closet Drawer:</label>
        <select id="modal-drawer-choice" class="w-full bg-slate-900 border border-cyan-400/60 rounded-xl p-2.5 text-xs text-white font-bold focus:outline-none">
          <option value="Skirts" selected>Skirts</option>
          <option value="Shirts">Shirts &amp; Blouses</option>
          <option value="Pants">Pants &amp; Jeans</option>
          <option value="Shorts">Shorts</option>
          <option value="Jackets">Jackets &amp; Coats</option>
          <option value="Sweaters">Sweaters</option>
          <option value="Shoes">Shoes &amp; Heels</option>
          <option value="Purses">Purses</option>
          <option value="Jewelry">Jewelry</option>
          <option value="Hats">Hats</option>
          <option value="Glasses">Glasses</option>
          <option value="Perfume">Perfumes</option>
        </select>
      </div>
      <input type="file" id="cam-snap" accept="image/*" capture="environment" class="hidden" onchange="processPrecisionUpload(this)">
      <input type="file" id="gal-pick" accept="image/*" multiple class="hidden" onchange="processPrecisionUpload(this)">
      <div class="space-y-2 pt-1">
        <button onclick="document.getElementById('cam-snap').click()" class="w-full py-3 bg-gradient-to-r from-teal-700 to-cyan-400 text-slate-950 font-bold rounded-xl text-xs flex items-center justify-center gap-2 active:scale-95"><i class="fa-solid fa-camera"></i> Take a Pic Now</button>
        <button onclick="document.getElementById('gal-pick').click()" class="w-full py-3 bg-slate-900 border border-slate-700 text-white font-bold rounded-xl text-xs flex items-center justify-center gap-2 active:scale-95"><i class="fa-solid fa-images text-purple-400"></i> Gallery / Multi-Photo Select</button>
      </div>
    </div>
  </div>
""")
with open("p7.txt", "w") as f: f.write("".join(p))
