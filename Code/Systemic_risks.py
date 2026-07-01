import math
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

frameworks = [
    ("UN",    45, 0.36, "hybrid survey",    "mixed"),
    ("STI",  150, 0.62, "expert foresight", "abductive"),
    ("WEF",  205, 0.68, "survey+foresight", "mixed"),
    ("EUR",  193, 0.76, "expert foresight", "abductive"),
    ("EY",   338, 0.88, "horizon scan",     "abductive"),
    ("SONAR",322, 0.80, "horizon scan",     "abductive"),
    ("AXA",  226, 0.92, "survey",           "inductive"),
    ("ALZ",  244, 0.90, "survey",           "inductive"),
    ("AON",  258, 0.92, "survey",           "inductive"),
    ("PRO",  273, 0.94, "survey",           "inductive"),
]

df = pd.DataFrame(frameworks, columns=["Code", "theta", "radius", "Method", "Epistemology"])
df["x"] = df["radius"] * df["theta"].apply(lambda t: math.cos(math.radians(t)))
df["y"] = df["radius"] * df["theta"].apply(lambda t: math.sin(math.radians(t)))

label_offsets = {
    "UN":    ( 0.06,  0.03),
    "STI":   (-0.07,  0.03),
    "WEF":   (-0.08, -0.01),
    "EUR":   (-0.09,  0.00),
    "EY":    ( 0.07,  0.02),
    "SONAR": ( 0.08, -0.01),
    "AXA":   (-0.07, -0.03),
    "ALZ":   (-0.02, -0.09),
    "AON":   ( 0.02, -0.10),
    "PRO":   ( 0.06, -0.08),
}

method_colors = {
    "survey": "#4C78A8",
    "hybrid survey": "#B07AA1",
    "survey+foresight": "#9C755F",
    "expert foresight": "#F28E2B",
    "horizon scan": "#E15759",
}
epistemology_markers = {
    "inductive": "o",
    "abductive": "D",
    "mixed": "s",
}

fig, ax = plt.subplots(figsize=(7.6, 8.0))
ax.set_aspect("equal")
ax.axis("off")

# Shaded rings: draw outer to inner
ax.add_patch(Circle((0, 0), 1.00, facecolor="#E9EEF5", edgecolor="none", alpha=0.75, zorder=0))
ax.add_patch(Circle((0, 0), 0.66, facecolor="#F3EEE8", edgecolor="none", alpha=0.92, zorder=0))
ax.add_patch(Circle((0, 0), 0.33, facecolor="#EDF1EA", edgecolor="none", alpha=0.95, zorder=0))

# Ring outlines
for r, lw, color in [(1.0, 1.0, "0.78"), (0.66, 0.9, "0.80"), (0.33, 0.9, "0.82")]:
    ax.add_patch(Circle((0, 0), r, fill=False, edgecolor=color, linewidth=lw, zorder=1))

# Ranked-diagnostic axis
ax.plot([-1.08, 1.08], [0, 0], color="0.55", linewidth=1.0, zorder=1)

# Axis and ring labels
ax.text(-1.13, 0, "Ranked", ha="right", va="center", fontsize=11.5, rotation=90)
ax.text(1.13, 0, "Diagnostic", ha="left", va="center", fontsize=11.5, rotation=270)
ax.text(0, 0.15, "Public", ha="center", va="center", fontsize=10)
ax.text(0, 0.50, "Think-tank /\nhybrid", ha="center", va="center", fontsize=9.5)
ax.text(0, 0.83, "Private", ha="center", va="center", fontsize=10)

# Points and labels
for _, row in df.iterrows():
    ax.scatter(
        row["x"], row["y"],
        s=155,
        marker=epistemology_markers[row["Epistemology"]],
        color=method_colors[row["Method"]],
        edgecolor="white",
        linewidth=0.9,
        zorder=3
    )

for _, row in df.iterrows():
    dx, dy = label_offsets[row["Code"]]
    ha = "left" if dx >= 0 else "right"
    ax.text(row["x"] + dx, row["y"] + dy, row["Code"], fontsize=10.5, ha=ha, va="center")

ax.set_xlim(-1.24, 1.24)
ax.set_ylim(-1.12, 1.12)

# Legends
method_order = ["survey", "hybrid survey", "survey+foresight", "expert foresight", "horizon scan"]
method_handles = [
    ax.scatter([], [], s=120, marker="o", color=method_colors[m], edgecolor="white", linewidth=0.8)
    for m in method_order
]
leg1 = ax.legend(
    method_handles, method_order,
    title="Method",
    loc="lower center", bbox_to_anchor=(0.5, -0.12),
    ncol=3, frameon=False, fontsize=9.0, title_fontsize=9.5,
    handletextpad=0.55, columnspacing=1.4
)
ax.add_artist(leg1)

epi_order = ["inductive", "abductive", "mixed"]
epi_handles = [
    ax.scatter([], [], s=120, marker=epistemology_markers[e], color="0.45", edgecolor="white", linewidth=0.8)
    for e in epi_order
]
ax.legend(
    epi_handles, epi_order,
    title="Epistemology",
    loc="lower center", bbox_to_anchor=(0.5, -0.21),
    ncol=3, frameon=False, fontsize=9.0, title_fontsize=9.5,
    handletextpad=0.65, columnspacing=1.8
)

png = "institutional_global_risk_frameworks_circle_shaded.png"
pdf = "institutional_global_risk_frameworks_circle_shaded.pdf"
svg = "institutional_global_risk_frameworks_circle_shaded.svg"
csv = "institutional_global_risk_frameworks_circle_shaded_coordinates.csv"
fig.savefig(png, dpi=300, bbox_inches="tight")
fig.savefig(pdf, bbox_inches="tight")
fig.savefig(svg, bbox_inches="tight")
df.to_csv(csv, index=False)

plt.show()
print(f"Saved PNG: {png}")
print(f"Saved PDF: {pdf}")
print(f"Saved SVG: {svg}")
print(f"Saved CSV: {csv}")