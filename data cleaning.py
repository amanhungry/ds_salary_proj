# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:40:57 2021

@author: ASUS
"""

import pandas as pd
df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing

df = df[df['Salary Estimate'] != "-1"] #its not a numeric data type hence -1 will be treated as a string 

df["hourly"] = df["Salary Estimate"].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0 )

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

minus_phr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary', '').replace(':', ''))

min_salary = minus_phr.apply(lambda x: int(x.split('-')[0]))


max_salary = minus_phr.apply(lambda x: int(x.split('-')[1]) )


avg_salary = (min_salary + max_salary)/2

# Company name text only
df["company_txt"] = df.apply(lambda x:  x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis =1 ) #iterating each over each row by putting axis = 1 it makes sure we are iterating over the columns

# state field

df["job_state"] = df['Location'].apply(lambda x: x.split(',')[1] )    
print(df.job_state.value_counts())

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company
df['age'] = df.Founded.apply(lambda x: x if x <0  else 2020 - x)



# parsing of job description(python ,etc)
#python

df["[python_yn"] =  df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0 ) 

#r-studio
df['R-yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0 ) 

#spark

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower()  else 0 )

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0 )

#excel  
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0 )
    

df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv("salary_data_cleaned.csv", index =False)

aman = pd.read_csv("salary_data_cleaned.csv")

