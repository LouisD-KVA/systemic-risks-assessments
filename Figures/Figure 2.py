from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch

# ============================================================
# OUTPUT
# ============================================================

OUTPUT_STEM = "figure2_standalone"

# ============================================================
# CONSTANTS
# ============================================================

ORDER = ["WEF", "UN", "EY", "STI", "SONAR", "EUR", "AXA", "ALZ", "AON", "PRO"]

# Okabe-Ito colour-blind-safe palette
HORIZON_COLORS = {
    "Short (0-2 years)": "#E69F00",   # orange
    "Medium (2-5 years)": "#009E73", # bluish green
    "Long (>5 years)": "#0072B2",     # blue
    "N/A": "#B3B3B3",        # grey
}

# ============================================================
# PANEL A DATA: HORIZONS BY EDITION
# ============================================================

horizon_rows = [
    ["WEF",2006,1,0,1], ["WEF",2007,1,0,1], ["WEF",2008,1,0,1], ["WEF",2009,1,0,1],
    ["WEF",2010,1,0,1], ["WEF",2011,0,0,1], ["WEF",2012,0,0,1], ["WEF",2013,0,0,1],
    ["WEF",2014,0,0,1], ["WEF",2015,0,0,1], ["WEF",2016,0,0,1], ["WEF",2017,0,0,1],
    ["WEF",2018,0,0,1], ["WEF",2019,0,0,1], ["WEF",2020,1,0,1], ["WEF",2021,1,0,1],
    ["WEF",2022,1,0,1], ["WEF",2023,1,0,1], ["WEF",2024,1,0,1], ["WEF",2025,1,0,1],
    ["WEF",2026,1,0,1],

    ["UN",2024,1,1,1],

    ["EY",2019,1,0,0], ["EY",2020,1,0,0], ["EY",2021,1,0,0], ["EY",2022,1,0,0],
    ["EY",2023,1,0,0], ["EY",2024,1,0,0], ["EY",2025,1,0,0], ["EY",2026,1,0,0],

    ["STI",2017,1,0,0], ["STI",2018,1,0,0], ["STI",2019,1,0,0], ["STI",2020,1,0,0],
    ["STI",2021,1,0,0], ["STI",2022,1,0,0], ["STI",2023,1,0,0], ["STI",2024,1,0,0],
    ["STI",2025,1,0,0], ["STI",2026,1,0,0],

    ["SONAR",2013,1,1,0], ["SONAR",2014,1,1,0], ["SONAR",2015,1,1,0], ["SONAR",2016,1,1,0],
    ["SONAR",2017,1,1,0], ["SONAR",2018,1,1,0], ["SONAR",2019,1,1,0], ["SONAR",2020,1,1,0],
    ["SONAR",2021,1,1,0], ["SONAR",2022,1,1,0], ["SONAR",2023,1,1,0], ["SONAR",2024,1,1,0],
    ["SONAR",2025,1,1,0],

    ["EUR",2008,1,0,0], ["EUR",2009,1,0,0], ["EUR",2010,1,0,0], ["EUR",2011,1,0,0],
    ["EUR",2012,1,0,0], ["EUR",2013,1,0,0], ["EUR",2014,1,0,0], ["EUR",2015,1,0,0],
    ["EUR",2016,1,0,0], ["EUR",2017,1,0,0], ["EUR",2018,1,0,0], ["EUR",2019,1,0,0],
    ["EUR",2020,1,0,0], ["EUR",2021,1,0,0], ["EUR",2022,1,0,0], ["EUR",2023,1,0,0],
    ["EUR",2024,1,0,0], ["EUR",2025,1,0,0], ["EUR",2026,1,0,0],

    ["AXA",2014,np.nan,np.nan,np.nan], ["AXA",2015,np.nan,np.nan,np.nan],
    ["AXA",2016,np.nan,np.nan,np.nan], ["AXA",2017,np.nan,np.nan,np.nan],
    ["AXA",2018,0,0,1], ["AXA",2019,0,0,1], ["AXA",2020,0,0,1], ["AXA",2021,0,0,1],
    ["AXA",2022,0,0,1], ["AXA",2023,0,0,1], ["AXA",2024,0,0,1], ["AXA",2025,0,0,1],

    ["ALZ",2012,1,0,0], ["ALZ",2013,1,0,0], ["ALZ",2014,1,0,0], ["ALZ",2015,1,0,0],
    ["ALZ",2016,1,0,0], ["ALZ",2017,1,0,0], ["ALZ",2018,1,0,0], ["ALZ",2019,1,0,0],
    ["ALZ",2020,1,0,0], ["ALZ",2021,1,0,0], ["ALZ",2022,1,0,0], ["ALZ",2023,1,0,0],
    ["ALZ",2024,1,0,0], ["ALZ",2025,1,0,0], ["ALZ",2026,1,0,0],

    ["AON",2007,1,0,0], ["AON",2009,1,0,0], ["AON",2011,1,0,0], ["AON",2013,1,0,0],
    ["AON",2015,1,0,0], ["AON",2017,1,0,0], ["AON",2019,1,0,0], ["AON",2021,1,1,0],
    ["AON",2023,1,1,0], ["AON",2025,1,1,0],

    ["PRO",2013,0,1,1], ["PRO",2014,0,1,1], ["PRO",2015,0,1,1], ["PRO",2016,0,1,1],
    ["PRO",2017,0,1,1], ["PRO",2018,0,1,1], ["PRO",2019,0,1,1], ["PRO",2020,0,1,1],
    ["PRO",2021,0,1,1], ["PRO",2022,0,1,1], ["PRO",2023,0,1,1], ["PRO",2024,0,1,1],
    ["PRO",2025,0,1,1], ["PRO",2026,0,1,1],
]

horizons = pd.DataFrame(
    horizon_rows,
    columns=[
        "Code",
        "Edition year",
        "Short horizon (0-2 years)",
        "Medium horizon (2-5 years)",
        "Long horizon (>5 years)",
    ],
)

# ============================================================
# PANEL B DATA: PARTICIPANT TYPES
# ============================================================

participant_data = [
    ["WEF",   1, 0, 1, 0, 0],
    ["UN",    1, 0, 0, 0, 1],
    ["EY",    0, 0, 0, 1, 0],
    ["STI",   0, 0, 0, 1, 0],
    ["SONAR", 0, 0, 0, 1, 0],
    ["EUR",   0, 0, 0, 1, 0],
    ["AXA",   1, 1, 0, 0, 0],
    ["ALZ",   0, 0, 1, 0, 0],
    ["AON",   0, 0, 1, 0, 0],
    ["PRO",   0, 0, 1, 0, 0],
]

participant_columns = ["Assessment", "Experts", "Public", "Business", "Internal", "Officials"]
participants = pd.DataFrame(participant_data, columns=participant_columns)

# ============================================================
# PANEL C DATA: RISK DIMENSIONS
# ============================================================

risk_data = [
    ["WEF",   1, 0, 0, 1, 1, 1],
    ["UN",    1, 0, 0, 1, 1, 1],
    ["EY",    1, 1, 0, 1, 0, 0],
    ["STI",   1, 0, 0, 0, 0, 0],
    ["SONAR", 1, 1, 0, 1, 0, 0],
    ["EUR",   1, 0, 0, 0, 0, 0],
    ["AXA",   0, 0, 0, 1, 1, 0],
    ["ALZ",   0, 0, 0, 0, 0, 0],
    ["AON",   0, 1, 0, 1, 1, 0],
    ["PRO",   0, 0, 0, 1, 0, 0],
]

risk_columns = [
    "Assessment",
    "Hazard",
    "Exposure",
    "Vulnerability",
    "Consequences",
    "Response",
    "Interactions",
]
risk_dimensions = pd.DataFrame(risk_data, columns=risk_columns)

# ============================================================
# PLOT SETTINGS
# ============================================================

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "figure.dpi": 160,
})

def draw_binary_matrix(ax, data, columns, panel_letter, rotation=30):
    """Draw monochrome matrix with filled circles only for positive entries."""
    data = data.set_index("Assessment").loc[ORDER].reset_index()
    categories = columns[1:]

    for row_idx, assessment in enumerate(ORDER):
        y = len(ORDER) - 1 - row_idx
        for col_idx, category in enumerate(categories):
            if int(data.loc[row_idx, category]) == 1:
                ax.scatter(
                    col_idx,
                    y,
                    s=120,
                    marker="o",
                    facecolors="black",
                    edgecolors="black",
                    linewidths=1.1,
                    zorder=3,
                )

    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=rotation, fontsize=11)

    # Center rotated labels above columns
    for label in ax.get_xticklabels():
        label.set_horizontalalignment("center")
        label.set_verticalalignment("bottom")
        label.set_rotation_mode("anchor")

    ax.set_yticks(range(len(ORDER)))
    ax.set_yticklabels(list(reversed(ORDER)))

    ax.xaxis.tick_top()
    ax.tick_params(
        axis="x",
        top=True,
        bottom=False,
        labeltop=True,
        labelbottom=False,
        length=0,
        pad=8,
    )
    ax.tick_params(axis="y", length=0)

    for x in range(len(categories)):
        ax.axvline(x, color="0.84", linewidth=0.9, zorder=0)

    for y in range(len(ORDER)):
        ax.axhline(y, color="0.90", linewidth=0.9, zorder=0)

    ax.set_xlim(-0.55, len(categories) - 0.45)
    ax.set_ylim(-0.5, len(ORDER) - 0.5)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.text(
        -0.12, 1.04, panel_letter,
        transform=ax.transAxes,
        fontsize=15,
        fontweight="bold",
        ha="left",
        va="bottom",
    )

# ============================================================
# FIGURE
# ============================================================

fig = plt.figure(figsize=(14.5, 8.8))

grid = fig.add_gridspec(
    2,
    2,
    width_ratios=[1.8, 1.15],
    height_ratios=[1, 1],
    wspace=0.18,
    hspace=0.42,
)

# ---------------- Panel A ----------------
ax_a = fig.add_subplot(grid[:, 0])

year_min = int(horizons["Edition year"].min())
year_max = int(horizons["Edition year"].max())
years = np.arange(year_min, year_max + 1)
y_positions = {code: len(ORDER) - 1 - idx for idx, code in enumerate(ORDER)}

for _, row in horizons.iterrows():
    code = row["Code"]
    if code not in y_positions or pd.isna(row["Edition year"]):
        continue

    year = int(row["Edition year"])
    y = y_positions[code]

    flags = []
    if pd.notna(row["Short horizon (0-2 years)"]) and int(row["Short horizon (0-2 years)"]) == 1:
        flags.append("Short (0-2 years)")
    if pd.notna(row["Medium horizon (2-5 years)"]) and int(row["Medium horizon (2-5 years)"]) == 1:
        flags.append("Medium (2-5 years)")
    if pd.notna(row["Long horizon (>5 years)"]) and int(row["Long horizon (>5 years)"]) == 1:
        flags.append("Long (>5 years)")
    if not flags:
        flags = ["N/A"]

    width = 0.76
    height = 0.62
    segment_height = height / len(flags)

    for segment_index, flag in enumerate(flags):
        ax_a.add_patch(
            Rectangle(
                (year - width / 2, y - height / 2 + segment_index * segment_height),
                width,
                segment_height,
                facecolor=HORIZON_COLORS[flag],
                edgecolor="white",
                linewidth=0.5,
                zorder=3,
            )
        )

ax_a.set_yticks([y_positions[code] for code in ORDER])
ax_a.set_yticklabels(ORDER)
ax_a.set_xticks(years)
ax_a.set_xticklabels(years, rotation=90)
ax_a.set_xlim(year_min - 0.6, year_max + 0.6)
ax_a.set_ylim(-0.75, len(ORDER) - 0.25)
ax_a.set_xlabel("Edition year")

ax_a.grid(axis="x", color="0.90", linewidth=0.7, zorder=0)
ax_a.tick_params(axis="both", length=0)

for spine in ax_a.spines.values():
    spine.set_visible(False)

ax_a.text(
    -0.03, 1.015, "A",
    transform=ax_a.transAxes,
    fontsize=15,
    fontweight="bold",
    ha="left",
    va="bottom",
)

legend_handles = [
    Patch(facecolor=HORIZON_COLORS[label], edgecolor="none", label=label)
    for label in HORIZON_COLORS
]

ax_a.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.115),
    ncol=4,
    frameon=False,
    fontsize=10.5,
    handlelength=1.8,
    columnspacing=1.6,
)

# ---------------- Panel B ----------------
ax_b = fig.add_subplot(grid[0, 1])
draw_binary_matrix(ax_b, participants, participant_columns, "B", rotation=30)

# ---------------- Panel C ----------------
ax_c = fig.add_subplot(grid[1, 1])
draw_binary_matrix(ax_c, risk_dimensions, risk_columns, "C", rotation=30)

fig.subplots_adjust(
    left=0.055,
    right=0.995,
    top=0.91,
    bottom=0.13,
)

# ============================================================
# SAVE
# ============================================================

for ext in ["png", "pdf", "svg"]:
    kwargs = {"bbox_inches": "tight"}
    if ext == "png":
        kwargs["dpi"] = 300
    fig.savefig(f"{OUTPUT_STEM}.{ext}", **kwargs)


plt.tight_layout()
plt.savefig("Figure_2_SRA.png", dpi=1000)  # Save the combined image
plt.show()
