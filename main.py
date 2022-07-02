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
config_gain = {'algorithm': 'ID3'}
config = {'algorithm': 'C4.5'}
le = preprocessing.LabelEncoder()
df_dump['jenis_poli'] = le.fit_transform(df_dump.jenis_poli)
labels_name = ['Bedah', 'Bedah Mulut', 'Bedah Syaraf', 'Bedah Tulang atau Orthopedi', 'Bedah Tumor', 'Bedah Urologi', 'Gigi Spesialis Orthodonti', 'Gigi Spesialis Periodonti', 'Gigi & Mulut', 'Kardiologi atau Jantung', 'Kebidanan & Kadungan', 'Kesehatan Anak', 'Kesehatan Gigi dan Mulut Anak',
               'Kesehatan Jiwa', 'Kulit & Kelamin', 'Mata', 'Paru-paru', 'Penyakit Dalam', 'Rehabilitasi Medik', 'Skin Care', 'Sub Spesialis Bedah Anak', 'Sub Spesialis Bedah Tumor (Onkologi)', 'Sub Spesialis Onkologi Ginekologi', 'Syaraf', 'THT', 'Tumbuh Kembang Anak (REMEDIA)']


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
    df = pd.DataFrame(database.query(), columns=atribut)
    st.dataframe(df.head())
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
        df_gains.rename(columns={'jenis_poli': 'Decision'}, inplace=True)
        gains = Training.findGains(df_gains, config_gain)
        st.write(gains)

        model = chef.fit(df_dump.copy(), config=config,
                         target_label='jenis_poli')
        st.write('------------------------')
        # st.write(model)
        st.write('Classification running...')
        st.write('Build Decision Tree...')
        # hasil = evaluate.evaluate(df_gains)
        # st.write(hasil)


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

        x = '''
def findDecision(obj): #obj[0]: jk, obj[1]: usia, obj[2]: keluhan_1, obj[3]: keluhan_2, obj[4]: keluhan_3
	# {"feature": "keluhan_1", "instances": 3292, "metric_value": 3.8164, "depth": 1}
	if obj[2] == 'BATUK':
		# {"feature": "usia", "instances": 194, "metric_value": 0.9381, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 162, "metric_value": 0.1471, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 83, "metric_value": 0.3332, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 49, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 11.26530612244898
				elif obj[0] == 'Perempuan':
					return 11
				else: return 11.0
			elif obj[3] == 'PILEK':
				# {"feature": "jk", "instances": 50, "metric_value": 0.6572, "depth": 4}
				if obj[0] == 'Laki-laki':
					return 11
				elif obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 21, "metric_value": 0.3709, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					elif obj[4] == 'DEMAM':
						return 11
					elif obj[4] == 'HIDUNG TERSUMBAT':
						return 11
					elif obj[4] == 'PANAS':
						return 11
					elif obj[4] == 'SESAK':
						return 11
					else: return 11.0
				else: return 11.619047619047619
			elif obj[3] == 'DEMAM':
				return 11
			elif obj[3] == 'MUNTAH':
				return 11
			elif obj[3] == 'PANAS':
				return 11
			elif obj[3] == 'PUSING':
				return 11
			elif obj[3] == 'KERINGAT DINGIN':
				return 11
			elif obj[3] == 'MAAG':
				return 11
			elif obj[3] == 'ALERGI':
				return 11
			elif obj[3] == 'ASMA':
				return 11
			elif obj[3] == 'DIARE':
				return 11
			elif obj[3] == 'SARIAWAN':
				return 11
			elif obj[3] == 'MIMISAN':
				return 11
			else: return 11.0
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 32, "metric_value": 1.0053, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 23, "metric_value": 0.2626, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 16, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 17
					else: return 14.8125
				elif obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 16
					else: return 17.571428571428573
				else: return 17.571428571428573
			elif obj[3] == 'DEMAM':
				return 17.0
			elif obj[3] == 'FLU':
				return 16.5
			elif obj[3] == 'SESAK':
				return 12.5
			elif obj[3] == 'TELINGA GATAL':
				return 24
			elif obj[3] == 'PUSING':
				return 16
			elif obj[3] == 'RADANG':
				return 24
			else: return 24.0
		else: return 16.125
	elif obj[2] == 'BAPIL':
		# {"feature": "usia", "instances": 172, "metric_value": 0.076, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 10
		else: return 10.0
	elif obj[2] == 'DEMAM':
		# {"feature": "usia", "instances": 159, "metric_value": 0.4661, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 151, "metric_value": 0.2941, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 79, "metric_value": 0.2782, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 52, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 11.25
				elif obj[3] == 'BATUK':
					return 11
				elif obj[3] == 'PILEK':
					return 11
				elif obj[3] == 'BAPIL':
					return 11
				elif obj[3] == 'FLU':
					return 11
				elif obj[3] == 'BINTIK BINTIK':
					return 11
				elif obj[3] == 'MUAL':
					return 11
				elif obj[3] == 'BATUK BERDAHAK':
					return 11
				elif obj[3] == 'BINTIK MERAH':
					return 11
				elif obj[3] == 'MUNTAH':
					return 11
				elif obj[3] == 'PERUT KEMBUNG':
					return 11
				elif obj[3] == 'DIARE':
					return 11
				elif obj[3] == 'KUPING SAKIT':
					return 11
				else: return 11.0
			elif obj[0] == 'Perempuan':
				return 11
			else: return 11.0
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 8, "metric_value": 0.9686, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 1.4059, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					return 13.0
				elif obj[3] == 'LEMAS':
					return 17
				elif obj[3] == 'MUNTAH':
					return 17
				else: return 17.0
			elif obj[0] == 'Perempuan':
				return 17
			else: return 17.0
		else: return 15.5
	elif obj[2] == 'KONTROL KESEHATAN':
		return 11
	elif obj[2] == 'KONTROL HAMIL':
		return 10
	elif obj[2] == 'VAKSIN':
		# {"feature": "usia", "instances": 54, "metric_value": 0.2291, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 10
		else: return 10.0
	elif obj[2] == 'IMM':
		return 11
	elif obj[2] == 'IMUNISASI':
		return 11
	elif obj[2] == 'DIARE':
		# {"feature": "usia", "instances": 46, "metric_value": 2.1551, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 17
		else: return 17.0
	elif obj[2] == 'KONTROL KULIT & KELAMIN':
		return 14
	elif obj[2] == 'GATAL GATAL':
		# {"feature": "usia", "instances": 42, "metric_value": 0.1517, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 27, "metric_value": 0.0477, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 14, "metric_value": 0.0303, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 13, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 14.23076923076923
				elif obj[3] == 'PANU':
					return 14
				else: return 14.0
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 13, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 13, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 13.692307692307692
				else: return 13.692307692307692
			else: return 13.692307692307692
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 15, "metric_value": 0.0633, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 13.1
				else: return 13.1
			elif obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 12.2
				else: return 12.2
			else: return 12.2
		else: return 12.8
	elif obj[2] == 'MATA':
		return 15
	elif obj[2] == 'PANAS':
		return 11
	elif obj[2] == 'KONTROL GIGI DAN MULUT':
		return 12
	elif obj[2] == 'DEMAM ':
		return 11
	elif obj[2] == 'BATUK PILEK':
		# {"feature": "jk", "instances": 30, "metric_value": 0.6553, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "keluhan_2", "instances": 16, "metric_value": 0.2173, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "usia", "instances": 14, "metric_value": 0.0, "depth": 4}
				if obj[1] == 'anak':
					# {"feature": "keluhan_3", "instances": 14, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 11.928571428571429
				else: return 11.928571428571429
			elif obj[3] == 'PANAS':
				return 11
			else: return 11.0
		elif obj[0] == 'Perempuan':
			return 11
		else: return 11.0
	elif obj[2] == 'KONTROL BEDAH':
		return 0
	elif obj[2] == 'SAKIT GIGI':
		# {"feature": "usia", "instances": 27, "metric_value": 1.2745, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 18, "metric_value": 0.1421, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 16, "metric_value": 0.0565, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 11, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 8
					else: return 7.363636363636363
				elif obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 8
					else: return 6.6
				else: return 6.6
			elif obj[3] == 'BENGKAK':
				return 8
			elif obj[3] == 'GUSI BENGKAK':
				return 8
			else: return 8.0
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 9, "metric_value": 0.0658, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 12
					else: return 11.833333333333334
				else: return 11.833333333333334
			elif obj[0] == 'Laki-laki':
				return 12
			else: return 12.0
		else: return 11.88888888888889
	elif obj[2] == 'HAMIL':
		return 10
	elif obj[2] == 'GATAL':
		# {"feature": "usia", "instances": 25, "metric_value": 0.2987, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 17, "metric_value": 0.4775, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 15.3
				else: return 15.3
			elif obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 7, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 14.142857142857142
				else: return 14.142857142857142
			else: return 14.142857142857142
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 8, "metric_value": 0.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 12.5
			elif obj[0] == 'Perempuan':
				return 12.5
			else: return 12.5
		else: return 12.5
	elif obj[2] == 'KONSULTASI KEBIDANAN & KANDUNGAN':
		return 10
	elif obj[2] == 'TAMBAL GIGI':
		# {"feature": "usia", "instances": 24, "metric_value": 1.2518, "depth": 2}
		if obj[1] == 'dewasa':
			return 8
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 6, "metric_value": 0.5479, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 12
			elif obj[0] == 'Perempuan':
				return 10.666666666666666
			else: return 10.666666666666666
		else: return 11.333333333333334
	elif obj[2] == 'MUAL':
		# {"feature": "usia", "instances": 24, "metric_value": 1.6583, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 17
		else: return 17.0
	elif obj[2] == 'MUNTAH':
		# {"feature": "usia", "instances": 22, "metric_value": 1.2498, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 17
		else: return 17.0
	elif obj[2] == 'PUSING':
		# {"feature": "keluhan_2", "instances": 22, "metric_value": 1.9567, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 14, "metric_value": 0.3149, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "jk", "instances": 10, "metric_value": 0.1746, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 8, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 23
					else: return 18.0
				elif obj[0] == 'Laki-laki':
					return 20.0
				else: return 20.0
			elif obj[1] == 'anak':
				return 14.25
			else: return 14.25
		elif obj[3] == 'BURAM':
			return 15
		elif obj[3] == 'SEDANG HAMIL':
			return 10
		elif obj[3] == 'PILEK':
			return 11
		elif obj[3] == 'BINTIK DI KULIT':
			return 11
		elif obj[3] == 'DADA NYERI':
			return 9
		elif obj[3] == 'DEMAM':
			return 17
		elif obj[3] == 'WAJAH KAKU ':
			return 23
		elif obj[3] == 'MUAL':
			return 11
		else: return 11.0
	elif obj[2] == 'BENJOLAN':
		# {"feature": "keluhan_2", "instances": 21, "metric_value": 3.6977, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 5, "metric_value": 2.1396, "depth": 3}
			if obj[1] == 'dewasa':
				return 4.666666666666667
			elif obj[1] == 'anak':
				return 15.5
			else: return 15.5
		elif obj[3] == 'PAYUDARA':
			return 0
		elif obj[3] == 'TANGAN':
			return 0
		elif obj[3] == 'BAHU':
			return 8.5
		elif obj[3] == 'KEPALA':
			return 11
		elif obj[3] == 'GUSI':
			return 1
		elif obj[3] == 'PUNGGUNG':
			return 0
		elif obj[3] == 'BENGKAK':
			return 2
		elif obj[3] == 'KAKI':
			return 0
		elif obj[3] == 'KELENJAR':
			return 0
		elif obj[3] == 'PINGGANG':
			return 0
		elif obj[3] == 'PINGGUL':
			return 0
		else: return 0.0
	elif obj[2] == 'SAKIT PERUT':
		# {"feature": "usia", "instances": 20, "metric_value": 0.2179, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 10
		else: return 10.0
	elif obj[2] == 'CABUT GIGI':
		# {"feature": "jk", "instances": 20, "metric_value": 1.2043, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 14, "metric_value": 0.4946, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 1
					else: return 3.1
				else: return 3.1
			elif obj[1] == 'anak':
				return 7.25
			else: return 7.25
		elif obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 6, "metric_value": 0.5523, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 12
					else: return 11.2
				else: return 11.2
			elif obj[1] == 'dewasa':
				return 8
			else: return 8.0
		else: return 10.666666666666666
	elif obj[2] == 'SESAK':
		# {"feature": "keluhan_2", "instances": 19, "metric_value": 1.0342, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 11, "metric_value": 0.5103, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "jk", "instances": 7, "metric_value": 0.7128, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 9
					else: return 11.8
				elif obj[0] == 'Laki-laki':
					return 9
				else: return 9.0
			elif obj[1] == 'anak':
				return 11
			else: return 11.0
		elif obj[3] == 'PUSING':
			return 12.5
		elif obj[3] == 'BATUK':
			return 14.0
		elif obj[3] == 'PUNGGUNG':
			return 17
		elif obj[3] == 'FLU':
			return 17
		elif obj[3] == 'MUAL':
			return 9
		elif obj[3] == 'KULIT PIPI MERAH':
			return 11
		else: return 11.0
	elif obj[2] == 'ALERGI':
		# {"feature": "keluhan_2", "instances": 19, "metric_value": 1.5697, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 18, "metric_value": 0.4366, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "jk", "instances": 14, "metric_value": 0.613, "depth": 4}
				if obj[0] == 'Laki-laki':
					return 11
				elif obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 14
					else: return 12.714285714285714
				else: return 12.714285714285714
			elif obj[1] == 'dewasa':
				return 14
			else: return 14.0
		elif obj[3] == 'HIDUNG TERSUMBAT':
			return 24
		else: return 24.0
	elif obj[2] == 'KONSULTASI KESEHATAN':
		return 11
	elif obj[2] == 'KONSUL KESEHATAN':
		return 11
	elif obj[2] == 'BATUK ':
		# {"feature": "usia", "instances": 17, "metric_value": 2.6356, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.1172, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 6, "metric_value": 0.0161, "depth": 4}
				if obj[0] == 'Laki-laki':
					return 16.75
				elif obj[0] == 'Perempuan':
					return 16.5
				else: return 16.5
			elif obj[3] == 'BADAN SAKIT':
				return 17
			elif obj[3] == 'DEMAM':
				return 17
			elif obj[3] == 'PILEK':
				return 17
			elif obj[3] == 'SESAK NAFAS':
				return 17
			else: return 17.0
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'PILEK':
		# {"feature": "usia", "instances": 16, "metric_value": 5.6292, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 24
		else: return 24.0
	elif obj[2] == 'SAKIT MATA':
		# {"feature": "usia", "instances": 15, "metric_value": 0.8282, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 11, "metric_value": 0.2831, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 8, "metric_value": 0.0249, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 11.8
				elif obj[0] == 'Perempuan':
					return 12.333333333333334
				else: return 12.333333333333334
			elif obj[3] == 'LEHER IRITASI':
				return 11
			elif obj[3] == 'DEMAM':
				return 11
			elif obj[3] == 'PILEK':
				return 11
			else: return 11.0
		elif obj[1] == 'dewasa':
			return 15
		else: return 15.0
	elif obj[2] == 'KONSUL KANDUNGAN':
		return 10
	elif obj[2] == 'GUSI BENGKAK':
		# {"feature": "jk", "instances": 15, "metric_value": 0.4297, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 12, "metric_value": 0.31, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 8
					else: return 9.5
				else: return 9.5
			elif obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.1715, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 12
					else: return 11.0
				elif obj[3] == 'TAMBAL GIGI':
					return 12
				else: return 12.0
			else: return 11.166666666666666
		elif obj[0] == 'Laki-laki':
			return 8
		else: return 8.0
	elif obj[2] == 'RADANG':
		# {"feature": "usia", "instances": 15, "metric_value": 3.8547, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 21.666666666666668
		else: return 21.666666666666668
	elif obj[2] == 'FLU':
		# {"feature": "usia", "instances": 15, "metric_value": 4.1638, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 11, "metric_value": 0.047, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 8, "metric_value": 0.0245, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 11
					else: return 11.142857142857142
				elif obj[0] == 'Laki-laki':
					return 11
				else: return 11.0
			elif obj[3] == 'BATUK':
				return 11
			elif obj[3] == 'DEMAM':
				return 11
			else: return 11.0
		elif obj[1] == 'dewasa':
			return 22.25
		else: return 22.25
	elif obj[2] == 'DM':
		return 17
	elif obj[2] == 'TB':
		# {"feature": "usia", "instances": 14, "metric_value": 2.4087, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 0.0393, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 16
					else: return 16.2
				else: return 16.2
			elif obj[0] == 'Laki-laki':
				return 16
			else: return 16.0
		else: return 16.166666666666668
	elif obj[2] == 'SAKIT TELINGA':
		# {"feature": "keluhan_2", "instances": 14, "metric_value": 3.348, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 24
		elif obj[3] == 'HIDUNG TERSUMBAT':
			return 24
		elif obj[3] == 'PILEK':
			return 24
		elif obj[3] == 'PUSING':
			return 11
		else: return 11.0
	elif obj[2] == 'KONTROL UROLOGI':
		return 5
	elif obj[2] == 'SAKIT PINGGANG':
		# {"feature": "keluhan_2", "instances": 14, "metric_value": 0.7625, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 12, "metric_value": 0.767, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 8, "metric_value": 0.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 8, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 23
					else: return 20.125
				else: return 20.125
			elif obj[0] == 'Laki-laki':
				return 16.0
			else: return 16.0
		elif obj[3] == 'PUSING':
			return 11
		elif obj[3] == 'MENGGIGIL':
			return 17
		else: return 17.0
	elif obj[2] == 'BEDAH TUMOR':
		return 21
	elif obj[2] == 'KONSUL':
		# {"feature": "keluhan_2", "instances": 12, "metric_value": 2.0566, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 9, "metric_value": 0.8149, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 7, "metric_value": 0.5329, "depth": 4}
				if obj[1] == 'anak':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 25
					else: return 21.666666666666668
				elif obj[1] == 'dewasa':
					return 24
				else: return 24.0
			elif obj[0] == 'Perempuan':
				return 25
			else: return 25.0
		elif obj[3] == 'EVALUASI':
			return 25
		elif obj[3] == 'TERAPI':
			return 25
		elif obj[3] == 'SDH AGAK ENAKAN':
			return 9
		else: return 9.0
	elif obj[2] == 'BATUK PILEK ':
		# {"feature": "usia", "instances": 11, "metric_value": 3.7372, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 24
		else: return 24.0
	elif obj[2] == 'KONSUL KEBIDANAN':
		return 10
	elif obj[2] == 'SARIAWAN':
		# {"feature": "usia", "instances": 11, "metric_value": 3.7372, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 24
		else: return 24.0
	elif obj[2] == 'CACAR':
		# {"feature": "usia", "instances": 11, "metric_value": 0.7216, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 8, "metric_value": 0.9922, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				return 11
			elif obj[3] == 'SARIAWAN':
				return 14
			else: return 14.0
		elif obj[1] == 'dewasa':
			return 14
		else: return 14.0
	elif obj[2] == 'GIGI BERLUBANG':
		# {"feature": "usia", "instances": 11, "metric_value": 1.1786, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 6, "metric_value": 0.336, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 11.0
			elif obj[0] == 'Perempuan':
				return 12
			else: return 12.0
		elif obj[1] == 'dewasa':
			return 8
		else: return 8.0
	elif obj[2] == 'KONSUL KULIT & KELAMIN':
		return 14
	elif obj[2] == 'CEK HAMIL':
		return 10
	elif obj[2] == 'IMUN':
		return 11
	elif obj[2] == 'KONTROL REHAB':
		return 18
	elif obj[2] == 'CEK KANDUNGAN':
		return 10
	elif obj[2] == 'KANDUNGAN':
		return 10
	elif obj[2] == 'PERAWATAN GIGI DAN MULUT':
		return 12
	elif obj[2] == 'KONTROL KANDUNGAN':
		return 10
	elif obj[2] == 'SAKIT KEPALA':
		# {"feature": "usia", "instances": 9, "metric_value": 1.158, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 8, "metric_value": 0.4831, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 7, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 23
					else: return 21.0
				else: return 21.0
			elif obj[0] == 'Laki-laki':
				return 17
			else: return 17.0
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'KONSULTASI KULIT & KELAMIN':
		# {"feature": "usia", "instances": 9, "metric_value": 0.1381, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 0.0286, "depth": 3}
			if obj[0] == 'Perempuan':
				return 13.666666666666666
			elif obj[0] == 'Laki-laki':
				return 13.333333333333334
			else: return 13.333333333333334
		elif obj[1] == 'anak':
			return 14
		else: return 14.0
	elif obj[2] == 'FLEK':
		# {"feature": "usia", "instances": 9, "metric_value": 0.4714, "depth": 2}
		if obj[1] == 'dewasa':
			return 10
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'GIGI':
		# {"feature": "usia", "instances": 9, "metric_value": 0.6302, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 0.588, "depth": 3}
			if obj[0] == 'Perempuan':
				return 6.25
			elif obj[0] == 'Laki-laki':
				return 8
			else: return 8.0
		elif obj[1] == 'anak':
			return 10.666666666666666
		else: return 10.666666666666666
	elif obj[2] == 'USG':
		# {"feature": "jk", "instances": 9, "metric_value": 0.0, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 9, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 9, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 9, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 10
					else: return 9.444444444444445
				else: return 9.444444444444445
			else: return 9.444444444444445
		else: return 9.444444444444445
	elif obj[2] == 'GIGI BERLUBANG ':
		return 8
	elif obj[2] == 'BATUK BERDAHAK':
		# {"feature": "usia", "instances": 9, "metric_value": 3.301, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 20.0
		else: return 20.0
	elif obj[2] == 'JERAWAT':
		return 14
	elif obj[2] == 'KONSUL REHAB':
		return 18
	elif obj[2] == 'GATAL GATAL ':
		return 14
	elif obj[2] == 'PILEK ':
		# {"feature": "usia", "instances": 8, "metric_value": 4.2993, "depth": 2}
		if obj[1] == 'anak':
			return 11
		elif obj[1] == 'dewasa':
			return 24
		else: return 24.0
	elif obj[2] == 'MUNTAH MUNTAH':
		return 11
	elif obj[2] == 'SESAK NAFAS':
		# {"feature": "keluhan_2", "instances": 8, "metric_value": 1.3877, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 2.4154, "depth": 3}
			if obj[0] == 'Perempuan':
				return 10.666666666666666
			elif obj[0] == 'Laki-laki':
				return 16.5
			else: return 16.5
		elif obj[3] == 'ASMA':
			return 16
		elif obj[3] == 'GAMPANG CAPEK':
			return 9
		elif obj[3] == 'SAKIT DADA':
			return 17
		else: return 17.0
	elif obj[2] == 'IMUNISASI ':
		return 11
	elif obj[2] == 'LUKA':
		# {"feature": "keluhan_2", "instances": 7, "metric_value": 3.9144, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 7.0
		elif obj[3] == 'DADA':
			return 14
		elif obj[3] == 'HIDUNG':
			return 11
		elif obj[3] == 'MUKA':
			return 11
		elif obj[3] == 'KETIAK':
			return 14
		elif obj[3] == 'SUNAT':
			return 0
		else: return 0.0
	elif obj[2] == 'MATA BERAIR':
		# {"feature": "usia", "instances": 7, "metric_value": 1.9795, "depth": 2}
		if obj[1] == 'dewasa':
			return 15
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'SAKIT TENGGOROKAN':
		# {"feature": "usia", "instances": 7, "metric_value": 5.8728, "depth": 2}
		if obj[1] == 'dewasa':
			return 24
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'KB':
		return 10
	elif obj[2] == 'NYERI KAKI':
		# {"feature": "keluhan_2", "instances": 7, "metric_value": 3.3838, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 1.0718, "depth": 3}
			if obj[0] == 'Perempuan':
				return 18.0
			elif obj[0] == 'Laki-laki':
				return 23
			else: return 23.0
		elif obj[3] == 'ROBEKAN DI LUTUT':
			return 3
		elif obj[3] == 'MATA PENGLIHATAN KABUR':
			return 9
		else: return 9.0
	elif obj[2] == 'KEHAMILAN':
		return 10
	elif obj[2] == 'MATA MERAH':
		# {"feature": "jk", "instances": 7, "metric_value": 0.8283, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 15
		elif obj[0] == 'Perempuan':
			return 13.0
		else: return 13.0
	elif obj[2] == 'NYERI PERUT':
		# {"feature": "usia", "instances": 7, "metric_value": 1.1493, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 5, "metric_value": 1.4, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 17
			elif obj[0] == 'Perempuan':
				return 13.5
			else: return 13.5
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'LUTUT SAKIT':
		# {"feature": "jk", "instances": 7, "metric_value": 0.1574, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 15.25
		elif obj[0] == 'Perempuan':
			return 12.333333333333334
		else: return 12.333333333333334
	elif obj[2] == 'BAPIL ':
		return 11
	elif obj[2] == 'KONSULTASI':
		# {"feature": "usia", "instances": 7, "metric_value": 1.8332, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 5, "metric_value": 0.2, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 25
			elif obj[0] == 'Perempuan':
				return 24.5
			else: return 24.5
		elif obj[1] == 'dewasa':
			return 19.5
		else: return 19.5
	elif obj[2] == 'PANAS ':
		return 11
	elif obj[2] == 'KEPUTIHAN':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.2526, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 0.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 10
					else: return 11.6
				else: return 11.6
			else: return 11.6
		elif obj[3] == 'KONSUL LANJUTAN':
			return 10
		else: return 10.0
	elif obj[2] == 'PERIKSA MATA':
		return 15
	elif obj[2] == 'KONTROL GIGI':
		# {"feature": "jk", "instances": 6, "metric_value": 0.2761, "depth": 2}
		if obj[0] == 'Perempuan':
			return 7.0
		elif obj[0] == 'Laki-laki':
			return 8
		else: return 8.0
	elif obj[2] == 'KONTROL KAWAT GIGI':
		return 6
	elif obj[2] == 'TELINGA':
		return 24
	elif obj[2] == 'PERAWATAN GIGI':
		# {"feature": "jk", "instances": 6, "metric_value": 0.824, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 8
		elif obj[0] == 'Perempuan':
			return 10.0
		else: return 10.0
	elif obj[2] == 'TELINGA SAKIT':
		return 24
	elif obj[2] == 'NYERI PINGGANG':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 2.2361, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 23
		elif obj[3] == 'KAKI SAKIT':
			return 17
		elif obj[3] == 'SARAF KEJEPIT':
			return 23
		else: return 23.0
	elif obj[2] == 'ASMA':
		# {"feature": "usia", "instances": 6, "metric_value": 2.2113, "depth": 2}
		if obj[1] == 'dewasa':
			return 16.25
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'SAKIT KAKI':
		# {"feature": "usia", "instances": 6, "metric_value": 2.4494, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 5, "metric_value": 1.9144, "depth": 3}
			if obj[0] == 'Perempuan':
				return 6.75
			elif obj[0] == 'Laki-laki':
				return 17
			else: return 17.0
		elif obj[1] == 'anak':
			return 23
		else: return 23.0
	elif obj[2] == 'MATA ':
		return 15
	elif obj[2] == 'MANTOUX':
		return 11
	elif obj[2] == 'RADANG TENGGOROKAN':
		# {"feature": "usia", "instances": 6, "metric_value": 6.1283, "depth": 2}
		if obj[1] == 'dewasa':
			return 24
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'KAKI SAKIT':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 20.0
		elif obj[3] == 'NGILU':
			return 23
		elif obj[3] == 'MUAL':
			return 17
		else: return 17.0
	elif obj[2] == 'KAKI BENGKAK':
		# {"feature": "jk", "instances": 6, "metric_value": 0.6786, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 5, "metric_value": 0.6431, "depth": 3}
			if obj[1] == 'dewasa':
				return 14.0
			elif obj[1] == 'anak':
				return 11
			else: return 11.0
		elif obj[0] == 'Perempuan':
			return 9
		else: return 9.0
	elif obj[2] == 'KONSUL GIGI':
		return 8
	elif obj[2] == 'SINUS':
		return 24
	elif obj[2] == 'BEHEL':
		return 6
	elif obj[2] == 'KEHAMILAN ':
		return 10
	elif obj[2] == 'HAID':
		return 10
	elif obj[2] == 'GIGI PATAH':
		# {"feature": "usia", "instances": 5, "metric_value": 1.9596, "depth": 2}
		if obj[1] == 'dewasa':
			return 8
		elif obj[1] == 'anak':
			return 12
		else: return 12.0
	elif obj[2] == 'NYERI DADA':
		# {"feature": "jk", "instances": 5, "metric_value": 1.6, "depth": 2}
		if obj[0] == 'Perempuan':
			return 9
		elif obj[0] == 'Laki-laki':
			return 13.0
		else: return 13.0
	elif obj[2] == 'PROSTAT':
		# {"feature": "jk", "instances": 5, "metric_value": 0.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 5, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 5
					else: return 7.4
				else: return 7.4
			else: return 7.4
		else: return 7.4
	elif obj[2] == 'CEK MATA':
		return 15
	elif obj[2] == 'ALERGI ':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 1.4697, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 11
		elif obj[3] == 'BATUK':
			return 11
		elif obj[3] == 'WAJAH':
			return 14
		elif obj[3] == 'KULIT':
			return 14
		elif obj[3] == 'GATAL KULIT':
			return 11
		else: return 11.0
	elif obj[2] == 'PERUT SAKIT':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 2.1834, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 10.75
		elif obj[3] == 'DADA SAKIT ':
			return 17
		else: return 17.0
	elif obj[2] == 'NYERI LAMBUNG':
		# {"feature": "usia", "instances": 5, "metric_value": 2.4, "depth": 2}
		if obj[1] == 'dewasa':
			return 17
		elif obj[1] == 'anak':
			return 11
		else: return 11.0
	elif obj[2] == 'DIARE ':
		return 11
	elif obj[2] == 'SAKIT PUNGGUNG':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 1.7367, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 14.333333333333334
		elif obj[3] == 'SAKIT KEPALA':
			return 11
		elif obj[3] == 'SESAK NAFAS':
			return 17
		else: return 17.0
	elif obj[2] == 'SPESIALIS BEDAH':
		return 20
	elif obj[2] == 'DEMAM TINGGI':
		return 11
	elif obj[2] == 'BENJOLAN DI LEHER':
		# {"feature": "jk", "instances": 5, "metric_value": 3.9966, "depth": 2}
		if obj[0] == 'Perempuan':
			return 23.25
		elif obj[0] == 'Laki-laki':
			return 11
		else: return 11.0
	elif obj[2] == 'KONSUL GIGI DAN MULUT':
		return 12
	elif obj[2] == 'SAKIT DADA':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 2.4056, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 9.5
		elif obj[3] == 'BATUK':
			return 17
		else: return 17.0
	elif obj[2] == 'ASAM LAMBUNG':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 3.2, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 17
		elif obj[3] == 'SESAK':
			return 9
		else: return 9.0
	elif obj[2] == 'GATAL ':
		return 13.25
	elif obj[2] == 'LEPAS JAHITAN':
		return 1
	elif obj[2] == 'MAAG':
		return 17
	elif obj[2] == 'SPEECH DELAY':
		return 11
	elif obj[2] == 'USG 4 DIMENSI':
		return 10
	elif obj[2] == 'RUAM':
		return 12.5
	elif obj[2] == 'SAKIT LAMBUNG ':
		return 17
	elif obj[2] == 'TERAPI REHAB':
		return 18
	elif obj[2] == 'BEJOLAN PAYUDARA':
		return 0
	elif obj[2] == 'MENCRET':
		return 11
	elif obj[2] == 'GIGI BOLONG':
		return 10.0
	elif obj[2] == 'THT':
		return 24
	elif obj[2] == 'BERSIHKAN TELINGA':
		return 24
	elif obj[2] == 'TERAPI':
		return 23.25
	elif obj[2] == 'SUSAH BAB':
		return 11
	elif obj[2] == 'TANGAN KESEMUTAN':
		return 18.25
	elif obj[2] == 'TELINGA BERDENGUNG ':
		return 24
	elif obj[2] == 'PASANG KB':
		return 10
	elif obj[2] == 'MATA BENGKAK':
		return 14.0
	elif obj[2] == 'LEMAS':
		return 13.5
	elif obj[2] == 'LAMBUNG':
		return 17
	elif obj[2] == 'HERNIA':
		return 2.75
	elif obj[2] == 'SAKIT':
		return 15.5
	elif obj[2] == 'PERIKSA KANDUNGAN':
		return 10
	elif obj[2] == 'KONTROL KEHAMILAN':
		return 10
	elif obj[2] == 'KONTROL':
		return 9
	elif obj[2] == 'SAKIT MATA ':
		return 15
	elif obj[2] == 'BENGKAK':
		return 10.0
	elif obj[2] == 'ISK':
		return 15.0
	elif obj[2] == 'SUNAT':
		return 0
	elif obj[2] == 'SAKIT BADAN':
		return 12.333333333333334
	elif obj[2] == 'TAMBAL':
		return 8
	elif obj[2] == 'VERTIGO':
		return 23
	elif obj[2] == 'HHD':
		return 9
	elif obj[2] == 'GATAL GATAL SELURUH BADAN':
		return 14.666666666666666
	elif obj[2] == 'RADIOLOGI':
		return 7.333333333333333
	elif obj[2] == 'PARU':
		return 19.0
	elif obj[2] == 'SAKIT LUTUT':
		return 12.333333333333334
	elif obj[2] == 'CHF':
		return 11.666666666666666
	elif obj[2] == 'VAKSIN PCV':
		return 11
	elif obj[2] == 'OBAT HABIS':
		return 9
	elif obj[2] == 'BENTOL BENTOL':
		return 12.0
	elif obj[2] == 'DADA SAKIT':
		return 9
	elif obj[2] == 'DADA NYERI':
		return 11.666666666666666
	elif obj[2] == 'DADA SESAK':
		return 16.666666666666668
	elif obj[2] == 'DERMATITIS':
		return 14
	elif obj[2] == 'LBP':
		return 23
	elif obj[2] == 'VAKSIN DPT':
		return 11
	elif obj[2] == 'AMANDEL':
		return 19.666666666666668
	elif obj[2] == 'KONTROL KEHAMILAN ':
		return 10
	elif obj[2] == 'MIMISAN':
		return 15.333333333333334
	elif obj[2] == 'BENJOLAN ':
		return 15.0
	elif obj[2] == 'SAKIT MAAG':
		return 17
	elif obj[2] == 'VAKSIN ':
		return 11
	elif obj[2] == 'SETELAH LAHIRAN':
		return 11
	elif obj[2] == 'GIGI SAKIT':
		return 8
	elif obj[2] == 'BURAM':
		return 15
	elif obj[2] == 'FISIOTERAPI':
		return 18
	elif obj[2] == 'EVALUASI':
		return 22.666666666666668
	elif obj[2] == 'PAP SMEAR':
		return 10
	elif obj[2] == 'BEDAH SYARAF':
		return 2
	elif obj[2] == 'GATAL-GATAL':
		return 11
	elif obj[2] == 'KONSUL UROLOGI':
		return 5
	elif obj[2] == 'BINTIK MERAH':
		return 11
	elif obj[2] == 'STROKE':
		return 23
	elif obj[2] == 'VAKSIN BCG':
		return 11
	elif obj[2] == 'LUKA BAKAR':
		return 14
	elif obj[2] == 'SARIAWAN ':
		return 11
	elif obj[2] == 'VAKSIN CAMPAK':
		return 11
	elif obj[2] == 'TELINGA BERDENGUNG':
		return 24
	elif obj[2] == 'MERIANG':
		return 13.0
	elif obj[2] == 'PERIKSA GIGI':
		return 7.0
	elif obj[2] == 'KONSUL JANTUNG':
		return 9
	elif obj[2] == 'KENCING SAKIT':
		return 8.0
	elif obj[2] == 'PERIODONTI':
		return 7
	elif obj[2] == 'PASANG BEHEL':
		return 6
	elif obj[2] == 'JARI KAKU':
		return 23
	elif obj[2] == 'KONTROL IUD':
		return 10
	elif obj[2] == 'JATUH':
		return 6.5
	elif obj[2] == 'GAMAU MAKAN':
		return 11
	elif obj[2] == 'PIPI BENGKAK':
		return 16.0
	elif obj[2] == 'REMATOLOGI':
		return 17
	elif obj[2] == 'KATARAK':
		return 15
	elif obj[2] == 'PILEK TERSUMBAT':
		return 24
	elif obj[2] == 'SAKIT BAK':
		return 5
	elif obj[2] == 'KONTROL HAMIL ':
		return 10
	elif obj[2] == 'RUAM DI BAGIAN PANTAT':
		return 11
	elif obj[2] == 'HEMOROID':
		return 0
	elif obj[2] == 'GUSI BERDARAH':
		return 7.5
	elif obj[2] == 'PENGLIHATAN BURAM':
		return 15
	elif obj[2] == 'HERPES':
		return 14
	elif obj[2] == 'NYERI GIGI':
		return 8
	elif obj[2] == 'KONSLULTASI KESEHATAN':
		return 11
	elif obj[2] == 'GIGI GOYANG':
		return 10.0
	elif obj[2] == 'CKD':
		return 17
	elif obj[2] == 'DIABET':
		return 17
	elif obj[2] == 'GATAL KULIT':
		return 14
	elif obj[2] == 'HIPERTENSI':
		return 17
	elif obj[2] == 'RUAM MERAH':
		return 11
	elif obj[2] == 'GATEL GATEL':
		return 14
	elif obj[2] == 'NYERI BAGIAN KAKI':
		return 18
	elif obj[2] == 'HNP':
		return 23
	elif obj[2] == 'IMM DPT':
		return 11
	elif obj[2] == 'GATAL GATAL DI KAKI':
		return 14
	elif obj[2] == 'IMUNIASI':
		return 11
	elif obj[2] == 'HYPERTIROID':
		return 17
	elif obj[2] == 'MUAL MUAL':
		return 17
	elif obj[2] == 'FIMOSIS':
		return 0
	elif obj[2] == 'TIDAK BISA PIPIS':
		return 2.5
	elif obj[2] == 'BATUK SESAK':
		return 11
	elif obj[2] == 'ASAM LAMBUNG NAIK':
		return 17
	elif obj[2] == 'OPERASI':
		return 0
	elif obj[2] == 'TUMBUH GIGI':
		return 11.5
	elif obj[2] == 'TELINGA SAKIT ':
		return 24
	elif obj[2] == 'KONTROL RUTIN':
		return 15.5
	elif obj[2] == 'CABUT JAITAN':
		return 1
	elif obj[2] == 'TELINGA BINDENG':
		return 24
	elif obj[2] == 'KTKA':
		return 18.0
	elif obj[2] == 'MANTUK':
		return 11
	elif obj[2] == 'LAMBUNG SAKIT':
		return 17
	elif obj[2] == 'SINUSITIS':
		return 24
	elif obj[2] == 'ANGKAT IUD':
		return 10
	elif obj[2] == 'MATA BURAM':
		return 15
	elif obj[2] == 'BUANG AIR KECIL NYERI':
		return 11
	elif obj[2] == 'KETERLAMBATAN BICARA':
		return 25
	elif obj[2] == 'BAK TIDAK LANCAR':
		return 5
	elif obj[2] == 'SUSAH BAK':
		return 5
	elif obj[2] == 'BINTIK2 MERAH':
		return 11
	elif obj[2] == 'BAK SAKIT':
		return 11.0
	elif obj[2] == 'TANGAN SAKIT':
		return 19.5
	elif obj[2] == 'KONTROL ULANG':
		return 16.5
	elif obj[2] == 'SAKIT LAMBUNG':
		return 14.0
	elif obj[2] == 'TAMBALAN LEPAS':
		return 8
	elif obj[2] == 'PASCA MELAHIRKAN':
		return 10
	elif obj[2] == 'ANYANG ANYANGAN':
		return 11.0
	elif obj[2] == 'CEK KB':
		return 10
	elif obj[2] == 'TUMIT SAKIT':
		return 10.5
	elif obj[2] == 'KURANG DENGAR':
		return 24
	elif obj[2] == 'SAKIT NELAN':
		return 17.5
	elif obj[2] == 'SAKIT LEHER':
		return 17.0
	elif obj[2] == 'SAKIT PERUT ':
		return 14.0
	elif obj[2] == 'KULIT KERING':
		return 14
	elif obj[2] == 'CEK KESEHATAN':
		return 12.5
	elif obj[2] == 'KULIT MERAH MERAH':
		return 14
	elif obj[2] == 'JAMUR KAKI':
		return 14
	elif obj[2] == 'SAKIT PIPIS':
		return 8.0
	elif obj[2] == 'TUMIT SAKIT ':
		return 20.5
	elif obj[2] == 'CEPAT LELAH':
		return 17
	elif obj[2] == 'DIABETES':
		return 17
	elif obj[2] == 'ABSES':
		return 0.5
	elif obj[2] == 'WASIR':
		return 0
	elif obj[2] == 'EKSIM':
		return 14
	elif obj[2] == 'SAKIT TANGAN':
		return 20.0
	elif obj[2] == 'MASIH SESAK':
		return 9
	elif obj[2] == 'CEK SPIRAL':
		return 10
	elif obj[2] == 'EKSIM ':
		return 14
	elif obj[2] == 'TELINGA MENDENGUNG':
		return 24
	elif obj[2] == 'SAKIT TENGGOROKAN ':
		return 14.0
	elif obj[2] == 'EXIM':
		return 14
	elif obj[2] == 'KONTROL KB':
		return 10
	elif obj[2] == 'NYERI TELINGA KURANG DENGAR':
		return 24
	elif obj[2] == 'NYERI ULUHATI':
		return 17
	elif obj[2] == 'NYERI TULANG EKOR':
		return 3
	elif obj[2] == 'NYERI TELINGA':
		return 24
	elif obj[2] == 'NYERI TULANG BELAKANG':
		return 18
	elif obj[2] == 'MATA KURANG FOKUS':
		return 15
	elif obj[2] == 'NYERI TELINGA KANAN':
		return 24
	elif obj[2] == 'MATA KABUR ':
		return 15
	elif obj[2] == 'MATA AGAK BINTIT':
		return 15
	elif obj[2] == 'ODONTECTOMY':
		return 1
	elif obj[2] == 'MATA MERAH BENGKAK':
		return 15
	elif obj[2] == 'MATA IRITASI':
		return 15
	elif obj[2] == 'MATA BERAIR TERUS':
		return 15
	elif obj[2] == 'OSTEOPOROSIS':
		return 3
	elif obj[2] == 'BADAN SAKIT':
		return 23
	elif obj[2] == 'LUTUT LUKA':
		return 11
	elif obj[2] == 'LUTUT NYERI':
		return 18
	elif obj[2] == 'MAMPET':
		return 24
	elif obj[2] == 'PENAMBALAN GIGI':
		return 12
	elif obj[2] == 'PEMBENGKAKAN JANTUNG':
		return 9
	elif obj[2] == 'PEGAL DI PINGGANG':
		return 9
	elif obj[2] == 'PEGAL':
		return 23
	elif obj[2] == 'MASIH SESAK NAFAS':
		return 9
	elif obj[2] == 'PASCA DEMAM':
		return 11
	elif obj[2] == 'MATA AGAK BENGKAK':
		return 15
	elif obj[2] == 'MATA BELEKAN':
		return 15
	elif obj[2] == 'PASANG KAWAT GIGI':
		return 6
	elif obj[2] == 'MATA KANAN SEPERTI ADA TITIK':
		return 17
	elif obj[2] == 'MATA BERBAYANG':
		return 15
	elif obj[2] == 'PANAS TINGGI':
		return 11
	elif obj[2] == 'PANAS DINGIN':
		return 11
	elif obj[2] == 'PANAS DALAM':
		return 11
	elif obj[2] == 'MATA BURAM ':
		return 15
	elif obj[2] == 'MATA GATAL':
		return 15
	elif obj[2] == 'NYERI TANGAN':
		return 0
	elif obj[2] == 'MATA PERIH':
		return 15
	elif obj[2] == 'NYERI SENDI':
		return 23
	elif obj[2] == 'NYERI KUPING KANAN':
		return 24
	elif obj[2] == 'NYERI DI SELURUH BADAN':
		return 17
	elif obj[2] == 'NYERI DI LUTUT ':
		return 23
	elif obj[2] == 'MENS TIDAK NORMAL':
		return 10
	elif obj[2] == 'MENS TIDAK TERATUR':
		return 10
	elif obj[2] == 'MENSTRUASI SAKIT':
		return 10
	elif obj[2] == 'NYERI DADA KIRI':
		return 9
	elif obj[2] == 'MENSTRUASI TIDAK LANCAR':
		return 10
	elif obj[2] == 'MERAH MERAH':
		return 14
	elif obj[2] == 'NYERI BERKURANG':
		return 18
	elif obj[2] == 'MINUS':
		return 15
	elif obj[2] == 'NYERI BAGIAN PERUT':
		return 5
	elif obj[2] == 'NYERI BAGIAN LUTUT DAN PINGGANG':
		return 23
	elif obj[2] == 'MINUS NAMBAH':
		return 15
	elif obj[2] == 'NYERI BAG LUTUT':
		return 3
	elif obj[2] == 'MSH ADA SESAK NAFAS':
		return 9
	elif obj[2] == 'NYERI BAGIAN DADA':
		return 9
	elif obj[2] == 'MUAL ':
		return 17
	elif obj[2] == 'NYERI BAGIAN BELAKANG':
		return 18
	elif obj[2] == 'NYERI AREA PERUT':
		return 17
	elif obj[2] == 'MUKA KERING':
		return 14
	elif obj[2] == 'MUNTAH DARAH':
		return 11
	elif obj[2] == 'NGILU DI PINGGANG BELAKANG ':
		return 23
	elif obj[2] == 'MUNTAH DIARE':
		return 17
	elif obj[2] == 'NELEN SAKIT':
		return 11
	elif obj[2] == 'NAFAS SESAK':
		return 9
	elif obj[2] == 'MENS BANYAK':
		return 10
	elif obj[2] == 'MENDENGUNG':
		return 24
	elif obj[2] == 'NYERI PUNGGUNG':
		return 23
	elif obj[2] == 'MENCRET TERUS ':
		return 11
	elif obj[2] == 'NYERI PUNDAK':
		return 17
	elif obj[2] == 'NYERI PERUT KIRI':
		return 5
	elif obj[2] == 'NYERI PERUT KANAN BAWAH':
		return 17
	elif obj[2] == 'NYERI PERUT DAN DADA':
		return 17
	elif obj[2] == 'NYERI PERUT BAWAH':
		return 10
	elif obj[2] == 'MATA KELUAR KOTORAN':
		return 11
	elif obj[2] == 'MATA KEMASUKAN DEBU':
		return 15
	elif obj[2] == 'MATA NYERI':
		return 15
	elif obj[2] == 'NYERI PERGELANGAN TANGAN':
		return 11
	elif obj[2] == 'NAFAS BERAT':
		return 9
	elif obj[2] == 'MATA SEBELAH KIRI':
		return 15
	elif obj[2] == 'MATA SEBELAH KIRI SPT ADA MENGGANJAL':
		return 15
	elif obj[2] == 'MATA GAK NYAMAN':
		return 15
	elif obj[2] == 'MATANYA GATAL':
		return 15
	elif obj[2] == 'MAU BUSINASI':
		return 5
	elif obj[2] == 'MAU KB':
		return 10
	elif obj[2] == 'ALAT KELAMIN':
		return 14
	elif obj[2] == 'PERIKSA FESES':
		return 11
	elif obj[2] == 'SKIN CARE ':
		return 19
	elif obj[2] == 'TEST PENDENGARAN':
		return 24
	elif obj[2] == 'NYERI PADA KAKI':
		return 17
	elif obj[2] == 'MAU USG':
		return 10
	elif obj[2] == 'NYERI OTOT KAKI':
		return 23
	elif obj[2] == 'NYERI LUTUT':
		return 17
	elif obj[2] == 'MELEPUH DI WAJAH':
		return 14
	elif obj[2] == 'TERGIGIT':
		return 8
	elif obj[2] == 'RAMBUT RONTOK':
		return 14
	elif obj[2] == 'PENDARAHAN':
		return 10
	elif obj[2] == 'SYARAF KEJEPIT':
		return 23
	elif obj[2] == 'SKOLIOSIS':
		return 3
	elif obj[2] == 'SPONDYLOSIS':
		return 3
	elif obj[2] == 'STERIL GIGI':
		return 12
	elif obj[2] == 'SUKA SESAK ':
		return 17
	elif obj[2] == 'SULIT BAB':
		return 11
	elif obj[2] == 'SULIT NAFAS':
		return 24
	elif obj[2] == 'SUNTIK HEMOFILI':
		return 11
	elif obj[2] == 'SUSAH NELEN':
		return 11
	elif obj[2] == 'SUSP HEPATITIS':
		return 11
	elif obj[2] == 'TAI LALAT DIGARUK BERDARAH':
		return 14
	elif obj[2] == 'TANGAN INFEKSI':
		return 0
	elif obj[2] == 'TAMBAL ':
		return 8
	elif obj[2] == 'TAMBAL GIGI ':
		return 8
	elif obj[2] == 'TAMBAL GIGI BERLUBANG':
		return 12
	elif obj[2] == 'TAMBAL GIGI PERMANEN':
		return 8
	elif obj[2] == 'TAMBAL SAKIT':
		return 8
	elif obj[2] == 'TAMBALAN':
		return 12
	elif obj[2] == 'TAMBALAN GIGI':
		return 8
	elif obj[2] == 'TAMBALAN GIGI GOYANG':
		return 8
	elif obj[2] == 'TAMBALAN GIGI LEPAS ':
		return 8
	elif obj[2] == 'SESEK NAFAS':
		return 11
	elif obj[2] == 'SESAK KALAU PAGI':
		return 16
	elif obj[2] == 'SERUMEN':
		return 24
	elif obj[2] == 'SERING MIMISAN':
		return 24
	elif obj[2] == 'SAKIT SENDI':
		return 17
	elif obj[2] == 'SAKIT TULANG BELAKANG':
		return 23
	elif obj[2] == 'SAKIT TULANG RUSUK':
		return 23
	elif obj[2] == 'SAKIT ULUHATI ':
		return 17
	elif obj[2] == 'HABIS KECELAKAAN':
		return 3
	elif obj[2] == 'SALIT PERUT':
		return 17
	elif obj[2] == 'SCALLING':
		return 8
	elif obj[2] == 'SCHIZOPHRENIA':
		return 13
	elif obj[2] == 'SCIATICA ':
		return 23
	elif obj[2] == 'SCOLIOSIS':
		return 18
	elif obj[2] == 'BINTIK MERAH BAGIAN PERUT':
		return 11
	elif obj[2] == 'DADA KANAN NYERI ':
		return 9
	elif obj[2] == 'MUKA MERAH':
		return 11
	elif obj[2] == 'SEKITARAN KUPING SAKIT':
		return 24
	elif obj[2] == 'SERING JATUH ':
		return 11
	elif obj[2] == 'SERING KELUAR KOTORAN':
		return 15
	elif obj[2] == 'SERING KRAM':
		return 23
	elif obj[2] == 'LEBAM DI TANGAN DAN KAKI':
		return 17
	elif obj[2] == 'SERING MEMEGANG DADA':
		return 11
	elif obj[2] == 'TANGAN LUKA':
		return 11
	elif obj[2] == 'TANGAN KAKU':
		return 17
	elif obj[2] == 'SAKIT SEKITAR BAHU':
		return 17
	elif obj[2] == 'TUMBUH GIGI BARU':
		return 12
	elif obj[2] == 'TIDAK NAFSU MAKAN':
		return 11
	elif obj[2] == 'TINDAKAN':
		return 1
	elif obj[2] == 'TINDAKAN ':
		return 1
	elif obj[2] == 'TINNITUS':
		return 24
	elif obj[2] == 'TREMOR TANGAN DAN KAKI':
		return 17
	elif obj[2] == 'TULANG EKOR':
		return 23
	elif obj[2] == 'TULANG PINGGUL RETAK':
		return 23
	elif obj[2] == 'TULANG RUSUK SAKIT':
		return 11
	elif obj[2] == 'TULANG SAKIT':
		return 3
	elif obj[2] == 'VAKSIN DBD':
		return 11
	elif obj[2] == 'TANGAN KRAM':
		return 17
	elif obj[2] == 'VAKSIN DPT ':
		return 11
	elif obj[2] == 'VAKSIN MR':
		return 11
	elif obj[2] == 'VAKSIN PCV ':
		return 11
	elif obj[2] == 'VASKIN':
		return 11
	elif obj[2] == 'VERUKA VULGARIS':
		return 14
	elif obj[2] == 'VIRUS':
		return 11
	elif obj[2] == 'VISUME':
		return 10
	elif obj[2] == 'WAJAH ADA BRUNTUSAN':
		return 14
	elif obj[2] == 'WAJAH BERUNTUSAN DAN PUTIH ':
		return 14
	elif obj[2] == 'TIDAK MENS':
		return 10
	elif obj[2] == 'TESPEK POSITIF':
		return 10
	elif obj[2] == 'NYERI DI PAYUDARA':
		return 21
	elif obj[2] == 'TENSI TIDAK STABIL':
		return 17
	elif obj[2] == 'TB USUS':
		return 11
	elif obj[2] == 'TIDAK BISA TIDUR':
		return 13
	elif obj[2] == 'TELAT BERBICARA':
		return 25
	elif obj[2] == 'TELING BERDARAH':
		return 24
	elif obj[2] == 'TELINGA ADA CAIRAN':
		return 24
	elif obj[2] == 'TELINGA BERDENGUNG DAN BERAIR':
		return 24
	elif obj[2] == 'TELINGA BINDENG ':
		return 24
	elif obj[2] == 'TELINGA GATAL':
		return 24
	elif obj[2] == 'TELINGA KADANG MENDENGUNG':
		return 24
	elif obj[2] == 'TELINGA BERDARAH':
		return 24
	elif obj[2] == 'TELINGA KANAN GAK ENAK ':
		return 24
	elif obj[2] == 'TELINGA KELUAR DARAH ':
		return 24
	elif obj[2] == 'TELINGA KANAN NYERI':
		return 11
	elif obj[2] == 'TELINGA KELUAR AIR':
		return 24
	elif obj[2] == 'TELINGA KEMASUKAN SEMUT':
		return 24
	elif obj[2] == 'TELINGA BERNANAH':
		return 24
	elif obj[2] == 'TELINGA NGEUREUBEUK':
		return 24
	elif obj[2] == 'TELINGA SERING BERDENGUNG ':
		return 24
	elif obj[2] == 'TENGGOROKAN SAKIT':
		return 11
	elif obj[2] == 'SAKIT SENDI ':
		return 17
	elif obj[2] == 'SAKIT PUNDAK ':
		return 17
	elif obj[2] == 'PENDARAHAN ':
		return 10
	elif obj[2] == 'PIPIS SAKIT':
		return 5
	elif obj[2] == 'PERUT TEGANG DAN NYERI':
		return 17
	elif obj[2] == 'PERUTNYA SAKIT':
		return 11
	elif obj[2] == 'PILEK TIDAK KUNJUNG SEMBUH':
		return 24
	elif obj[2] == 'PINGGANG KECETIT':
		return 23
	elif obj[2] == 'PINGGANG PEGEL':
		return 17
	elif obj[2] == 'PINGGUL SAKIT':
		return 23
	elif obj[2] == 'PINGGUL SAKIT ':
		return 23
	elif obj[2] == 'PINGSAN':
		return 11
	elif obj[2] == 'PIPI KANAN SAKIT ':
		return 23
	elif obj[2] == 'PIPISNYA SAKIT':
		return 0
	elif obj[2] == 'PUNGGUNG SAKIT':
		return 9
	elif obj[2] == 'POLIP':
		return 10
	elif obj[2] == 'PORT RI':
		return 10
	elif obj[2] == 'KELUAR DARAH TERUS':
		return 10
	elif obj[2] == 'SIRCUM':
		return 0
	elif obj[2] == 'PREMATUR':
		return 11
	elif obj[2] == 'PROGRAM HAMIL':
		return 10
	elif obj[2] == 'PROGRAM KEHAMILAN':
		return 10
	elif obj[2] == 'PROMIL':
		return 10
	elif obj[2] == 'PTERYGIUM':
		return 15
	elif obj[2] == 'PERUT SERING SAKIT':
		return 11
	elif obj[2] == 'PERUT SEBELAH KIRI SAKIT ':
		return 17
	elif obj[2] == 'PERUT PERIH':
		return 17
	elif obj[2] == 'PERUT PANAS':
		return 11
	elif obj[2] == 'PENDENGARAN KURANG':
		return 24
	elif obj[2] == 'PENDENGARAN TERASA BERKURANG':
		return 24
	elif obj[2] == 'PENGAPURAN KAKI KIRI ':
		return 3
	elif obj[2] == 'PENGLIHATAN AGAK SILAU':
		return 15
	elif obj[2] == 'PENGLIHATAN KABUR':
		return 15
	elif obj[2] == 'PERAWATAN CABUT GIGI':
		return 8
	elif obj[2] == 'PERAWATAN GIGI ':
		return 8
	elif obj[2] == 'PERAWATN GIGI':
		return 8
	elif obj[2] == 'PERAWTAN GIGI BERLUBANG':
		return 8
	elif obj[2] == 'PERIKSA GIGI LANJUTAN':
		return 8
	elif obj[2] == 'PERIKSA LANJUTAN':
		return 8
	elif obj[2] == 'PERIKSA MINUS DAN PLUS MATA':
		return 15
	elif obj[2] == 'PERIKSA RAHANG':
		return 0
	elif obj[2] == 'TENGGOROKAN':
		return 24
	elif obj[2] == 'PERLU TERAPI':
		return 11
	elif obj[2] == 'PERUT KEMBUNG':
		return 17
	elif obj[2] == 'PERUT MELILIT DAN BEGAH ':
		return 17
	elif obj[2] == 'PERUT MELILIT':
		return 17
	elif obj[2] == 'PERUT NYERI':
		return 10
	elif obj[2] == 'PUNGGUNG DAN TANGAN SAKIT':
		return 17
	elif obj[2] == 'PUSER BERDARAH':
		return 11
	elif obj[2] == 'SAKIT PINGGUL':
		return 3
	elif obj[2] == 'SAKIT KUPING':
		return 24
	elif obj[2] == 'SAKIT LUTUT KANAN':
		return 3
	elif obj[2] == 'SAKIT DI PUNGGUNG':
		return 17
	elif obj[2] == 'SAKIT EKSIM':
		return 14
	elif obj[2] == 'SAKIT GIGI ':
		return 12
	elif obj[2] == 'SAKIT GIGI GRAHAM ':
		return 8
	elif obj[2] == 'SAKIT GUSI':
		return 12
	elif obj[2] == 'SAKIT KEPALA SEBELAH':
		return 23
	elif obj[2] == 'SAKIT KEPALA TERUS':
		return 11
	elif obj[2] == 'SAKIT SAAT BERJALAN':
		return 3
	elif obj[2] == 'SAKIT LENGAN':
		return 23
	elif obj[2] == 'PUSING ':
		return 10
	elif obj[2] == 'SAKIT LIDAH':
		return 24
	elif obj[2] == 'SAKIT MATA MERAH':
		return 15
	elif obj[2] == 'SAKIT PANGGUL':
		return 10
	elif obj[2] == 'SAKIT PASCA OPERASI':
		return 17
	elif obj[2] == 'SAKIT PERSENDIAN BAHU':
		return 23
	elif obj[2] == 'SAKIT PERUT BAGIAN BAWAH':
		return 10
	elif obj[2] == 'SAKIT PERUT BAGIAN RAHIM':
		return 10
	elif obj[2] == 'SAKIT PERUT BAWAH':
		return 10
	elif obj[2] == 'SAKIT PINGGANG ':
		return 23
	elif obj[2] == 'SAKIT DI LEHER':
		return 18
	elif obj[2] == 'SAKIT DI KELAMIN ':
		return 14
	elif obj[2] == 'SAKIT DI BAGIAN PINGGANG':
		return 17
	elif obj[2] == 'SAKIT BAGIAN KAKI':
		return 23
	elif obj[2] == 'PUSING LIAT CAHAYA':
		return 23
	elif obj[2] == 'RADANG SAKIT TENGGOROKAN':
		return 24
	elif obj[2] == 'RADANG TENGGOROKAN ':
		return 24
	elif obj[2] == 'RADIASI':
		return 15
	elif obj[2] == 'LUPUS':
		return 17
	elif obj[2] == 'REMATIK':
		return 17
	elif obj[2] == 'BATU GINJAL':
		return 5
	elif obj[2] == 'RENCANA SC':
		return 10
	elif obj[2] == 'RETINAL DISORDER':
		return 15
	elif obj[2] == 'REUMATIK':
		return 17
	elif obj[2] == 'REWEL':
		return 11
	elif obj[2] == 'RUAM ':
		return 14
	elif obj[2] == 'RUAM DI MUKA':
		return 14
	elif obj[2] == 'RUAM DI BADAN':
		return 11
	elif obj[2] == 'RUJUKAN DR LAURA':
		return 9
	elif obj[2] == 'SAKI GIGI':
		return 8
	elif obj[2] == 'SAKI GUSI BAGIAN ATAS ':
		return 8
	elif obj[2] == 'SAKI KAKI ':
		return 17
	elif obj[2] == 'SAKIT BAGIAN BAHU SAMPAI BAWAH':
		return 18
	elif obj[2] == 'LUTUT KERAM ':
		return 0
	elif obj[2] == 'TELINGA BENGKAK ':
		return 24
	elif obj[2] == 'LUKA TAPI TIDAK SEMBUH SEMBUH ':
		return 14
	elif obj[2] == 'DPT':
		return 11
	elif obj[2] == 'TBC ':
		return 16
	elif obj[2] == 'TELINGA ':
		return 24
	elif obj[2] == 'UPPUSIN':
		return 24
	elif obj[2] == 'CEREBRAL PALSY':
		return 11
	elif obj[2] == 'CERVICAL DISC DISORDERS':
		return 23
	elif obj[2] == 'BIOPSI':
		return 0
	elif obj[2] == 'COTTON BUD KETINGGALAN DI KUPING':
		return 24
	elif obj[2] == 'DADA BERDEBAR':
		return 9
	elif obj[2] == 'DADA KIRI SAKIT':
		return 11
	elif obj[2] == 'DADA TERASA NYERI':
		return 9
	elif obj[2] == 'DAHAK':
		return 17
	elif obj[2] == 'DAHAK BERDARAH':
		return 11
	elif obj[2] == 'DARAH TINGGI ':
		return 17
	elif obj[2] == 'DBD':
		return 11
	elif obj[2] == 'DEBAR GAK NYAMAN':
		return 9
	elif obj[2] == 'DECUBITUS':
		return 14
	elif obj[2] == 'DEMAM MUNTAH':
		return 11
	elif obj[2] == 'DENGKUL SAKIT ':
		return 3
	elif obj[2] == 'DIARE CAIR':
		return 11
	elif obj[2] == 'PENDENGARAN':
		return 24
	elif obj[2] == 'CEK KANDUNGAN ':
		return 10
	elif obj[2] == 'TERTUSUK PAKU':
		return 0
	elif obj[2] == 'CAK KANDUNGAN':
		return 10
	elif obj[2] == 'BUKA PERBAN':
		return 0
	elif obj[2] == 'BUKA VERBAN':
		return 10
	elif obj[2] == 'BUKIT MAKMUR':
		return 10
	elif obj[2] == 'BUSINASI ':
		return 5
	elif obj[2] == 'CABUT':
		return 8
	elif obj[2] == 'CABUT GIGI ':
		return 1
	elif obj[2] == 'CACAR ':
		return 14
	elif obj[2] == 'CACAR AIR':
		return 11
	elif obj[2] == 'CAMPAK':
		return 11
	elif obj[2] == 'CEK IUD':
		return 10
	elif obj[2] == 'CEDERA OTOT PUNGGUNG':
		return 18
	elif obj[2] == 'DARAH':
		return 11
	elif obj[2] == 'GERAHAM ':
		return 8
	elif obj[2] == 'GIGI ':
		return 8
	elif obj[2] == 'GULA DARAH':
		return 17
	elif obj[2] == 'GUSI':
		return 8
	elif obj[2] == 'CEK HAMIL ':
		return 10
	elif obj[2] == 'TIDAK BISA MENCIUM BAU':
		return 24
	elif obj[2] == 'KEPALA ADA KULIT KERING':
		return 14
	elif obj[2] == 'DUDUK LAMA KELEYENGAN':
		return 23
	elif obj[2] == 'BUKA JAHITAN':
		return 21
	elif obj[2] == 'DYSPEPSI':
		return 17
	elif obj[2] == 'GATAL PERIH ':
		return 11
	elif obj[2] == 'GATAL GATAL DI KEMALUAN':
		return 11
	elif obj[2] == 'GATAL GATAL DI TELAPAK KAKI':
		return 14
	elif obj[2] == 'GATEL':
		return 14
	elif obj[2] == 'GATEL TANGAN':
		return 14
	elif obj[2] == 'GEA':
		return 11
	elif obj[2] == 'GEJALA TIFUS':
		return 11
	elif obj[2] == 'GERAHAM BELAKANG SAKIT ':
		return 8
	elif obj[2] == 'GIG BERLUBANG':
		return 12
	elif obj[2] == 'GIGI ATAS KANAN SAKIT':
		return 8
	elif obj[2] == 'GIGI BENGKAK KANAN KIRI':
		return 8
	elif obj[2] == 'GIGI COPOT':
		return 8
	elif obj[2] == 'GIGI GOYANG ':
		return 8
	elif obj[2] == 'GIGI LEPAS':
		return 8
	elif obj[2] == 'GIGI LUBANG':
		return 8
	elif obj[2] == 'GIGI MASUK KE GUSI':
		return 12
	elif obj[2] == 'HABIS JATUH':
		return 17
	elif obj[2] == 'HAID TIDAK NORMAL':
		return 10
	elif obj[2] == 'HEPATITITIS ':
		return 11
	elif obj[2] == 'GATAL TENGGOROKAN':
		return 24
	elif obj[2] == 'GATAL DI TELINGA':
		return 24
	elif obj[2] == 'GATAL PADA TANGAN/SIKU DAN KULIT VAGINA':
		return 14
	elif obj[2] == 'GANGGUAN MOOD':
		return 13
	elif obj[2] == 'DYSPEPSIA':
		return 11
	elif obj[2] == 'EPILEPSI':
		return 23
	elif obj[2] == 'FISSURA ANI':
		return 20
	elif obj[2] == 'FLEK ':
		return 10
	elif obj[2] == 'FLU ':
		return 24
	elif obj[2] == 'GA BISA BAK':
		return 5
	elif obj[2] == 'HALUSINASI':
		return 13
	elif obj[2] == 'GANGGUAN BICARA':
		return 11
	elif obj[2] == 'GANGGUAN SENSORI':
		return 11
	elif obj[2] == 'TIMBUL BENTOL BENTOL YANG BERISI CAIRAN BENING':
		return 14
	elif obj[2] == 'GANTI KARET':
		return 6
	elif obj[2] == 'GANTI TAMBALAN':
		return 8
	elif obj[2] == 'GATAL DI BAGIAN KAKI':
		return 14
	elif obj[2] == 'GATAL DI LUTUT':
		return 14
	elif obj[2] == 'GATAL DI PAHA':
		return 14
	elif obj[2] == 'GATAL DI TANGAN DAN KAKI':
		return 14
	elif obj[2] == 'GATAL DI TANGAN':
		return 14
	elif obj[2] == 'GATAL DI TELINGA ':
		return 24
	elif obj[2] == 'BUKA KB':
		return 10
	elif obj[2] == 'BUANG AIR KECIL SAKIT DAN BERDARAH':
		return 11
	elif obj[2] == 'LUKA OPERASI BERAIR':
		return 0
	elif obj[2] == 'BCG VAKSIN':
		return 11
	elif obj[2] == 'BAB BERLENDIR':
		return 11
	elif obj[2] == 'BAB SUSAH':
		return 11
	elif obj[2] == 'SERING BUANG AIR KECIL':
		return 5
	elif obj[2] == 'RADIOLOGI ':
		return 17
	elif obj[2] == 'BADAN LEMES PUSING':
		return 17
	elif obj[2] == 'BADAN MENGGIGIL':
		return 11
	elif obj[2] == 'BADAN MERAH MERAH':
		return 11
	elif obj[2] == 'BADAN PADA SAKIT ':
		return 17
	elif obj[2] == 'BADAN SEBELAH SAKIT':
		return 23
	elif obj[2] == 'BAK BERDARAH':
		return 5
	elif obj[2] == 'BANYAK BINTIK MERAH':
		return 14
	elif obj[2] == 'BAPIL GATAL':
		return 11
	elif obj[2] == 'BATUK ADA DARAH ':
		return 11
	elif obj[2] == 'BATUK ALERGI':
		return 11
	elif obj[2] == 'BATUK BERDAHAK SUDAH SEMINGGU':
		return 11
	elif obj[2] == 'BATUK KERING ':
		return 24
	elif obj[2] == 'BATUK PANAS':
		return 11
	elif obj[2] == 'BATUK KELUAR DARAH':
		return 16
	elif obj[2] == 'BATUK BATUK':
		return 17
	elif obj[2] == 'ASTRA':
		return 11
	elif obj[2] == 'ASAM URAT TINGGI':
		return 17
	elif obj[2] == 'ASAM MUAL':
		return 17
	elif obj[2] == 'ANUS':
		return 11
	elif obj[2] == 'SAKIT TEGGOROKAN':
		return 24
	elif obj[2] == 'BEJOLAN':
		return 11
	elif obj[2] == 'BENGKAK DI TELINGA':
		return 24
	elif obj[2] == 'BENJOLAN ANUS':
		return 0
	elif obj[2] == 'BENJOLAN LEHER':
		return 0
	elif obj[2] == 'BENJOLAN LENGAN':
		return 0
	elif obj[2] == 'BENJOLAN LUTUT':
		return 0
	elif obj[2] == 'BEJOLAN PUNDAK':
		return 0
	elif obj[2] == 'KAKI':
		return 14
	elif obj[2] == 'ASAM LAMBUNG TINGGI':
		return 17
	elif obj[2] == 'PERUT':
		return 14
	elif obj[2] == 'TANGAN':
		return 14
	elif obj[2] == 'BADAN':
		return 11
	elif obj[2] == 'DURI DI TENGGOROKAN':
		return 24
	elif obj[2] == 'GURATAN MERAH':
		return 14
	elif obj[2] == 'PENGGUMPALAN DARAH OTAK':
		return 23
	elif obj[2] == 'ALERGI OBAT':
		return 16
	elif obj[2] == 'IMPLAN':
		return 10
	elif obj[2] == 'BCG':
		return 11
	elif obj[2] == 'BELIKAT NGILU':
		return 23
	elif obj[2] == 'BUANG AIR KECIL PERIH':
		return 14
	elif obj[2] == 'BELUM BAK':
		return 11
	elif obj[2] == 'BIANG KERINGAT ':
		return 11
	elif obj[2] == 'BIBIR KERING':
		return 14
	elif obj[2] == 'BIBIR PECAH PECAH':
		return 14
	elif obj[2] == 'BIDURAN':
		return 11
	elif obj[2] == 'BINTIK BINTIK MERAH':
		return 11
	elif obj[2] == 'BINTIK DI BAGIAN MULUT':
		return 14
	elif obj[2] == 'BINTIK HITAM DI WAJAH':
		return 14
	elif obj[2] == 'BINTIK MERAH DEKAT MATA':
		return 14
	elif obj[2] == 'BINTIK MERAH DI DADA DAN DI PUNGGUNG':
		return 11
	elif obj[2] == 'BINTIK MERAH DI KEPALA':
		return 11
	elif obj[2] == 'BINTIK MERAH DI LEHER DAN BADAN':
		return 11
	elif obj[2] == 'BINTIK2 MERAH DI KULIT':
		return 11
	elif obj[2] == 'BINTIK MERAH DI WAJAH':
		return 14
	elif obj[2] == 'BISUL':
		return 14
	elif obj[2] == 'BLIGHTED OVUM':
		return 10
	elif obj[2] == 'BRONCHITIS':
		return 17
	elif obj[2] == 'BRUNTUS':
		return 14
	elif obj[2] == 'BRUNTUSAN GATAL':
		return 11
	elif obj[2] == 'BUAH ZAKAR BESAR SEBELAH ':
		return 0
	elif obj[2] == 'BERUNTUSAN DI WAJAH':
		return 14
	elif obj[2] == 'BERSIHKAN TELINGA ':
		return 24
	elif obj[2] == 'BERSIHKAN CERUMEN':
		return 24
	elif obj[2] == 'BENTOL BENTOL DI TANGAN DAN BADAN':
		return 11
	elif obj[2] == 'BENGKAK BEKAS SUNTIKAN':
		return 0
	elif obj[2] == 'BENGKAK DI BAGIAN KELAMIN ':
		return 14
	elif obj[2] == 'BENGKAK DI BAGIAN MATA':
		return 15
	elif obj[2] == 'BENGKAK DI MATA':
		return 11
	elif obj[2] == 'BENJOLAN DI TELINGA':
		return 11
	elif obj[2] == 'BENJOLAN DI SELANGKANGAN':
		return 14
	elif obj[2] == 'BENJOLANNYA TETEP ADA':
		return 15
	elif obj[2] == 'BENOL BENTOL DI BADAN ':
		return 14
	elif obj[2] == 'BERASA ADA CAHAYA PUTIH':
		return 15
	elif obj[2] == 'BERSIHIN TELINGA':
		return 24
	elif obj[2] == 'BERAT BADAN TIDAK NAIK SIGNIFIKAN':
		return 11
	elif obj[2] == 'BERCAK BERNANAH DI PUNGUNG':
		return 14
	elif obj[2] == 'BERDENGUNG':
		return 24
	elif obj[2] == 'BERLUBANG':
		return 8
	elif obj[2] == 'BEROBAT':
		return 5
	elif obj[2] == 'BERSIHIN GIGI':
		return 8
	elif obj[2] == 'BERSIHIN KOTORAN TELINGA':
		return 24
	elif obj[2] == 'BERSIHIN KUPING':
		return 24
	elif obj[2] == 'HIDUNG KEMASUKAN':
		return 24
	elif obj[2] == 'HIDUNG MAMPET':
		return 24
	elif obj[2] == 'HIDUNG SAKIT ':
		return 24
	elif obj[2] == 'KONTROL TELINGA':
		return 24
	elif obj[2] == 'LUTUT':
		return 3
	elif obj[2] == 'KONTROL MENINGITIS':
		return 11
	elif obj[2] == 'KONTROL OBAT':
		return 11
	elif obj[2] == 'KONTROL ORTHO':
		return 6
	elif obj[2] == 'PARKINSON':
		return 23
	elif obj[2] == 'PASCA KURET':
		return 10
	elif obj[2] == 'KONTROL PASCA LAHIR':
		return 11
	elif obj[2] == 'PASCA OPERASI':
		return 0
	elif obj[2] == 'PERAWAT GIGI':
		return 8
	elif obj[2] == 'KONTROL PILEK':
		return 11
	elif obj[2] == 'KONTROL POST LAHIR':
		return 11
	elif obj[2] == 'PTERIGIUM':
		return 15
	elif obj[2] == 'GINEKOLOGI':
		return 22
	elif obj[2] == 'RENCANA TINDAKAN ':
		return 17
	elif obj[2] == 'PEGAL DI LEHER':
		return 9
	elif obj[2] == 'SUSAH TIDUR':
		return 9
	elif obj[2] == 'SAKIT GINJAL':
		return 5
	elif obj[2] == 'SAKIT TENGGOROK':
		return 24
	elif obj[2] == 'SETELAH SESAR':
		return 10
	elif obj[2] == 'KAWAT GIGI':
		return 8
	elif obj[2] == 'KONTROL KANDUNGAN ':
		return 10
	elif obj[2] == 'KACA MATA':
		return 15
	elif obj[2] == 'DIABET ':
		return 17
	elif obj[2] == 'ONKOLOGI':
		return 22
	elif obj[2] == 'BARU MELAHIRKAN':
		return 10
	elif obj[2] == 'BBLR':
		return 11
	elif obj[2] == 'BPH':
		return 5
	elif obj[2] == 'KONTROL CABUT KUKU':
		return 0
	elif obj[2] == 'CAD':
		return 9
	elif obj[2] == 'CHOLELITIASIS':
		return 0
	elif obj[2] == 'COLIC RENAL':
		return 5
	elif obj[2] == 'ENDOMETRIOSIS':
		return 10
	elif obj[2] == 'K2':
		return 17
	elif obj[2] == 'KONTROL FLEK':
		return 11
	elif obj[2] == 'KONTROL FLEK ':
		return 11
	elif obj[2] == 'GANGGUAN ANXIETAS':
		return 13
	elif obj[2] == 'GULA':
		return 17
	elif obj[2] == 'ESWL':
		return 5
	elif obj[2] == 'PAPSMEAR':
		return 10
	elif obj[2] == 'ISK ':
		return 17
	elif obj[2] == 'KONTROL JANTUNG':
		return 9
	elif obj[2] == 'SPIRAL':
		return 10
	elif obj[2] == 'BENJOLAN DI LUBANG TELINGA':
		return 24
	elif obj[2] == 'HIDUNG SAKIT':
		return 24
	elif obj[2] == 'SAKIT BELAKANG TELINGA':
		return 24
	elif obj[2] == 'KUPING MENDENGING':
		return 17
	elif obj[2] == 'KUPING SAKIT':
		return 24
	elif obj[2] == 'LAMBUNG NYERI':
		return 17
	elif obj[2] == 'LAMBUNG SAKIT ':
		return 17
	elif obj[2] == 'LEHER BENGKAK':
		return 11
	elif obj[2] == 'LEHER NYERI':
		return 11
	elif obj[2] == 'LEMES':
		return 17
	elif obj[2] == 'LENGAN SUKA KESEMUTAN':
		return 23
	elif obj[2] == 'LENGAN SAKIT':
		return 17
	elif obj[2] == 'LEPAS BEHEL':
		return 8
	elif obj[2] == 'LEPAS IUD':
		return 10
	elif obj[2] == 'LEPAS KB':
		return 10
	elif obj[2] == 'LIDAH DAN TENGGOROKAN ADA BENJOLAN':
		return 24
	elif obj[2] == 'LIDAH PUTIH':
		return 11
	elif obj[2] == 'LIVER':
		return 17
	elif obj[2] == 'LUKA BASAH':
		return 5
	elif obj[2] == 'LUKA DI KAKI ':
		return 14
	elif obj[2] == 'LUKA DIKAKI':
		return 0
	elif obj[2] == 'LUKA MATA':
		return 15
	elif obj[2] == 'KUNING':
		return 11
	elif obj[2] == 'KULIT WAJAH MERAH':
		return 14
	elif obj[2] == 'KULIT SIKU KERING':
		return 14
	elif obj[2] == 'TANGAN PEGAL':
		return 16
	elif obj[2] == 'TELINGA TERSUMBAT':
		return 24
	elif obj[2] == 'TUMOR':
		return 4
	elif obj[2] == 'MRI':
		return 23
	elif obj[2] == 'BERAT BADAN KURANG':
		return 11
	elif obj[2] == 'HABIS OBAT':
		return 9
	elif obj[2] == 'JARI KESEMUTAN':
		return 17
	elif obj[2] == 'LEPAS JAITAN':
		return 0
	elif obj[2] == 'NYERI BAK':
		return 5
	elif obj[2] == 'AGAK LEMES':
		return 11
	elif obj[2] == 'KULIT SENSITIF':
		return 11
	elif obj[2] == 'TELINGA KOTOR':
		return 24
	elif obj[2] == 'OPERSI AMANDEL':
		return 11
	elif obj[2] == 'KULIT HIDUNG HITAM':
		return 14
	elif obj[2] == 'KULIT KAKI GATAL ':
		return 14
	elif obj[2] == 'KULIT KELUPAS ':
		return 14
	elif obj[2] == 'KULIT KERAS DI BAGIAN KAKI':
		return 14
	elif obj[2] == 'KULIT KERING DI TANGAN DAN PAYUDARA':
		return 14
	elif obj[2] == 'KULIT PUTIH PUTIH DI WAJAH':
		return 14
	elif obj[2] == 'TEKANAN DARAH TIDAK STABIL':
		return 23
	elif obj[2] == 'KONSULTASI USG':
		return 10
	elif obj[2] == 'KONSULTASI SC':
		return 17
	elif obj[2] == 'PILEK BAU':
		return 24
	elif obj[2] == 'KAKI KESEMUTAN':
		return 23
	elif obj[2] == 'KAKI PECAH PECAH':
		return 14
	elif obj[2] == 'KAKI PEGAL':
		return 23
	elif obj[2] == 'KAKI PEGAL-PEGAL':
		return 9
	elif obj[2] == 'KALAU CAPEK ADA NYERI DADA':
		return 9
	elif obj[2] == 'TULANG BUNYI':
		return 3
	elif obj[2] == 'KALO JALAN SAKIT':
		return 23
	elif obj[2] == 'KANKER':
		return 0
	elif obj[2] == 'KAPALAN DI KAKI':
		return 14
	elif obj[2] == 'DOKTER KULIT':
		return 14
	elif obj[2] == 'KEJANG NYERI KEPALA':
		return 23
	elif obj[2] == 'KEL':
		return 14
	elif obj[2] == 'KELENJAR':
		return 11
	elif obj[2] == 'KELOPAK MATA KANAN BENGKAK':
		return 15
	elif obj[2] == 'KELUAR BINTIK DI BADAN':
		return 11
	elif obj[2] == 'KELUAR CAIRAN HIDUNG':
		return 24
	elif obj[2] == 'KELUAR DARAH':
		return 10
	elif obj[2] == 'KELUAR FLEK':
		return 10
	elif obj[2] == 'KEMASUKAN KERTAS ':
		return 24
	elif obj[2] == 'KAKI KESELEO':
		return 18
	elif obj[2] == 'KAKI KANAN BAAL':
		return 23
	elif obj[2] == 'KAKI GATAL':
		return 14
	elif obj[2] == 'JARI TANGAN KAKU':
		return 23
	elif obj[2] == 'IMUNISASI DPT':
		return 11
	elif obj[2] == 'IMUNISASI ROTAVIRUS':
		return 11
	elif obj[2] == 'INFEKSI TELINGA':
		return 24
	elif obj[2] == 'INGIN TAMPIL CANTIK':
		return 14
	elif obj[2] == 'IPD':
		return 11
	elif obj[2] == 'IRITASI MATA':
		return 15
	elif obj[2] == 'IUD':
		return 10
	elif obj[2] == 'JAMUR':
		return 14
	elif obj[2] == 'JARI TIDAK BISA DIGERAKKAN':
		return 23
	elif obj[2] == 'KAKI BENGKAK DAN SAKIT':
		return 17
	elif obj[2] == 'JARI TELUNJUK BENGKAK':
		return 9
	elif obj[2] == 'JARI TIDAK BISA DI TEKUK':
		return 17
	elif obj[2] == 'JATUH TERKENA KEPALA':
		return 11
	elif obj[2] == 'JATUNG BERDEBAR':
		return 9
	elif obj[2] == 'JEMPOL BENGKAK':
		return 14
	elif obj[2] == 'JERAWAT KULIT KEPALA':
		return 14
	elif obj[2] == 'AGAK PEGAL':
		return 9
	elif obj[2] == 'KADAR GULA TINGGL':
		return 17
	elif obj[2] == 'KEMBUNG':
		return 17
	elif obj[2] == 'KEMUNGKINAN CACAR ':
		return 11
	elif obj[2] == 'KENCING TIDAK LANCAR KALO TIDAK MINUM OBAT':
		return 5
	elif obj[2] == 'MASALAH KULIT':
		return 14
	elif obj[2] == 'KONSUL PRE CURRETAGE':
		return 17
	elif obj[2] == 'SIKLUS HAID':
		return 10
	elif obj[2] == 'KONSUL TERAPI ':
		return 18
	elif obj[2] == 'KONSUL TERAPI':
		return 18
	elif obj[2] == 'KONSUL TULANG':
		return 3
	elif obj[2] == 'KONSUL TULANG BELAKANG':
		return 18
	elif obj[2] == 'KONSUL TYPOID':
		return 11
	elif obj[2] == 'TERAPI WICARA':
		return 25
	elif obj[2] == 'KONSULEN DR DIAN':
		return 24
	elif obj[2] == 'KONSUL LUKA':
		return 14
	elif obj[2] == 'SUKA MIMISAN':
		return 24
	elif obj[2] == 'KONSULTASI ':
		return 21
	elif obj[2] == 'KONSULTASI GIGI':
		return 8
	elif obj[2] == 'BENJOLAN KULIT':
		return 0
	elif obj[2] == 'BELUM HAMIL':
		return 10
	elif obj[2] == 'HSG':
		return 10
	elif obj[2] == 'KANTUNG KEMIH ':
		return 5
	elif obj[2] == 'KOLESTEROL':
		return 17
	elif obj[2] == 'MELAHIRKAN':
		return 10
	elif obj[2] == 'KONSUL KUKU TANGAN':
		return 14
	elif obj[2] == 'KEPALA GATAL':
		return 14
	elif obj[2] == 'REUMATIK ':
		return 17
	elif obj[2] == 'KEPALA PUSING':
		return 23
	elif obj[2] == 'KEPALA PUSING ':
		return 23
	elif obj[2] == 'KEPALA TERBENTUR':
		return 11
	elif obj[2] == 'KERAM PERUT':
		return 14
	elif obj[2] == 'KESEDAK DURI':
		return 24
	elif obj[2] == 'KESEMUTAN DI TANGAN':
		return 17
	elif obj[2] == 'KETOMBE DI KULIT KEPALA':
		return 14
	elif obj[2] == 'KETUSUK DURI':
		return 24
	elif obj[2] == 'HABIS INSISI HORDEULUM':
		return 15
	elif obj[2] == 'KB ':
		return 10
	elif obj[2] == 'KONSULTASI KESEHATAN JIWA':
		return 13
	elif obj[2] == 'KONSUL ':
		return 25
	elif obj[2] == 'KETINGGALAN KAPAS':
		return 24
	elif obj[2] == 'KONSUL BERAT BADAN':
		return 11
	elif obj[2] == 'KONSUL DR HERLINA':
		return 18
	elif obj[2] == 'KONSUL EVALUASI TERAPI':
		return 3
	elif obj[2] == 'KONSUL HIPERBILIRUBIN':
		return 11
	elif obj[2] == 'JALAN JINJIT':
		return 25
	elif obj[2] == 'WASIR ':
		return 0
	else: return 0.0

        '''

        # for i in file:
        #    st.code(i, language='python')

        # line = file.readline()

        st.code(x, language='python')

    # st.code(file.readlines())

    # view_tree = pd.DataFrame("outputs/rules/regression/rules.py")
    # st.dataframe(view_tree)
    # st.json(json)
