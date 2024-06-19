# Manipulando arquivos texto
import os

with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write("Estou aqui!\n")
    linhas = ['Proxima linha', 'Outra linha']
    arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem."
with open('arquivoteste.txt', 'w') as arquivo:
    arquivo.write(texto)

arquivo = open('teste2.txt', 'w')
arquivo.write(texto + "\n")
arquivo.write("Outra linha" + "\n")
arquivo.write("Finalizei o  texto." + "\n")
arquivo.close()

with open('teste2.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

conteudo = open('arquivoteste.txt', 'r')
print(conteudo.read())
conteudo.close()

lista = []
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
    for linha in linhas:
        lista.append(linha)

for linha in lista:
    print(linha)
    

# os.rename("arquivo.txt", "excluir.txt")
# os.remove("excluir.txt")  
# os.remove("arquivoteste.txt")  
# os.remove("teste2.txt")  

caminho_pasta = "./"
arquivos = os.listdir(caminho_pasta)
for arquivo in arquivos:
    print(arquivo)

prefixo = "novo_"
outra_pasta = "./excluir/"
for arquivo in arquivos:
    caminho_atual = os.path.join(caminho_pasta, arquivo)
    renomeado = os.path.join(outra_pasta, prefixo + arquivo)
    os.rename(caminho_atual, renomeado)
