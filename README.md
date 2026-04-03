# A Li'l Love Inn — Website

Static HTML site replacing Squarespace. Hosted on Cloudflare Pages. Images on Cloudflare R2.

## File Structure

```
lilloveinn/
├── index.html          ← Home page
├── mom-pops.html       ← Mom & Pop's property
├── lil-love-inn.html   ← A Li'l Love Inn cottage
├── the-castle.html     ← The Castle property
├── the-vision.html     ← The Vision (all 3 properties)
├── about.html          ← About Us
├── inquire.html        ← Contact / Inquire form
├── css/
│   └── style.css       ← All shared styles
├── js/
│   └── main.js         ← Nav, scroll effects, form handler
└── download_images.py  ← Script to download images from Squarespace
```

## Step 1 — Download Images

Run the download script on your Mac:
```bash
cd ~/Desktop/lilloveinn
python3 download_images.py
```
This saves all images to `./images/`.

## Step 2 — Upload to Cloudflare R2

1. Go to https://dash.cloudflare.com → R2
2. Create bucket: `lilloveinn-images`
3. Upload everything in the `images/` folder
4. Enable "Public access" on the bucket
5. Note your public URL: `https://pub-XXXX.r2.dev/`

## Step 3 — Update Image URLs in HTML

Find & replace in all HTML files:
- Find: `https://images.squarespace-cdn.com/content/v1/6617b4042c2ab03d8de452b0/`
- Replace: `https://pub-XXXX.r2.dev/` (your R2 URL)

Each image filename maps to your R2 bucket. The download script saves them with the same filenames used in the HTML.

## Step 4 — Set Up Contact Form (Free)

1. Go to https://web3forms.com
2. Enter your email → Get a free access key
3. In `index.html` and `inquire.html`, replace `YOUR_WEB3FORMS_KEY` with your key
4. Form submissions will email you directly. Free for up to 250/month.

## Step 5 — Deploy to Cloudflare Pages

1. Create a GitHub account if needed: https://github.com
2. Create a new repo called `lilloveinn`
3. Upload all these files to the repo
4. Go to https://dash.cloudflare.com → Pages → Create a project
5. Connect GitHub → Select `lilloveinn` repo → Deploy
6. Cloudflare gives you a free URL like `lilloveinn.pages.dev`

## Step 6 — Connect Your Domain (lilloveinn.com)

**Current status:** Domain is at GoDaddy, pointed at Squarespace.

### Option A: Transfer domain to Cloudflare (recommended — saves ~$10/yr)
1. Log into GoDaddy → Find lilloveinn.com → Get EPP/transfer code
2. In Cloudflare → Registrar → Transfer domain → Enter code
3. Takes 5-7 days to transfer

### Option B: Just change nameservers (faster, keep at GoDaddy)
1. In Cloudflare → Add site → Enter lilloveinn.com
2. Cloudflare gives you 2 nameserver addresses
3. Log into GoDaddy → Update nameservers to Cloudflare's
4. Takes 24-48 hours to propagate
5. Then in Cloudflare Pages → Custom domain → Add lilloveinn.com

## Editing the Site

To update any text or content:
- Open the relevant `.html` file in any text editor
- Make changes
- Push to GitHub — Cloudflare auto-deploys in ~1 minute

To add photos later:
- Upload to R2 bucket
- Add `<img src="...">` tags in HTML

## Domain Expiry Reminder

`lilloveinn.com` expires: **October 19, 2026** (at GoDaddy)
Make sure to renew or transfer before then!
