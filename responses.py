from datetime import time


def sampleResponses(inputText):
    userMessage = str(inputText).lower()

    if userMessage in ("/start", "hai", "hello"):
        return "Selamat Datang di Chatbot Layanan Rawat Jalan"

    if userMessage in ("/poli", "poli"):
        return "Anda Masuk ke Menu Pemilihan Layanan Poli Rawat Jalan"

    if userMessage in ("/jadwal", "jadwal"):
        return "Anda Masuk ke Menu Jadwal Layanan Poli"

    return "wrong message.."
