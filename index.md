##  Proyecto final de Curso Herramientas de Productividad para Ciencia de Datos.

###  Introducción.


Este repositorio se creó como parte de un proyecto final de el curso propedéutico "Herramientas de Productividad para Ciencia de Datos" de la maestría en ciencia de datos de la universidad de sonora, con el propósito de analizar los datos de casos de Covid-19 durante el día 1 de Febrero del 2022 pertenecientes al país de México. Así como también se mostrará la forma y metodología utilizada para realizar este procedimiento.

You can use the [editor on GitHub](https://github.com/elgiroma/mcd_project/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

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



