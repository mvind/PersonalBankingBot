import json

def uploadJson(dict):

    try:
        with open('lon_data_db.json', 'a') as db_file:
            #json_data = json.load(db_file)
            #print(list(json_data.values()))
            print('appending new values')

    except FileNotFoundError: # Create new file if none is found
        with open('lon_data_db.json', 'w') as db_file:
            json.dump(dict, db_file, indent=4,ensure_ascii=False)
        print(dict, 'has succesfully been stored as JSON')
