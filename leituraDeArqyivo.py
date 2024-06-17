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
arquivo.write("\nOutra linha\n")
arquivo.write("Finalizei o  texto.")
arquivo.close()


        
  
    