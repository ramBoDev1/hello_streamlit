import streamlit as st
import pandas as pd
import numpy as np
import time

#1
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
#2
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)
#3
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=(f'col {i+1}' for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))
#4
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [13.757548, 100.517884],
    columns=['lat', 'lon'])
st.map(map_data)
#5
x = st.slider("")  # 👈 this is a widget
st.write(x, 'squared is', x * x)
#6
st.text_input("Your name", key="name")
st.write(st.session_state.name)
#7
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.table(chart_data)
#8
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
st.write('You selected: ', option)
#9
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
#10
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
#11
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
#12
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'