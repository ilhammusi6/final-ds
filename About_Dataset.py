import pandas as pd
import streamlit as st

import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.header('Analisa Dan Prediksi Tarif Taxi')
st.write('**Pelatihan Data Science 1.0** - dibimbing')
st.write('Jakarta , 4 Januari 2026')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['About Dataset', 
                            'Dashboards', 
                            'Machine Learning',
                            'Prediction App',
                            'Contact Me'])

with tab1:
    import about
    about.about_dataset()

with tab2:
    import visualisasi
    visualisasi.chart()

with tab3:
    import machine_learning
    machine_learning.ml_model()

with tab4:
    import prediction
    prediction.prediction_app()

with tab5:
    import kontak
    kontak.contact_me()

