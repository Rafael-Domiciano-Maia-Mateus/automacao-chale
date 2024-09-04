import pyautogui
import time
import json

pyautogui.alert("Não mexa em NADA! Quando o código acabar eu aviso")

pyautogui.PAUSE = 1

def localizar_clicar(img, x, y, dalay, conf=0.1):
    while True:
        if not pyautogui.locateOnScreen(img, confidence=conf):
            time.sleep(dalay)
        else:
            pyautogui.click(x=x, y=y)
            break


# Abrir navegador
pyautogui.hotkey("win", "1")

# Entrar na página dos chalés
localizar_clicar("pag_chale.png", x=74, y=85, dalay=1)

time.sleep(3)

# Tratar caso de login
if not pyautogui.locateOnScreen("espera.png", confidence=0.1):
    if pyautogui.locateOnScreen("caso1.png", confidence=0.1):
        pyautogui.alert("Vai ter que fazer login, aperte 'ok' para confirmar")
        while True:
            # Clicar em confirmar email
            localizar_clicar("caso1.png", x=954, y=388, dalay=2)

             # Clicar em confirmar senha
            localizar_clicar("senha.png", x=947, y=400, dalay=1)
            break

# Apertar o botão "financeiro"
while True:
    if not pyautogui.locateOnScreen("espera.png", confidence=0.1):
        time.sleep(1)
        break
    else:
        time.sleep(4)
        pyautogui.click(x=1428, y=191)
        break

# Apertar botão de fatura "fatura"
localizar_clicar("espera1.png", x=1416, y=277, dalay=2)

# Avisar que não tem nenhuma fatura pendente
while True:
    if not pyautogui.locateOnScreen("tem_boleto.png", confidence=0.1):
        pyautogui.alert("Não tem nenhum boleto em aberto!")
        break
    else:
        break   # Está com o "break porque o resto do código ainda não esta pronto"

time.sleep(2)
pyautogui.alert("O código acabou")
