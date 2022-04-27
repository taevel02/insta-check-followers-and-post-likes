import pandas as pd
import numpy as np

if __name__ == '__main__':
    f = open('candidates.txt', 'r')
    candidates = f.read().split(', ')

    df = pd.DataFrame([[candidate] for candidate in candidates])
    print(df)
    df.to_excel('candidates.xlsx', index=False, header=False)
