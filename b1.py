p = []
p.append("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Toy's Wardrobe & Glam Closet</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
  <style>
    body { background: radial-gradient(circle at top, #1e0538 0%, #060b17 55%, #001f1a 100%); color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; min-height: 100vh; }
    .glass { background: rgba(255, 255, 255, 0.06); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.12); }
    .neon-cyan { border: 1px solid #00F0FF; box-shadow: 0 0 16px rgba(0, 240, 255, 0.25); }
    .hide-scrollbar::-webkit-scrollbar { display: none; }
    .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    .carousel-container { display: flex; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory; padding: 12px 4px; }
    .carousel-item { flex: 0 0 84%; scroll-snap-align: center; }
    .pie-wedge { position: absolute; width: 100%; height: 100%; border-radius: 50%; clip-path: polygon(50% 50%, 50% 0%, 85.35% 14.64%); transform-origin: 50% 50%; cursor: pointer; }
  </style>
</head>
<body class="pb-24 selection:bg-cyan-400 selection:text-black">
""")
with open("p1.txt", "w") as f: f.write("".join(p))
