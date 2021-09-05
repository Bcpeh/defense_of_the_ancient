
def convert_seconds(time):
    ''''
    Converts time from integer to Hour:Minutes:Seconds format
    :param time: integer representation of time in seconds
    :return: time in H:MM:SS format
    '''
    h = time//3600
    sec = time%60
    sec = ['0' + str(sec) if sec < 10 else sec][0]
    if h > 0 :
        time = time%3600
        minutes = time//60
        minutes = ['0' + str(minutes) if minutes < 10 else minutes][0]
        return(str(h)+ ':' + str(minutes)+ ':' + str(sec))
    else:
        return(str(time//60)+ ':' + str(sec))

def calculate_starting_stats(base_stats, base_attribute, additional_values=0,decimal=0):
    '''
    
    '''

    start_stats = base_stats + (base_attribute*additional_values)
    #Round off the value
    if decimal != 0:
        return round(start_stats,decimal)
    else:
        return round(start_stats)

def preprocess_df(df):
    df = df[['hero_id', 'localized_name', 
                        'base_health','base_health_regen', 'base_mana', 'base_mana_regen', 'base_armor',
                        'base_attack_min', 'base_str', 'base_agi','base_int',
                        'str_gain', 'agi_gain', 'int_gain','primary_attr']]
    hero_list = df['localized_name'].tolist()
    target_cols = ['health','health_regen', 'mana', 'mana_regen', 'armor', 
            'attack_min','base_str', 'base_agi','base_int',
            'str_gain', 'agi_gain', 'int_gain']
    df['base_primary_attr'] = df.loc[:,'primary_attr'].apply(lambda row: 'base_' + row)
    df['health']=df.apply(lambda row: calculate_starting_stats(row['base_health'],row['base_str'],20), axis=1)
    df['armor']=df.apply(lambda row: calculate_starting_stats(row['base_armor'],row['base_agi'],(1/6)), axis=1)
    df['health_regen']=df.apply(lambda row: calculate_starting_stats(row['base_health_regen'],row['base_str'],(0.1),1), axis=1)
    df['mana']=df.apply(lambda row: calculate_starting_stats(row['base_mana'],row['base_str'],12), axis=1)
    df['mana_regen']=df.apply(lambda row: calculate_starting_stats(row['base_mana_regen'],row['base_str'],0.05,1), axis=1)
    i = df.columns.get_indexer(df['base_primary_attr'])
    df['attack_min'] = df['base_attack_min'] + df.values[df.index, i]
    df = df.loc[:,('hero_id', 'localized_name', 
                        'health','health_regen', 'mana', 'mana_regen', 'armor',
                        'attack_min', 'base_str', 'base_agi','base_int',
                        'str_gain', 'agi_gain', 'int_gain')]
    df[target_cols] = df[target_cols].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
    df = df.set_index('localized_name')
    df = df.iloc[:,1:]
    df.columns = [word.capitalize() for word in df.columns]
    return hero_list, df