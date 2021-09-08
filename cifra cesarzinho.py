import string
from time import process_time


alfabeto = string.ascii_lowercase 

def criptografar():
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Bem-Vindo ao Nosso Programa.")
    print("Programa Feito Por Rafael J. Tiago S.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    message = input("Escreva sua mensagem aqui: ").lower()
    print()
    chave = int(input("Coloque sua chave aqui: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    criptografada_mensagem = ""

    for b in message:

        if b in alfabeto:
            posição = alfabeto.find(b)
            nova_posição = (posição + chave) % 26
            nova_mensagem = alfabeto[nova_posição]
            criptografada_mensagem += nova_mensagem
        else:
            criptografada_mensagem += b

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Sua Mensagem Criptografada é:\n")
    print(criptografada_mensagem)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
criptografar()

def decrypt():
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    encrypted_message = input("Escreva sua mensagem aqui para ser descriptografada: ").strip()
    print()
    chave = int(input("Escreva sua chave: "))
    
    decrypted_message = ""

    for b in encrypted_message:

        if b in alfabeto:
            posição = alfabeto.find(b)
            nova_posição = (posição - chave) % 26
            nova_mensagem = alfabeto[nova_posição]
            decrypted_message += nova_mensagem
        else:
            decrypted_message += b

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Sua mensagem descriptografada é:\n")
    print(decrypted_message)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

decrypt()
