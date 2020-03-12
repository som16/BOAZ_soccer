import numpy as np
import pandas as pd



#########################
#       READ FILE       #
#########################

def read_file(filename):
    ext = filename.split('.')[1]
    
    if ext in ['txt', 'csv']:
        file = pd.read_csv(filename, header = None, index_col = 0)
    else:
        file = pd.read_excel(filename, header = None, index_col = 0)
        
    drop_n = file.drop(1, axis = 1)
    
    return drop_n



#########################
#     MODIFY FORMAT     #
#########################

def wide2long(filename, div = 'player'):
    data = read_file(filename)
    df = pd.DataFrame()
    
    n = 10 if div =='player' else 4
    
    for i in range(n):
        sav = data.iloc[:, 5*i : 5*i+5]
        savIND = sav.index
        savVAL = sav.values
        
        
    df = df.append(pd.DataFrame(savVAL, columns = ['cx', 'cy', 'w', 'h', 'label']).assign(frame = savIND))
    df = df[['frame','cx', 'cy','label']]
        
    return df




#      MERGE DATA       #
#########################

def full_data(team1, team2, ball):
    t1 = wide2long(team1)
    t2 = wide2long(team2)
    b = wide2long(ball, 'ball')
    
    full = pd.concat([t1, t2, b]).sort_values(by=['label', 'frame'])
    full.index = range(len(full))
    
    return full
