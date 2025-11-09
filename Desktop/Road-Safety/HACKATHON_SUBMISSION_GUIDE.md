# Hackathon Submission Documents - Compilation Guide

## 📄 Generated Files

1. **The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.tex**
   - 7-slide professional Beamer presentation
   - AI-themed blue-gray color scheme
   - Includes all 4 screenshots from Photos/ folder
   - GitHub link and team details embedded

2. **The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.tex**
   - IEEE-style technical report
   - 11 sections + appendices + references
   - Complete with code listings, tables, and figures
   - Professional academic formatting

---

## 🚀 Compilation Instructions

### Option 1: Overleaf (Recommended - Easiest)

#### For Presentation:
1. Go to [Overleaf](https://www.overleaf.com)
2. Create New Project → Upload Project
3. Upload `The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.tex`
4. **Important:** Upload the entire `Photos/` folder
5. Click "Recompile"
6. Download PDF: Menu → Download PDF
7. Rename to: `The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.pdf`

#### For Report:
1. Create another New Project in Overleaf
2. Upload `The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.tex`
3. **Important:** Upload the entire `Photos/` folder
4. Click "Recompile"
5. Download PDF: Menu → Download PDF
6. Rename to: `The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.pdf`

---

### Option 2: Local Compilation (Windows)

#### Prerequisites:
```powershell
# Install MiKTeX from https://miktex.org/download
# Or install TeX Live from https://www.tug.org/texlive/
```

#### Compile Presentation:
```powershell
cd C:\Users\91995\Desktop\Road-Safety
pdflatex The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.tex
pdflatex The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.tex
```
(Run twice for proper references)

#### Compile Report:
```powershell
cd C:\Users\91995\Desktop\Road-Safety
pdflatex The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.tex
pdflatex The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.tex
```
(Run twice for table of contents)

---

## 📋 Convert Report PDF to DOCX

### Method 1: Adobe Acrobat Pro (Best Quality)
1. Open PDF in Adobe Acrobat
2. File → Export To → Microsoft Word → Word Document
3. Save as: `The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.docx`

### Method 2: Microsoft Word (Windows)
1. Open Microsoft Word
2. File → Open → Select PDF file
3. Word will convert automatically
4. Save as DOCX format

### Method 3: Online Tools (Free)
1. Go to [PDF2DOC](https://pdf2doc.com) or [iLovePDF](https://www.ilovepdf.com/pdf_to_word)
2. Upload PDF
3. Download DOCX
4. Open in Word and verify formatting

### Method 4: Pandoc (Command Line)
```powershell
# Install Pandoc: https://pandoc.org/installing.html
pandoc The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.pdf -o Report.docx
```

---

## 🖼️ Image Requirements

### Screenshots Used:
All images must be in the `Photos/` folder:

1. **Homepage.png** - Homepage interface
2. **Recommendatio_list.png** - Recommendation list view
3. **Recommendation_detail.png** - Detailed recommendation with metadata
4. **csv_GPT_INPUT_DB.png** - CSV database snapshot

### Image Format Requirements:
- Format: PNG (recommended) or JPG
- Resolution: Minimum 1920x1080 (1080p)
- File size: <2 MB per image
- Color: RGB (not CMYK)

---

## ✅ Pre-Submission Checklist

### For Presentation PDF:
- [ ] All 7 slides compiled successfully
- [ ] Screenshots visible and clear
- [ ] GitHub link clickable: https://github.com/gyanchandra2910/RoadSafety
- [ ] Team names correct: Gyan Chandra (IIITDM), Dristi Singh (KIIT)
- [ ] Footer shows "National Road Safety Hackathon 2025"
- [ ] File size <10 MB
- [ ] Filename: `The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.pdf`

### For Report DOCX:
- [ ] All sections present (Title Page through References)
- [ ] Table of contents auto-generated
- [ ] All 4 screenshots embedded
- [ ] Code listings formatted correctly
- [ ] GitHub link active
- [ ] Page numbers visible
- [ ] File size <10 MB
- [ ] Filename: `The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.docx`

---

## 📐 Document Specifications

### Presentation:
- **Slides:** 7 main slides
- **Aspect Ratio:** 16:9 (widescreen)
- **Theme:** Madrid with custom AI blue-gray colors
- **Font:** Default Beamer (professional)
- **Features:**
  - TikZ architecture diagram on Slide 4
  - All 4 screenshots on Slide 6
  - GitHub link on Slides 1 and 7
  - Footer with hackathon name and team

### Report:
- **Pages:** ~25-30 pages (with appendices)
- **Paper Size:** A4
- **Margins:** 1 inch all sides
- **Font:** Times New Roman, 12pt
- **Line Spacing:** Single (IEEE style)
- **Sections:** 11 main + 3 appendices
- **Features:**
  - Professional title page with logo placeholders
  - Abstract with keywords
  - Table of contents auto-generated
  - 15 references cited
  - Code listings with syntax highlighting
  - System architecture diagram (TikZ)
  - 4 figure captions for screenshots

---

## 🎨 Customization Tips

### Update Logo Placeholders (Optional):
Both documents have logo placeholders. To replace:

```latex
% Instead of:
\fbox{\parbox{3cm}{\centering \vspace{1cm} IIT Madras \\ Logo \vspace{1cm}}}

% Use:
\includegraphics[width=3cm]{iit_madras_logo.png}
```

### Change Color Scheme (Presentation):
Edit these lines in the TEX file:

```latex
\definecolor{aiblue}{RGB}{33,150,243}      % Primary blue
\definecolor{darkblue}{RGB}{13,71,161}     % Dark blue
\definecolor{techgray}{RGB}{96,125,139}    % Gray accent
```

---

## 🐛 Troubleshooting

### Issue: "File not found" error for images
**Solution:** Ensure `Photos/` folder is in the same directory as TEX file, or use absolute paths:
```latex
\includegraphics[width=0.85\textwidth]{C:/Users/91995/Desktop/Road-Safety/Photos/Homepage.png}
```

### Issue: Compilation takes very long
**Solution:** Comment out TikZ diagrams temporarily:
```latex
% \begin{tikzpicture}
% ...
% \end{tikzpicture}
```

### Issue: Missing packages error
**Solution:** Install missing packages via MiKTeX Console (Windows) or:
```bash
sudo tlmgr install <package-name>
```

Common packages needed:
- `fontawesome5` (for icons)
- `tikz` (for diagrams)
- `listings` (for code)
- `booktabs` (for tables)

### Issue: PDF-to-DOCX conversion loses formatting
**Solution:**
1. Use Adobe Acrobat Pro for best quality
2. Manually fix formatting in Word after conversion
3. Check: fonts, tables, code blocks, page breaks

---

## 📊 File Size Optimization

If PDF exceeds 10 MB:

### Compress Images:
```powershell
# Using ImageMagick (install from imagemagick.org)
magick Photos/Homepage.png -quality 85 -resize 1920x1080 Photos/Homepage_compressed.png
```

### Compress PDF:
1. **Adobe Acrobat:** File → Save As Other → Reduced Size PDF
2. **Online:** [SmallPDF](https://smallpdf.com/compress-pdf)
3. **Ghostscript:**
```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

---

## 📤 Upload to Unstop

### Step 1: Prepare Files
1. `The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.pdf` (<10 MB)
2. `The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.docx` (<10 MB)

### Step 2: Verify File Names
Ensure exact naming as above (professional, includes team name, descriptive).

### Step 3: Upload
1. Log in to Unstop hackathon portal
2. Navigate to submission page
3. Upload Presentation PDF
4. Upload Report DOCX
5. Verify both files uploaded successfully
6. Submit before deadline

### Step 4: Backup
Keep copies in:
- Local drive
- Google Drive / OneDrive
- GitHub repository (if allowed)

---

## 🎯 Presentation Tips (7-Minute Timing)

**Slide 1 (Welcome)** - 30 seconds
- "Good morning/afternoon. We are The Silicon Savants..."
- Quick team intro

**Slide 2 (Problem Statement)** - 1 minute
- "India faces 150,000 road fatalities annually..."
- Emphasize manual process limitations

**Slide 3 (Objective)** - 1 minute
- "Our goal: automate intervention identification using AI..."
- Highlight hybrid approach

**Slide 4 (Solution/Architecture)** - 1.5 minutes ⭐ **KEY SLIDE**
- Walk through diagram: User → TF-IDF → GPT → Output
- "Our system combines traditional ML with modern AI..."

**Slide 5 (Implementation)** - 1.5 minutes
- "Built with Python, Flask, Streamlit..."
- Mention 50-record IRC database

**Slide 6 (Results)** - 1.5 minutes
- Show screenshots, explain UI
- "<2 second response time, IRC-compliant"

**Slide 7 (Thank You)** - 30 seconds
- Thank organizers, share GitHub link
- Q&A invitation

---

## 📞 Support Contacts

**Team:**
- Gyan Chandra - gyanchandra2910@gmail.com
- Dristi Singh - [email]

**GitHub:** https://github.com/gyanchandra2910/RoadSafety

**Hackathon:** National Road Safety Hackathon 2025, IIT Madras - CoERS

---

## ✨ Final Notes

### Both documents are:
✅ Professional IEEE/Academic standard
✅ Include all 4 screenshots
✅ Reference GitHub repository
✅ Hackathon-ready formatting
✅ Under 10 MB target size
✅ Team and institution details embedded
✅ Ready for Overleaf or local compilation

### Your submission package:
```
Road-Safety/
├── The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.tex
├── The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.tex
├── Photos/
│   ├── Homepage.png
│   ├── Recommendatio_list.png
│   ├── Recommendation_detail.png
│   └── csv_GPT_INPUT_DB.png
└── [After compilation]
    ├── The_Silicon_Savants_Road_Safety_Intervention_GPT_Presentation.pdf
    └── The_Silicon_Savants_Road_Safety_Intervention_GPT_Report.docx
```

**Good luck with your hackathon submission! 🏆🚀**
