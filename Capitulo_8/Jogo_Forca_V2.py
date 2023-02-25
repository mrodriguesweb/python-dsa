#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bibliotecas utilizadas
from urllib.request import urlopen
from bs4 import BeautifulSoup
from numpy import random


# In[ ]:


# Classe do jogo da Forca
class Hangman():
    
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_corretas = []
        self.letras_erradas = []
        self.palavra_atual = "_"
        
    # Checa se o player ganhou
    def checkWin(self):
        
        objeto = False
        
        if (self.palavra_atual.count('_') == 0):
            objeto = True
        else:
            objeto = False
        
        return objeto

    # Checa se o player perdeu
    def checkLose(self):
        
        objeto = False
        
        if (len(self.letras_erradas) == 6):
            objeto = True
        else:
            objeto = False
            
        return objeto

    # Apresenta o Input atual do player
    def showInput(self):
        nova_palavra = " "
        
        for letra in self.palavra:
            if letra in self.letras_corretas:
                nova_palavra += letra + " "
            elif letra == " ":
                nova_palavra += " "
            else:
                nova_palavra += "_ "

        return nova_palavra

    # Imprime o boneco da Forca
    def showHangman(self):
        if len(self.letras_erradas) == 0:
            print("  _____  \n" + " |     | \n" + " |     \n" + " |     \n" + " |     \n" + " |     \n")
        elif len(self.letras_erradas) == 1:
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |     \n" + " |     \n" + " |     \n")
        elif len(self.letras_erradas) == 2:
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |     |\n" + " |     \n" + " |     \n")
        elif len(self.letras_erradas) == 3: 
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |    /|\n" + " |     \n" + " |     \n")
        elif len(self.letras_erradas) == 4: 
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |    /|\ \n" + " |     \n" + " |     \n")
        elif len(self.letras_erradas) == 5:
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |    /|\ \n" + " |    / \n" + " |     \n")
        elif len(self.letras_erradas) == 6:
            print("  _____  \n" + " |     | \n" + " |     O\n" + " |    /|\ \n" + " |    / \ \n" + " |     \n")    
          
    # Verifica se o Player ganhou ou perdeu, para imprimir a mensagem
    def finalizaJogo(self):
        if (self.checkWin() == True):
            print("Parabéns! Você venceu!")
        elif (self.checkLose() == True):
            print("Suas tentativas acabaram. Tente novamente!")
    
    # Função principal do jogo, para o player realizar suas tentativas
    def adivinhaLetra(self):
        
        while (self.checkWin() == False) and (self.checkLose() == False):
            print("Tentativas erradas: {} \n".format(self.letras_erradas))
            letra_escolhida = input("Escolha uma letra: ")
            while (letra_escolhida not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')):
                letra_escolhida = input("Letra invalida. Escolha novamente: ")

            if (letra_escolhida in self.palavra) and (letra_escolhida not in self.letras_corretas):
                self.letras_corretas.append(letra_escolhida)
                print(self.showInput())
            elif (letra_escolhida in self.letras_corretas):
                print("Você já digitou essa letra!")
                print(self.showInput())
            else:
                print(self.showInput())
                self.letras_erradas.append(letra_escolhida)

            self.showHangman()
            self.palavra_atual = self.showInput()
            self.checkWin()


# In[ ]:


# Função para tratar os textos coletados (nome dos filmes)
def trata_texto(string):
    
    string = string.upper()
    
    nova_string = ""
    
    lista_vazio = [':', 'º', ',', '.', '!', "'", '...']
    lista_a = ['Ã', 'À', 'Á', 'Â']
    lista_o = ['Ó', 'Õ', 'Ô']
    lista_e = ['É', 'Ê']
    lista_space = ['·', '-']
    
    for letra in string:
        
        if letra in lista_vazio:
            nova_string += ""
        elif letra in lista_a:
            nova_string += "A"
        elif letra in lista_o:
            nova_string += "O"
        elif letra in lista_e:
            nova_string += "E"
        elif letra in lista_space:
            nova_string += " "
        elif letra == "Í":
            nova_string += "I"
        elif letra == "Ú":
            nova_string += "U"
        elif letra == " ":
            nova_string += " "
        else:
            nova_string += letra
            
    nova_string = nova_string.replace("II", "2")
    nova_string = nova_string.replace("VI ", "4 ")
    
    return nova_string


# In[ ]:


# url da página contendo os 250 melhores filmes de todos os tempos, pelo IMDB
url = "https://www.imdb.com/chart/top/"


# In[ ]:


# Abre a página (Retorna um objeto HTTP Response)
page = urlopen(url)


# In[ ]:


# Para extrair o HTML da página. Primeiro retorna uma sequencia de bytes, depois decodifica
html_bytes = page.read()
html = html_bytes.decode("utf-8")


# In[ ]:


soup = BeautifulSoup(html, "html.parser")


# In[ ]:


# Seleciona todas as tags 'img' no html
filme1 = list(soup.find_all("img"))


# In[ ]:


lista_filmes = []


# In[ ]:


# Extrai somente os nomes dos filmes
for item in filme1:
    
    inicio = str(item).index("alt=")
    fim = str(item).index("height")
    
    lista_filmes.append(trata_texto(str(item)[inicio + 5:fim - 2]))

    


# In[ ]:


print("------- JOGO DA FORCA -------")


# In[ ]:


print("- Boa Sorte !! - \n")


# In[ ]:


print("Tema: Filmes")


# In[ ]:


# Seleciona um filmes aleatório entre os 250
ind_palavra = random.randint(250)


# In[ ]:


palavra = lista_filmes[ind_palavra]


# In[ ]:


hang1 = Hangman(palavra)


# In[ ]:


hang1.adivinhaLetra()


# In[ ]:


hang1.finalizaJogo()

