import numpy
import pandas as pd

def get_eccentricity(filename, slice=0):
    post = PostProcess() #rewrite to to work w/o PyMD dependency
    df = post.getDataFrame(filename).loc[slice:,:] 
    print(df)
    ix = df['I1'].to_numpy()
    iy = df['I2'].to_numpy()
    iz = df['I3'].to_numpy()
    return pd.Series(np.sqrt(1 - ((ix + iy - iz) / (-ix + iy + iz)))) # change to write to file, double-check equation --> this equation may be wrong