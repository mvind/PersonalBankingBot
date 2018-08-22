from tabula import read_pdf
import tabula
import pandas as pd
import re

# Cols
"""
['Lønseddel for perioden  1. juli - 31. juli 2018', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']
"""
def scrape(file_path):
    """
    This function returns a object containing all important
    salary data.

    ### Example of return object
    {
        // List of data

        'tandsikring': [3029, 32.67] # Data tag and value
        'sunhedsikring': [3064, 86.00]
        .
        .
        .

    }
    """


    # Scrape salary table
    df_raw = read_pdf(file_path, area=(235.13, 34.66, 757.56, 573.25))

    dfparser(df_raw)

def dfparser(df):
    global reObj
    r = df.shape[0]
    c = df.shape[1]
    #df = pd.DataFrame(df)
    for i in range(r):
        row = list(df.iloc[i])

        if i != 0:

            pass
        else:
            # First row is always the meta data for the return object
            reObj['meta'] = row



    print(reObj)



if __name__ == '__main__':
    reObj = {}
    scrape('./resources/lonseddel.PDF')
