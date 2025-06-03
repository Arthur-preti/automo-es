import pyautogui
import time
#pyautogui.click -> clicar em algo
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever algo
#pyautogui.hotkey -> uma combinação de teclas

#pausar 0.5 segundos para continuar
pyautogui.PAUSE = 0.5

#passo 1: entrar no sistema da empresa ou site - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("Enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")


#passo 2: fazer login
time.sleep(0.5)
pyautogui.click(891, 429)
pyautogui.write("arthurpreti6@gmail.com")
pyautogui.press("Tab")
pyautogui.write('arthurbacana')
pyautogui.click(960, 591)

#espera de segurança
time.sleep(3)

#passo 3: importar os dados

    #pandas -> ler arquivos de dados!!
import pandas as pd
tabela = pd.read_csv("produtos.csv")

#passo 4: Cadastrar os produtos
#passo 5: cadastrar até acabar!
    #pyautogui.scroll -> para scrollar, + para cima e - para baixo
for linha in tabela.index: #para cada linha da tabela
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(739, 315)
    pyautogui.write(codigo)
    pyautogui.press('Tab')

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('Tab')

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(f"{categoria}")
    pyautogui.press("Tab")
    pyautogui.scroll(-100)

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(f"{preco_unitario}")
    pyautogui.press("Tab")

    custo =  tabela.loc[linha, "custo"]
    pyautogui.write(f"{custo}")
    pyautogui.press("Tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")
    pyautogui.press("Enter")
    pyautogui.scroll(10000)

