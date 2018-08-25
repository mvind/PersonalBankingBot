from tabula import read_pdf
import tabula, re, datetime, time, regex
import pandas as pd


def listTostr(list):
    'Take all elements for a list and return as one whitespaced str'
    s = ''
    for e in list:
        s += e+' '
    return s

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

    dfparser(df_raw, title='test1.0')

def dfparser(df, **kwargs):
    global reObj
    r = df.shape[0]
    c = df.shape[1]
    #df = pd.DataFrame(df)
    for i in range(r):
        row = list(df.iloc[i])

        if i != 0:
            print(row)
            s = row[0]
            reDict = {}

            # Get id_tag
            try:
                id_tag = re.search(r'^\d{4}',s, re.UNICODE).group(0)
                if id_tag:
                    reDict['id'] = str(id_tag)
            except:
                pass

            # Get description
            try:
                desc_raw = re.split(r'\d',s)

                desc = [l for l in desc_raw if l not in ('.', ',','', ', ', '-')]
                desc = listTostr(desc)
                reDict['desc'] = desc
            except:
                pass

            # Get values
            # 1. Check first element for the row
            # -----------------------------------
            # If ID exclude the first four digits
            if 'id' in reDict:
                try:
                    s = s[4:]
                    data_li = re.findall(r'(\d[0-9.,]+)',s)
                    reDict['value'] = data_li
                except:
                    pass

            elif 'id' not in reDict:
                try:
                    s = str(row[0])
                    data2_li = re.findall(r'(\d[0-9.,]+)',s)
                    reDict['value'] = data2_li
                except:
                    pass

            reObj.update({'r'+str(i): reDict})

            # 2. Check row elements 2-5
            data3_li = []
            for el in row[1:]:
                if str(el) != 'nan':
                    data3_li.append(str(el)) # Gonna be str format anyways after json formating

            try:
                reDict['value']+= data3_li
            except KeyError:
                reDict['value'] = li

        else:
            # First row is always the meta data for the return object
            title = 'undefined' # Default
            title = kwargs['title']
            timestamp = datetime.datetime.today()
            reObj['meta'] = row + [timestamp.isoformat(), title]


    # Use json dump function to return nice formated obj
    print(reObj)



if __name__ == '__main__':
    reObj = {}
    scrape('./resources/lonseddel.PDF')
