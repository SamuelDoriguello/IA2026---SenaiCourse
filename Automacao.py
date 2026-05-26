import pyautogui as pt


pt.press('win')
pt.write('word')
pt.press('enter')
pt.sleep(5)

pt.leftClick(x=347, y=294)
texto = "Nesse pull request, o deploy automatizado no Heroku facilitou a resolução de conflito dos parametros passados em funções privadas."
pt.write(texto)
pt.sleep(1)
pt.hotkey('ctrl', 'b')

pt.sleep(1)
pt.leftClick(x = 448, y = 517)
nome = faker.name()
pt.write(nome)
pt.sleep(1)
pt.press('enter')
pt.hotkey('alt', 'F4')