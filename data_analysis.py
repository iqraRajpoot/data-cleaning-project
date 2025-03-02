import numpy as np
import pandas as pd
import os


class data_cleaner:

    def __init__(self, path, data_name):
        self.path = path
        self.data_name = data_name
        
    def data_cleaner_func(self, path, data_name):

        if not os.path.exists(path):
            print("path is not valid")
            return

        else:
            # checking file path
            if path.endswith('.csv'):
                print('file type is csv')
                data = pd.read_csv(path, encoding_errors= 'ignore')
            elif path.endswith('.xlsx'):
                print('file type is xlsx')
                data = pd.read_excel(path)

            else:
                print('unknown file type')
                return

        # total number of rows and columns in the ds

        print(data.head())
        rows = data.shape[0]
        print("total rows: ", rows)
        colmns = data.shape[1]
        print("total colmns: ", colmns)

        # checking for duplocatess
        duplicate = data.duplicated()  #it will show you the duplicate data in true and false for each row
        print(f"duplicate data is: {duplicate}")
        # total number of duplicate records
        total_duplictes = data.duplicated().sum()
        print(f"total duplicates: {total_duplictes}")
        # show duplicated records in a ds
        if total_duplictes >0:
            duplicated_records = data[data.duplicated()]
            print(f"duplicated records {duplicated_records}")
            # saving these records into csv
            without_duplicates = duplicated_records.to_csv(f'{data_name}_duplicates.csv', index=None )

        dropping_dup = data.drop_duplicates()
        print(f"clean data: {dropping_dup}")

        missing_value = data.isnull().sum().sum()
        print(f"missing value: {missing_value}")
        missing_val_clmns = data.isnull().sum()
        print(f"missing value records {missing_val_clmns}")

        # droping_by_col = data.dropna(subset='branch')
        # print(f"dropping_by_col {droping_by_col}")

        columns = data.columns

        for col in columns:
            # print(f"columns name: {data[col]} and type is: {data[col].dtype}")
            if data[col].dtype in (int, float):
                data[col] = data[col].fillna(data[col].mean())
                if data[col].dtype == float:
                    data[col] = data[col].round().astype('Int64')
                print(f'filling by colmns: {data[col]}')
            else:
                data.dropna(subset = col, inplace = True)

        print('dataset is ready to test!!!')
        print(f"num of rows: {data.shape[0]} number of cols: {data.shape[1]}")
        data.to_csv(f'{data_name} cleaned_data.csv', index = None)
        print('data is ready!!!')



if __name__ == "__main__":

    path = input("Please enter dataset path :")
    data_name = input("Please enter dataset name :")
    class_ins = data_cleaner(path, data_name)
    output = class_ins.data_cleaner_func(path, data_name)
    print(output)
  