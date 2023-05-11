#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Projeto 2</font>
# 
# ## <font color='blue'>Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo</font>

# ![DSA](imagens/projeto2.png)

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[2]:


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# ## Carregando os Dados

# In[3]:


# Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')


# In[4]:


# Shape
df_dsa.shape


# In[5]:


# Amostra dos dados
df_dsa.head()


# In[6]:


# Amostra dos dados
df_dsa.tail()


# ## Análise Exploratória

# In[7]:


# Colunas do conjunto de dados
df_dsa.columns


# In[8]:


# Verificando o tipo de dado de cada coluna
df_dsa.dtypes


# In[9]:


# Resumo estatístico da coluna com o valor de venda
df_dsa['Valor_Venda'].describe()


# In[10]:


# Verificando se há registros duplicados
df_dsa[df_dsa.duplicated()]


# In[11]:


# Verificando de há valores ausentes
df_dsa.isnull().sum()


# In[12]:


df_dsa.head()


# ## Pergunta de Negócio 1:
# 
# ### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# In[13]:


from sqlalchemy import create_engine
import sqlite3


# In[14]:


engine = create_engine('sqlite:///dsa_perguntas.db')

df_dsa.to_sql('tbl_dataset', engine, if_exists='replace')


# In[15]:


conn = sqlite3.connect('dsa_perguntas.db')


# In[16]:


cur = conn.cursor()


# In[66]:


query = """ SELECT Cidade, round(SUM(Valor_Venda), 2) FROM tbl_dataset WHERE Categoria = "Office Supplies" GROUP BY Cidade ORDER BY 2 DESC LIMIT 5 """


# In[67]:


cur.execute(query)


# In[68]:


print(cur.fetchall())


# ## Pergunta de Negócio 2:
# 
# ### Qual o Total de Vendas Por Data do Pedido?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[85]:


query = """ SELECT Data_Pedido, round(SUM(Valor_Venda), 2) FROM tbl_dataset GROUP BY Data_Pedido """


# In[86]:


cur.execute(query)


# In[87]:


dados = cur.fetchall()


# In[88]:


datas = []
totais = []
for i in range(0, len(dados)):
    datas.append(dados[i][0])
    totais.append(dados[i][1])


# In[93]:


plt.figure(figsize = (200, 6))
plt.bar(datas, totais, label = 'Totais por Data', color = 'blue')
plt.legend()
plt.show()


# ## Pergunta de Negócio 3:
# 
# ### Qual o Total de Vendas por Estado?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[94]:


query = """ SELECT Estado, round(SUM(Valor_Venda), 2) FROM tbl_dataset GROUP BY Estado """


# In[95]:


cur.execute(query)


# In[96]:


dados = cur.fetchall()


# In[97]:


estados = []
totais = []
for i in range(0, len(dados)):
    estados.append(dados[i][0])
    totais.append(dados[i][1])


# In[98]:


plt.figure(figsize = (70, 6))
plt.bar(estados, totais, label = 'Totais por Estado', color = 'blue')
plt.legend()
plt.show()


# ## Pergunta de Negócio 4:
# 
# ### Quais São as 10 Cidades com Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[99]:


query = """ SELECT Cidade, round(SUM(Valor_Venda), 2) FROM tbl_dataset GROUP BY Cidade ORDER BY 2 DESC LIMIT 10 """


# In[100]:


cur.execute(query)


# In[101]:


dados = cur.fetchall()


# In[102]:


cidades = []
totais = []
for i in range(0, len(dados)):
    cidades.append(dados[i][0])
    totais.append(dados[i][1])


# In[107]:


plt.figure(figsize = (20, 6))
plt.bar(cidades, totais, label = 'Cidades com mais vendas', color = 'blue')
plt.legend()
plt.show()


# ## Pergunta de Negócio 5:
# 
# ### Qual Segmento Teve o Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de pizza.

# In[108]:


query = """ SELECT Segmento, round(SUM(Valor_Venda), 2) FROM tbl_dataset GROUP BY Segmento ORDER BY 2 DESC """


# In[109]:


cur.execute(query)


# In[110]:


dados = cur.fetchall()


# In[111]:


segmentos = []
totais = []
for i in range(0, len(dados)):
    segmentos.append(dados[i][0])
    totais.append(dados[i][1])


# In[114]:


plt.figure(figsize = (10, 6))
plt.pie(totais, labels = segmentos, startangle = 90, shadow = True, explode = (0,0.2,0))
plt.show()


# ## Pergunta de Negócio 6 (Desafio Nível Baby):
# 
# ### Qual o Total de Vendas Por Segmento e Por Ano?

# In[20]:


query = """ SELECT Segmento, SUBSTRING(Data_Pedido, 7, 4) as Ano, round(SUM(Valor_Venda), 2) 
    FROM tbl_dataset GROUP BY Segmento, SUBSTRING(Data_Pedido, 7, 4) ORDER BY 2 """


# In[21]:


cur.execute(query)


# In[22]:


dados = cur.fetchall()


# In[61]:


segmentos = []
anos = []
totais = []
for i in range(0, len(dados)):
    segmentos.append(dados[i][0])
    anos.append(dados[i][1])
    totais.append(dados[i][2])
    
segmentos = list(set(segmentos))
anos = list(set(anos))

lst_valores = []
valores = []

x = 0

for i in range(0, len(anos)):
    
    for j in range(0, len(segmentos)):
        
        valores.insert(j, totais[x])
        x = x + 1
        
    lst_valores.insert(i, valores)
    valores = []
        
print(lst_valores)


# In[63]:


posicoes = np.arange(len(anos))
largura = 0.2

fig, ax = plt.subplots()

anos.sort()

for i, seg in enumerate(segmentos):
    barras = ax.bar(posicoes + i * largura, [lst_valores[j][i] for j in range(len(anos))], largura, label=seg)

ax.set_ylabel('Valor de Venda')
ax.set_xlabel('Ano')
ax.set_xticks(posicoes + largura * (len(segmentos) - 1) / 2)
ax.set_xticklabels(anos)
ax.legend(title='Segmento')

plt.show()


# ## Pergunta de Negócio 7 (Desafio Nível Júnior):
# 
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# 
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# 
# ### Quantas Vendas Receberiam 15% de Desconto?

# In[64]:


df_dsa.head()


# In[71]:


query = """ SELECT COUNT(Valor_Venda) 
    FROM tbl_dataset WHERE Valor_Venda > 1000 """


# In[88]:


cur.execute(query)


# In[89]:


print(f'Total de vendas impactadas pelo desconto de 15%: {list(cur.fetchall())[0][0]}')


# In[117]:


query = """ SELECT SUM(Valor_Venda),
                (SELECT SUM(Valor_Venda) FROM tbl_dataset WHERE Valor_Venda > 1000),
                (SELECT SUM(Valor_Venda) - ((SUM(Valor_Venda) * 15) / 100) FROM tbl_dataset WHERE Valor_Venda > 1000),
                (SELECT SUM(Valor_Venda) FROM tbl_dataset WHERE Valor_Venda < 1000),
                (SELECT SUM(Valor_Venda) - ((SUM(Valor_Venda) * 10) / 100) FROM tbl_dataset WHERE Valor_Venda < 1000),
                (SELECT SUM(Valor_Venda) - ((SUM(Valor_Venda) * 15) / 100)
    FROM tbl_dataset WHERE Valor_Venda > 1000) + (SELECT SUM(Valor_Venda) - ((SUM(Valor_Venda) * 10) / 100)
    FROM tbl_dataset WHERE Valor_Venda < 1000)
    FROM tbl_dataset """


# In[139]:


cur.execute(query)


# In[140]:


dados = cur.fetchall()


# In[141]:


print(f'Soma das vendas: {round(dados[0][0], 2)}\nSoma das vendas impactadas pelo desconto de 15%: {round(dados[0][1], 2)} \nTotal após desconto aplicado de 15%: {round(dados[0][2], 2)} \nSoma das vendas impactadas pelo desconto de 10%: {round(dados[0][3], 2)} \nTotal após desconto aplicado de 10%: {round(dados[0][4], 2)} \nSoma total das vendas após os descontos: {round(dados[0][5], 2)} \n      ')


# ## Pergunta de Negócio 8 (Desafio Nível Master):
# 
# ### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

# In[62]:


query = """ SELECT AVG(Valor_Venda),
                AVG(case when Valor_Venda > 1000 THEN (Valor_Venda - (Valor_Venda * 0.15)) ELSE Valor_Venda END) AS MEDIA
    FROM tbl_dataset """


# In[63]:


cur.execute(query)


# In[64]:


dados = cur.fetchall()


# In[65]:


print(f'Média geral das vendas: {round(dados[0][0], 2)}\nMédia geral das vendas após o desconto de 15%: {round(dados[0][1], 2)} ')


# In[60]:


totais = [round(dados[0][0], 2), round(dados[0][1], 2)]
labels = ['Média geral das vendas (atual)', 'Média geral das vendas após o desconto de 15%']
cores = ['green', 'red']


# In[61]:


plt.figure(figsize = (10, 5))
plt.bar(labels, totais, color = cores)
plt.show()


# ## Pergunta de Negócio 9 (Desafio Nível Master Ninja):
# 
# ### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# 
# Demonstre o resultado através de gráfico de linha.

# In[66]:


df_dsa.head()


# In[17]:


query = """ SELECT Segmento, SUBSTRING(Data_Pedido, 7, 4) as Ano, SUBSTRING(Data_Pedido, 4, 2) as Mes, round(AVG(Valor_Venda), 2) 
    FROM tbl_dataset GROUP BY Segmento, SUBSTRING(Data_Pedido, 7, 4), SUBSTRING(Data_Pedido, 4, 2) ORDER BY 2, 3 """


# In[18]:


cur.execute(query)


# In[19]:


dados = cur.fetchall()


# In[56]:


segmentos = []
anos = []
meses = []
totais = []
for i in range(0, len(dados)):
    segmentos.append(dados[i][0])
    anos.append(dados[i][1])
    meses.append(dados[i][2])
    totais.append(dados[i][3])
    
segmentos = list(set(segmentos))
anos = list(set(anos))
meses = list(set(meses))

lst_valores_anos = []
lst_val_mes = []
valores = []

x = 0

for i in range(0, len(anos)):
    
    for k in range(0, len(meses)):
    
        for j in range(0, len(segmentos)):

            valores.insert(j, totais[x])
            x = x + 1

        lst_val_mes.insert(i, valores)
        valores = []
    
    lst_valores_anos.insert(i, lst_val_mes)
    lst_val_mes = []
    
anos.sort()
meses.sort()
    
print(segmentos)
print(anos)
print(meses)

lst_anomes_consumer = []
lst_anomes_home = []
lst_anomes_corpor = []

for i in range(0, len(anos)):
    
    for j in range(0, len(meses)):
        
        for k in range(0, len(segmentos)):
        
            if k == 0:
                lst_anomes_consumer.append(anos[i] + meses[j])
            elif k == 1:
                lst_anomes_home.append(anos[i] + meses[j])
            else:
                lst_anomes_corpor.append(anos[i] + meses[j])
    
print(lst_anomes_consumer)
print(lst_anomes_home)
print(lst_anomes_corpor)


# In[64]:


valores_consumer = []
valores_home = []
valores_corpor = []

for i in lst_valores_anos:
    
    for j in i:
        
        controle = 0
        
        for k in j:
            
            if controle == 0:
                valores_consumer.append(k)
            elif controle == 1:
                valores_home.append(k)
            else:
                valores_corpor.append(k)
                
            controle = controle + 1

x = lst_anomes_consumer

y = valores_consumer
z = valores_home
p = valores_corpor

fig = plt.figure(figsize=(20, 6))

axes = fig.add_axes([0, 0, 0.8, 0.8])

axes.plot(x, y, color='red', label='Consumer')
axes.plot(x, z, color='blue', label='Home Office')
axes.plot(x, p, color='green', label='Corporate')

axes.set_xlabel('x')
axes.set_ylabel('y')

axes.legend(title='Segmento')

axes.set_xticklabels(x, rotation=80)
axes.set_title('Gráfico de Linha');


# ## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):
# 
# ### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 
# 
# Demonstre tudo através de um único gráfico.

# In[17]:


df_dsa.head()


# In[45]:


query = """ SELECT Categoria, SubCategoria, round(SUM(Valor_Venda), 2) 
    FROM tbl_dataset GROUP BY Categoria, SubCategoria ORDER BY 3 DESC LIMIT 12 """


# In[46]:


cur.execute(query)


# In[47]:


dados = cur.fetchall()


# In[48]:


categorias = []
totais = []
for i in range(0, len(dados)):
    categorias.append(dados[i][0] + "-" + dados[i][1])
    totais.append(dados[i][2])


# In[49]:


fig, ax = plt.subplots(figsize=(20, 6))

ax.bar(categorias, totais, label='SubCategorias', color='blue')

ax.set_xlabel('Categorias - Subcategorias')
ax.set_ylabel('Total de Vendas')
ax.set_title('SubCategorias com Mais Vendas')

ax.set_xticklabels(categorias, rotation=80) 

ax.legend()

plt.show()


# # Fim
