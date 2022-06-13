import numpy as np

def sinW(Fs, f, sample):
    x = np.arange(sample)
    y = np.sin(2*np.pi*f*x/Fs)

    return x, y