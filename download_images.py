#!/usr/bin/env python3
"""
Download all A Li'l Love Inn images from Squarespace CDN.
Run: python3 download_images.py
Images will be saved to ./images/ folder.
"""

import urllib.request
import os
import time
from urllib.parse import unquote

# All image URLs from the site
IMAGES = [
    # Logo
    ("Logo_JPG2.jpg", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/2083158c-6e88-4050-815c-a9110fbd8290/Logo_JPG2.jpg?format=1500w"),
    # Home hero
    ("hero_sunset.jpeg", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/3da9e0eb-b0d2-4488-99cc-d0fec545a3f3/IMG_0096.jpeg?format=2500w"),
    # Property card images (painterly/filtered)
    ("card_mompops.JPG", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/2408cd34-8357-41dc-a069-a3b528910d63/IMG_3539.JPG?format=1500w"),
    ("card_lilloveinn.jpg", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/356b345e-5c0b-416d-be59-0c445ff0ebe3/323baffa-d13a-4016-838e-73dbec2b0726.jpg?format=1500w"),
    ("card_castle.jpeg", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/6d9d7806-9c93-43f0-8f6e-3e99c3e65c45/77a71e0c-268e-4d5e-a6e7-dd4dc87cb5db.jpeg?format=1500w"),
    ("card_vision.jpeg", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/a86652ae-e476-4929-86e6-ccbd13a031a0/218034f8-c744-6266-1713-0f9d0606fd47.jpeg?format=1500w"),
    # Gallery images
    ("gallery_1.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/9c4b71b4-3faf-435f-b520-2b1cb275b870/tempImagedg3iZN.png?format=2500w"),
    ("gallery_2.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/2dac1baa-0963-43ef-934d-fb58d1521e95/tempImageBGWBbR.png?format=2500w"),
    ("gallery_3.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/0ddb0a80-5a0b-473e-95e0-1089355dd8f9/tempImagekQTYoL.png?format=2500w"),
    ("gallery_4.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/d1e27097-f9b1-48af-a2d5-a2cb3494082f/tempImageIJkRyC.png?format=2500w"),
    # Airbnb superhost screenshots
    ("airbnb_stats_1.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/a2540eb8-dbf4-4f9d-9e67-74d16ddb0024/Screenshot+2024-04-08+at+12.30.21%E2%80%AFPM.png?format=1500w"),
    ("airbnb_stats_2.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/32e2a1af-653b-4bb1-8ee1-fe51dc1c4ae9/Screenshot+2024-04-08+at+12.30.36%E2%80%AFPM.png?format=1500w"),
    ("airbnb_stats_3.png", "https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/59750279-0f05-4621-a0c0-665fd06c3477/Screenshot+2024-04-08+at+12.30.29%E2%80%AFPM.png?format=1500w"),
]

def download_images():
    os.makedirs("images", exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    print(f"Downloading {len(IMAGES)} images...\n")
    success = 0
    
    for filename, url in IMAGES:
        filepath = os.path.join("images", filename)
        if os.path.exists(filepath):
            print(f"  ✓ Already exists: {filename}")
            success += 1
            continue
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
            with open(filepath, 'wb') as f:
                f.write(data)
            size_kb = len(data) // 1024
            print(f"  ✓ Downloaded: {filename} ({size_kb} KB)")
            success += 1
            time.sleep(0.3)  # Be polite to CDN
        except Exception as e:
            print(f"  ✗ Failed: {filename} — {e}")
    
    print(f"\nDone! {success}/{len(IMAGES)} images downloaded to ./images/")
    print("\nNext step: Upload the images/ folder to Cloudflare R2")
    print("Then update image URLs in your HTML files to point to your R2 bucket.")

if __name__ == "__main__":
    download_images()
