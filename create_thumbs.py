from PIL import Image
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(ROOT, 'logo.png')
out_dir = os.path.join(ROOT, 'assets', 'school')
os.makedirs(out_dir, exist_ok=True)

if not os.path.exists(logo_path):
    print('logo.png not found in repo root')
    raise SystemExit(1)

img = Image.open(logo_path).convert('RGBA')

def save_thumb(img, size, name, quality=85):
    thumb = img.copy()
    thumb.thumbnail(size, Image.LANCZOS)
    out_path = os.path.join(out_dir, name)
    # save as PNG to preserve transparency when present
    thumb.save(out_path)
    print('saved', out_path)

save_thumb(img, (900, 600), 'logo_large.png')
save_thumb(img, (600, 400), 'logo_thumb.png')
save_thumb(img, (240, 160), 'logo_small.png')

print('thumbnails created')
