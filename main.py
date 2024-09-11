import pyautogui
import time

pyautogui.alert("Não mexa em NADA! Quando o código acabar eu aviso")

pyautogui.PAUSE = 1

def localizar_clicar(img, x, y, dalay, conf=0.2):
    while True:
        if not pyautogui.locateOnScreen(img, confidence=conf):
            time.sleep(dalay)
        else:
            pyautogui.click(x=x, y=y)
            break


def login():
    try:
        time.sleep(4.5)
        while True:
            if pyautogui.locateOnScreen("caso1.png", confidence=0.7):
                pyautogui.click(x=954, y=421)
                if pyautogui.locateOnScreen("senha.png", confidence=0.1):
                    time.sleep(1)
                    pyautogui.click(x=919, y=441)
                    break
            else:
                break

    except Exception as e:
        pyautogui.alert("Você já está logado.")


# Abrir navegador
pyautogui.hotkey("win", "1")

# Entrar na página dos chalés
localizar_clicar("pag_chale.png", x=74, y=85, dalay=1)

# Tratar caso de login
login()

# Apertar o botão "financeiro"
time.sleep(2)
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

