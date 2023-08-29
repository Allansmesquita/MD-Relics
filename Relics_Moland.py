"""Relics Auto Click ATUALIZADO 28/04 --> FUNCIONOU!!"""
import time
import pyautogui


pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

selecionar_boss = "não"
for stage in range(1, 4, +1):
    print('iniciando stage {}'.format(stage))
    # selecionar BOSS

    turno = 1

    boss = pyautogui.locateCenterOnScreen('boss.PNG', confidence=0.9)
    while boss == None:
        time.sleep(1)
        # selecionar marauder

        relics = pyautogui.locateCenterOnScreen(
            'relicsmau.PNG', confidence=0.85)

        if relics is not None:
            time.sleep(1)
            pyautogui.click(relics)

            print('Marauder {} encontrado'.format(turno))
            # procurar = "não"
            # inserir function proximos passos retornar "procurar = não"

            autoc = pyautogui.locateCenterOnScreen(
                'autochallenge.PNG', confidence=0.9)
            if autoc is not None:
                pyautogui.click(autoc)
                print("Challenge em andamento (click icone )")
            else:
                pyautogui.click(1053, 830)
                print("Challenge em andamento (click coord)")
            time.sleep(1)

            challengeEmAndamento = "sim"
            while challengeEmAndamento == "sim":
                try:
                    time.sleep(1)
                    # clicar em victory
                    victory = pyautogui.locateCenterOnScreen(
                        'victory.PNG', confidence=0.9)
                    if victory is not None:
                        pyautogui.click(victory)
                        print("Venceu um challenge")
                        challengeEmAndamento = "não"
                        time.sleep(5)
                    # print("Victory is: ", victory)
                except:  # pylint: disable=bare-except
                    time.sleep(10)
                    print("Não Terminou o Challenge")

            # Skills
            pyautogui.click(828, 630, duration=0.2)
            time.sleep(5)
            print("Round {} finalizado".format(turno))
            time.sleep(1)

        else:
            print(
                "Marauder Não encontrado, escolher entre HP recovery ou Support Station")
            time.sleep(1)

            hp_restory = pyautogui.locateCenterOnScreen(
                'restorehp.png', confidence=0.94)
            time.sleep(1)
            if hp_restory is not None:
                time.sleep(1)
                pyautogui.click(hp_restory)
                print('HP Recovery do round {} encontrado'.format(turno))
                time.sleep(1)
                pyautogui.click(1047, 711)

            else:
                support_station = pyautogui.locateCenterOnScreen(
                    'supportstation.png', confidence=0.94)  # a partir do 89 acertou o alvo
                time.sleep(1)
                if support_station is not None:
                    time.sleep(1)
                    pyautogui.click(support_station)
                    print(
                        'Support station foi a unica opção no round {}'.format(turno))
                    time.sleep(1)
                    pyautogui.click(970, 577)  # selecionar hero
                    time.sleep(1)
                    pyautogui.click(970, 731)  # yes
                else:
                    print('Nada foi encontrado.')
                    pyautogui.scroll(2000)

                    break  # modificação24/05

        boss = pyautogui.locateCenterOnScreen('boss.PNG', confidence=0.90)
        turno = turno + 1

    if boss is not None:
        print('Selecionar boss agora')

        time.sleep(1)
        pyautogui.click(boss)
        # selecionar botão autochallenge
        time.sleep(5)
        autoc = pyautogui.locateCenterOnScreen(
            'autochallenge.PNG', confidence=0.7)
        pyautogui.click(autoc)
        print("Challenge final em andamento")
        time.sleep(5)
        challengeEmAndamento = "sim"
        while challengeEmAndamento == "sim":
            try:
                time.sleep(1)
                # clicar em victory
                victory = pyautogui.locateCenterOnScreen(
                    'victory.PNG', confidence=0.7)
                if victory is not None:
                    pyautogui.click(victory)
                    print("Venceu o challenge final")
                    challengeEmAndamento = "não"
                    time.sleep(5)
            except:  # pylint: disable=bare-except
                time.sleep(15)
                print("Não Terminou o Challenge final")

        # Skills
        pyautogui.click(828, 630, duration=0.2)
        time.sleep(5)
    else:
        print('Boss não encontrado!')
        time.sleep(5)

    teleport = pyautogui.locateCenterOnScreen('teleport.PNG', confidence=0.7, minSearchTime=5)
    if teleport is not None:
        print('Teleport Encontrado')  # >>CLICK TP<<<
        pyautogui.click(teleport)
        time.sleep(1)

        yes = pyautogui.locateCenterOnScreen('yes.PNG', confidence=0.7)
        pyautogui.click(yes)
        if yes is not None:
            print('Teletransportanto para proximo stage')  # >>>YES<<<
    else:
        print('Teleport não encontrado 1')
        pyautogui.click(965, 351)  # clicar no teleport
        time.sleep(1)
        next_stage = pyautogui.locateCenterOnScreen('Next_Stage.PNG', confidence=0.7)
        if next_stage is not None:
            pyautogui.click(1058, 708)  # BOTAO YES
        else:
            autoc = pyautogui.locateCenterOnScreen('autochallenge.PNG', confidence=0.7)
            print('Selecionar Autochallenge vs Boss')
            pyautogui.click(autoc)
            i = 1
            challengeEmAndamento = "sim"
            while challengeEmAndamento == "sim":
                try:
                    time.sleep(1)
                    # clicar em victory
                    victory = pyautogui.locateCenterOnScreen('victory.PNG', confidence=0.7)
                    if victory is not None:
                        pyautogui.click(victory)
                        print("Venceu o challenge final")
                        challengeEmAndamento = "não"
                        time.sleep(5)
                        # Skills
                        pyautogui.click(828, 630, duration=0.2)
                        time.sleep(5)
                        #SELEÇÃO DO TELEPORT
                        teleport = pyautogui.locateCenterOnScreen('teleport.PNG', confidence=0.7, minSearchTime=5)
                        if teleport is not None:
                            print('Teleport Encontrado')  # >>CLICK TP<<<
                            pyautogui.click(teleport)
                            time.sleep(1)

                            yes = pyautogui.locateCenterOnScreen('yes.PNG', confidence=0.7)
                            pyautogui.click(yes)
                            if yes is not None:
                                print('Teletransportanto para proximo stage')  # >>>YES<<<
                            else:
                                print('Teleport não encontrado 2')                            
                    else: 
                        time.sleep(15)
                        print("Não Terminou o Challenge final")
                        i = i+1
                        if i > 10:
                            break

                        
                except:  # pylint: disable=bare-except
                    time.sleep(15)
                    print("Except")
                    
            

    print("Stage {} finalizado com Sucesso".format(stage))
    selecionar_boss = "não"
time.sleep(2)
