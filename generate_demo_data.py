import os
from PIL import Image, ImageDraw, ImageFont

def create_sample_images():
    img_dir = os.path.join(os.path.dirname(__file__), "demo_images")
    os.makedirs(img_dir, exist_ok=True)

    items = [
        {
            "filename": "dell_laptop_lost.png",
            "bg": (20, 24, 35),
            "accent": (56, 189, 248),
            "title": "DELL LAPTOP (LOST)",
            "detail": "Navy Blue Sleeve + React Sticker",
            "shape": "laptop",
            "sticker": True
        },
        {
            "filename": "dell_laptop_found.png",
            "bg": (22, 27, 40),
            "accent": (56, 189, 248),
            "title": "NAVY LAPTOP (FOUND)",
            "detail": "Found at Library 2nd Floor",
            "shape": "laptop",
            "sticker": True
        },
        {
            "filename": "airpods_case_lost.png",
            "bg": (240, 243, 246),
            "accent": (150, 160, 175),
            "title": "AIRPODS PRO (LOST)",
            "detail": "White Case with Spigen Carabiner",
            "shape": "earbuds",
            "sticker": False
        },
        {
            "filename": "airpods_case_found.png",
            "bg": (245, 247, 250),
            "accent": (140, 150, 165),
            "title": "WHITE PODS (FOUND)",
            "detail": "Turned in at Cafeteria Counter",
            "shape": "earbuds",
            "sticker": False
        },
        {
            "filename": "leather_wallet.png",
            "bg": (92, 51, 23),
            "accent": (180, 120, 70),
            "title": "BROWN WALLET",
            "detail": "Woodland Leather Bi-fold",
            "shape": "wallet",
            "sticker": False
        },
        {
            "filename": "metal_bottle.png",
            "bg": (40, 70, 90),
            "accent": (0, 229, 255),
            "title": "STEEL BOTTLE",
            "detail": "Milton 750ml Aqua Blue",
            "shape": "bottle",
            "sticker": False
        }
    ]

    for item in items:
        img_path = os.path.join(img_dir, item["filename"])
        img = Image.new("RGB", (400, 300), color=item["bg"])
        draw = ImageDraw.Draw(img)

        draw.rectangle([5, 5, 395, 295], outline=item["accent"], width=3)

        if item["shape"] == "laptop":
            draw.rectangle([80, 70, 320, 200], fill=(45, 55, 72), outline=(100, 116, 139), width=3)
            draw.rectangle([95, 80, 305, 185], fill=(15, 23, 42), outline=(56, 189, 248), width=2)
            draw.polygon([(60, 200), (340, 200), (360, 225), (40, 225)], fill=(30, 41, 59), outline=(100, 116, 139))
            if item["sticker"]:
                draw.ellipse([180, 115, 220, 155], fill=(14, 165, 233), outline=(255, 255, 255), width=2)
                draw.text((188, 128), "AI", fill=(255, 255, 255))
        elif item["shape"] == "earbuds":
            draw.rounded_rectangle([130, 80, 270, 210], radius=35, fill=(255, 255, 255), outline=(203, 213, 225), width=4)
            draw.line([(130, 130), (270, 130)], fill=(203, 213, 225), width=2)
            draw.ellipse([196, 155, 204, 163], fill=(34, 197, 94))
        elif item["shape"] == "wallet":
            draw.rounded_rectangle([90, 85, 310, 215], radius=15, fill=(120, 66, 32), outline=(180, 110, 60), width=4)
            draw.line([(90, 150), (310, 150)], fill=(70, 35, 15), width=3)
            draw.rectangle([240, 130, 290, 170], fill=(90, 45, 20), outline=(217, 119, 6), width=2)
        elif item["shape"] == "bottle":
            draw.rounded_rectangle([150, 90, 250, 235], radius=20, fill=(14, 116, 144), outline=(6, 182, 212), width=3)
            draw.rectangle([175, 60, 225, 90], fill=(203, 213, 225), outline=(100, 116, 139), width=2)

        draw.rectangle([10, 240, 390, 290], fill=(15, 23, 42))
        draw.text((20, 248), item["title"], fill=(248, 250, 252))
        draw.text((20, 268), item["detail"], fill=(148, 163, 184))

        img.save(img_path)
    print(f"Generated {len(items)} sample demo images in {img_dir}")

if __name__ == "__main__":
    create_sample_images()
