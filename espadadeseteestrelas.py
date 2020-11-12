from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('ESPADA DE SETE ESTRELAS'.center(52), font='Consolas')],
    [sg.Text('Arquivo da conversa:', font='Consolas'), sg.Input(key='arq', size=(40, 1))],
    [sg.Text('Palavra marcada:    ', font='Consolas'), sg.Input(key='word', size=(40, 1))],
    [sg.Button('Buscar', font='Consolas', size=(52, 1))]
]

janela = sg.Window('ESPADA DE SETE ESTRELAS', layout)

while True:
    try:
        eventos, valores = janela.read()
        nome = valores['arq']
        palavra = valores['word'].lower()
        conversa = open(nome, 'rt', encoding="utf8")
        conversa = str(conversa.read().lower())
        total = conversa.count(palavra)
    except:
        print(f'Erro :/')
    else:
        if eventos == sg.WIN_CLOSED:
            break
        if total == 0 and eventos == 'Buscar':
            print(f'\n\033[37mA palavra \033[1;35m{palavra}\033[m não apareceu \033[1;31mnenhuma\033[m vez na conversa')
        elif total == 1 and eventos == 'Buscar':
            print(f'\n\033[37mA palavra \033[1;35m{palavra}\033[m apareceu \033[1;31m1\033[m vez na conversa')
        elif total > 1 and eventos == 'Buscar':
            print(f'\n\033[37mA palavra \033[1;35m{palavra}\033[m apareceu \033[1;31m{total}\033[m vezes na conversa')

print('\33[1;31mFIM DA EXECUÇÃO!\033[m')
