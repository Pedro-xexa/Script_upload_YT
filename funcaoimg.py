from python_imagesearch.imagesearch import imagesearch


def clicar_na_imagem(path, pyautogui):

    pos = imagesearch(path)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
    else:
        print("image not found")

###################################################################


def clicar_nao_infantil(path, pyautogui):

    pos = imagesearch(path)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
    else:
        print("image not found")

###################################################################


def visibilidade(path, pyautogui):
    pos = imagesearch(path)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
    else:
        print("image not found")

####################################################################


def naolistado(path, pyautogui):
    pos = imagesearch(path)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
    else:
        print("image not found")

###################################################################


def selecionar(path, pyautogui):
    pos = imagesearch(path)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1], 1)
    else:
        print("image not found")
