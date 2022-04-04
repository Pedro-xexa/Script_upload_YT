import pyautogui
import time
import funcaoimg


pyautogui.alert(
    'O código vai começar. Cuidado para não mexer no teclado e no mouse pois pode dar erro')
pyautogui.PAUSE = 0.5

#abrir o you tube studio#
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.keyDown('win')
pyautogui.press('up')
pyautogui.keyUp('win')
pyautogui.write('https://studio.youtube.com/channel/UCGVzpOEAk9Fjm1GKwRh4uzw')
pyautogui.press('enter')
time.sleep(2)

#selecionar a opção enviar videos#
funcaoimg.clicar_na_imagem('enviar.png', pyautogui)

#abrir pasta com o arquivo e maximizar#
pyautogui.press('win')
pyautogui.write('videoaula')
pyautogui.press('enter')
time.sleep(1)
pyautogui.keyDown('win')
pyautogui.press('up')
pyautogui.keyUp('win')
time.sleep(1)

#Arrastar video da pasta para o menu#
pyautogui.moveTo(227, 241)
pyautogui.mouseDown()
time.sleep(1)
pyautogui.moveTo(929, 525, 1)
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
funcaoimg.selecionar('selecionar.png', pyautogui)
time.sleep(1)
pyautogui.mouseUp()

# colocar conteudo como não infantil#
time.sleep(3)
pyautogui.scroll(-400)
funcaoimg.clicar_nao_infantil('naoinfantil.png', pyautogui)
#selecionar visibilidade#
funcaoimg.visibilidade('visibilidade.png', pyautogui)

#selecionar não listado#
funcaoimg.naolistado('naolistado.png', pyautogui)

#finalização#
pyautogui.alert('O código acabou de rodar, verifique os campos na aba Detalhes e se a opção "Não listado" na aba de Visibilidade está selecionada. Por favor selecione a Playlist para qual o vídeo fará parte')
