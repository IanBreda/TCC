import pefile
import shap
import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Função para extrair informações PE
def extrair_informacoes_pe(arquivo_pe):
    try:
        pe = pefile.PE(arquivo_pe)

        number_of_sections = pe.FILE_HEADER.NumberOfSections
        size_of_stack_reserve = pe.OPTIONAL_HEADER.SizeOfStackReserve
        export_size = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
        resource_size = pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size

        # Retornar como dicionário
        return {
            'NumberOfSections': number_of_sections,
            'SizeOfStackReserve': size_of_stack_reserve,
            'ExportSize': export_size,
            'ResourceSize': resource_size
        }
    except Exception as e:
        print(f"Erro ao processar {arquivo_pe}: {e}")
        return None

# Caminhos para os arquivos
caminho_arquivo = os.path.abspath(__file__)
caminho_diretorio = os.path.dirname(caminho_arquivo)
caminho_planilha = os.path.join(caminho_diretorio, 'data_file.csv')

# Carregar os dados
df = pd.read_csv(caminho_planilha)

# Definir features e rótulos
features = ['ExportSize', 'NumberOfSections', 'SizeOfStackReserve', 'ResourceSize']
X = df[features]
y = df['Benign']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Treinar o modelo
rf = RandomForestClassifier(n_estimators=30, random_state=0, max_depth=5)
rf.fit(X_train, y_train)

# Criar o explicador SHAP para o modelo RandomForest
explainer = shap.TreeExplainer(rf)

# Cálculo dos valores SHAP para o conjunto de teste
shap_values = explainer(X_train)

# Selecionando os valores SHAP para a classe 1
shap_values_class_1 = shap_values[:, :, 1]

# Plotando o gráfico de resumo para a classe 1
shap.summary_plot(shap_values_class_1, X_train)

y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Precisão do Modelo:", accuracy)

pipeline = Pipeline([
    ('classifier', RandomForestClassifier(n_estimators=30, random_state=0))
])
cross_val_scores = cross_val_score(pipeline, X, y, cv=5)
print("Validação Cruzada:", cross_val_scores)
print("Média da validação cruzada:", cross_val_scores.mean())

print("\nReport das Classificações:")
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão:")
print(conf_matrix)

importances = rf.feature_importances_
feature_names = X.columns

print('\nImportância das Features:')
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance}")

# Caminho para salvar resultados
nome_arquivo = 'resultados_teste.txt'
resultados_teste_modelo = os.path.join(caminho_diretorio, nome_arquivo)

# Processar arquivos .exe
caminho_diretorio = 'C:\\Program Files'
with open(resultados_teste_modelo, 'w') as file:  # Abrir arquivo para escrita
    for diretorio, pasta, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo.endswith('.exe'):
                arquivo_pe = os.path.join(diretorio, arquivo)
                
                # Extrair informações do arquivo PE
                info = extrair_informacoes_pe(arquivo_pe)
                if info is None:
                    continue
                
                # Criar DataFrame com as informações extraídas
                new_data = pd.DataFrame([info])
                
                # Garantir que as colunas estão na ordem correta
                new_data = new_data[features]
                
                # Fazer a previsão
                result = rf.predict(new_data)
                
                # Salvar o resultado no arquivo
                if result[0] == 0:
                    file.write(f"{arquivo_pe}, ransomware\n")
                else:
                    file.write(f"{arquivo_pe}, benigno\n")

print('Arquivo gerado, encerrando...')
