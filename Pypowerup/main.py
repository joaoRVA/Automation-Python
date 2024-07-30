# Esse é um projeto de automação de preenchimento dos dados de um sistema

import pyautogui
import time
import pandas as pd

# comandos basicos do pyautogui:
# pyautogui.click()
# pyautogui.press()
# pyautogui.hotkey()
# pyautogui.scroll()
# pyautogui.write()

# passo 1: abrir o navegador
# passo 2: entrar no sistema da empresa / link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 3: fazer login
# passo 4: importar os dados dos produtos e preenche-los no sistema
# passo 5: looping do passo 4 até acabar



# abrir o navegador
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)
# entrar no sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# fazer login
time.sleep(2)
pyautogui.click(x=974, y=475)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("joaovitordeaquino18@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

#importar os dados dos produtos e preenche-los no sistema
time.sleep(3)


# pandas

tabela = pd.read_csv('Pypowerup/produtos.csv')

# Repetição
for linha in tabela.index:
    pyautogui.click(x=641, y=338)
    # codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    # obs
    if str(tabela.loc[linha, "obs"]) != 'nan':
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # Enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    time.sleep(2)