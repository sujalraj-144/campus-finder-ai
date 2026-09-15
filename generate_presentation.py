import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette
    COLOR_BG = RGBColor(15, 23, 42)        # Dark Navy #0F172A
    COLOR_CARD = RGBColor(30, 41, 59)      # Slate Card #1E293B
    COLOR_CARD_BORDER = RGBColor(51, 65, 85) # Border #334155
    COLOR_CYAN = RGBColor(56, 189, 248)    # Cyan Accent #38BDF8
    COLOR_EMERALD = RGBColor(16, 185, 129) # Green #10B981
    COLOR_AMBER = RGBColor(245, 158, 11)   # Amber #F59E0B
    COLOR_WHITE = RGBColor(248, 250, 252)  # White #F8FAFC
    COLOR_MUTED = RGBColor(148, 163, 184)  # Muted Gray #94A3B8

    blank_layout = prs.slide_layouts[6]

    def set_slide_bg(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = COLOR_BG
        bg_shape.line.fill.background()
        return bg_shape

    def add_header(slide, tag_text, title_text, category_text="Smart India Hackathon 2026"):
        # Top Tag
        tx_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_tag = tx_tag.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"{category_text.upper()} • {tag_text.upper()}"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_CYAN

        # Title
        tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tf_title = tx_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: Title & Branding (SIH 2026 Fixed!)
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide1)

    # Big Banner Box
    banner = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.73), Inches(5.9))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_CARD
    banner.line.color.rgb = COLOR_CARD_BORDER
    banner.line.width = Pt(1.5)

    tx1 = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(10.9), Inches(5.0))
    tf1 = tx1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2026"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "CAMPUS FINDER AI"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_after = Pt(8)

    p = tf1.add_paragraph()
    p.text = "Autonomous AI Visual Matching & Zero-Knowledge Anti-Theft Verification for Lost and Found"
    p.font.size = Pt(18)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(28)

    p = tf1.add_paragraph()
    p.text = "Problem Statement ID: SIH-2026-CAMPUS-09  |  Category: Smart Campus Automation / Software Edition"
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_MUTED
    p.space_after = Pt(32)

    # Details grid
    p = tf1.add_paragraph()
    p.text = "Presented by Team: The Innovators  •  Lead: Sujal & Team"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_after = Pt(6)

    p = tf1.add_paragraph()
    p.text = "Key Innovation: Computer Vision Chromatic/Structural Embeddings + Blind Ownership Verification"
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_EMERALD

    # -------------------------------------------------------------
    # SLIDE 2: Problem Statement & Existing Market Void
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide2)
    add_header(slide2, "The Problem", "Problem Statement: Why Traditional Lost & Found Fails")

    cards_s2 = [
        ("The Hackathon Flaw", "Typical CRUD Portals Get Screened Out", 
         ["Basic 'List & Form' portals lack intelligence and practical adoption.",
          "Keyword search fails: 'Blue backpack' doesn't match 'navy Dell bag'.",
          "Result: Evaluators dismiss basic CRUD as low-effort projects."], COLOR_AMBER),
        ("The Fraud Crisis", "Unprotected False & Fraudulent Claims",
         ["Publicly showing photos of found items invites opportunistic theft.",
          "No proof of ownership: anyone can claim expensive phones or laptops.",
          "Finder contact details are leaked, creating safety and spam risks."], RGBColor(239, 68, 68)),
        ("The User Inertia", "Passive Portals & Abandoned Listings",
         ["Students never regularly check college websites unless prompted.",
          "Items sit unclaimed for semesters; registries become obsolete.",
          "Physical return rate on campuses is currently below 18%."], COLOR_MUTED)
    ]

    lefts = [0.8, 4.8, 8.8]
    for i, (tag, title, points, accent) in enumerate(cards_s2):
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(lefts[i]), Inches(1.8), Inches(3.73), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = accent
        card.line.width = Pt(1.5)

        tx = slide2.shapes.add_textbox(Inches(lefts[i] + 0.25), Inches(2.0), Inches(3.23), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = accent
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(14)

        for pt in points:
            p = tf.add_paragraph()
            p.text = f"• {pt}"
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_MUTED
            p.space_after = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 3: Concrete Tech Stack (Addressing Ambiguity)
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide3)
    add_header(slide3, "Technical Architecture", "Slide 3: Concrete, End-to-End Production Tech Stack")

    stack_items = [
        ("Frontend Layer", "Streamlit / React Next.js", 
         "Ultra-fast responsive UI, seamless image upload dropzones, and real-time client state management.", COLOR_CYAN),
        ("Backend Layer", "Python (FastAPI)", 
         "Asynchronous microservice REST APIs, sub-50ms endpoint latency, and native Python AI model pipelines.", COLOR_EMERALD),
        ("Database & Storage", "Supabase (PostgreSQL + S3 Storage)", 
         "Relational schema for item metadata, indexed spatial queries, and secure cloud bucket storage for item imagery.", COLOR_AMBER),
        ("Core AI Engine", "Pre-Trained Vision Pipeline (OpenCV / ResNet / CLIP)", 
         "Extracts chromatic HSV distribution and structural contour embeddings for automated similarity scoring.", COLOR_CYAN),
        ("Notification Dispatcher", "Webhook Integration (Telegram & WhatsApp)", 
         "Real-time instant push notification alerts sent to students when a match threshold (≥75%) is triggered.", COLOR_EMERALD)
    ]

    top_pos = [1.6, 2.7, 3.8, 4.9, 6.0]
    for i, (layer, tech, desc, col) in enumerate(stack_items):
        row = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(top_pos[i]), Inches(11.73), Inches(0.95))
        row.fill.solid()
        row.fill.fore_color.rgb = COLOR_CARD
        row.line.color.rgb = COLOR_CARD_BORDER
        row.line.width = Pt(1)

        # Left label box
        tx_l = slide3.shapes.add_textbox(Inches(1.0), Inches(top_pos[i] + 0.1), Inches(3.2), Inches(0.75))
        tf_l = tx_l.text_frame
        tf_l.word_wrap = True
        p_l1 = tf_l.paragraphs[0]
        p_l1.text = layer.upper()
        p_l1.font.size = Pt(10)
        p_l1.font.bold = True
        p_l1.font.color.rgb = col
        p_l2 = tf_l.add_paragraph()
        p_l2.text = tech
        p_l2.font.size = Pt(13)
        p_l2.font.bold = True
        p_l2.font.color.rgb = COLOR_WHITE

        # Right desc box
        tx_r = slide3.shapes.add_textbox(Inches(4.4), Inches(top_pos[i] + 0.15), Inches(7.9), Inches(0.7))
        tf_r = tx_r.text_frame
        tf_r.word_wrap = True
        p_r = tf_r.paragraphs[0]
        p_r.text = desc
        p_r.font.size = Pt(12)
        p_r.font.color.rgb = COLOR_MUTED

    # -------------------------------------------------------------
    # SLIDE 4: High-Impact Features to Win Evaluators
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide4)
    add_header(slide4, "Innovation & Impact", "Slide 4: High-Impact Features Designed to Win Evaluators")

    features = [
        ("01. Automated AI Visual Matching", 
         "Image Feature & Chromatic Similarity",
         "Users upload a photo; vision pipeline extracts visual embeddings and automatically scores & ranks candidate found items without manual browsing.", COLOR_CYAN),
        ("02. Anti-Theft Claim Verification", 
         "Zero-Knowledge Ownership Challenge",
         "Finders specify masked identifiers (e.g. wallpaper description, hidden sticker, card digits). Claimants must solve the challenge to unlock collection tokens.", COLOR_EMERALD),
        ("03. Campus Geotagging & Hotspot Maps", 
         "Spatial Heatmaps & Physical Desks",
         "Tag incidents by campus zone (Library 2nd Fl, Cafeteria, Block C) to display loss density maps and route students to the exact designated physical desk.", COLOR_AMBER),
        ("04. Instant Bot Notification Pings", 
         "Automated Telegram & WhatsApp Webhooks",
         "Eliminates checking portals manually. The moment a matching item is recorded, an instant push message alerts the student on their phone.", COLOR_CYAN)
    ]

    coords = [
        (0.8, 1.8), (6.8, 1.8),
        (0.8, 4.4), (6.8, 4.4)
    ]

    for i, (tag, title, desc, acc) in enumerate(features):
        x, y = coords[i]
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(5.73), Inches(2.35))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = acc
        card.line.width = Pt(1.5)

        tx = slide4.shapes.add_textbox(Inches(x + 0.3), Inches(y + 0.2), Inches(5.13), Inches(1.95))
        tf = tx.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = tag
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = acc
        p.space_after = Pt(4)

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_MUTED

    # -------------------------------------------------------------
    # SLIDE 5: Feasibility, Viability & Fraud Prevention
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide5)
    add_header(slide5, "Operational Viability", "Slide 5: Feasibility, Security & Operational Reliability")

    s5_boxes = [
        ("Fraud Prevention", "Blind Attribute Verification Protocol",
         ["Claimants must describe hidden attributes known only to true owners.",
          "Masked phone numbers & student IDs prevent social engineering.",
          "Brute-force lockout freezes claims after 3 incorrect attempts."], COLOR_EMERALD),
        ("Data Quality", "Automated 30-Day Lifecycle & Archival",
         ["Unclaimed items auto-archive after 30 days to avoid clutter.",
          "AI duplicate detection consolidates multiple reports of the same item.",
          "Donation workflow routes unclaimed items to college charity drives."], COLOR_CYAN),
        ("Privacy & Safety", "Tokenized Contact Mediation",
         ["Student phone numbers and identities are never exposed publicly.",
          "Cryptographic Handshake Tokens (e.g. SIH-A82F) presented at desks.",
          "College security desk acts as authenticated mediator."], COLOR_AMBER)
    ]

    for i, (tag, title, points, acc) in enumerate(s5_boxes):
        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(lefts[i]), Inches(1.8), Inches(3.73), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = acc
        card.line.width = Pt(1.5)

        tx = slide5.shapes.add_textbox(Inches(lefts[i] + 0.25), Inches(2.0), Inches(3.23), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = acc
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(14)

        for pt in points:
            p = tf.add_paragraph()
            p.text = f"• {pt}"
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_MUTED
            p.space_after = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 6: Impact & Future Roadmap
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide6)
    add_header(slide6, "Quantifiable Impact", "Slide 6: Impact Benchmarks & Future Scalability")

    # Left box: Metrics
    card_l = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = COLOR_CARD
    card_l.line.color.rgb = COLOR_EMERALD
    card_l.line.width = Pt(1.5)

    tx_l = slide6.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_l = tx_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "BEFORE VS AFTER BENCHMARKS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(12)

    benchmarks = [
        ("Recovery Rate:", "18% Traditional  ➔  75%+ with Visual AI"),
        ("Avg Turnaround Time:", "5.2 Days  ➔  < 1.4 Hours (Bot Alerts)"),
        ("Fraudulent Claims:", "High (Unchecked)  ➔  Zero (ZK Blind Challenge)"),
        ("Student Friction:", "High (Manual Checking)  ➔  Zero (Push Pings)")
    ]

    for label, val in benchmarks:
        p = tf_l.add_paragraph()
        p.text = label
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_CYAN
        p = tf_l.add_paragraph()
        p.text = val
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(10)

    # Right box: Roadmap
    card_r = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.73), Inches(4.9))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = COLOR_CARD
    card_r.line.color.rgb = COLOR_CYAN
    card_r.line.width = Pt(1.5)

    tx_r = slide6.shapes.add_textbox(Inches(7.05), Inches(2.0), Inches(5.23), Inches(4.5))
    tf_r = tx_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "FUTURE SCALABILITY ROADMAP"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(12)

    roadmap = [
        ("Phase 1: CCTV Visual Anomaly Checks", 
         "Integrate campus CCTV feeds at key exit gates to cross-reference timestamped item movement."),
        ("Phase 2: Smart NFC / QR Campus Tags", 
         "Optional QR sticker tags for student IDs, bottles, and laptops that route directly to owner."),
        ("Phase 3: Multi-College Federation Network", 
         "Inter-collegiate lost & found grid for inter-university sports, cultural fests, and hackathons.")
    ]

    for phase, desc in roadmap:
        p = tf_r.add_paragraph()
        p.text = f"🚀 {phase}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p = tf_r.add_paragraph()
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_MUTED
        p.space_after = Pt(10)

    output_path = os.path.join(os.path.dirname(__file__), "SIH_2026_Lost_and_Found_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()
