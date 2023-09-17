dgrey = '0.8'
lgrey = '0.65'

rcDict = {'figure.figsize':(9,6),
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

def reorder(df, first_cols = [], last_cols = []):
    '''Move requested columns to the first and last indices'''
    
    dupes = [value for value in first_cols if value in last_cols]
    if len(dupes) != 0:
        print(f'Heads Up, you requested duplicate colums: {dupes}')
            
    return df[first_cols + list(df.drop(columns = first_cols + last_cols)) + last_cols]
