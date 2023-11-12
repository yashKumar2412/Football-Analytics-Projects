import pandas as pd

def format_data(csv_file):
    
    df = pd.read_csv(csv_file)
    
    df['GF_Home_P90'] = round(df['GF_Home'] / df['MP_Home'], 2)
    df['GA_Home_P90'] = round(df['GA_Home'] / df['MP_Home'], 2)
    df['GF_Away_P90'] = round(df['GF_Away'] / df['MP_Away'], 2)
    df['GA_Away_P90'] = round(df['GA_Away'] / df['MP_Away'], 2)

    df['xG_Home_P90'] = round(df['xG_Home'] / df['MP_Home'], 2)
    df['xGA_Home_P90'] = round(df['xGA_Home'] / df['MP_Home'], 2)
    df['xG_Away_P90'] = round(df['xG_Away'] / df['MP_Away'], 2)
    df['xGA_Away_P90'] = round(df['xGA_Away'] / df['MP_Away'], 2)
    
    df = df.drop(['Team', 'GF_Home', 'GA_Home', 'xG_Home', 'xGA_Home', 'GF_Away', 'GA_Away', 'xG_Away', 'xGA_Away'], axis=1)
    
    return df