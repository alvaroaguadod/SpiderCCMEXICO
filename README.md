# CCMEXICO scraper project

Scrapy project for data extraction in https://ccmexico.com.mx/


## Spider Parameters

|   Params   |        Type        | Description                                                                                                                                  | Mandatory |
| :--------: | :-----------------: | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| searchlist |        string        | Accepts any search keyword                                                                             | YES       |   
| category |        string        | Section where the scraper will scrape. Look at the list of available sections.                                                                                                                                    | NO       |
|   blog   |       string       | Section where the scraper will scrape. Look at the list of available sections within the blog.                                                                                         | NO        |


The parameter fields only accept a string, more than one spider is not supported
## Local development

### Setting Up the environment

Install dependencies.

```bash
pip install -r requirements
```

### How run the spider

- By scrapy command

```bash
scrapy crawl CCMEXICOSpider -a searchlist=gobierno -o prueba.json

scrapy crawl CCMEXICOSpider -a category="comercio internacional" -o prueba.json

scrapy crawl CCMEXICOSpider -a blog="home newsletter" -o prueba.json

```

- By python command

````bash
python main.py
````
##  Manual Deployment

Login zyte cloud

```bash
shub login #Then add zyte cloud credencial
```

Upload the project to zyte cloud:

- Deploy in dev

```bash
shub deploy 
```

- Deploy in pro

```bash
shub deploy pro
```

Set ZYTE_SMARTPROXY_APIKEY variable in zyte cloud project in settings section.

Set SMTP_SERVER, USER_EMAIL, USER_EMAIL_PASSWORD, RECIPIENT_LIST, EMAIL_SUBJECT and ENABLE_ERROR_EMAIL variables to enable the email error notification.



## Run spider in zyte cloud by postman
### Url

> https://app.scrapinghub.com/api/run.json

### Body parameters

|               Params               |  Type  | Description                                                        | Mandatory |
| :--------------------------------: | :----: | :----------------------------------------------------------------: | :-------: |
|              project               |  int   | Id project (default: 648571 / pro: 648574).                        | YES       |
|              spider                | string | CCMEXICOSpider                                                     | YES       |
| [More parameters](#spider-parameters) |        |                                                                 |           |


## Example of returned item

## Example of returned item

```
[
{"author": "Boletín no. 458", "date": "07 de diciembre de 2022", "text": "La Cámara de Comercio, Servicios y Turismo de la Ciudad de México realizó una estimación de la derrama económica que generará la celebración guadalupana. Al respecto, José de Jesús Rodríguez Cárdenas, presidente de Canaco, dijo que la derrama económica esperada para el festejo del próximo 12 de diciembre será de 1 mil 243 millones de pesos en ventas de comercios y servicios, es decir, 16.1 por ciento más que en 2021. Señaló que los feligreses que llegarán a la Basílica destinarán de $200 a $1,300 pesos a gastos alimenticios y hospedaje. En este aspecto, dijo, se prevé que el 90% de los peregrinos pernoctará en los alrededores o en viviendas de familiares o amigos y sólo el 10% se hospedará en algún hotel de la zona. El líder empresarial estimó que arribarán más de 16 millones 300 mil visitantes a la Ciudad de México, el fin de semana previo al festejo del 12 de diciembre. Lo cual equivale a 36.3 por ciento más que el número de personas que acudieron en el 2021. El dirigente del comercio establecido consideró que la celebración requerirá de un gran esfuerzo de planeación y logística por parte de las autoridades, debido a que los visitantes superarán las 11 millones 959 mil personas que se tenían calculadas. Finalmente, puntualizó que los negocios con mayor dinamismo económico serán los giros de alimentos preparados, florerías, hospedaje, establecimientos de comida rápida, minisúper, tiendas de abarrotes, venta de artículos religiosos y artesanías."},
{"title": "El único  interés de los llamados “bloques negros” es desprestigiar: Canaco CDMX", "author": "Boletín No. 451", "date": "29 de septiembre de 2022", "text": "La Cámara Nacional de Comercio, Servicios y Turismo de la Ciudad de México expresa su preocupación por la persistente violencia durante las marchas feministas que, si bien son testimonio del ejercicio a la libertad de expresión, también son origen de graves afectaciones a la ciudanía, empresarios del comercio y los servicios, desde diferentes perspectivas. Al respecto, el presidente de la Canaco CDMX, José de Jesús Rodríguez Cárdenas,  añadió que si bien el día de ayer se reportó saldo blanco luego de la marcha en favor de la despenalización del aborto y el derecho a la interrupción del embarazo, también es verdad que cada vez que hay una manifestación con alguna demanda de justicia,  casi siempre hay afectaciones en comercios, restaurantes e instituciones de servicio, los cuales se ven en la necesidad de tapiar fachadas completas desde un día antes, lo cual incide negativamente en el nivel de ventas. El líder del comercio establecido en la CDMX agregó que los comerciantes, cuyas actividades se desarrollan en el corredor Reforma–Centro Histórico y alrededores, se ven seriamente afectados: “El 42 por ciento de la actividad económica de la alcaldía Cuauhtémoc se concentra en este corredor y debido a la marcha de ayer, se estiman ventas no realizadas por más de 9 millones de pesos, además de daños materiales por 208 mil pesos, aproximadamente”. José de Jesús Rodríguez Cárdenas ha señalado en reiteradas ocasiones que “un derecho como la libertad de expresión no puede estar por encima de otros derechos fundamentales, como la libertad de tránsito o de comercio y al respecto recordó que las actividades comerciales son el sustento de muchas familias”. Destacó que tan solo en el corredor Reforma–Centro Histórico y áreas circunvecinas existen empresas que son fuente de 250 mil empleos, muchos de ellos pagados por actividad diaria. Finalmente, el líder del comercio organizado de la Ciudad de México manifestó su reconocimiento a la labor del Grupo Atenea y al operativo diseñado por las autoridades del Gobierno de la CDMX para contener a los grupos violentos. Sin embargo, añadió, lo ideal sería que de una vez por todas se desactivaran todos aquellos denominados “bloques negros” cuyo interés es desprestigiar las legítimas demandas sociales y dar la impresión de ingobernabilidad."},
{"title": "Canaco CDMX saluda el nombramiento de Raquel Buenrostro, en la SE", "author": "Boletín No. 453", "date": "7 de octubre de 2022", "text": "La Cámara Nacional de Comercio, Servicios y Turismo de la Ciudad de México, manifiesta su beneplácito por el nombramiento de la maestra Raquel Buenrostro Sánchez como nueva titular de la Secretaría de Economía, con la certeza que su experiencia y capacidad le permitirán un desempeño exitoso en beneficio de la economía de nuestro país. El presidente de la CANACO Ciudad de México; José de Jesús Rodríguez Cárdenas felicita cumplidamente a la maestra Buenrostro por su designación en esta relevante encomienda, reconociendo además de sus capacidades, la apertura que la caracteriza para dialogar temas de interés común desde nuestro sector y reiterando la disposición de trabajar en conjunto identificando los asuntos pendientes en la agenda del sector terciario encaminada a la sustentabilidad y reactivación económica. Asimismo, reconocemos su labor al frente del Servicio de Administración Tributaria (SAT) donde se alcanzaron importantes acuerdos en favor del sector que representamos. La Canaco Ciudad de México mantiene su permanente apertura y disposición a coadyuvar con la Secretaría de Economía sobre las materias de interés para el comercio organizado, con el propósito inamovible de aportar con propuestas y trabajo concreto a favor del crecimiento económico sostenible de nuestro sector y en beneficio de las familias mexicanas. "},
]
```

