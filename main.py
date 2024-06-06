import pyautogui as gui
import webbrowser as web
import time as tm
from datetime import datetime, time

numero_telefone = '1_4508505068'
hora_envio = time(hour=20, minute=30)  # Este é o horário de envio da mensagem

while True:
    agora = datetime.now()
    hora_atual = agora.time().replace(second=0, microsecond=0)  # Hora atual sem segundos

    if hora_atual == hora_envio:
        web.open(f'https://web.whatsapp.com/send?phone={numero_telefone}')
        tm.sleep(25)  # Espera o WhatsApp Web carregar
        gui.write('BOA NOITE, FAMILIA!!')
        gui.press('enter')
        tm.sleep(10)  # Espera enviar mensagem
        break

    tm.sleep(20)  # Verifica a cada minuto