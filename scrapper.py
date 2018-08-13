from tabula import read_pdf
import os

def scrape(file_path):
    '''
    This functions take in a loenseddel in .PDF format,
    and extracts all salary data, and returns a list object with the information.
    '''
    text_data = []
    df =read_pdf(file_path, output_format='json')

    # First get each sub list in data list.
    for i in range(len(df[0]['data'])):
        data_table = df[0]['data'][i]

        # For each sub data list extract text element
        for j in range(len(data_table)):
            try:
                if data_table[j]['text'] == '':
                    break
                #print(data_table[j]['text'])
                text_data.append(data_table[j]['text'])
            except:
                print('Error in text')

    return text_data

    
scrape('lonseddel.PDF')
