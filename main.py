import flet as ft
import os
from tkinter.filedialog import askdirectory

def main(page: ft.Page):

    page.window.left = 1300
    page.window.top = 550
    page.window.width = 600
    page.window.height = 400
    page.window.maximizable = False
    page.padding = 30

    def selecionar_caminho(e):
        caminho = askdirectory(title="Selecione uma pasta")
        tex_caminho.value = caminho
        tex_caminho.update()
        page.update()
        return caminho

    def organizar_arquivos(caminho):
        # Verifica se o caminho está vazio ou é inválido
        if not caminho or not os.path.isdir(caminho):
            page.snack_bar = ft.SnackBar(
                ft.Text("Insira um caminho válido!"))
            page.snack_bar.open = True
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
            nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
            for pasta in locais:
                if extensao in locais[pasta]:
                    if not os.path.exists(f"{caminho}/{pasta}"):
                        os.mkdir(f"{caminho}/{pasta}")
                    os.rename(f"{caminho}/{arquivo}",
                              f"{caminho}/{pasta}/{arquivo}")

        page.snack_bar = ft.SnackBar(
            ft.Text("Arquivos organizados com sucesso!"))
        page.snack_bar.open = True
        page.update()
        return

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
        on_click=lambda e: organizar_arquivos(tex_caminho.value),
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
