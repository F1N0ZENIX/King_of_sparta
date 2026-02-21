import os
import time


# -------- limpar tela --------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# -------- tela inicial --------
def tela_inicial():
    limpar_tela()

    print(r"""
██╗  ██╗██╗███╗   ██╗ ██████╗      ██████╗ ███████╗     ███████╗██████╗  █████╗ ██████╗ ████████╗ █████╗ 
██║ ██╔╝██║████╗  ██║██╔════╝     ██╔═══██╗██╔════╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
█████╔╝ ██║██╔██╗ ██║██║  ███╗    ██║   ██║█████╗       ███████╗██████╔╝███████║██████╔╝   ██║   ███████║
██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║   ██║██╔══╝       ╚════██║██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║
██║  ██╗██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║          ███████║██║     ██║  ██║██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝          ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
""")

    print("\n🔥 Bem-vindo ao jogo!")
    print("⚔ Prepare-se para a batalha, guerreiro espartano!\n")
    input("Pressione ENTER para começar...")


# -------- início do jogo --------
def iniciar_jogo():
    limpar_tela()
    print ("Você acorda em uma prisão, ao seu lado tem um cadaver já em decomposição, você precisa fugir daí")
    print("[1] Procurar algo no corpo")
    print("[2] explorar a cela")
    escolha1 = int(input(" "))
    if escolha1 == 1:
        limpar_tela()
        print("você encontrou uma colher, e agora?")
        print ("[1] ver inventário")
        print ("[2] explorar a cela")
        e11 = int(input(" "))
        if e11 == 2:
        	limpar_tela()
        	print ("Você encontrou um buraco, gostaria de usar sua colher para cavar?")
        	print("[1]sim")
        	print("[2]não")
        	e112 =int(input (" "))
        	if e112 == 1:
        		limpar_tela()
        		print("depois de horas você consegue escapar")
        		print("Você conseguiu o Final Beta")
        if e11 == 1:
            limpar_tela()
            print ("🥄")
            print ("[1] fechar inventário")
            e111 = int(input(" "))
            if e111 == 1:
            	limpar_tela()
            	print ("e agora?")
            	print ("[1] explorar a cela")
            	print ("[2] esperar")
            	e1111 = int(input(" "))
            	if e1111 == 1:
            		limpar_tela()
            		print ("Você encontrou um buraco? quer usar a colher para cavar?")
            		print ("[1] sim")
            		print ("[2] não")
            		e11111 = int(input (" "))
            		if e11111 == 1:
            			limpar_tela()
            			print ("algumas horas depois você consegue fugir parabéns!")
            			print ("Você conseguiu o Final beta inv")
    time.sleep(2)
    


# -------- programa principal --------
tela_inicial()
iniciar_jogo()