import argparse
import numpy as np
import pandas as pd

def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

def save_data(data_path, df):
    df.to_csv(data_path.replace('.csv','_processed.csv'), index=False)
    return None

def log_txf(df, cols: list):
    for col in cols:
        df['log_'+col] = np.log(df[col]+1)
    return df

def months_residence(x):
    if x <12:
        return 'less_than_1yr'
    if 12 <= x <24:
        return '1_to_2yr'
    if 24 <=x <36:
        return '2_to_3yr'
    return 'more_than_3yr'

def run(data_path):
    df = load_data(data_path)
    df = log_txf(df, ['yearly_income'])
    save_data(data_path, df)
    return df

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--data_path", type=str)
    args = argparser.parse_args()
    run(args.data_path)