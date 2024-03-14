import requests
import pandas as pd

def get_fighter_data(api_endpoint):
    response = requests.get(api_endpoint)
    return response.json()

def add_fighter_ids(df, fighters_data):
    name_to_id = {f"{fighter['FirstName']} {fighter['LastName']}": fighter['FighterId'] for fighter in fighters_data}
    
    df['FighterId'] = None
    
    for index, row in df.iterrows():
        fighter_id = name_to_id.get(row['name'])
        if fighter_id:
            df.at[index, 'FighterId'] = fighter_id
    return df


csv_file_path = 'final_values.csv'

api_endpoint = 'https://api.sportsdata.io/v3/mma/scores/json/Fighters?key=f82ff5c263094c3998543b2108a1d370'

fighters_data = get_fighter_data(api_endpoint)

df = pd.read_csv(csv_file_path)

df_with_ids = add_fighter_ids(df, fighters_data)

df_with_ids.to_csv('final_with_ids.csv', index=False)