import os
from PIL import Image, ImageDraw, ImageFont

def generate_id_samples():
    img_dir = os.path.join(os.path.dirname(__file__), "demo_images")
    os.makedirs(img_dir, exist_ok=True)

    # 1. Rohan Sharma ID Card
    id1 = Image.new("RGB", (600, 380), color=(255, 255, 255))
    draw1 = ImageDraw.Draw(id1)
    # Header banner
    draw1.rectangle([0, 0, 600, 85], fill=(15, 23, 42))
    draw1.rectangle([0, 85, 600, 90], fill=(245, 158, 11))
    draw1.text((30, 18), "TKR COLLEGE OF ENGG & TECHNOLOGY", fill=(245, 158, 11))
    draw1.text((30, 42), "AUTONOMOUS | MEDBOWLI, MEERPET, HYDERABAD", fill=(203, 213, 225))
    draw1.text((30, 62), "STUDENT IDENTITY CARD", fill=(56, 189, 248))

    # Photo placeholder
    draw1.rectangle([35, 115, 175, 275], fill=(226, 232, 240), outline=(100, 116, 139), width=2)
    draw1.ellipse([75, 140, 135, 200], fill=(148, 163, 184))
    draw1.rectangle([55, 215, 155, 273], fill=(148, 163, 184))

    # Details
    draw1.text((200, 115), "STUDENT NAME:", fill=(100, 116, 139))
    draw1.text((200, 135), "ROHAN SHARMA", fill=(15, 23, 42))

    draw1.text((200, 165), "ROLL NO (HT NO):", fill=(100, 116, 139))
    draw1.rectangle([195, 185, 410, 225], fill=(238, 242, 255), outline=(99, 102, 241), width=2)
    draw1.text((210, 192), "24K91A0501", fill=(30, 27, 75))

    draw1.text((200, 235), "DEPARTMENT:", fill=(100, 116, 139))
    draw1.text((200, 255), "COMPUTER SCIENCE & ENGG (CSE)", fill=(15, 23, 42))

    draw1.text((200, 285), "VALID TILL: 2028 | BLOOD GROUP: O+ve", fill=(100, 116, 139))

    # Barcode simulation at bottom
    draw1.rectangle([0, 320, 600, 380], fill=(241, 245, 249))
    for x in range(40, 560, 8):
        if x % 16 != 0:
            draw1.rectangle([x, 330, x + 4, 370], fill=(15, 23, 42))

    id1_path = os.path.join(img_dir, "tkrcet_id_rohan.png")
    id1.save(id1_path)

    # 2. Priya Patel ID Card
    id2 = Image.new("RGB", (600, 380), color=(255, 255, 255))
    draw2 = ImageDraw.Draw(id2)
    draw2.rectangle([0, 0, 600, 85], fill=(15, 23, 42))
    draw2.rectangle([0, 85, 600, 90], fill=(245, 158, 11))
    draw2.text((30, 18), "TKR COLLEGE OF ENGG & TECHNOLOGY", fill=(245, 158, 11))
    draw2.text((30, 42), "AUTONOMOUS | MEDBOWLI, MEERPET, HYDERABAD", fill=(203, 213, 225))
    draw2.text((30, 62), "STUDENT IDENTITY CARD", fill=(56, 189, 248))

    draw2.rectangle([35, 115, 175, 275], fill=(226, 232, 240), outline=(100, 116, 139), width=2)
    draw2.ellipse([75, 140, 135, 200], fill=(148, 163, 184))
    draw2.rectangle([55, 215, 155, 273], fill=(148, 163, 184))

    draw2.text((200, 115), "STUDENT NAME:", fill=(100, 116, 139))
    draw2.text((200, 135), "PRIYA PATEL", fill=(15, 23, 42))

    draw2.text((200, 165), "ROLL NO (HT NO):", fill=(100, 116, 139))
    draw2.rectangle([195, 185, 410, 225], fill=(238, 242, 255), outline=(99, 102, 241), width=2)
    draw2.text((210, 192), "24K91A0412", fill=(30, 27, 75))

    draw2.text((200, 235), "DEPARTMENT:", fill=(100, 116, 139))
    draw2.text((200, 255), "ELECTRONICS & COMMUNICATION (ECE)", fill=(15, 23, 42))

    draw2.text((200, 285), "VALID TILL: 2028 | BLOOD GROUP: B+ve", fill=(100, 116, 139))

    draw2.rectangle([0, 320, 600, 380], fill=(241, 245, 249))
    for x in range(40, 560, 8):
        if x % 14 != 0:
            draw2.rectangle([x, 330, x + 4, 370], fill=(15, 23, 42))

    id2_path = os.path.join(img_dir, "tkrcet_id_priya.png")
    id2.save(id2_path)

    # 3. Hall Ticket Sample
    ht = Image.new("RGB", (600, 420), color=(250, 250, 250))
    draw_ht = ImageDraw.Draw(ht)
    draw_ht.rectangle([5, 5, 595, 415], outline=(15, 23, 42), width=3)
    draw_ht.rectangle([0, 0, 600, 75], fill=(30, 41, 59))
    draw_ht.text((50, 15), "JAWAHARLAL NEHRU TECHNOLOGICAL UNIVERSITY HYDERABAD", fill=(248, 250, 252))
    draw_ht.text((120, 38), "TKR COLLEGE OF ENGINEERING & TECHNOLOGY (K9)", fill=(245, 158, 11))
    draw_ht.text((150, 55), "SEMESTER END EXAMINATIONS HALL TICKET", fill=(203, 213, 225))

    draw_ht.text((40, 100), "HALL TICKET NUMBER:", fill=(100, 116, 139))
    draw_ht.rectangle([35, 120, 280, 160], fill=(254, 243, 199), outline=(217, 119, 6), width=2)
    draw_ht.text((50, 128), "23K91A0108", fill=(120, 53, 15))

    draw_ht.text((320, 100), "CANDIDATE NAME:", fill=(100, 116, 139))
    draw_ht.text((320, 128), "NARESH KUMAR", fill=(15, 23, 42))

    draw_ht.text((40, 180), "COURSE: B.TECH | BRANCH: CIVIL ENGINEERING", fill=(15, 23, 42))
    draw_ht.text((40, 210), "EXAMINATION CENTER: TKR CAMPUS CENTER #01", fill=(100, 116, 139))

    # Exam table simulation
    draw_ht.rectangle([35, 245, 565, 380], outline=(100, 116, 139), width=1)
    draw_ht.line([(35, 280), (565, 280)], fill=(100, 116, 139), width=1)
    draw_ht.text((50, 255), "SUBJECT CODE & NAME", fill=(15, 23, 42))
    draw_ht.text((420, 255), "DATE & TIME", fill=(15, 23, 42))
    draw_ht.text((50, 290), "CE301PC: Strength of Materials", fill=(71, 85, 105))
    draw_ht.text((420, 290), "24-OCT-2026 FN", fill=(71, 85, 105))
    draw_ht.text((50, 320), "CE302PC: Fluid Mechanics", fill=(71, 85, 105))
    draw_ht.text((420, 320), "26-OCT-2026 FN", fill=(71, 85, 105))
    draw_ht.text((50, 350), "CE303PC: Surveying & Geomatics", fill=(71, 85, 105))
    draw_ht.text((420, 350), "28-OCT-2026 FN", fill=(71, 85, 105))

    ht_path = os.path.join(img_dir, "tkrcet_hallticket.png")
    ht.save(ht_path)
    print("Generated realistic ID and Hall ticket samples.")

if __name__ == "__main__":
    generate_id_samples()
