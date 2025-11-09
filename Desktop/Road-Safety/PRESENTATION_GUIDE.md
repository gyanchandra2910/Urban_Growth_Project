# LaTeX Presentation Compilation Guide

## 📄 File: presentation.tex

### How to Compile

#### Option 1: Overleaf (Recommended - Easiest)
1. Go to [Overleaf](https://www.overleaf.com)
2. Create a new project → Upload Project
3. Upload `presentation.tex`
4. Click "Recompile" - PDF will be generated automatically
5. Download PDF: Menu → Download PDF

#### Option 2: Local LaTeX Installation

**Windows:**
```powershell
# Install MiKTeX from https://miktex.org/download
# Then compile:
pdflatex presentation.tex
pdflatex presentation.tex  # Run twice for proper references
```

**Linux:**
```bash
# Install TeX Live
sudo apt-get install texlive-full

# Compile
pdflatex presentation.tex
pdflatex presentation.tex
```

**macOS:**
```bash
# Install MacTeX from https://www.tug.org/mactex/
# Then compile:
pdflatex presentation.tex
pdflatex presentation.tex
```

### Required LaTeX Packages

The following packages are used (usually included in standard distributions):
- `beamer` - Presentation framework
- `tikz` - Graphics and diagrams
- `graphicx` - Image handling
- `booktabs` - Professional tables
- `hyperref` - Hyperlinks

### Customization Tips

#### 1. Add Institution Logos
Replace the placeholder boxes on Slide 1 and 7 with actual logos:

```latex
% Instead of:
\fbox{\parbox{3cm}{\centering \vspace{1cm} IIT Madras \\ Logo \vspace{1cm}}}

% Use:
\includegraphics[width=3cm]{iit_madras_logo.png}
```

#### 2. Change Color Scheme
Modify colors in the preamble:

```latex
\definecolor{primaryblue}{RGB}{0,51,102}      % Main color
\definecolor{secondaryblue}{RGB}{0,102,204}   % Accent color
\definecolor{accentgray}{RGB}{64,64,64}       % Gray color
```

Popular alternatives:
- **Red theme**: `{RGB}{139,0,0}` and `{RGB}{220,20,60}`
- **Green theme**: `{RGB}{0,100,0}` and `{RGB}{34,139,34}`
- **Purple theme**: `{RGB}{75,0,130}` and `{RGB}{138,43,226}`

#### 3. Add Images
Place images in the same folder and use:

```latex
\begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{architecture_diagram.png}
    \caption{System Architecture}
\end{figure}
```

#### 4. Change Theme
Replace `\usetheme{Madrid}` with:
- `\usetheme{Berlin}` - Classic sidebar
- `\usetheme{Copenhagen}` - Clean and minimal
- `\usetheme{Frankfurt}` - Navigation bullets
- `\usetheme{Montpellier}` - Tree navigation

#### 5. Update Contact Information
On the Thank You slide, replace placeholders:

```latex
{\small \textcolor{accentgray}{Contact: gyan@example.com | GitHub: github.com/yourrepo}}
```

### Presentation Structure

**7 Main Slides:**
1. ✅ Welcome Slide (Title, Team, Organizers)
2. ✅ Problem Statement (Challenges in road safety)
3. ✅ Objective & Motivation (Why this project matters)
4. ✅ Proposed Solution (Architecture diagram + workflow)
5. ✅ Implementation (Tech stack, tools, design)
6. ✅ Results & Output (Demo with example)
7. ✅ Thank You Slide (Acknowledgements)

**2 Backup Slides:**
- Technical Details (TF-IDF & GPT specs)
- Future Enhancements (Roadmap)

### Presentation Tips

#### Timing (for Stage 1 - 7 minutes)
- Slide 1: 30 seconds (Introduction)
- Slide 2: 1 minute (Problem context)
- Slide 3: 1 minute (Objective)
- Slide 4: 1.5 minutes (Solution architecture - KEY SLIDE)
- Slide 5: 1.5 minutes (Implementation)
- Slide 6: 1 minute (Results demo)
- Slide 7: 30 seconds (Thank you)

#### Speaker Notes

**Slide 1:**
"Good morning/afternoon. We are The Silicon Savants from IIITDM Kancheepuram, presenting our solution for Problem Statement 1.3 - Road Safety Intervention GPT."

**Slide 2:**
"India faces a critical road safety crisis with 150,000 annual fatalities. Current intervention identification is manual, time-consuming, and inconsistent."

**Slide 3:**
"Our objective is to automate this process using AI, providing IRC-compliant recommendations in seconds instead of hours."

**Slide 4:** (MOST IMPORTANT)
"Our hybrid approach combines TF-IDF similarity search for precision with GPT-3.5 for contextual reasoning. User describes an issue, our system searches 50 curated interventions, and GPT generates data-backed explanations."

**Slide 5:**
"Built with Python, Flask backend, Streamlit frontend, and OpenAI GPT. The system is modular, extensible, and production-ready."

**Slide 6:**
"Here's a live example: For damaged signs with poor visibility, the system recommends retro-reflective replacements per IRC:67-2012 with 67% relevance, completing in under 2 seconds."

**Slide 7:**
"Thank you for your attention. We believe this tool can save lives by empowering faster, data-driven road safety decisions."

### Export Settings

For best quality PDF:
1. Use PDF/A-1b format (archival)
2. Embed all fonts
3. Resolution: 300 DPI minimum
4. File size: Keep under 10 MB

In Overleaf, these are handled automatically.

### Troubleshooting

**Issue: "File not found" error**
- Ensure all image files are in the same directory
- Use relative paths or full paths

**Issue: Colors not displaying**
- Some PDF viewers don't support all colors
- Test in Adobe Reader and browser preview

**Issue: Compilation takes too long**
- Comment out complex TikZ diagrams temporarily
- Use draft mode: `\documentclass[draft]{beamer}`

**Issue: Text overflow**
- Reduce font size: `\small` or `\footnotesize`
- Split content across multiple slides

### Assets Needed (Optional)

To enhance the presentation, prepare these files:
1. `iit_madras_logo.png` - IIT Madras logo (transparent background)
2. `coers_logo.png` - CoERS logo
3. `iiitdm_logo.png` - IIITDM Kancheepuram logo
4. `architecture_diagram.png` - System architecture (can be generated from TikZ)
5. `screenshot_output.png` - Streamlit UI screenshot with results

### Final Checklist

Before submission:
- [ ] Compile successfully without errors
- [ ] All 7 slides present and formatted
- [ ] Team names and contact info updated
- [ ] Logos added (if available)
- [ ] Spell-check completed
- [ ] File size < 10 MB
- [ ] PDF tested in multiple viewers
- [ ] Presentation rehearsed (7-minute target)

---

## 🎯 Quick Start for Hackathon

1. **Upload to Overleaf** → Instant compilation
2. **Download PDF** → Ready for submission
3. **Print Notes** → Speaker guide for rehearsal
4. **Practice** → 7-minute presentation

Your presentation is **hackathon-ready**! Good luck! 🚀
