import pandas as pd
from datetime import datetime
from data_type import DataType
import utils.df_utils as utils

class CSVManager:

    def readCsv(self, path, data_type):
        """
        Read a CSV file and convert it to a data list of the specified data type.

        path: Path to the CSV file.
        data_type: DataType object specifying the csv origin format.

        Returns:
        data_list: List of data in the desired data type.

        Raises:
        Exception: If the data type is unknown.
        """
        if(isinstance(data_type, DataType)):
            df = pd.read_csv(path, header=None)
            data_list = self.dataframeToDataList(df, data_type)
            return data_list
        else:
            raise Exception("Unknown DataType")
        
      
    def dataframeToDataList(self, df, data_type):
            """
            Convert a DataFrame to a data list of the specified data type.

            df: Input DataFrame containing the data.
            data_type: DataType object specifying the csv origin format.

            Returns:
            data_list: List of data in the specified data type.

            """

            # Drop rows with all NaN values from the DataFrame
            df = df.dropna(how='all') 
            
            # Normalize the data in the DataFrame based on the specified data type
            df = self.normalizeData(df, data_type)
            return self.toList(df)

   
    def normalizeData(self, dataframe, data_type):
        """
        Normalize the data in the DataFrame based on the specified data type.

        dataframe: Input DataFrame containing the data.
        data_type: Data type specifying the desired normalization rules.

        Returns:
        dataframe: DataFrame with the normalized data.

        """
        if (data_type == DataType.HIRED_EMPLOYEES):
            # Set a default date of January 1, 2000
            default_date = "2000-01-01T00:00:00Z"

            # Fill missing values in column 1 with empty string
            dataframe[1] = utils.fillStr(dataframe[1], '')

            # Fill missing values in column 2 with default date and convert to datetime format
            dataframe[2] = utils.fillDefault(dataframe[2], default_date)
            dataframe[2] = pd.to_datetime(dataframe[2], format='%Y-%m-%dT%H:%M:%SZ')

            # Fill missing values in column 3 and 4 with zero (integer) using fillInt function from utils
            dataframe[3] = utils.fillInt(dataframe[3], set_int=True)
            dataframe[4] = utils.fillInt(dataframe[4], set_int=True)

        return dataframe
    

    
    def toList(self, df):
        """
        Convert a DataFrame to a list of tuples.

        df: Input DataFrame containing the data.

        Returns:
        data: List of tuples representing the data from the DataFrame.

        """
        data = []
        for i, row in df.iterrows():
            # Convert each row of the DataFrame to a tuple and append it to the data list
            data.append(tuple(row))
        return data
