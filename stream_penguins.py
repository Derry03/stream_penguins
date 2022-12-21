import pickle
import numpy as np
import streamlit as st
from PIL import Image

model = pickle.load(open("penguins_model.sav", "rb"))

add_title = st.sidebar.header("Meet the penguins:")
with st.sidebar:
    subheader = st.caption(
        "Untuk mengetahui Spesies Pinguin di kepulauan Palmer Archipelago (Antarctica). Kita harus tau Berapa panjang & kedalaman culmen? Culmen adalah punggung atas paruh burung (definisi dari Bahasa Oxford).")
    image = Image.open("culmen.jpg")
    st.image(image, caption='Culmen Pinguin', width=300)

# Judul
st.title("KLASIFIKASI SPESIES PINGUIN PALMER ARCHIPELAGO (ANTARTICA)")
st.header("Tugas UAS Business Intelligence")

tab1, tab2 = st.tabs(["Dashboard", "About"])

with tab1:
    pulau = st.radio(
        'Nama Pulau di Kepulauan Palmer Archipelago (Antarctica)', ('Torgersen', 'Dream', 'Biscoe'))
    if (pulau == 'Torgersen'):
        island = '2'
    elif (pulau == 'Dream'):
        island = '1'
    else:
        island = '0'
    culmen_length_mm = st.text_input('Panjang Culmen (mm)')
    culmen_depth_mm = st.text_input('Kedalaman Culmen (mm)')
    flipper_length_mm = st.text_input('Panjang Sirip (mm)')
    body_mass_g = st.text_input('Indeks Masa Tubuh')
    jk = st.selectbox('Jenis Kelamin', ("FEMALE", "MALE"))
    if (jk == 'FEMALE'):
        sex = '1'
    else:
        sex = '2'

    penguins_klasi = ''

    if st.button('SPESIES PINGUIN'):
        udara_prediction = model.predict(
            [[island, culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g, sex]])

        if (udara_prediction == 0):
            penguins_klasi = 'INI ADALAH SPESIES ADELIE'
        elif (udara_prediction == 1):
            penguins_klasi = 'INI ADALAH SPESIES CHINSTRAP'
        else:
            penguins_klasi = 'INI ADALAH SPESIES GENTOO'

    st.success(penguins_klasi)

with tab2:
    st.header("About")

    st.subheader("NIM    : 191351018")
    st.subheader("Nama  : Derry Asari Nuryadi")
    st.subheader("Kelas  : Malam B")
    image = Image.open("penguins.jpg")
    st.image(image, caption='Pinguin Palmer Archipelago (Antarctica)', width=500)
