#captura dos dados

print("Cole as placas:\n")

placas = []

while True:
    linha = input()
    if linha == "":
        break
    placas.append(linha.strip())

#Realizando a busca no site

from playwright.sync_api import sync_playwright

with sync_playwright() as teste:
    navegador = teste.chromium.launch(headless=True)

    pagina = navegador.new_page()

    pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

    resultado = []

    for placa in placas:

        pagina.get_by_role("textbox", name="Digite a Placa").fill(placa)

        pagina.get_by_role("button", name="Pesquisar").click()

        pagina.wait_for_timeout(5000)

        texto = pagina.get_by_text("Veículo está no pátio")

        if texto.count() > 0:
            resposta = ("Veículo está no pátio")
        else:
            resposta = ("Veículo não se encontra no pátio")

        resultado.append(f"{placa} - {resposta}")

        pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

    navegador.close()

#Criando o arquivo

with open("placas.txt", "w") as arquivo:
    for linha in resultado:
        arquivo.write(linha + "\n")

