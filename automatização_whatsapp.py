import pyautogui as spam
import time

numero_de_mensagens = 0
msg = input('Mensagem ?')

i = 0

time.sleep(5)

for numero_de_mensagens in range(int(input('Numero De Mensagens ?'))):
    numero_de_mensagens  += 1
    spam.typewrite(msg)
    spam.press('ENTER')