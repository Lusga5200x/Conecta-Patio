# Interface do programa

import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Conecta Pátio")
janela.geometry("600x400")

# Texto superior
texto1 = tk.Label(janela, text="Digite os chassis:")
texto1.pack(pady=10)

# Campo de busca
campo_busca = tk.Text(janela, width=50, height=10)
campo_busca.pack(pady=10)

# Texto de status
texto2 = tk.Label(janela, text="")
texto2.pack(pady=10)

# Barra de carregamento
barra = ttk.Progressbar(janela, length=300)
barra.pack(pady=10)

# Consulta no site
def busca_no_site():

    texto2.config(text="Pesquisando...")
    janela.update()

    # captura dos dados
    texto = campo_busca.get("1.0", tk.END)
    chassis = texto.splitlines()
    chassis = [p.strip() for p in chassis if p.strip()]

    if len(chassis) == 0:
        texto2.config(text="Nenhum chassi informado")
        return

    from playwright.sync_api import sync_playwright

    import os

    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = r"C:\Users\eolcb\AppData\Local\ms-playwright"

    with sync_playwright() as teste:
        navegador = teste.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        headless=True
        )
        
        pagina = navegador.new_page()

        pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

        barra['value'] = 0
        janela.update()

        resultado = []

        for i, chassi in enumerate(chassis):

            pagina.get_by_role("textbox", name="Digite o Chassi").fill(chassi)
            pagina.get_by_role("button", name="Pesquisar").click()

            pagina.wait_for_load_state("networkidle")

            pagina.wait_for_timeout(2000)

            texto = pagina.get_by_text("Veículo não se encontra no pátio")

            if texto.count() > 0:
                resposta = "Veículo não se encontra no pátio"
            else:
                resposta = "Veículo está no pátio"

            resultado.append(f"{chassi} - {resposta}")

            pagina.goto("https://www.consorciorioparkingcarioca.com/consulta-de-veiculo")

            # barra de progresso real
            barra['value'] = (i + 1) / len(chassis) * 100
            janela.update()

        navegador.close()

        barra['value'] = 100
        janela.update()

    # mensagem final
    texto2.config(text="Concluído! Escolha onde salvar o arquivo.")
    janela.update()

    # reset visual
    barra['value'] = 0
    janela.update()

    # salva arquivo UMA vez só
    criando_o_arquivo(resultado)


def criando_o_arquivo(resultado):

    from tkinter import Tk
    from tkinter.filedialog import asksaveasfilename

    Tk().withdraw()

    caminho_arquivo = asksaveasfilename(
        initialfile="chassis.txt",
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


# Botão
botao = tk.Button(janela, text="BUSCAR", width=20, command=busca_no_site)
botao.pack(pady=10)

janela.mainloop()
