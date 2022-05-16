import pandas

col_names = ['Gtm', 'H', '2B', '3B', 'HR']
#data = pandas.read_csv('SamplePlayerData.csv', usecols=col_names) #Creates dataframe with given columns

#print (data)


#doubles = data.2B.tolist()

def to_song(file_name): 
    print("This is file name:", file_name)
    data = pandas.read_csv(file_name, usecols=col_names) #Creates dataframe with given columns
    note_list = [] #List to hold the musical note keys

    for i, row in data.iterrows():
        #if HR is not 0 return 4
        if row[4] != 0:
            note_list.append(4)
        elif row[3] != 0:
            note_list.append(3)
        elif row[2] != 0:
            note_list.append(2)
        elif row[1] != 0:
            note_list.append(1)
        else:
            note_list.append(0)
    
    return note_list



    
