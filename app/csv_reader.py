import pandas as pd

def readcsv(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df