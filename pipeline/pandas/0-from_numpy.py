#!/usr/bin/env python3
"""
Numpy array'den pandas DataFrame oluşturan modül
"""
import pandas as pd


def from_numpy(array):
    """
    Bir numpy.ndarray'den pd.DataFrame oluşturur
    """
    # Kolon sayısını al
    num_cols = array.shape[1]
    
    # A, B, C gibi harfleri kolon ismi olarak oluştur (26 kolona kadar)
    col_names = [chr(i) for i in range(ord('A'), ord('A') + num_cols)]
    
    # DataFrame oluştur ve döndür
    return pd.DataFrame(array, columns=col_names)
