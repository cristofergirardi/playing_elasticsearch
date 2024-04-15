import pandas as pd
import numpy as np
import math
from common.sentences import get_random_text

class JsonRead:
    
    def __init__(self):
        self.file_path = './files/biggerfile.json'
        self.companies = set()
        self.employees = pd.DataFrame()

    def read_file(self):
        self.employees = pd.read_json(self.file_path)
        list_age = []
        list_phrase = []
        list_companies = []
        self.employees.drop("website", axis=1, inplace=True)
        for index, row in self.employees.iterrows():             
            companies_name = row["email"].split("@")[1].split(".")[0]
            self.companies.add(companies_name)
            list_age.append(self.generate_random_age(30,70))
            list_phrase.append(get_random_text())
            list_companies.append(companies_name)

        self.employees["age"] = list_age
        self.employees["phrase"] = list_phrase
        self.employees["company_name"] = list_companies
            

    def get_companies(self):
        return self.companies
    
    def get_employees(self):
        return self.split_df_chunks(self.employees,1000)
    
    def generate_random_age(self, min_age, max_age):
        return np.random.randint(min_age, max_age)
    
    def split_df_chunks(self, data_df,chunk_size):
        total_length     = len(data_df)
        total_chunk_num  = math.ceil(total_length/chunk_size)
        normal_chunk_num = math.floor(total_length/chunk_size)
        chunks = []
        for i in range(normal_chunk_num):
            chunk = data_df[(i*chunk_size):((i+1)*chunk_size)]
            chunks.append(chunk)
        if total_chunk_num > normal_chunk_num:
            chunk = data_df[(normal_chunk_num*chunk_size):total_length]
            chunks.append(chunk)
        return chunks
