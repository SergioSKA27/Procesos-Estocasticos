import random
import pandas as pd
import streamlit as st

def f(n):
  table = []
  ntr = 0


  for i in range(0,n):
    p = i
    rn = random.random()
    if len(table) ==0:
      ini = 0
    else:
      ini = table[-1][-1]
    if rn <= .30:
      ent = 0
    elif rn <= .80:
      ent = 1
    else:
      ent = 2

    if ent +ini < 4:
      acu = ent+ini
    else:
      acu = 3

    if acu > 0:
      tr = 1
    else:
      tr = 0
      ntr += 1

    pend = acu-tr

    table.append([p,ini,rn,ent,acu,tr,pend])

  return table,ntr

iters = st.slider('Numero de iteraciones', 1, 1000, 100)
if st.button('Generar'):
    data,ntr = f(iters)
    st.write('Numero de periodos sin trabajar:', ntr)
    pdata = pd.DataFrame(data, columns = ['Periodo','Inventario Inicial','Random','Demanda','Inventario Acumulado','Trabajando','Pendiente'])
    st.dataframe(pdata)
