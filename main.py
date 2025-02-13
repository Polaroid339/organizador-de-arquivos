import flet as ft
import os
from tkinter.filedialog import askdirectory


def main(page: ft.Page):

    page.window.left = 700
    page.window.top = 350
    page.window.width = 600
    page.window.height = 400
    page.window.maximizable = False
    page.padding = 30

    snack_bar = ft.SnackBar(content=ft.Text(""), open=False)
    page.add(snack_bar)

    def selecionar_caminho(e):
        caminho = askdirectory(title="Selecione uma pasta")
        if caminho:
            tex_caminho.value = caminho
            tex_caminho.update()

    def organizar_arquivos(e):
        caminho = tex_caminho.value.strip()

        if not caminho or not os.path.isdir(caminho):
            snack_bar.content.value = "Insira um caminho válido!"
            snack_bar.open = True
            page.update()
            return

        lista_arquivos = os.listdir(caminho)

        locais = {
            "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
            "Vídeos": [".mp4", ".avi", ".mkv", ".wmv", ".flv", ".ts", ".mov"],
            "Músicas": [".mp3", ".wav", ".wma", ".ogg", ".flac", ".midi", ".aac", ".alac"],
            "Executáveis": [".exe", ".msi", ".bat", ".sh", ".apk", ".jar", ".bin"],
            "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".tar.gz", ".xz", ".bz2"],
            "Pdfs": [".pdf"],
            "Documentos": [".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp", ".epub"],
            "Textos": [".txt", ".md", ".csv", ".json", ".log"],
        }

        for arquivo in lista_arquivos:
            caminho_arquivo = os.path.join(caminho, arquivo)
            if os.path.isdir(caminho_arquivo):
                continue

            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            for pasta, extensoes in locais.items():
                if extensao in extensoes:
                    pasta_destino = os.path.join(caminho, pasta)
                    if not os.path.exists(pasta_destino):
                        os.mkdir(pasta_destino)

                    destino_arquivo = os.path.join(pasta_destino, arquivo)

                    contador = 1
                    while os.path.exists(destino_arquivo):
                        novo_nome = f"{nome}_{contador}{extensao}"
                        destino_arquivo = os.path.join(
                            pasta_destino, novo_nome)
                        contador += 1

                    os.rename(caminho_arquivo, destino_arquivo)

        snack_bar.content.value = "Arquivos organizados com sucesso!"
        snack_bar.open = True
        page.update()

    titulo = ft.Text(
        value="Organizador de Arquivos",
        color="blue",
        text_align="center",
        size=25
    )

    tex_caminho = ft.TextField(
        label="Caminho da pasta",
        hint_text="Digite o caminho de uma pasta",
    )

    botao1 = ft.ElevatedButton(
        text="Selecionar Pasta",
        on_click=selecionar_caminho,
        icon="folder",
        height=50,
        width=300,
        elevation=3,
        style=ft.ButtonStyle(color="green")
    )

    botao2 = ft.ElevatedButton(
        text="Organizar Arquivos",
        on_click=organizar_arquivos,
        icon="check",
        height=50,
        width=300,
        elevation=3,
        style=ft.ButtonStyle(color="green")
    )

    page.add(
        ft.Column(
            [
                titulo,
                ft.Container(height=15),
                tex_caminho,
                ft.Container(height=15),
                botao1,
                botao2,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()


ft.app(main)
