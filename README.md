# TCC
Neste repositório você encontra tudo sobre o meu TCC:
- Monografia
- Modelo de aprendizado de máquina
- Conjunto de dados para o treinamento do modelo
- Protótipo do Ransomware
- Outros códigos que foram utilizados
- Chaves de criptografia (AES-128, e RSA-2048)

# Sobre o modelo:
- O modelo foi treinado com um conjunto de dados retirado do kaggle, portanto, pode não refletir dados reais (melhor explicado na monografia)
- O modelo também utiliza técnicas de XAI (Explainable Artificial Intelligence) ou (Inteligência Artificial Explicável), que me ajudaram a entender melhor meu conjunto de dados, após alguns problemas
- Após ser treinado, o modelo extrai informações de arquivos executáveis da pasta >C:\\Program Files< para continuar seus testes e gerar mais resultados (nenhum arquivo é alterado, o modelo apenas lê algumas informações que ele usará como as features nos testes)
- Após os testes, ele gera um arquivo de texto (.txt) com os resultados

# Sobre o protótipo:
- O protótipo foi criado como uma ferramenta didática (apenas) e é (quase) inofensivo
- O autor (EU) não se responsabiliza por quaisquer danos que o protótipo possa causar (SIMULE ELE POR SUA CONTA E RISCO!)
- O intuito do protótipo foi para aprender mais sobre criptografia e sobre o comportamento dos ransomwares

# COMO RODAR O PROTÓTIPO (Passo a Passo):
#OBSERVAÇÃO: talvez seja necessário um conhecimento em programação python para pequenos ajustes de código
- Desative o antivírus de seu computador
- Crie uma pasta (com qualquer nome) na sua área de trabalho (ou onde desejar)
- Inclua o arquivo do ransomware (.py) nessa pasta, juntamente com arquivos .txt ou .png ou .pdf (para os testes)
- Use o VS Code (ou outra plataforma) para rodar o arquivo .py do ransomware
- O ransomware deve criptografar TODOS os arquivos com as extensões especificadas (ele evita outros tipos de arquivos)
- Ele criptografa usando a chave AES-128 (ela será gerada pelo próprio vírus) e, por fim, criptografa a chave AES usando a chave RSA (pública)
- O ransomware também vai gerar um arquivo de ajuda (readme.help, que pode ser lido pelo bloco de notas) e uma ferramenta de decriptografia (.py) para o usuário
- A ferramenta de descriptografia deve ser gerada (e executada) juntamente com a chave RSA (privada, que deve estar incluída neste repositório) na MESMA pasta que foi criada por você na sua área de trabalho (para funcionar corretamente)
- Caso o usuário ainda não tenha salvo a chave RSA privada juntamente com a ferramenta de descriptografia, ela NÃO vai funcionar e deve exibir uma mensagem indicando que você pague o resgate (é só baixar a chave aqui)
- Por fim, todos os arquivos devem voltar ao normal e se tornarem acessíveis novamente!
- Se completar todos os passos corretamente, tudo deve correr bem, e será possível ver (de forma não tão sofisticada) o funcionamento de um ransomware :)
