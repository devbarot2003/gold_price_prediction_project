import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Gold Price Prediction")

data = pickle.load(open('gld_data.pkl', 'rb'))
model = pickle.load(open('regressor.pkl', 'rb'))




spx = st.slider("Select SPX value?", 676, 2900, 1654)
st.write("The selected value of SPX is", spx)


uso = st.slider("Select SPX value?", 7, 118, 31)
st.write("The selected value of SPX is", uso)

slv = st.slider("Select SPX value?", 8, 47, 20)
st.write("The selected value of SPX is", slv)


eu = st.slider("Select SPX value?", 1.0, 1.6, 1.2)
st.write("The selected value of SPX is", eu)

if st.button("Predict Price"):

    query = np.array([spx, uso, slv, eu])

    # query = query.reshape(1,-1)
    # pred = model.predict(query)
    # st.title(pred[0])
    query = query.reshape(1, -1)
    pred = model.predict(query)[0]  # Extract the prediction from the array

    # Format the prediction with three decimal places and add a dollar sign
    formatted_pred = "${:.3f}".format(pred)

    st.title(formatted_pred)

   