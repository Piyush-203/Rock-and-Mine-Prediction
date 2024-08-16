import streamlit as st
import numpy as np
import pickle as pk

# loading the saved model
file = open('model.pkl', 'rb')

model = pk.load(file)


st.title("Rock vs Mine Prediction")

st.write("This is a simple web application that predicts whether a rock is a mine or not based on the input")

# input features from the user
input = st.text_input("Enter the 60 features :",'')

if input:
    try:
        # Convert the input data from string to tuple
        input_data_tuple = eval(input)
        
        # Ensure the input is in the correct format
        if isinstance(input_data_tuple, tuple) and len(input_data_tuple) == 60:
            # Convert the tuple to a NumPy array and reshape it
            numpy_input = np.asarray(input_data_tuple)
            reshaped_input = numpy_input.reshape(1, -1)

            # Predict the result
            prediction = model.predict(reshaped_input)

            # Output the result
            if prediction[0] == 'R':
                st.success('The object is a Rock')
            else:
                st.error('The object is a Mine')
        else:
            st.error('Please enter exactly 60 values in the tuple.')
    
    except:
        st.error('Invalid input format. Please enter a tuple.')