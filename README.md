# Clinical Pattern Analysis of Melanoma and Non-Melanoma Skin Lesions
### Using the HAM10000 Dataset

An academic exploratory project analyzing clinical and demographic patterns in dermatoscopic skin lesion data. The focus is on understanding how **age**, **sex**, and **body localization** relate to lesion type -- using statistical analysis and simple machine learning on metadata only.

> **Disclaimer:** This is an educational project only. It is not a clinical tool and must not be used for medical decision-making.

---

## Project Structure

```
skincancer/
+-- HAM10000_metadata.csv          # Main metadata file (10,015 rows)
+-- HAM10000_images_part_1/        # Dermatoscopic images (5,000 images)
+-- HAM10000_images_part_2/        # Dermatoscopic images (5,015 images)
+-- skin_lesion_analysis.ipynb     # Main analysis notebook
+-- requirements.txt               # Python dependencies
+-- figures/                       # Auto-generated output plots
+-- README.md                      # This file
+-- report.md                      # Full academic report
```

---

## Dataset

**HAM10000** (*Human Against Machine with 10,000 training images*) is a publicly available dataset of dermatoscopic images with confirmed diagnoses.

| Column | Description |
|--------|-------------|
| `lesion_id` | Unique lesion identifier |
| `image_id` | Unique image identifier |
| `dx` | Diagnosis code (7 classes) |
| `dx_type` | Confirmation method (histo, follow_up, consensus, confocal) |
| `age` | Patient age in years |
| `sex` | Patient sex (male / female) |
| `localization` | Body site of the lesion |

### Diagnosis Classes

| Code | Full Name | Class |
|------|-----------|-------|
| `nv` | Melanocytic Nevi | Benign |
| `bkl` | Benign Keratosis-like Lesions | Benign |
| `df` | Dermatofibroma | Benign |
| `vasc` | Vascular Lesions | Benign |
| `mel` | Melanoma | Malignant-like |
| `bcc` | Basal Cell Carcinoma | Malignant-like |
| `akiec` | Actinic Keratosis / Bowen's Disease | Malignant-like |

---

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Launch Jupyter**
```bash
jupyter notebook skin_lesion_analysis.ipynb
```

**3. Run all cells**

In Jupyter: `Kernel -> Restart & Run All`

---

## Notebook Sections

| Section | Content |
|---------|---------|
| 0 | Setup and imports |
| 1 | Biomedical background and research questions |
| 2 | Dataset loading and overview |
| 3 | Data cleaning (missing values, age binning, clinical grouping) |
| 4 | Exploratory Data Analysis (8 plots) |
| 5 | Statistical analysis (Chi-square, Kruskal-Wallis, Mann-Whitney U) |
| 6 | Optional ML -- metadata-only melanoma screening models |
| 7 | Discussion and limitations |
| 8 | Conclusion |

---

## Key Outputs

After running the notebook, the `figures/` folder will contain:

- `fig1_case_counts.png` -- Case distribution per diagnosis
- `fig2_age_by_diagnosis.png` -- Age box plot per diagnosis
- `fig3_malignant_by_age_group.png` -- Benign vs Malignant-like by age group
- `fig4_diagnosis_by_sex.png` -- Sex split per diagnosis
- `fig5_diagnosis_by_location.png` -- Top-7 body sites per diagnosis
- `fig6_heatmap_dx_location.png` -- Diagnosis x localization heatmap
- `fig7_class_breakdown.png` -- Overall class breakdown (pie + bar)
- `fig8_dxtype_by_diagnosis.png` -- Confirmation method per diagnosis
- `fig9_confusion_matrices.png` -- ML model confusion matrices
- `fig10_feature_importance.png` -- Random Forest feature importances

---

## Research Questions

1. Are patient age, sex, and body localization associated with lesion diagnosis type?
2. Does melanoma show distinct demographic patterns compared to benign lesions?
3. Can clinical metadata alone provide meaningful signal for early risk screening?

---

## Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn
- scipy, scikit-learn
- jupyter

See `requirements.txt` for the full list.

---

## Source

Dataset: HAM10000 -- Tschandl P., Rosendahl C., Kittler H. (2018). *The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions.* Scientific Data.
