import streamlit as st
import math

def anyBase(n, b=2):
    return '0' if n == 0 else ' '.join(str(n // b ** i % b) for i in range(int(math.log(n, b)), -1, -1))

def fromAnyBase(n, b=2):
    return sum(int(c) * b ** i for i, c in enumerate(reversed(n.split(' '))))

st.title('Base Conversion Tool')

base = st.number_input('Enter base:', min_value=2, value=6)  # Set default base as 6

number = st.text_input('Enter number:', value='123')  # Text field for the number input
if st.button('Convert to Base'):
    try:
        base_string = anyBase(int(number), base)
        st.text_input('Base representation:', value=base_string)  # This field updates with the conversion result
    except Exception as e:
        st.error(f"Error: {str(e)}")

base_string = st.text_input('Enter base string:', value='1 0 1 1 0 1 0 1')  # Text field for the base string input
if st.button('Convert to Integer'):
    try:
        number = fromAnyBase(base_string, base)
        st.text_input('Integer value:', value=str(number))  # This field updates with the conversion result
    except Exception as e:
        st.error(f"Error: {str(e)}")
