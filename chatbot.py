from telebot import *
from chefboost import Chefboost as chef
import pandas as pd
import streamlit as st
from sklearn import preprocessing
import imp
#from app.database import database
import time

#database = database()
api = '5393292456:AAHe6eYVty2SWs4h-9GeMDjzgMMeowMcPLE'
bot = TeleBot(api)

df = pd.read_csv("./dataset/dataset7.csv",
                 delimiter="[,;]", engine='python')
df_dump = df.copy()

le = preprocessing.LabelEncoder()
df_dump['jenis_poli'] = le.fit_transform(df_dump.jenis_poli)
labels_name = ['Bedah', 'Bedah Mulut', 'Bedah Syaraf', 'Bedah Tulang atau Orthopedi', 'Bedah Tumor', 'Bedah Urologi', 'Gigi Spesialis Orthodonti', 'Gigi Spesialis Periodonti', 'Gigi & Mulut', 'Kardiologi atau Jantung', 'Kebidanan & Kadungan', 'Kesehatan Anak', 'Kesehatan Gigi dan Mulut Anak',
               'Kesehatan Jiwa', 'Kulit & Kelamin', 'Mata', 'Paru-paru', 'Penyakit Dalam', 'Rehabilitasi Medik', 'Skin Care', 'Sub Spesialis Bedah Anak', 'Sub Spesialis Bedah Tumor (Onkologi)', 'Sub Spesialis Onkologi Ginekologi', 'Syaraf', 'THT', 'Tumbuh Kembang Anak (REMEDIA)']

# ** LOAD MODEL Regression FROM DIRECTORY **
#model = chef.load_model("model_Regression.pkl")
moduleName = "outputs/rules/regression/rules"
fp, pathname, description = imp.find_module(moduleName)
myrules = imp.load_module(moduleName, fp, pathname, description)

# Bot Start


@bot.message_handler(commands=['start', 'START'])
def selamat_datang(message):
    # print(message)
    f_nama = message.from_user.first_name
    #user_message = str(input_text).lower()
    bot.reply_to(
        message, 'Welcome to the Outpatient Poly Selection {} '.format(f_nama))
    bot.reply_to(
        message, """\
Please fill in the Format /poli[space]*"JK"*"USIA"*"Keluhan1"*"Keluhan2"*"Keluhan3"

If No complaints 2 and 3, then just type "TIDAK ADA"
Ex : 
/poli *Laki-laki*anak*BATUK*TIDAK ADA*TIDAK ADA
""")


@bot.message_handler(commands=['poli', 'POLI'])
def pemilihan_poli(message):
    #messid = message.message_id
    bot.reply_to(
        message, 'You Enter the Outpatient Poly Service Selection Menu')

    #cid = message.chat.id
    teks = message.text.split('*')
    print(teks)
    jk = teks[1]
    usia = teks[2]
    keluhan_1 = teks[3]
    keluhan_2 = teks[4]
    keluhan_3 = teks[5]
    mylist = [jk, usia.lower(), keluhan_1.upper(), keluhan_2.upper(),
              keluhan_3.upper()]
    result = labels_name[int(myrules.findDecision(
        [mylist[0], mylist[1], mylist[2], mylist[3], mylist[4]]))]
    print(mylist)
    bot.reply_to(
        message, 'The appropriate type of Poly Service is = {} '.format(result))


bot.infinity_polling()
