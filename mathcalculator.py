def sum(a,b):
    c=a+b
    return c
def diff(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c

import streamlit as st
import geometry
template = """<div style="background-color:blue;padding:1px;"> 
              <h2 style="color:orange;text-align:center"> Math App</h2>
            
                    </div>"""
st.markdown(template,unsafe_allow_html=True)
st.image("C:/Users/Jayanth/Desktop/background.jpg",width=750)
temp="""<h3 style="color:brown;text-align:center">Math app</h3>"""
st.markdown(temp,unsafe_allow_html=True)
st.title("Math app")
st.sidebar.image("C:/Users/Jayanth/Desktop/flower.jpeg",width = 200)
st.sidebar.title("select your math module")
dropdown=st.sidebar.selectbox("",["dropdown to select","arithmetic","geometry"])
if dropdown=="arithmetic":
    radio_button = st.sidebar.radio("select your choice", ["sum", "difference", "multiplication"])
    x = st.number_input("enter 1st number")
    y = st.number_input("enter 2nd number")
    if radio_button == "sum":
        result_sum = sum(x, y)
        if st.button("get result"):
            st.success("the sum of entered numbers is {}".format(result_sum))
            st.balloons()
    if radio_button == "diiference":
        result_diff = diff(x, y)
        if st.button("get result"):
            st.success("the difference of entered numbers is {}".format(result_diff))
            st.balloons()
    if radio_button == "multiplication":
        result_mul = mul(x, y)
        if st.button("get result"):
            st.success("the multiplication of entered numbers is {}".format(result_mul))
            st.balloons()

if dropdown=="geometry":
    radio_1=st.sidebar.radio("select one",["area_rectangle","area_circle"])
    if radio_1=="area_rectangle":
        len=st.number_input("enter length")
        breadth=st.number_input("enter breadth")
        result=geometry.area_rectangle(len,breadth)
        if st.button("get area"):
            st.success("area of rectangle is {}".format(result))
            st.balloons()
    if radio_1 == "area_circle":
        radius= st.number_input("enter radius")
        result = geometry.area_circle(radius)
        if st.button("get area"):
            st.success("area of circle is {}".format(result))
            st.balloons()
#to create sub links
col1,col2,col3=st.columns(3)
temp="""<h3 style="color:red;text-align:center">About Mathworks </h3>"""
col1.markdown(temp,unsafe_allow_html=True)
#col1.write("this is created by janu")
temp="""<h3 style="color:green;text-align:center">Functions of mathwoks</h3>"""
col2.markdown(temp,unsafe_allow_html=True)
#col2.write("copywrite @janu")
temp="""<h3 style="color:blue;text-align:center">Examples of mathworks</h3>"""
#col3.write("streamlit is  awesome")
col3.markdown(temp,unsafe_allow_html=True)