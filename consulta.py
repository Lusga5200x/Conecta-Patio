#captura dos dados

print("Cole as placas (Aperte o ENTER 3x):\n")

placas = []

while True:
    linha = input()
    if linha == "":
        break
    placas.append(linha.strip())

#Realizando a busca no site
import os
import sys

if getattr(sys, 'frozen', False):
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = os.path.join(sys._MEIPASS, 'ms-playwright')

from playwright.sync_api import sync_playwright

with sync_playwright() as teste:
    navegador = teste.chromium.launch(headless=True)

    pagina = navegador.new_page()

    pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

    resultado = []

    for placa in placas:

        pagina.get_by_role("textbox", name="Digite a Placa").fill(placa)

        pagina.get_by_role("button", name="Pesquisar").click()

        pagina.wait_for_timeout(3000)

        texto = pagina.get_by_text("Veículo não se encontra no pátio")

        if texto.count() > 0:
            resposta = ("Veículo não se encontra no pátio")
        else:
            resposta = ("Veículo está no pátio")

        resultado.append(f"{placa} - {resposta}")

        pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

    navegador.close()

#Criando o arquivo

from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

Tk().withdraw()

caminho_arquivo = asksaveasfilename(
    initialfile="placas.txt",
    defaultextension=".txt",
    filetypes=[("Arquivo de texto", "*.txt")],
    title="Salvar resultado como"
)

if caminho_arquivo:
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in resultado:
            arquivo.write(linha + "\n")

    print("\nArquivo salvo com sucesso!")
else:
    print("\nSalvamento cancelado.")

try:
    input("\nPressione ENTER para fechar...")
except:
    os.system("pause")
