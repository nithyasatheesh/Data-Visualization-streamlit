import streamlit as st


st.title("welcome")
st.header("Data visualization")
st.subheader("Types of Charts/Graphs")
st.info(" Information of Data visualization. Create different kind of charts using streamlit ")
st.warning(" come on time")

## error message
st.error(" wrong password")

st.write("Employee name")  # display the text along with the code
st.write(range(50))

#markdown
st.markdown("#### Different charts") # markdown or section
#emoji of moon
st.markdown(":moon:")

#text
st.text("New learners")

# to write a caption
st.caption("Caption is here")

# display a mathematical expression
st.latex(r'''a+b x^2+c''')

# create image
st.image("unext.png")

#widget
# checkbox
st.checkbox('login')

#button
st.button('click')

#radio widget
st.radio('pick your gender',["Male","Female","Other"])

# select box -for selecting single box
st.selectbox("pick your course",['Python','Cloud','ML','Cyber security'])

#multi select
st.multiselect("choose the dept",['Sales','Marketing','Analytics'])

# select slider
st.select_slider("Rating",["Bad","Good","Excellent","Fair"])

# slider -pick any number
st.slider("Enter your number",0,30)

# want to display number
st.number_input("pick a number",0,100)

# display text input
st.text_input("Enter email address")

# date input
st.date_input("Opening ceremony")

# time input widget
st.time_input("Hey what's the timing?")

#text area
st.text_area("Welcome to UNext website")

#upload any file # upto 250 mb
st.file_uploader("upload your file")
# choosing color
st.color_picker("color")

# track record (progress)
st.progress(90)

#spinner
import time as t
with st.spinner("just wait"):
    t.sleep(3)

#balloon
st.balloons()

#sidebar elemetns pin to the left
st.sidebar.title('welcome to UNext')
st.sidebar.text_input("Mail address")
st.sidebar.text_input("password")
st.sidebar.button("submit")

# Data visualization

import pandas as pd
import numpy as np
st.title("Bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)

#line chart

st.title("Line chart")
st.line_chart(data)

#area chart
st.title("Area chart")
st.area_chart(data)

#st.pydeck_chart (data)
#st.map(data)