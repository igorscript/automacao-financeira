import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# Solicita ao usuário o código da ação e as datas de início e fim
ticker = input("Digite o código da ação desejada: ")
data_inicial = input(
    "Insira a data inicial no formato inverso (ano-mês-dia): ")
data_final = input("Insira a data final no formato inverso (ano-mês-dia): ")

# Obtém os dados históricos da ação usando yfinance
dados = yfinance.Ticker(ticker).history(start=data_inicial, end=data_final)
fechamento = dados.Close

# Calcula a cotação máxima, mínima e média dos dados históricos
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_media = round(fechamento.mean(), 2)

# Define os detalhes do email
destinatario = input("Informe o endereço de email do destinatário aqui: ")
assunto = f'Relatório de Análises da Ação {ticker}'

# Monta a mensagem do email
mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker} - Período: {data_inicial} a {data_final}:

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minima}
Valor médio: R$ {valor_media}

Qualquer dúvida, estou à disposição!

Atte.
"""

# Abre o navegador e vai para o Gmail
webbrowser.open("https://www.gmail.com")
time.sleep(3)

# Configura uma pausa de 3 segundos entre as ações do pyautogui
pyautogui.PAUSE = 3

# Clica no botão 'Escrever' (coordenadas podem variar, ajustar conforme necessário)
pyautogui.click(x=99, y=213)

# Digita o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digita o assunto do email e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digita a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clica no botão 'Enviar' (coordenadas podem variar, ajustar conforme necessário)
pyautogui.click(x=708, y=660)

# Simula o atalho para fechar a janela (Alt + F4)
pyautogui.hotkey("alt", "f4")

# Exibe uma mensagem confirmando o envio do email
print("Email enviado com sucesso!")
