from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Patch

recurrence_data = [
    ("Geopolitical instability and state competition", 61.579365, "Geopolitical"),
    ("Cyber risk and digital security", 54.765873, "Technological"),
    ("Governance, regulation and institutional change", 44.166667, "Geopolitical"),
    ("AI and emerging technologies", 45.091270, "Technological"),
    ("Macroeconomic instability and market conditions", 42.083333, "Economic"),
    ("Climate change and Earth-system change", 41.436508, "Environmental"),
    ("Natural resources, water and biodiversity", 37.916667, "Environmental"),
    ("Conflict, violence and security", 33.940476, "Geopolitical"),
    ("Social cohesion, inequality and polarization", 35.238095, "Societal"),
    ("Extreme weather and natural hazards", 32.222222, "Environmental"),
    ("Business interruption, infrastructure and supply chains", 25.694444, "Economic"),
    ("Financial instability, debt and liquidity", 26.011905, "Economic"),
    ("Health, pandemics and biological risks", 26.480159, "Societal"),
    ("Workforce, labour and skills", 23.666667, "Societal"),
    ("Pollution and environmental degradation", 27.154762, "Environmental"),
    ("Energy, commodities and critical materials", 23.083333, "Economic"),
]

annual_share_data = {
    "Edition year": [2007, 2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "Economic":      [60.0, 70.0, 60.0, 40.0, 32.86, 31.71, 39.58, 35.90, 27.50, 14.81, 24.68, 19.23, 26.09, 31.75, 27.71, 22.89, 21.69, 15.00],
    "Environmental": [10.0,  0.0,  0.0, 20.0, 15.71, 17.07, 12.50, 15.38,  8.75, 12.96,  9.09, 17.95, 15.94, 22.22, 18.07, 22.89, 15.66, 16.67],
    "Geopolitical":  [10.0, 10.0, 10.0, 20.0, 18.57, 21.95, 16.67, 17.95, 28.75, 40.74, 37.66, 39.74, 28.99, 12.70, 25.30, 26.51, 28.92, 40.00],
    "Societal":      [20.0, 20.0, 20.0, 20.0, 18.57, 19.51, 18.75, 17.95, 21.25, 16.67, 15.58, 11.54, 17.39, 15.87, 16.87, 10.84, 15.66, 10.00],
    "Technological": [ 0.0,  0.0, 10.0,  0.0, 14.29,  9.76, 12.50, 12.82, 13.75, 14.81, 12.99, 11.54, 11.59, 17.46, 12.05, 16.87, 18.07, 18.33],
}

COLORS = {
    "Economic": "#E69F00",
    "Environmental": "#009E73",
    "Geopolitical": "#CC79A7",
    "Societal": "#D55E00",
    "Technological": "#0072B2",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.labelsize": 12,
    "xtick.labelsize": 10.5,
    "ytick.labelsize": 10.5,
    "figure.dpi": 160,
})

fig = plt.figure(figsize=(14.5, 8.8))
grid = fig.add_gridspec(
    2, 2,
    width_ratios=[1.8, 1.15],
    height_ratios=[1, 1],
    wspace=0.24,
    hspace=0.50,
)

ax_a = fig.add_subplot(grid[:, 0])
recurrence_sorted = sorted(recurrence_data, key=lambda x: x[1], reverse=True)
labels = [r[0] for r in recurrence_sorted]
values = [r[1] for r in recurrence_sorted]
cats = [r[2] for r in recurrence_sorted]
y = np.arange(len(labels))

ax_a.barh(y, values, color=[COLORS[c] for c in cats], edgecolor="none", height=0.72)
ax_a.set_yticks(y)
ax_a.set_yticklabels(labels, fontsize=9.8)
ax_a.invert_yaxis()
ax_a.set_xlabel("Report-balanced recurrence (%)")
ax_a.set_xlim(0, max(values) * 1.10)
ax_a.grid(axis="x", color="0.87", linewidth=0.8)
ax_a.set_axisbelow(True)
ax_a.tick_params(axis="both", length=0)
for spine in ax_a.spines.values():
    spine.set_visible(False)
ax_a.text(-0.10, 1.02, "A", transform=ax_a.transAxes,
          fontsize=15, fontweight="bold", ha="left", va="bottom")

ax_b = fig.add_subplot(grid[0, 1])
years = annual_share_data["Edition year"]
order = ["Economic", "Environmental", "Geopolitical", "Societal", "Technological"]
stack_vals = [annual_share_data[k] for k in order]
stack_colors = [COLORS[k] for k in order]

ax_b.stackplot(years, stack_vals, colors=stack_colors, labels=order, baseline="zero")
ax_b.set_ylim(0, 100)
ax_b.set_xlim(2006.5, max(years))
ax_b.set_ylabel("Share of formal products (%)")
ax_b.set_xlabel("Edition year")
xticks = [2007, 2011, 2014, 2017, 2020, 2023, 2026]
ax_b.set_xticks(xticks)
ax_b.set_xticklabels([str(x) for x in xticks], ha="center")
ax_b.tick_params(axis="x", length=0, pad=6)
ax_b.tick_params(axis="y", length=0, pad=6)
for spine in ax_b.spines.values():
    spine.set_visible(False)
ax_b.text(-0.02, 1.02, "B", transform=ax_b.transAxes,
          fontsize=15, fontweight="bold", ha="left", va="bottom")

legend_handles = [Patch(facecolor=COLORS[k], edgecolor="none", label=k) for k in order]
ax_a.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.075),
    ncol=3,
    frameon=False,
    fontsize=10.5,
    columnspacing=1.2,
    handletextpad=0.5,
)

ax_c = fig.add_subplot(grid[1, 1])
ax_c.set_xticks([])
ax_c.set_yticks([])
for spine in ax_c.spines.values():
    spine.set_visible(False)
ax_c.set_facecolor("white")
ax_c.add_patch(Rectangle((0, 0), 1, 1, transform=ax_c.transAxes,
                         fill=False, edgecolor="0.85", linewidth=0.8, linestyle="-"))
ax_c.text(-0.02, 1.02, "C", transform=ax_c.transAxes,
          fontsize=15, fontweight="bold", ha="left", va="bottom")

fig.subplots_adjust(
    left=0.29,
    right=0.985,
    top=0.94,
    bottom=0.17,
)

plt.savefig("Figure 3.png", dpi=1000)  # Save the combined image
plt.show()

