FROM ubuntu

LABEL Eliud Rodríguez

WORKDIR /root

RUN  apt-get -y update && \
     apt-get install -yq curl unzip git pip python3.8 python3-pip

RUN pip install csvkit pandas matplotlib

RUN  curl -L -O https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/historicos/2022/01/datos_abiertos_covid19_01.01.2022.zip &&\
     unzip datos_abiertos_covid19_01.01.2022.zip &&\
     csvcut -c SEXO,EDAD,DIABETES 220101COVID19MEXICO.csv > df_covid19.csv &&\
     rm datos_abiertos_covid19_01.01.2022.zip &&\
     rm 220101COVID19MEXICO.csv

ADD codigo.py /root/codigo.py

RUN python3 codigo.py

CMD ["bash"