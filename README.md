# Consulta de placas

Automação em Python utilizando Playwright para consultar placas de veículos no site do Consórcio Rio Parking Carioca.

## Funcionalidades futuras

- Interface gráfica
- Geração de executável (.exe)
- Otimização de desempenho
- Exportação para Excel

## Funcionalidades

- Leitura de múltiplas placas pelo terminal
- Consulta automática no site
- Verificação se o veículo está no pátio
- Geração de arquivo `.txt` com os resultados
- Execução automatizada com Playwright

## Tecnologias utilizadas

- Python
- Playwright

## Como funciona

O usuário cola uma lista de placas no terminal.

O sistema:

1. Captura as placas digitadas
2. Acessa o site de consulta
3. Pesquisa cada placa automaticamente
4. Verifica a resposta retornada
5. Salva os resultados em um arquivo `placas.txt`

## Exemplo de saída

```txt
ABC1234 - Veículo está no pátio
XYZ9876 - Veículo não se encontra no pátio
```

## Como executar

Instale as dependências:

```bash
pip install playwright
playwright install

```
## Aviso

Projeto desenvolvido para fins de estudo e automação utilizando Playwright.
