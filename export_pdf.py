import base64
import os
import markdown
from xhtml2pdf import pisa

md_path = "report.md"
pdf_path = "report.pdf"
figures_dir = "figures"

FIGURES = [
    ("fig1_case_counts.png",           "Figure 1: Case Count per Diagnosis"),
    ("fig2_age_by_diagnosis.png",       "Figure 2: Age Distribution per Diagnosis (Box Plot)"),
    ("fig3_malignant_by_age_group.png", "Figure 3: Benign vs. Malignant-like Proportion by Age Group"),
    ("fig4_diagnosis_by_sex.png",       "Figure 4: Sex Distribution Within Each Diagnosis (%)"),
    ("fig5_diagnosis_by_location.png",  "Figure 5: Diagnosis Count by Top-7 Body Localizations"),
    ("fig6_heatmap_dx_location.png",    "Figure 6: Heatmap - Diagnosis x Body Localization (%)"),
    ("fig7_class_breakdown.png",        "Figure 7: Benign vs. Malignant-like Class Breakdown"),
    ("fig8_dxtype_by_diagnosis.png",    "Figure 8: Diagnosis Confirmation Method per Diagnosis"),
    ("fig9_confusion_matrices.png",     "Figure 9: Confusion Matrices - Melanoma vs. Non-Melanoma Models"),
    ("fig10_feature_importance.png",    "Figure 10: Top-15 Feature Importances (Random Forest)"),
]


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def build_figures_html():
    html = """
<pdf:nextpage />
<h2 style="page-break-before: always;">Appendix: Analysis Figures</h2>
<p style="color:#555; font-size:10pt;">
  All figures below were generated from the HAM10000 cleaned metadata dataset.
  Run <em>skin_lesion_analysis.ipynb</em> to regenerate them.
</p>
<hr/>
"""
    found = 0
    for filename, caption in FIGURES:
        path = os.path.join(figures_dir, filename)
        if not os.path.exists(path):
            html += f'<p style="color:#999; font-style:italic;">{caption} -- (not found, run notebook first)</p>\n'
            continue
        found += 1
        b64 = img_to_base64(path)
        html += f"""
<div style="margin-bottom:24px; text-align:center;">
  <img src="data:image/png;base64,{b64}"
       style="max-width:100%; max-height:500px;" />
  <p style="font-style:italic; color:#444; font-size:9.5pt; margin-top:5px;">{caption}</p>
</div>
<hr style="border-top:1px solid #eee; margin:8px 0 18px 0;"/>
"""
    print(f"Embedded {found}/{len(FIGURES)} figures.")
    return html


# ── Read and convert markdown ──────────────────────────────────────────────────
with open(md_path, encoding="utf-8") as f:
    md_text = f.read()

body_html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc"])
figures_html = build_figures_html()

css = """
@page {
    size: A4;
    margin: 2.5cm 2.2cm 2.5cm 2.2cm;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
}
h1 {
    font-size: 17pt;
    color: #1a1a2e;
    border-bottom: 2px solid #1a1a2e;
    padding-bottom: 5px;
    margin-top: 0;
}
h2 {
    font-size: 13pt;
    color: #16213e;
    border-bottom: 1px solid #aaa;
    padding-bottom: 3px;
    margin-top: 22px;
}
h3 {
    font-size: 11pt;
    color: #0f3460;
    margin-top: 14px;
}
p { margin: 7px 0; }
blockquote {
    background: #f0f4ff;
    border-left: 4px solid #0f3460;
    margin: 10px 0;
    padding: 7px 12px;
    color: #444;
    font-style: italic;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
}
th {
    background-color: #1a1a2e;
    color: white;
    padding: 6px 9px;
    text-align: left;
}
td {
    padding: 5px 9px;
    border: 1px solid #ccc;
}
tr:nth-child(even) td { background: #f5f5f5; }
code {
    background: #f0f0f0;
    padding: 1px 4px;
    font-size: 9.5pt;
    font-family: Courier, monospace;
}
pre {
    background: #f4f4f4;
    padding: 10px;
    font-size: 9pt;
}
hr {
    border-top: 1px solid #ccc;
    margin: 16px 0;
}
"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Skin Lesion Analysis Report</title>
  <style>{css}</style>
</head>
<body>
{body_html}
{figures_html}
</body>
</html>"""

with open(pdf_path, "wb") as out:
    result = pisa.CreatePDF(full_html, dest=out, encoding="utf-8")

if result.err:
    print(f"Error during PDF generation: {result.err}")
else:
    size_kb = os.path.getsize(pdf_path) // 1024
    print(f"PDF saved to: {pdf_path}  ({size_kb} KB)")
