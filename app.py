import streamlit as st
import math

def anyBase(n, b=2):
    return '0' if n == 0 else ' '.join(str(n // b ** i % b) for i in range(int(math.log(n, b)), -1, -1))

def fromAnyBase(n, b=2):
    return sum(int(c) * b ** i for i, c in enumerate(reversed(n.split(' '))))

st.title('Base Conversion Tool')

# Input fields
n = st.text_input('Integer Value', '0')
base = st.text_input('Base', '2')

# Button to convert integer to any base
if st.button('To Base'):
    try:
        result = anyBase(int(n), int(base))
        st.text_input('Any Base String', result)
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Button to convert from any base to integer
if st.button('From Base'):
    any_base_string = st.text_input('Any Base String', '')
    try:
        result = fromAnyBase(any_base_string, int(base))
        st.text_input('Integer Value', str(result))
    except Exception as e:
        st.error(f"Error: {str(e)}")
