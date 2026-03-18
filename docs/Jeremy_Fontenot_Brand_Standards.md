# Jeremy Fontenot - IT Professional

## Brand Kit
Based on provided logo + domain: jeremyfontenot.online

## 1. Brand Identity

Brand Name: Jeremy Fontenot IT Professional

Primary Domain: jeremyfontenot.online

Brand Positioning:
Enterprise-grade IT professional specializing in systems administration, networking, and service desk excellence with a modern, security-first approach.

Brand Personality:
- Technical
- Precise
- Modern
- Secure
- Reliable

## 2. Logo System

Primary Logo:
- Circular JF mark with neon-tech hex pattern background
- Use on dark backgrounds only

Logo Variations:
- Full Logo (with text: JeremyFontenot.online)
- Icon Only (JF circle)
- Monochrome (white)
- Inverted (for light backgrounds)

Usage Rules:
- Do not distort or stretch
- Maintain glow and hex pattern integrity
- Minimum clear space: 20px around logo
- Minimum size: 64px (icon), 120px (full logo)

## 3. Color Palette

Primary Colors:
- Deep Navy (Background): #0F172A
- Slate Tech Blue (Secondary Background): #1E293B

Accent Colors:
- Cyber Cyan (Primary Accent): #38BDF8
- Bright Electric Blue (CTA and Highlights): #0EA5E9

Supporting Colors:
- Soft White (Primary Text): #F1F5F9
- Muted Gray Blue (Secondary Text): #94A3B8

Effects:
- Glow: rgba(56,189,248,0.6)
- Grid and Hex Lines: #38BDF8 at 30% opacity

## 4. Typography

Primary Font: Inter
- Recommended for modern UI and readability

Secondary Font: Roboto Mono
- Recommended for technical and code elements

Usage:
- Headings: Bold or Semi-Bold
- Body: Regular
- Technical or Code content: Roboto Mono

## 5. Visual Style

Core Elements:
- Hexagonal network patterns
- Data streams and digital lines
- Subtle particle effects
- Neon glow accents
- Circular UI elements to match the logo

Background Style:
- Dark radial gradient

```css
background: radial-gradient(circle at center, #1E293B 0%, #0F172A 100%);
```

## 6. UI and Web Branding (CSS Starter)

```css
:root {
  --bg-primary: #0F172A;
  --bg-secondary: #1E293B;
  --accent-primary: #38BDF8;
  --accent-secondary: #0EA5E9;
  --text-primary: #F1F5F9;
  --text-secondary: #94A3B8;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
}

.button-primary {
  background-color: var(--accent-secondary);
  color: white;
  border-radius: 8px;
  padding: 10px 16px;
}

.glow {
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.6);
}
```

## 7. Branding Assets to Generate

Use existing logo to create:
- Favicon set (16x16, 32x32, 64x64)
- Apple Touch Icon (180x180)
- Android Icons (192x192, 512x512)
- LinkedIn Banner (1584x396)
- GitHub Banner
- Email Signature
- Business Card
- Desktop Wallpaper (1920x1080)

## 8. Email Signature Copy

Jeremy Fontenot  
IT Professional

jeremyfontenot.online  
your-email@domain.com

Specializing in Systems Administration | Networking | Service Desk Operations

## 9. LinkedIn Banner Text

Main:
- Jeremy Fontenot
- IT Professional

Subtext:
- Systems Administration • Networking • Enterprise Support

## 10. Brand Voice

Tone:
- Professional
- Clear
- Technical but approachable

Messaging Style:
- Direct and structured
- Step-by-step explanations
- Focus on solutions and outcomes

## 11. Tagline Options

- Engineering Reliable IT Solutions
- Precision. Performance. IT Excellence.
- Modern Infrastructure. Proven Results.
- Built for Stability. Designed for Scale.

## Implementation Notes (Best Practice)

- Keep one source-of-truth for brand standards in SharePoint.
- Use CSS tokens to enforce consistency across web assets.
- Lock logo ratio and minimum clear-space requirements in templates.
- Verify contrast for accessibility in all digital use cases.
- Review banners and social crops on desktop and mobile before publishing.
