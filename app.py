import streamlit as st

st.title('Unit converter App')
st.markdown('Welcome to the unit converter app! Please select the type of conversion you would like to do from the sidebar.')

conversion_type = st.sidebar.radio('Select the conversion type', ['Temperature', 'Length', 'Weight'])

if conversion_type == 'Temperature':
    st.markdown('## Temperature Converter')
    temp = st.number_input('Enter the temperature in Celsius')
    temp_f = temp * 9/5 + 32
    st.write(f'Temperature in Fahrenheit: {temp_f}')
elif conversion_type == 'Length':
    st.markdown('## Length Converter')
    length = st.number_input('Enter the length in meters')
    length_cm = length * 100
    st.write(f'Length in centimeters: {length_cm}')
elif conversion_type == 'Weight':    
    st.markdown('## Weight Converter')
    weight = st.number_input('Enter the weight in kilograms')
    weight_g = weight * 1000
    st.write(f'Weight in grams: {weight_g}')
        

