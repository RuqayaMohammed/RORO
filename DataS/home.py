
import streamlit as st
import pandas as pd
import altair as alt

sal = pd.read_csv('salary.csv')
st.title('Data Science Job Salaries')
st.write('''This site shows charts of dataset about salaries of jobs in data science domain
the dataset has 11 columns with 607 rows as following: \n
1- work work_year: The year the salary was paid (2020,2021,2022) \n
2- experience_level: The experience level in the job during the year with the following possible values:( EN Entry-level / Junior MI Mid-level / Intermediate SE Senior-level / Expert EX Executive-level) \n
3- employment_type: The type of employement for the role:( PT Part-time FT Full-time CT Contract FL Freelance) \n
4- job_title: The role worked in during the year there are 50 types\n
5- salary: The total gross salary amount paid. \n
6- salary_currency: The currency of the salary paid \n
7- salary_in_usd: The salary in USD\n
8- employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code, it has 57 different countries\n
9- remote_ratio:The overall amount of work done remotely, possible values are as follows: 0 No remote work (less than 20%) 50 Partially remote 100 Fully remote (more than 80%) \n       
10- company_location:The country of the employer's main office or contracting branch as an ISO 3166 country code. it has 31 different countries  \n  
11- company_size: The average number of people that worked for the company during the year: S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250 employees (large) \n
  \n 
  Some finding of this dataset are following: \n 
  1- The are positive relation between experience_level and salary. \n
  2- The are positive relation between employee_residence and company_location and number of job types. \n
  3- The height country has company and employees is United States. \n 
  4- The most jobs are Full-time job.\n 
  5- The salary increasing with years. \n \n\n 
  This Map Shows The Location of Company
  ''')
st.map(sal)




