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


def login():
    time.sleep(5)
    if not pyautogui.locateOnScreen(("caso1.png" or "senha.png"), confidence=0.1):
        pyautogui.alert("Você já está logado.")
    elif not pyautogui.locateOnScreen("espera.png", confidence=0.1):
        pyautogui.alert("Aperte 'ok' para fazer login")
        while True:
            if not pyautogui.locateOnScreen("caso1.png", confidence=0.1):
                time.sleep(1)
            else:
                time.sleep(1)
                pyautogui.click(x=954, y=392)
            
            if not pyautogui.locateOnScreen("senha.png", confidence=0.1):
                time.sleep(1)
            else:
                time.sleep(1)
                pyautogui.click(x=947, y=438)
                break
        

# Abrir navegador
pyautogui.hotkey("win", "1")

# Entrar na página dos chalés
localizar_clicar("pag_chale.png", x=74, y=85, dalay=1)

# Tratar caso de login
login()

time.sleep(2)

# Apertar o botão "financeiro"
while True:
    if not pyautogui.locateOnScreen("espera.png", confidence=0.1):
        time.sleep(1)
        break
    else:
        time.sleep(2)
        pyautogui.click(x=1428, y=191)
        break

# Apertar botão de fatura "fatura"
localizar_clicar("espera1.png", x=1416, y=311, dalay=2)

# Boleto
while True:
    if not pyautogui.locateOnScreen("tem_boleto.png", confidence=0.1):
        pyautogui.alert("Não tem nenhum boleto em aberto!")
        break

    elif pyautogui.locateOnScreen("tem_boleto.png", confidence=0.1):
        # Clicar em boleto
        time.sleep(5)
        localizar_clicar("tem_boleto.png", x=451, y=536, dalay=1)

        time.sleep(1.5)

        pyautogui.click(
            x=831, 
            y=123, 
            clicks=4, 
            interval=0.3, 
            button='left'
        )

        pyautogui.scroll(-600)
        break

time.sleep(1.5)
pyautogui.alert("O código acabou")
