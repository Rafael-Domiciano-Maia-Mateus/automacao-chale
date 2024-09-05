import pyautogui
import time

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

time.sleep(2)

# Tratar caso de login
if not pyautogui.locateOnScreen("espera.png", confidence=0.1):
    if pyautogui.locateOnScreen("caso1.png", confidence=0.1):
        pyautogui.alert("Vai ter que fazer login, aperte 'ok' para confirmar")
        while True:
            # Clicar em confirmar email
            localizar_clicar("caso1.png", x=954, y=392, dalay=2)

             # Clicar em confirmar senha
            localizar_clicar("senha.png", x=947, y=438, dalay=1)
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
localizar_clicar("espera1.png", x=1416, y=311, dalay=2)

# Avisar que não tem nenhuma fatura pendente
while True:
    if not pyautogui.locateOnScreen("tem_boleto.png", confidence=0.1):
        pyautogui.alert("Não tem nenhum boleto em aberto!")
        break

# Clicar em boleto
time.sleep(5)
localizar_clicar("tem_boleto.png", x=451, y=536, dalay=1)

# Linhar o codigo de barras
pyautogui.click(
    x=831, 
    y=123, 
    clicks=5, 
    interval=0.25, 
    button='left'
)

pyautogui.scroll(-500)

# Fim do código
time.sleep(2)
pyautogui.alert("O código acabou")
