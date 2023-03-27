#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


agregado = pd.read_excel('Vendas dez-mar.xlsx')


# In[3]:


agregado


# In[21]:


vendas_março = pd.read_excel('vendas - março.xlsx')


# In[22]:


vendas_março


# In[35]:


import plotly_express as px


# In[40]:


grafico = px.histogram(vendas_março, x='Forma_pagamento', y='Preço_venda', text_auto=True, color='Forma_pagamento')
grafico.show()


# In[39]:


grafico = px.histogram(vendas_março, x='Obs.', y='Preço_venda', text_auto=True, color='Obs.')
grafico.show()


# In[30]:


grafico = px.histogram(agregado, x='Período', y='Faturamento', text_auto=True)
grafico.show()


# In[ ]:


# Por conta do Carnaval, o mês de Fevereiro ficou aquém com relação à Receita total. Em contrapartida, as vendas no mês de março foram alavancadas devido à feira no Centro Administrativo da Bahia (CAB).


# In[31]:


faturamento_loja_tamanho = vendas_março.groupby(['Produto', 'Preço_venda']).sum()


# In[32]:


faturamento_loja_tamanho


# In[ ]:




