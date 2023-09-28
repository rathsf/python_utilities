from plotnine import theme, element_text, element_line, element_rect, element_blank

dgrey = "0.2"
lgrey = "0.65"

rcDict = {
    "figure.figsize": (9, 6),
    "axes.labelsize": 14,
    "axes.facecolor": "white",  # color of plotting area
    "axes.edgecolor": lgrey,
    "xtick.bottom": True,
    "ytick.left": True,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "xtick.major.pad": 2,
    "ytick.major.pad": 2,
    "xtick.color": lgrey,
    "ytick.color": lgrey,
    "xtick.labelcolor": lgrey,
    "ytick.labelcolor": lgrey,
    "xaxis.labellocation": "center",
    "yaxis.labellocation": "center",
    "axes.titlesize": 18,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.linewidth": 1.5,
    "axes.titlepad": 8,
    "axes.grid.which": "major",
    "grid.color": "1",
    "grid.alpha": 1,
    "grid.linestyle": "dashed",
    "grid.linewidth": 0.75,
    "legend.borderaxespad": 0.75,
    "legend.borderpad": 0.75,
    "legend.columnspacing": 10,
    "legend.edgecolor": lgrey,
    "legend.facecolor": "1",
    "legend.fancybox": False,
    "legend.frameon": True,
    "legend.framealpha": 0.65,
    "legend.handleheight": 0.75,
    "legend.handlelength": 0,
    "legend.handletextpad": 1,
    "legend.labelcolor": dgrey,
    "legend.labelspacing": 0.2,
    "legend.markerscale": 1,
    "legend.title_fontsize": 14,
    "legend.fontsize": 12,
    "figure.dpi": 100,
}


def reorder(df, first_cols=[], last_cols=[]):
    """Move requested columns to the first and last indices"""

    dupes = [value for value in first_cols if value in last_cols]
    if len(dupes) != 0:
        print(f"Heads Up, you requested duplicate colums: {dupes}")

    return df[first_cols + list(df.drop(columns=first_cols + last_cols)) + last_cols]


palD3 = ['#1F77B4FF', '#FF7F0EFF', '#2CA02CFF', '#D62728FF', 
         '#9467BDFF', '#8C564BFF', '#E377C2FF', '#7F7F7FFF', 
         '#BCBD22FF', '#17BECFFF', '#AEC7E8FF', '#FFBB78FF', 
         '#98DF8AFF', '#FF9896FF', '#C5B0D5FF', '#C49C94FF', 
         '#F7B6D2FF', '#C7C7C7FF', '#DBDB8DFF', '#9EDAE5FF']

style = theme(
    text              = element_text(family = 'Droid Sans', size = 10, color = '0.15'),
    title             = element_text(size = 18, face = 'bold'),
    axis_title        = element_text(size = 10, face = 'bold'),
    legend_title      = element_text(size = 12, face = 'bold'),
    axis_text         = element_text(color = 'grey'),
    strip_text        = element_text(face  = 'bold'),
    axis_ticks_major  = element_line(color = 'grey'),
    legend_key        = element_blank(),
    panel_border      = element_rect(fill = 'white', color = 'grey', size = 1),
    panel_grid_major  = element_blank(),
    panel_grid_minor  = element_blank(),
    plot_background   = element_rect(fill = '0.96', color = 'none'),
    panel_background  = element_rect(fill = 'white'),
    legend_background = element_blank(),
    strip_background  = element_blank()
    )

# style_dark = theme(
#     text              = element_text(family = 'Droid Sans', size = 10, color = "#ABB2BF"),
#     title             = element_text(size = 18, face = 'bold'),
#     axis_title        = element_text(size = 10, face = 'bold'),
#     legend_title      = element_text(size = 12, face = 'bold'),
#     axis_text         = element_text(color = 'grey'),
#     strip_text        = element_text(face = 'bold'),
#     axis_ticks_major  = element_line(color = 'grey'),
#     legend_key        = element_blank(),
#     panel_border      = element_rect(fill  = 'white', color = 'grey', size = 1),
#     panel_grid_major  = element_blank(),
#     panel_grid_minor  = element_blank(),
#     plot_background   = element_rect(fill = '#24272e', color = 'none'),
#     panel_background  = element_rect(fill = 'white'),
#     legend_background = element_blank(),
#     strip_background  = element_blank(),
#     )