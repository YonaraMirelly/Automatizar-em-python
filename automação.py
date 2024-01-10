#Primeiro você precisa instalar a biblioteca no seu pc : pip install pyautogui

# .press() -> serve para pressionar uma tecla no teclado
# .write() -> serve para escrever com o teclado (como se fosse você digitando)
# .click() -> serve para clicar em algum lugar específico da tela com o mouse 
# .PAUSE = -> serve para definir o tempo de espera entre os comandos pyautogui
# .hotkey() -> serve para combinar teclas (ctrl C + ctrl V)
# .scroll() -> serve para rolar a tela : pra cima ou pra baixo
# time.sleep() -> tempo para esperar que o site carregue ANTES de começar a próxima etapa   
import pyautogui
import time
pyautogui.PAUSE = 2
pyautogui.press("win") #pressiona a aba do windows
pyautogui.write("chrome") #escreve 
pyautogui.press("enter") #entra

time.sleep(2)
# posicionei o mouse na minha conta do google chrome, mas se o seu 
# pc já estiver configurado para abrir direto, ele vai abrir direto...
# desse modo vc não precisaria desse comando aqui debaixo
pyautogui.click(x=549, y=785) 
pyautogui.click(x=506, y=101) # clica na aba de pesquisa
pyautogui.write("https://play.freerice.com/categories/english-vocabulary") # escreve na aba de pesquisa
pyautogui.press("enter") # "dá enter"

# Mais Alguns Exemplos...
#pyautogui.write("https://quickdraw.withgoogle.com/?locale=pt_BR") ...site para desenhar
#pyautogui.write("https://stars.chromeexperiments.com/") ...site interestelar
#pyautogui.write("http://weavesilk.com/") ...site de IA 

# Com esses conhecimentos, você consegue criar o seu código para
# automatizar tarefas repetitivas, simplificar processos e economizar tempo.