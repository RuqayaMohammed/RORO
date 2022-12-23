
import streamlit as st
import pandas as pd
import altair as alt
sal = pd.read_csv('salary.csv')
st.title('Data Science Job Salaries')
ur='https://cdn-icons-png.flaticon.com/512/261/261778.png'
s6=alt.Chart(sal).mark_image(url=ur).encode( x='country', size='salary_in_usd', y='salary_in_usd').interactive()
s77=alt.Chart(sal).mark_arc(innerRadius=50).encode( theta=alt.Theta(field="salary_in_usd", type="quantitative"),
color=alt.Color(field="work_year", type="nominal"))

op = st.slider('How many charts do you want to show',0,2,0)
if op == 1: 
   st.altair_chart(s6)
if op == 2 :
  st.altair_chart(s6)
  st.write("chart shows the average of salary in each year")
  st.altair_chart(s77)

  

st.write("chooes the color you want in area chart")
col= st.color_picker('Pick A Color', '#00f900')
ew=alt.Chart(sal).mark_area(color=col).encode(x='job_title',y='mean(salary_in_usd)')
st.altair_chart(ew)

con=st.select_slider("chooes the country to know the avalible job and the average of salary", sal['country'].unique())
s10=alt.Chart(sal[sal['country']==con]).mark_circle().encode(x='job_title', color='job_title',
y='mean(salary_in_usd)',size='mean(salary_in_usd)').interactive()
st.altair_chart(s10)

ye=st.number_input("pick a year (2020,2021,2022) to show employment type and its avreage salary in USD")
base = alt.Chart(sal[sal['work_year']==ye]).encode(
    theta=alt.Theta("work_year:Q", stack=True),
    radius=alt.Radius("work_year:N", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color="employment_type:N",
)
c1 = base.mark_arc(innerRadius=20)
c2 = base.mark_text(radiusOffset=10).encode(text="mean(salary_in_usd):Q")
st.altair_chart(c1+c2)

