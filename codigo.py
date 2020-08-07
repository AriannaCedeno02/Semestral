#codigo
import pandas as pd
from matplotlib import pyplot as plt
datos=pd.read_csv('estadistica.txt',header=0,delim_whitespace=True)
#x=casos nuevos
x=datos.ix[:, 1]
#defunciones
y=datos.ix[:, 2]
plt.plot(x,y,'g^')
plt.xlabel('casos nuevos')
plt.ylabel('defunciones')
print('estadisticas de defunciones')
print(y.describe())
print('estadisticas de casos nuevos')
print(x.describe())
#valores de los casos el maximo y el minimo
print('valor minimo de casos nuevos')
print(x.max())
print('valor maximo de casos nuevos')
print(x.min())
#valor maximo y minimo de defunciones
print('valor maximo de defunciones')
print(y.max())
print('valor minimo de defunciones')
print(y.min())
#conteo de datos
print('conteo de casos nuevos ya registrado')
print(x.count())
print('conteo de datos para defunciones ya registradas')
print(y.count())

#operacion para obtener el aproximado de defunciones
print('casos nuevo para hoy')
expr=var.x*1.2 ## supuestamente es la multiplicacion de la ultima variable de x que son los casos nuevos por el Rt que es 1,2%
#operacion de aproximado para casos nuevos
print('defunciones para hoy')
expr=var.x*2.2
# supuestamente es la multiplicacion de la ultima variable de yque son las defunciones por el Rt que es 2.2%
#operacion de aproximado nuevas defunciones

