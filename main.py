from turtle import onclick
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from app.database import database
from chefboost import Chefboost as chef
from chefboost.training import Training
from chefboost.commons import evaluate
from sklearn import preprocessing
from sklearn import tree
from pathlib import Path
import pydotplus
from IPython.display import Image
import json
import imp
# import chatbot as chatbot


# import chatbot
database = database()
# db = connection.connect(host="localhost", database='chatbot_rj',
#                        user = "root", passwd = "", use_pure = True)
query = "Select * from tbl_data"
df = pd.read_csv("./dataset/dataset7.csv",
                 delimiter="[,;]", engine='python')
df_dump = df.copy()
df_tree = df_dump.copy()
df_gains = df_dump.copy()
df_result = df_dump.copy()
config_gain = {'algorithm': 'ID3'}
config = {'algorithm': 'C4.5'}
le = preprocessing.LabelEncoder()
df_dump['jenis_poli'] = le.fit_transform(df_dump.jenis_poli)
labels_name = ['Bedah', 'Bedah Mulut', 'Bedah Syaraf', 'Bedah Tulang atau Orthopedi', 'Bedah Tumor', 'Bedah Urologi', 'Gigi Spesialis Orthodonti', 'Gigi Spesialis Periodonti', 'Gigi & Mulut', 'Kardiologi atau Jantung', 'Kebidanan & Kadungan', 'Kesehatan Anak', 'Kesehatan Gigi dan Mulut Anak',
               'Kesehatan Jiwa', 'Kulit & Kelamin', 'Mata', 'Paru-paru', 'Penyakit Dalam', 'Rehabilitasi Medik', 'Skin Care', 'Sub Spesialis Bedah Anak', 'Sub Spesialis Bedah Tumor (Onkologi)', 'Sub Spesialis Onkologi Ginekologi', 'Syaraf', 'THT', 'Tumbuh Kembang Anak (REMEDIA)']


def view_dataset():
    df = pd.DataFrame(database.query(), columns=atribut)
    st.dataframe(df.head())


def run_algo():
    df_gains.rename(columns={'jenis_poli': 'Decision'}, inplace=True)
    gains = Training.findGains(df_gains, config_gain)
    st.write(gains)

    model = chef.fit(df_dump.copy(), config=config,
                     target_label='jenis_poli')
    st.write('------------------------')
    # st.write(model)
    st.write('Proses running...')
    st.write('Build Decision Tree...')
    # hasil = evaluate.evaluate(df_gains)
    # st.write(hasil)

    # Main
st.title('Chatbot RJ')
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dataset", "Predict", "Tree"],
    )
if selected == "Dataset":
    st.write(f"Selected {selected}")
    # Define columns table
    atribut = ['id_data', 'jk', 'usia', 'keluhan_1',
               'keluhan_2', 'keluhan_3', 'jenis_poli']

    # View Table Data
    view_dataset()
    col1, col2 = st.columns(2)

    instance_jk = df['jk'].unique()
    instance_usia = df['usia'].unique()
    instance_keluhan1 = df['keluhan_1'].unique()
    instance_keluhan2 = df['keluhan_2'].unique()
    instance_keluhan3 = df['keluhan_3'].unique()
    instance_kelas = df['jenis_poli'].unique()

    with col1:
        st.write('Jumlah data : ', len(database.query()))
        st.write('-----')
        st.write('Jumlah instance tabel jk : ', len(instance_jk))
        st.write('Jumlah instance tabel keluhan_1 : ',
                 len(instance_keluhan1))
        st.write('Jumlah instance tabel keluhan_3 : ',
                 len(instance_keluhan3))
        st.write('-----')
    with col2:
        st.write('Jumlah kelas label : ', len(instance_kelas), ' kelas')
        st.write('-----')
        st.write('Jumlah instance tabel usia : ', len(instance_usia))
        st.write('Jumlah instance tabel keluhan_2 : ',
                 len(instance_keluhan2))
        st.write('-----')

    # st.dataframe(df_dump.head())

    if st.button('Run Training C4.5'):
        st.write('--RESULT--')
        run_algo()


if selected == "Predict":
    st.write(f"Selected {selected}")

    st.dataframe(df_dump.head())

    with st.form("form1", clear_on_submit=True):
        col1, col2 = st.columns(2)

        # ** LOAD MODEL Regression FROM DIRECTORY **
        # model = chef.load_model("/regression/model_Regression.pkl")
        moduleNameReg = "outputs/rules/regression/rules"
        fp, pathname, description = imp.find_module(moduleNameReg)
        myrules = imp.load_module(moduleNameReg, fp, pathname, description)

        with col1:
            jk = st.selectbox(
                'Jenis Kelamin',
                ('Laki-laki', 'Perempuan')
            )
            keluhan_1 = st.text_input(
                'Keluhan 1', max_chars=40, placeholder="ex : 'SAKIT MATA'").upper()
            keluhan_3 = st.text_input(
                'Keluhan 3', max_chars=40, value="TIDAK ADA").upper()
        with col2:
            usia = st.radio(
                "Usia",
                ('dewasa', 'anak')
            )
            keluhan_2 = st.text_input(
                'Keluhan 2', max_chars=40, value="TIDAK ADA").upper()

        submit = st.form_submit_button("OK")
        if submit:
            result = labels_name[int(myrules.findDecision(
                [jk, usia, keluhan_1, keluhan_2, keluhan_3]))]
            st.write("Jenis Kelamin = ", jk, " | ", "Usia = ", usia, " | ", "Keluhan 1 = ",
                     keluhan_1, " | ", "Keluhan 2 = ", keluhan_2, " | ", "Keluhan 3 = ", keluhan_3)
            st.write("Prediction Poli Service = ", result)

    # f.to_excel("./dataset/hasil_pre.xlsx")


if selected == "Tree":
    st.write(f"Selected {selected}")

    with open("./outputs/rules/regression/rule.txt") as file:
        st.code(file.read(), language='python')
