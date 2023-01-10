#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Comparando fazer a média dos dados antes do holo ou holo antes da média 

##média.antes.do.holo
#não.finalizado

import os
import numpy as np
from scipy.io import loadmat

directory = rf"OneDrive - Universidade Federal do Pará - UFPA/Documentos/LABNEP/EEG TESTE/DATASET/cleaned0_50Hz"
files = os.listdir(directory)

data=[]
channels_names = [] 

#lista dos nomes dos canais de cada dado (alguns tem mais que outros por conta da limpeza de ruídos/artefatos no pré-processamento)

for filename in files:
    channels = []
    f = os.path.join(directory, filename) 
    if os.path.isfile(f):
        matdat1 = loadmat(f)
        data.append(matdat1['data'])

        for n in range(matdat1['nbchan'][0][0]):
            channels.append(matdat1['chanlocs'][0][n][0][0])
            
        channels_names.append(channels)


# In[4]:


print(channels_names)


# In[5]:


#interseção para procurar os canais em comum de todos os arquivos    
res = list(set.intersection(*map(set, channels_names)))
print ("The common elements from N lists : " + str(res))

#percebe-se que a interseção resulta em um número de canais muito baixo, fazer a média desses poucos canais perderia-se muita informação


# In[7]:


##holo.antes.da.média
#não.finalizado

import os
import numpy as np
from scipy.io import loadmat

directory = r'OneDrive - Universidade Federal do Pará - UFPA/Documentos/LABNEP/EEG TESTE/DATASET/cleaned0_50Hz'
files = os.listdir(directory)

data=[]

for filename in files:
    f = os.path.join(directory, filename) 
    if os.path.isfile(f):
        matdat1 = loadmat(f)
        data.append(matdat1['data'].flatten()) #deve-se fazer o flatten() pq as funções da HHT3D só aceita arrays uni-dim


# In[ ]:




