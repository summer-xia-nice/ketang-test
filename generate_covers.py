from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, 'assets', 'covers')
os.makedirs(OUT_DIR, exist_ok=True)

images = [
    {'name': 'cover1.png', 'title': 'School Case Study', 'subtitle': '宝山二中心小学品牌页', 'accent': (37, 160, 249)},
    {'name': 'cover2.png', 'title': 'Video Portfolio', 'subtitle': '视频封面展示', 'accent': (122, 90, 255)},
    {'name': 'cover3.png', 'title': 'Project Reel', 'subtitle': '作品集视觉模板', 'accent': (0, 209, 164)},
]

for item in images:
    width, height = 1280, 720
    img = Image.new('RGB', (width, height), '#0b1320')
    draw = ImageDraw.Draw(img)

    # gradient background
    for i in range(height):
        ratio = i / height
        r = int(7 + ratio * 38)
        g = int(17 + ratio * 45)
        b = int(31 + ratio * 70)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    overlay = Image.new('RGBA', img.size, (0, 0, 0, 60))
    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    draw = ImageDraw.Draw(img)

    # accent bars
    for i in range(3):
        x0 = 120 + i * 260
        draw.rectangle([x0, 120, x0 + 220, 170], fill=item['accent'] + (180,))

    # text
    try:
        font_large = ImageFont.truetype('arial.ttf', 72)
        font_small = ImageFont.truetype('arial.ttf', 32)
    except Exception:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    title = item['title']
    subtitle = item['subtitle']
    draw.text((110, 280), title, font=font_large, fill=(255, 255, 255, 255))
    draw.text((110, 380), subtitle, font=font_small, fill=(205, 225, 245, 255))

    badge_text = '2026 Creative Demo'
    if hasattr(draw, 'textbbox'):
        bbox = draw.textbbox((0, 0), badge_text, font=font_small)
        badge_w = bbox[2] - bbox[0]
        badge_h = bbox[3] - bbox[1]
    else:
        badge_w, badge_h = font_small.getsize(badge_text)
    badge_x = width - badge_w - 140
    badge_y = height - badge_h - 120
    draw.rectangle([badge_x - 18, badge_y - 12, badge_x + badge_w + 18, badge_y + badge_h + 12], fill=(255, 255, 255, 24))
    draw.text((badge_x, badge_y), badge_text, font=font_small, fill=(234, 251, 255, 255))

    out_path = os.path.join(OUT_DIR, item['name'])
    img.convert('RGB').save(out_path)
    print('Saved', out_path)
