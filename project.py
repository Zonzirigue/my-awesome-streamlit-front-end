import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


with header:
	st.title('Welcome to my awesome data science project')
	st.text('in this project i look into the transaction of taxi in NYC. ...')


with dataset:
	st.header('NYC taxi dataset')
	st.text('i found this dataset on https://www.nyc.gov')

	taxi_data = pd.read_csv('data/taxi+_zone_lookup.csv')
	st.write(taxi_data.head())


with features:
	st.header('the features i created')

	st.markdown('* **first feature:** I created this feature because of this...')
	st.markdown('* **second feature:** I created this feature because of this...')


with model_training:
	st.header('time to train the model ok')
	st.text('here you get to choose the hyperparameters of the model ')