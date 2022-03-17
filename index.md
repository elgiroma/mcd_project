##  Proyecto final de Curso Propedéutico de la maestria en Ciencia de Datos. Herramientas de Productividad para Ciencia de Datos.

###  Introducción.


Este repositorio se creó como parte de un proyecto final de el curso propedéutico "Herramientas de Productividad para Ciencia de Datos" de la maestría en ciencia de datos de la universidad de sonora, con el propósito de analizar los datos de casos de Covid-19 durante el día 14 de Febrero del 2022 pertenecientes al país de México. Así como también se mostrará la forma y metodología utilizada para realizar este procedimiento.


### Problema.

Se plantea encontrar la cantidad de hombres y mujeres con covid el día de 14 de febrero del 2022 que tienen diabetes.


1. Clonamos el repositorio.
```
git clone https://github.com/elgiroma/mcd_project.git
```

2. Generamos la imagen del Dockerfile
```
docker build -t covidimage .
```

3. Generamos el contenedor
```
docker run -it --name mcd-contenedor covidimage
```

4. Así puedes abrir el contenedor
```
docker start -i ContenedorCovid
```

 5. Dentro del contenedor se encuentra el csv listo, la imágen agrega todas las librerías necesarias y se resuelve el problema con un script .py
 
 6. Estas son las gráficas de el número de hombres y mujeres con covid el 14 de febrero del 2022 que padecían con diabetes



<img width="350" alt="grafica_hombres" src="https://user-images.githubusercontent.com/43888949/158704380-d8756d3c-2010-4ab6-9d5b-23ef884c1904.png">
<img width="349" alt="grafica_mujeres" src="https://user-images.githubusercontent.com/43888949/158704454-7b595123-32cd-4729-bcd2-8fc188966189.png">
