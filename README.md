# 🚗 Conecta Pátio

Automação em Python utilizando **Playwright** para consulta de veículos no site do Consórcio Rio Parking Carioca.

---

## 📌 Funcionalidades

- 🖥️ Interface gráfica (Tkinter)
- 🔎 Campo de busca de chassis
- 📊 Barra de carregamento funcional
- 🚗 Consulta automática de múltiplos veículos por chassi
- 📍 Verificação se o veículo está no pátio
- 📄 Geração automática de arquivo `.txt`
- 💾 Escolha do local de salvamento
- 🤖 Automação com Playwright
- ⚙️ Versão executável `.exe`

---

## 🛠 Tecnologias utilizadas

- Python 🐍
- Playwright 🌐
- Tkinter 🖼️
- PyInstaller 📦

---

## ⚙️ Como funciona

O usuário insere uma lista de chassis no sistema.

A automação executa:

1. Coleta dos chassis informados
2. Acesso ao site de consulta
3. Busca individual de cada chassi
4. Análise da resposta retornada
5. Geração de um arquivo `.txt` com os resultados

---

## 📄 Exemplo de saída

```txt
9BWZZZ377VT200001 - Veículo está no pátio
9BWZZZ377VT200002 - Veículo não se encontra no pátio
```

## 🚀 Melhorias futuras
- Interface mais moderna
- Exportação para Excel
- Melhor performance na automação
