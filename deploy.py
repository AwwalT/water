import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('potable.pkl', 'rb'))

# A function that will process the user input
def material_prediction(input_data):
    
    # converted to array
    input_data_array = np.asarray(input_data)
    # reshape the so the model will understand it
    input_data_reshaped = input_data_array.reshape(1, -1)

    # Getting a prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return("This material is not Portable")
    else:
        return("This material is Portable")
    
def main():
    # giving the app a title
    st.title('Portable material testing App')

    ph = st.number_input('ph_level')
    Hardness = st.number_input('Hardness_level')
    Solids = st.number_input('Solids_level')
    Chloramines = st.number_input('Ch_level')
    Sulfate = st.number_input('Sulphate_level')
    Conductivity = st.number_input('Conductivity')
    Organic_carbon = st.number_input('Organic_level')
    Trihalomethanes = st.number_input('Tri_level')
    Turbidity = st.number_input('Tur_level')

    # code for prediction
    performance = ''

    # creating a button for prediction
    if st.button('Eligibility Result'):
        performance = material_prediction([float(ph), float(Hardness), float(Solids),
                                            float(Chloramines), float(Sulfate), float(Conductivity), float(Organic_carbon),
                                            float(Trihalomethanes), float(Turbidity)])
        st.success(performance)
if __name__ == '__main__':
    main()
