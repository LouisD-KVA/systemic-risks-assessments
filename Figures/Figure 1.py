from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

OUTPUT_STEM = "figure1_risk_lens_method_revised"

RISK_LENS_COLORS = {
    "Societal": "#0072B2",
    "Strategic": "#E69F00",
    "Insurance": "#CC79A7",
    "Enterprise": "#009E73",
}

METHOD_MARKERS = {
    "Survey": "o",
    "Horizon scan": "D",
    "Foresight": "^",
}

assessments = {
    "UN": {
        "xy": (0.18, 0.16),
        "risk_lens": "Societal",
        "methods": ["Survey", "Foresight"],
        "label_offset": (0.07, 0.09),
    },
    "WEF": {
        "xy": (-0.43, -0.34),
        "risk_lens": "Societal",
        "methods": ["Survey", "Foresight"],
        "label_offset": (-0.05, -0.13),
    },
    "STI": {
        "xy": (-0.39, 0.36),
        "risk_lens": "Strategic",
        "methods": ["Foresight"],
        "label_offset": (-0.13, 0.08),
    },
    "EY": {
        "xy": (0.74, 0.52),
        "risk_lens": "Strategic",
        "methods": ["Horizon scan"],
        "label_offset": (0.07, 0.08),
    },
    "EUR": {
        "xy": (-0.92, 0.18),
        "risk_lens": "Strategic",
        "methods": ["Foresight"],
        "label_offset": (-0.13, 0.09),
    },
    "SONAR": {
        "xy": (0.93, -0.18),
        "risk_lens": "Insurance",
        "methods": ["Horizon scan"],
        "label_offset": (0.10, -0.07),
    },
    "AXA": {
        "xy": (-1.02, -0.52),
        "risk_lens": "Societal",
        "methods": ["Survey"],
        "label_offset": (-0.16, 0.04),
    },
    "ALZ": {
        "xy": (-0.84, -0.84),
        "risk_lens": "Enterprise",
        "methods": ["Survey"],
        "label_offset": (-0.08, -0.06),
    },
    "AON": {
        "xy": (-0.52, -1.07),
        "risk_lens": "Enterprise",
        "methods": ["Survey"],
        "label_offset": (-0.02, -0.11),
    },
    "PRO": {
        "xy": (-0.17, -1.03),
        "risk_lens": "Enterprise",
        "methods": ["Survey"],
        "label_offset": (0.08, -0.01),
    },
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "figure.dpi": 160,
})

fig, ax = plt.subplots(figsize=(11.5, 9.5))

outer = Circle(
    (0, 0), 1.25,
    facecolor="#E1E5EA",
    edgecolor="#9A9A9A",
    linewidth=1.2,
    zorder=0,
)
middle = Circle(
    (0, 0), 0.82,
    facecolor="#F0ECE2",
    edgecolor="#9A9A9A",
    linewidth=1.2,
    zorder=1,
)
inner = Circle(
    (0, 0), 0.40,
    facecolor="#E1ECE5",
    edgecolor="#9A9A9A",
    linewidth=1.2,
    zorder=2,
)

for patch in [outer, middle, inner]:
    ax.add_patch(patch)

ax.plot([-1.48, 1.48], [0, 0], color="#707070", linewidth=1.2, zorder=3)

ax.text(
    -1.52, 0,
    "Rankings",
    ha="right",
    va="center",
    fontsize=18,
    fontweight="bold",
)
ax.text(
    1.52, 0,
    "Diagnostic",
    ha="left",
    va="center",
    fontsize=18,
    fontweight="bold",
)

ax.text(
    0, 1.08,
    "Commercial and advisory",
    ha="center",
    va="center",
    fontsize=16,
    color="#303030",
)
ax.text(
    0, 0.62,
    "Multistakeholder\nand nonprofit",
    ha="center",
    va="center",
    fontsize=15,
    color="#303030",
)
ax.text(
    0, 0.06,
    "Public",
    ha="center",
    va="center",
    fontsize=15,
    color="#303030",
)

method_offsets = {
    1: [(0.0, 0.0)],
    2: [(-0.035, 0.0), (0.035, 0.0)],
    3: [(-0.052, 0.0), (0.0, 0.0), (0.052, 0.0)],
}

for code, info in assessments.items():
    x, y = info["xy"]
    color = RISK_LENS_COLORS[info["risk_lens"]]
    methods = info["methods"]

    for (dx, dy), method in zip(method_offsets[len(methods)], methods):
        ax.scatter(
            x + dx,
            y + dy,
            s=230,
            marker=METHOD_MARKERS[method],
            facecolor=color,
            edgecolor="white",
            linewidth=1.2,
            zorder=6,
        )

    lx, ly = info["label_offset"]
    ax.text(
        x + lx,
        y + ly,
        code,
        fontsize=16,
        fontweight="bold",
        ha="left" if lx >= 0 else "right",
        va="center",
        color="#222222",
        zorder=7,
    )

risk_handles = [
    Line2D(
        [0], [0],
        marker="o",
        linestyle="None",
        markerfacecolor=color,
        markeredgecolor=color,
        markersize=10,
        label=label,
    )
    for label, color in RISK_LENS_COLORS.items()
]

method_handles = [
    Line2D(
        [0], [0],
        marker=METHOD_MARKERS[method],
        linestyle="None",
        markerfacecolor="#666666",
        markeredgecolor="#666666",
        markersize=10,
        label=method,
    )
    for method in ["Survey", "Horizon scan", "Foresight"]
]

risk_legend = ax.legend(
    handles=risk_handles,
    title="Risk lens",
    loc="lower left",
    bbox_to_anchor=(0.04, -0.17),
    frameon=False,
    fontsize=12,
    title_fontsize=14,
)
ax.add_artist(risk_legend)

ax.legend(
    handles=method_handles,
    title="Method",
    loc="lower right",
    bbox_to_anchor=(0.96, -0.17),
    frameon=False,
    fontsize=12,
    title_fontsize=14,
)

ax.set_xlim(-1.92, 1.92)
ax.set_ylim(-1.30, 1.36)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()

for ext in ["png", "pdf", "svg"]:
    kwargs = {"bbox_inches": "tight"}
    if ext == "png":
        kwargs["dpi"] = 300
    plt.savefig(f"{OUTPUT_STEM}.{ext}", **kwargs)

plt.tight_layout()
plt.savefig("Figure_1_SRA.png", dpi=1000)  # Save the combined image
plt.show()
