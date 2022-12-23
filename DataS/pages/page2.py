
import streamlit as st
import pandas as pd
import altair as alt
sal = pd.read_csv('salary.csv')
st.title('Data Science Job Salaries')
jtype = st.selectbox("Select the job type to know in which country avilable with its averag salary in USD",
                     sal['job_title'].unique())
s8=alt.Chart(sal[sal['job_title']==jtype]).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="salary_in_usd", type="quantitative"),
    color=alt.Color(field="country", type="nominal"),
)
st.altair_chart(s8)

exlevel=st.radio("Select experience level to know the type of job with average of salary",sal['experience_level'].unique())
p9 = alt.Chart(sal[sal['experience_level']==exlevel]).mark_line(color='red').encode(
    x = 'job_title',
    y ='mean(salary_in_usd)',
    tooltip = ['salary_in_usd','salary']
).interactive()
st.altair_chart(p9)

usd=st.button('convert salary currency to USD ')
if usd:
   s5=alt.Chart(sal).mark_bar().encode(x='country',y='salary_in_usd',color='country',
    tooltip=['country','salary_currency']).properties(height=500,width=1200)
else:
   s5=alt.Chart(sal).mark_bar().encode(x='country',y='salary',color='country',
    tooltip=['country','salary_currency']).properties(height=500,width=1500)
st.altair_chart(s5)


ex1=st.checkbox("Show this Chart based on level of experience")
if ex1:
 s4=alt.Chart(sal).mark_rect().encode(x='country',y='salary_in_usd',color='experience_level')
else:
 s4=alt.Chart(sal).mark_rect().encode(x='country',y='salary_in_usd')
st.altair_chart(s4)


