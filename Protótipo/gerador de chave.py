from Crypto.PublicKey import RSA
import os

caminho_arquivo = os.path.abspath(__file__)
caminho_diretorio = os.path.dirname(caminho_arquivo)

caminho_publica = os.path.join(caminho_diretorio, 'public.key')
caminho_privada = os.path.join(caminho_diretorio, 'private.key')

# Gerar um par de chaves RSA (2048 bits para maior segurança)
key = RSA.generate(2048)

# Exportar a chave privada (você deve armazenar isso com segurança e nunca incluir no código)
private_key = key.export_key()
with open(caminho_privada, 'wb') as priv_file:
    priv_file.write(private_key)

# Exportar a chave pública para incluir no código
public_key = key.publickey().export_key()
with open(caminho_publica, 'wb') as pub_file:
    pub_file.write(public_key)

print("Chaves RSA geradas.")