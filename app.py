import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.title('Welcome to streamlit test')

df = pd.DataFrame({
    'name':['Vishal', 'Lalit', 'Krushna', 'Dhananjay'],
    'roll':[22,33,53,47]
})

st.write(df)

name = st.text_input('Enter your name :')
if name:
    st.write(f'Wecome {name} to streamlit test.')
    
a = st.text_input('Do you want to see graph of above dataset table? (yes/no)')
if a == 'yes':
    fig = plt.figure(figsize=(12,6))
    plt.bar(df['name'], df['roll'])
    st.pyplot(fig)
elif a=='no':
    st.write('Ok thanks!!')