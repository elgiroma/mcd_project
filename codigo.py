import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./df_covid19.csv")

df_mujer = df[df.SEXO == 1]
df_hombre = df[df.SEXO == 2]


# HOMBRES
si_tiene_hombre = list(df_hombre.DIABETES).count(1)
no_tiene_hombre = list(df_hombre.DIABETES).count(2)
no_aplica_hombre = list(df_hombre.DIABETES).count(98)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
etiquetas_hombre = ['Si tiene (hombre)', 'No tiene (hombre)', 'No aplica (hombre)']
hombres = [si_tiene_hombre,no_tiene_hombre,no_aplica_hombre]
ax.bar(etiquetas_hombre,hombres)
plt.savefig('./grafica_hombres.png')
plt.show()


# MUJERES
si_tiene_mujer = list(df_mujer.DIABETES).count(1)
no_tiene_mujer = list(df_mujer.DIABETES).count(2)
no_aplica_mujer = list(df_mujer.DIABETES).count(98)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
etiquetas_mujer = ['Si tiene (mujer)', 'No tiene (mujer)', 'No aplica (mujer)']
mujeres = [si_tiene_mujer,no_tiene_mujer,no_aplica_mujer]
ax.bar(etiquetas_mujer,mujeres)
plt.savefig('./grafica_mujeres.png')
plt.show()
