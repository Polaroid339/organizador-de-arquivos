import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".wmv", ".flv"],
    "Musicas": [".mp3", ".wav", ".wma", ".ogg", ".flac"],
    "Executaveis": [".exe", ".msi", ".bat", ".sh"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Pdfs": [".pdf"],
    "Documentos": [".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp"],
    "Textos": [".txt", ".md", ".csv"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
