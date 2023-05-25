import pandas as pd
from dateutil.parser import parse
from data_type import DataType

class CSVManager:

    def readCsv(self, path, data_type):
        data_batch = []
        if(data_type == DataType.DEPARTMENTS or data_type == DataType.HIRED_EMPLOYEES or data_type == DataType.JOBS):
            dataframe = pd.read_csv(path, header=None)
            dataframe = dataframe.dropna(how='any')
            dataframe = self.cleanData(dataframe, data_type)
            data_batch = self.toList(dataframe)
        else:
            raise Exception("Unknown DataType")
        return data_batch
      

    def cleanData(self, dataframe, data_type):
        if(data_type == DataType.HIRED_EMPLOYEES):
            dataframe[2] = pd.to_datetime(dataframe[2], format='%Y-%m-%dT%H:%M:%SZ')
            dataframe[3] = dataframe[3].astype(int)
            dataframe[4] = dataframe[4].astype(int)
            print(dataframe)
        return dataframe
            
    
    def toList(self, df):
        data = []
        for i, row in df.iterrows():
            data.append(tuple(row))
        print(data)
        return data
