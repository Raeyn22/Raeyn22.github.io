

```markdown
# Supasoko – Farmer-to-Market E-Commerce Platform (https://raeyn22.github.io/#pricing)

A web platform connecting African farmers directly to buyers with real-time market price alerts (Demo data in KSh).

## Key Features
- **Farmer-Buyer Marketplace**: List and discover fresh produce
- **Price Alert System**: Get notified when crop prices hit targets
- **Kenyan Market Data**: Demo prices for maize, rice, tomatoes, etc.
- **Mobile-Friendly**: Works on all devices
- **Secure Auth**: Supabase-powered login/registration

## Technologies Used
**Frontend**:  
✔ HTML5/CSS3  
✔ JavaScript  
✔ Bootstrap 5  

**Backend**:  
✔ Supabase (Auth + Database)  
✔ Python (FastAPI - optional backend)  

## Live Demo
[View on Vercel/Render](#) *(Add your deployment link here)*

## Setup Instructions

### 1. Frontend Setup
```bash
git clone https://github.com/yourusername/supasoko.git
cd supasoko
```

### 2. Configure Supabase
1. Create a free account at [Supabase](https://supabase.com/)
2. Create a new project and get your:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`

3. Add to environment:
```env
# .env file
NEXT_PUBLIC_SUPABASE_URL=your-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

### 3. Deploy
**Vercel (Recommended for Frontend):**
- Connect your GitHub repo
- Add environment variables
- Deploy!

**Render (For Python Backend):**
```yaml
# render.yaml example
services:
  - type: web
    envVars:
      - key: SUPABASE_URL
        value: your-project-url
      - key: SUPABASE_KEY
        value: your-anon-key
```

## Project Structure
```
supasoko/
├── index.html          # Main frontend
├── styles/            # CSS files
├── scripts/           # JavaScript files
├── backend/           # Python API (optional)
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## License
MIT License - Free for educational and commercial use

## Support
For issues, please [open a GitHub ticket](https://github.com/Raeyn22/supasoko/issues).

---
**Farm Smart, Sell Smarter** 🌱📈  
*Empowering African Farmers Through Technology*
```


