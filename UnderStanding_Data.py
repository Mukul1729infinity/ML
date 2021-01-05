import pandas as pd
filepath="file_location/filename.csv" # getting the data file from the given location
filedata=pd.read_csv(filepath)        # reading the data from data set
filedata.describe()                   # it will the summary of the whole data set 
filedata.columns                      # it will give the list of column from the data set 
filedata=filedata.dropna(axis=0)      # drop missing value
