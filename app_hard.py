import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

st.header('Datos de Vehiculos en EUA.')

build_histogram = st.checkbox('Construir Histograma')
build_scatter = st.checkbox('Construir Diagrama de Dispersion')

if build_histogram:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches.')
    fig = go.Figure(data=[go.Histogram(x=car_data['cylinders'])])
    fig.update_layout(title_text='Distribución del numero de cilindros')

    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches.')
    fig = go.Figure(data=[go.Scatter(x=car_data['cylinders'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Diagrama de Dispersion del Numero de Cilindros vs Precio', xaxis_title='Numero de Cilindros', yaxis_title='Precio')

    st.plotly_chart(fig, use_container_width=True)