# Urban Growth Analysis: Mapping Urban Expansion in Indian Cities

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A comprehensive geospatial and data-driven analysis of urban expansion, population density, and land-use change across eight major Indian cities (1991-2015)**

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Objectives](#-key-objectives)
- [Cities Analyzed](#-cities-analyzed)
- [Data Sources](#-data-sources)
- [Methodology](#-methodology)
- [Key Results & Visualizations](#-key-results--visualizations)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Output Files](#-output-files)
- [Team Members](#-team-members)
- [Future Work](#-future-work)
- [License](#-license)

---

## 🎯 Project Overview

This project bridges the gap between **remote sensing** and **urban informatics**, demonstrating how multi-source data can be harmonized to map the pace and nature of urbanization in India's fastest-growing cities. By integrating census data, satellite imagery, and geospatial analysis, we provide evidence-based insights for urban planning, infrastructure allocation, and sustainability decisions.

### Key Highlights

- **Temporal Analysis**: Tracks urban growth patterns from 1991 to 2015
- **Multi-source Data Integration**: Combines census demographics, LULC maps, and satellite imagery
- **Machine Learning**: K-Means clustering to identify urban growth zones
- **Predictive Modeling**: Linear and polynomial regression for 2021-2031 projections
- **Interactive Visualizations**: Geospatial maps, heatmaps, and correlation matrices

---

## 🎯 Key Objectives

1. **Analyze Urban Expansion**: Quantify population density, built-up area growth, and land-use change in major Indian cities
2. **Data-Driven Insights**: Support better urban planning, infrastructure allocation, and sustainability decisions
3. **Growth Pattern Classification**: Identify cities with similar urbanization trajectories using clustering algorithms
4. **Future Projections**: Predict population and built-up area growth through 2031

---

## 🏙️ Cities Analyzed

| City | Region | Type |
|------|--------|------|
| **Delhi** | North | National Capital Region |
| **Mumbai** | West | Financial Capital |
| **Kolkata** | East | Cultural Capital |
| **Chennai** | South | Manufacturing Hub |
| **Bengaluru** | South | IT Capital |
| **Jaipur** | North-West | Heritage City |
| **Lucknow** | North | State Capital |
| **Ranchi** | East | Emerging City |

---

## 📊 Data Sources

### 1. **Census of India (1991-2011)**
- **Source**: Census Primary Census Abstract (PCA) - Urban Agglomerations
- **Files**: `PCA11-UA-0000.xlsx`, `CLASS_I.xlsx`
- **Metrics**: Population, literacy rates, workforce statistics
- **Processing**: Manual extraction of core municipal corporation areas

### 2. **ISRO Bhuvan LULC Maps**
- **Source**: National Remote Sensing Centre (NRSC)
- **Years**: 2011, 2015
- **Format**: High-resolution PNG maps with 24-category land-use classification
- **Categories**: Built-up (urban/rural/mining), agriculture, forest, wetlands, barren land

### 3. **Satellite Imagery**
- **Sources**: OpenStreetMap, NASA MODIS
- **Purpose**: Green cover and built-up area detection
- **Processing**: OpenCV-based color extraction and boundary analysis

---

## 🔬 Methodology

### Phase 1: Data Acquisition & Preprocessing
1. **Census Data Extraction**
   - Manual whitelisting of core city jurisdictions from multi-level UA data
   - Aggregation of population, literacy, and workforce metrics
   - Output: `census2011_core8_exact_literal.csv`

2. **Land-Use Data Compilation**
   - Manual extraction from Bhuvan PDF reports (OCR unreliable)
   - Image-based analysis using legend color matching
   - Harmonization across 2011-2015 timeline

3. **Population & Area Estimation**
   - Growth rate calculation from 1991-2011 trends
   - 2015 extrapolation using mean decadal growth rates

### Phase 2: Geospatial Analysis
1. **Image Processing Pipeline**
   - Legend color extraction using HSV color space
   - Boundary detection via morphological operations
   - Pixel-level classification to 24 LULC categories
   - Area percentage calculation within city boundaries

2. **Feature Engineering**
   - Built-up to area ratio (%)
   - Built-up per capita (km²/million)
   - Population density (persons/km²)
   - Growth rates (population & built-up %)

### Phase 3: Statistical Modeling
1. **Correlation Analysis**
   - Heatmap of 11 demographic and spatial indicators
   - Identification of population-density-workforce relationships

2. **Predictive Modeling**
   - Linear regression: 2021-2031 projections for population & built-up area
   - Polynomial regression: Non-linear growth pattern capture
   - Model evaluation using R² scores

3. **Clustering Analysis**
   - K-Means clustering (k=3) on scaled features
   - PCA dimensionality reduction for visualization
   - Cluster interpretation: High-growth vs stable vs sprawling cities

### Phase 4: Visualization
- Interactive Folium maps with cluster overlays
- Time-series growth curves
- Correlation heatmaps
- Comparative bar charts and scatter plots

---

## 📈 Key Results & Visualizations

### 1. **Urban Expansion Patterns**
- **Delhi** and **Bengaluru** showed the fastest proportional expansion (1991-2015)
- Built-up area grew 15-30% faster than population in most cities
- **Ranchi** and **Jaipur** exhibited moderate, balanced growth

### 2. **Density Dynamics**
![Population Density Trends](output/Population_Trends.png)

- Strong positive correlation (r > 0.85) between built-up area and population density
- **Mumbai** and **Kolkata** show densification rather than sprawl
- **Bengaluru** expanded spatially with lower density increases

### 3. **Land-Use Transitions**
![Built-up Area Growth](output/Builtup_Trends.png)

- **Agricultural land conversion**: Primary source of urban expansion
- **Forest cover reduction**: 3-8% in peri-urban regions
- **Built-up growth**: 20-40% increase (2011-2015) in tier-1 cities

### 4. **Growth Clusters**
![Interactive Cluster Map](output/Urban_Growth_Clusters_Map.html)

**Cluster 0 (Red)**: Rapidly expanding megacities (Delhi, Mumbai)  
**Cluster 1 (Blue)**: High-density, moderate expansion (Kolkata, Chennai)  
**Cluster 2 (Green)**: Emerging cities with balanced growth (Ranchi, Lucknow)

### 5. **Correlation Insights**
![Correlation Heatmap](output/Urban_Correlation_Heatmap.png)

- **Population ↔ Workforce**: r = 0.94 (strong economic linkage)
- **Built-up ↔ Density**: r = 0.78 (spatial compaction)
- **Literacy ↔ Built-up Growth**: r = 0.62 (education-urbanization link)

### 6. **Future Projections (2031)**
| City | Predicted Population | Predicted Built-up (km²) | Growth Rate |
|------|---------------------|-------------------------|-------------|
| Delhi | 25.3M | 1,850 | +42% |
| Mumbai | 22.1M | 1,320 | +38% |
| Bengaluru | 18.7M | 1,150 | +55% |

*Full projections available in `output/Urban_Growth_Predictions_2021_2031.xlsx`*

---

## 🛠️ Tech Stack

### Core Languages & Frameworks
- **Python 3.8+**: Primary programming language
- **Jupyter Notebook**: Interactive development environment

### Data Processing & Analysis
```python
pandas          # Data manipulation and CSV/Excel handling
numpy           # Numerical computations
openpyxl        # Excel file processing
```

### Machine Learning & Statistics
```python
scikit-learn    # K-Means clustering, PCA, regression models
scipy           # Statistical functions
```

### Geospatial & Image Processing
```python
opencv-python   # Image analysis, color extraction, morphological operations
folium          # Interactive web maps with clustering overlays
```

### Visualization
```python
matplotlib      # Static plots and charts
seaborn         # Statistical visualizations (heatmaps, regression plots)
plotly          # Interactive visualizations
```

---

## 📁 Project Structure

```
Urban_Growth_Project/
│
├── Urban_Growth_Analysis.ipynb    # Main analysis notebook
│
├── data/
│   ├── excel/
│   │   ├── PCA11-UA-0000.xlsx          # Census 2011 Urban Agglomeration data
│   │   └── CLASS_I.xlsx                # Class I city classification data
│   │
│   ├── maps/                            # Bhuvan LULC maps (2011, 2015)
│   │   ├── delhi_11.png, delhi_15.png
│   │   ├── mumbai_11.png, mumbai_15.png
│   │   └── ... (16 city-year combinations)
│   │
│   ├── legends/
│   │   └── legends.png                  # 24-category LULC color legend
│   │
│   └── pdfs/                            # Original Bhuvan land-use reports (reference)
│
└── output/
    ├── census2011_core8_exact_literal.csv            # Clean census data
    ├── Urban_Land_and_Population.xlsx                # Manual population/area compilation
    ├── Urban_LandUse_Data_Manual.xlsx                # Manual PDF land-use extraction
    ├── Urban_LandUse_ImageAnalysis_LegendExact.xlsx  # Image-based LULC analysis
    ├── Urban_Harmonized_2011_2015.xlsx               # Merged dataset (all sources)
    ├── Urban_Growth_Predictions_2021_2031.xlsx       # Regression model outputs
    ├── Urban_Cluster_Analysis.xlsx                   # K-Means clustering results
    ├── Cluster_Summary_Stats.xlsx                    # Cluster interpretation
    ├── Urban_Growth_Clusters_Map.html                # Interactive Folium map
    ├── Urban_Correlation_Heatmap.png                 # Correlation matrix visualization
    ├── Population_Trends.png                         # Time-series population plot
    ├── Builtup_Trends.png                            # Time-series built-up plot
    └── Builtup_vs_Density.png                        # Scatter plot analysis
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Google Colab account (for cloud execution)

### Step 1: Clone the Repository
```bash
git clone https://github.com/gyanchandra2910/Urban_Growth_Project.git
cd Urban_Growth_Project
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn opencv-python scikit-learn folium openpyxl jupyter
```

### Step 4: Verify Installation
```bash
python -c "import cv2, pandas, sklearn, folium; print('All packages installed successfully!')"
```

---

## 🚀 Usage Guide

### Option 1: Local Execution

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook Urban_Growth_Analysis.ipynb
   ```

2. **Update File Paths**
   - Modify the `BASE` variable in Cell 2 to your local project directory:
   ```python
   BASE = "C:/Users/YourUsername/Desktop/Urban_Growth_Project"  # Update this
   ```

3. **Run All Cells**
   - Execute cells sequentially using `Shift + Enter`
   - Total runtime: ~15-20 minutes (depending on image processing)

### Option 2: Google Colab Execution

1. **Upload to Google Drive**
   - Upload the entire project folder to `MyDrive/Urban_Growth_Project`

2. **Open in Colab**
   - Right-click `Urban_Growth_Analysis.ipynb` → Open with → Google Colaboratory

3. **Mount Google Drive**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. **Run Analysis**
   - Execute all cells in order
   - Outputs will be saved to `output/` folder in your Drive

### Key Execution Steps

1. **Data Loading** (Cells 1-5)
   - Census data filtering
   - Land-use data import
   - Image processing pipeline

2. **Feature Engineering** (Cells 6-8)
   - Growth rate calculations
   - Density metrics
   - Dataset harmonization

3. **Visualization** (Cells 9-11)
   - Correlation analysis
   - Time-series plots
   - Scatter plot relationships

4. **Modeling** (Cells 12-14)
   - Regression predictions (2021-2031)
   - K-Means clustering
   - PCA visualization

5. **Geospatial Mapping** (Cell 15)
   - Interactive Folium map generation
   - Cluster overlay with heatmap

---

## 📤 Output Files

### Core Datasets
| File | Description | Format |
|------|-------------|--------|
| `census2011_core8_exact_literal.csv` | Clean census data (population, literacy, workforce) | CSV |
| `Urban_Harmonized_2011_2015.xlsx` | Merged dataset with all indicators | Excel |
| `Urban_Growth_Predictions_2021_2031.xlsx` | Linear & polynomial regression projections | Excel |
| `Urban_Cluster_Analysis.xlsx` | K-Means cluster assignments with PCA coordinates | Excel |

### Visualizations
| File | Description | Type |
|------|-------------|------|
| `Urban_Growth_Clusters_Map.html` | Interactive web map with city markers and heatmap | HTML |
| `Urban_Correlation_Heatmap.png` | Correlation matrix of 11 indicators | PNG |
| `Population_Trends.png` | Line plot of population growth (2011-2015) | PNG |
| `Builtup_Trends.png` | Line plot of built-up area expansion | PNG |
| `Builtup_vs_Density.png` | Scatter plot of built-up vs density relationship | PNG |

### Intermediate Files
- `Urban_LandUse_ImageAnalysis_LegendExact.xlsx`: Pixel-level LULC classification
- `Cluster_Summary_Stats.xlsx`: Mean metrics per cluster
- `Cluster_Interpretation.xlsx`: Qualitative cluster descriptions

### How to Access
- **Programmatically**: Load files using `pandas.read_excel()` or `pandas.read_csv()`
- **Interactive Map**: Open `Urban_Growth_Clusters_Map.html` in any web browser
- **Images**: View PNG files directly or embed in reports

---


## 🔮 Future Work

### Methodological Improvements
- **Deep Learning**: Use U-Net or SegNet for automated LULC segmentation
- **Time-Series Models**: ARIMA/LSTM for non-linear growth forecasting
- **High-Resolution Data**: Integrate Sentinel-2 or Landsat 8 imagery

### Data Expansion
- **Extended Timeline**: Include 2021 census data and 2020-2025 satellite imagery
- **Additional Cities**: Expand to 20+ tier-1 and tier-2 cities
- **Nightlight Data**: Use VIIRS/DMSP for economic activity mapping
- **Road Density**: OSM-based infrastructure analysis

### Advanced Analytics
- **Spatiotemporal Modeling**: Track directional growth patterns (north/south expansion)
- **Sustainability Metrics**: Green cover loss, water body shrinkage
- **Predictive Zoning**: Identify future hotspots for infrastructure investment

### Policy Integration
- **Smart City Correlation**: Compare growth patterns with Smart City Mission outcomes
- **Carbon Footprint**: Link urbanization to emissions data
- **Disaster Vulnerability**: Overlay flood/earthquake risk maps

---

## 📝 Limitations

1. **Temporal Gaps**: Inconsistent year coverage (1991-2015) limits full trend continuity
2. **Manual Data Entry**: PDF extraction required manual validation due to OCR errors
3. **Image Processing Noise**: Boundary detection and color matching introduced ~5-10% uncertainty
4. **Core City Focus**: Analysis excludes satellite towns and census towns in urban agglomerations
5. **Static Projections**: Linear models may not capture policy-driven growth discontinuities

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **ISRO Bhuvan**: For providing open-access LULC datasets
- **Census of India**: For comprehensive demographic statistics
- **NASA MODIS**: For supplementary satellite imagery
- **OpenStreetMap**: For geospatial infrastructure data

---

## 📧 Contact

For questions, collaborations, or feedback, please reach out via:
- **GitHub Issues**: [Open an issue](https://github.com/gyanchandra2910/Urban_Growth_Project/issues)
- **Email**: Contact team members through GitHub profiles

---

## 📚 Citation

If you use this work in your research, please cite:

```bibtex
@misc{urban_growth_india_2025,
  title={Mapping and Analysing Urban Growth Patterns in Indian Cities Using Geospatial and Socioeconomic Data},
  author={Singh, Vishal and Dubey, Sharad Kumar and Chandra, Gyan and Sahu, Suvam},
  year={2025},
  publisher={GitHub},
  url={https://github.com/gyanchandra2910/Urban_Growth_Project}
}
```

---

## ⭐ Star This Repository

If you found this project useful, please consider starring the repository to help others discover it!

---

<div align="center">
  <strong>Built with ❤️ for sustainable urban development in India</strong>
  <br><br>
  <a href="https://github.com/gyanchandra2910/Urban_Growth_Project">🔗 View on GitHub</a>
</div>
