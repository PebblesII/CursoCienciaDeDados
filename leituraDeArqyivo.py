with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write("Estou aqui!\n")
    linhas = ['Proxima linha', 'Outra linha']
    arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem."
with open('arquivoteste.txt', 'w') as arquivo:
    arquivo.write(texto)

arquivo = open('teste2.txt', 'w')
arquivo.write(texto)
arquivo.write("Outra linha")
arquivo.write("Finalizei o  texto.")
arquivo.close()

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

  
    