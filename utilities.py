from plotnine import theme, element_text, element_line, element_rect, element_blank

dgrey = "black"
lgrey = "black"

rcDict = {
    'figure.figsize':(9,6),
    'axes.labelsize':14, 
    'axes.facecolor':'white', # color of plotting area
    'axes.edgecolor':lgrey,
    
    'xtick.bottom':True,      'ytick.left':True, 
    'xtick.major.size':3,     'ytick.major.size':3,
    'xtick.major.pad':2,      'ytick.major.pad':2,
    'xtick.color':lgrey,      'ytick.color':lgrey,
    'xtick.labelcolor':lgrey, 'ytick.labelcolor':lgrey,
    
    'xaxis.labellocation':'center', 
    'yaxis.labellocation':'center',
    
    'axes.titlesize':18,
    'axes.titleweight':'bold', 
    'axes.titlelocation':'left',
    'axes.linewidth':1.5,
    'axes.titlepad':8,
    
    'axes.grid.which':'major', 
    'grid.color':'1',
    'grid.alpha':1,
    'grid.linestyle':'dashed',
    'grid.linewidth':0.75,
    
    'legend.borderaxespad':0.75,
    'legend.borderpad':0.75, 
    'legend.columnspacing':10,
    'legend.edgecolor':lgrey, 
    'legend.facecolor':'1',
    'legend.fancybox':False,
    'legend.frameon':True,
    'legend.framealpha':0.65,
    'legend.handleheight':0.75,
    'legend.handlelength':0,
    'legend.handletextpad':1,
    
    'legend.labelcolor':dgrey,
    'legend.labelspacing':0.2,
    'legend.markerscale':1, 
    'legend.title_fontsize':14, 
    'legend.fontsize':12,

    'figure.dpi':100
    }


pltRows = ['P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
pltCols = [str(x).zfill(2) for x in list(range(1, 25))]


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

adobe = ['#0fb5ae', '#4046ca', '#f68511', '#de3d82', 
         '#7e84fa', '#72e06a', '#147af3', '#7326d3', 
         '#e8c600', '#cb5d00', '#008f5d', '#bce931']

custom = ['#9467bd', '#7fd7c1', '#e88b00', '#d9739e', 
         '#68b0cf', '#008f5d', '#d13e38', '#2777b4', 
         '#72e06a', '#9f765e', '#008f5d', '#bce931']

mode20 = ['#9473ae', '#f19900', '#37b067', '#d15d58', '#6296bc', 
          '#85ccba', '#f7cf4a', '#376c72', '#d48ad4', '#9f765e', 
          '#c7c1d1', '#ffc097', '#bbe2ad', '#808080', '#b7e0e6',
          '#cef2df', '#eedebe', '#7db8b9', '#ebc7e8', '#dac1b1',
          ]

mode20b= ['#8a6cae', '#f7cf4a', '#76ccb6', '#d15d58', '#6296bc', 
          '#f19900', '#37b067', '#376c72', '#a84680', '#a17b64', 
          '#c5b3e8', '#bbe2ad', '#ffac97', '#cef2df', '#d48ad4',
          '#7db8b9', '#d4bbac', '#b7e0e6', '#ebcae8', '#eedebe',
          ]


gemstone = ['#bcc7ee', '#8263b1', '#6fe3d4', '#00c7ad', 
         '#f19900', '#c75e0c', '#b1abb4', '#8b6f8b', 
         '#96bbba', '#4b877a']

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

dark = (style + theme(
    text              = element_text(color = '#ABB2BF'),
    axis_text         = element_text(color = '#ABB2BF'),
    axis_ticks_major  = element_line(color = '#ABB2BF'),
    panel_border      = element_rect(fill = '#ABB2BF', color = 'grey', size = 1),
    panel_grid_major  = element_blank(),
    panel_grid_minor  = element_blank(),
    plot_background   = element_rect(fill = '#292c33'),
    panel_background  = element_rect(fill = '#1e2125'),
    legend_background = element_blank(),
    strip_background  = element_blank()
    )
    )



# import patchworklib as pw
# from plotnine import *
# from plotnine.data import *

# g1 = (ggplot(mtcars) + geom_point(aes("mpg", "disp")) + utl.style + theme(figure_size=[3,3]))
# g2 = (ggplot(mtcars) + geom_boxplot(aes("gear", "disp", group = "gear")) + utl.style + theme(figure_size=[3,3]))
# g3 = (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + stat_smooth(method='lm') + facet_wrap('~gear'))
# g4 = (ggplot(data=diamonds) + geom_bar(mapping=aes(x="cut", fill="clarity"), position="dodge"))

# g1 = pw.load_ggplot(g1, figsize=(2,3))
# g2 = pw.load_ggplot(g2, figsize=(2,3))
# g3 = pw.load_ggplot(g3, figsize=(3,3))
# g4 = pw.load_ggplot(g4, figsize=(5,2))

##g1234 = (g1|g2)
##g1234.savefig()

##print(g1, g2)