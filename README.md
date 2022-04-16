# Dataset_Fase_2

El link del repositorio es el siguiente: https://github.com/rnoguer22/Dataset_Fase_2.git

Pincha [aquí](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset?resource=download) para acceder al link del dataset

__________________________________________________________________________________________________________________________________________________________________________

PARTE 1: COMO FUNCIONAN LOS MODELOS

Para un mayor entendimiento de esta fase del trabajo, consideramos que es importante explicar qué es un modelo de análisis de datos y su importancia.

A la hora de definir qué es un modelo de análisis, se podría decir que es la primera representación técnica de un sistema. Utiliza una mezcla de formatos en texto y diagramas para representar los requisitos del software, las funciones y el comportamiento.

En general, las empresas realizan análisis de datos para ganar un mayor conocimiento del entorno y de las necesidades del cliente de cara al producto que se está vendiendo. Por ejemplo, son clave para averiguar qué es lo que quiere el cliente, los riesgos que pueden llegar a afectar a la empresa o para recopilar información sustancial a la hora de emprender.

El modelo de análisis se complementa de cuatro elementos fundamentales. Estos elementos sirven para clasificar principalmente los diferentes diagramas y otros derivados conocidos en plataformas como sistemas de información e ingeniería de software entre otros. Además estos con clasificados en elementos de escenario, elementos de flujo, elementos de clases y elementos de comportamiento. Para explicarlos sencillamente, son los distintos tipos de UML que reflejan como funciona nuestro programa o algoritmo.

En el lenguaje que nos ocupa actualmente, Python, los datos se analizan mediante Pandas, la librería que se usa para el análisis y tratamiento de datos. Nos proporciona la clase Dataframe, la cual permite almacenar los datos en un objeto similar a una tabla de una base de datos.


MODELO DE PÁGINA Y APP:
![esquema Vinho](https://user-images.githubusercontent.com/91722847/163686507-739bafc0-7552-4e20-ad1c-12604ca99fad.png)

![clases vinho](https://user-images.githubusercontent.com/91722847/163686509-d7b83472-a2a8-4c3e-b96f-dd7b0fedcbc5.png)


--Una vez que tenemos construido nuestro primer modelo, podemos tener 2 problemas en el, uno es el underfitting y otro es el overfitting.
  A continuación, veremos como podemos solucionar estos problemas para conseguir un modelo lo mas estable posible.
## Underfitting
El problema del underfitting llega cuando generalizamos nuestro modelo, en nuestro caso sería por ejemplo, si solo vendieramos un tipo de vino y lo catalogaramos como el unico vino posible, cuando nuestros clientes prueben otro vino distinto, no lo considerarian vino como tal, pues el unico concepto que tienen de vino es es un tipo determinado.
Si nuestros datos de entrenamiento son muy pocos nuestra maquina(Machine Learning) no sera capaz de generalizar el conocimiento y estara incurriendo en underfitting
El algoritmo no sera capaz de darnos un resultado bueno por falta de “materia prima” para hacer solido su conocimiento.

## Overfitting
El problema del overfitting llega cuando nuestra maquina solo se ajustara a aprender los casos particulares que le enseñamos y sera incapaz de reconocer nuevos datos de entrada. Cuando “sobre-entrenamos” nuestro modelo y caemos en el overfitting, en nuestro modelo, sería tener una gran cantidad de tipos de vino pero no todos los tipos, nuestro algoritmo estara considerando como validos solo los datos identicos a los de nuestro conjunto de entrenamiento –incluidos sus defectos– y siendo incapaz de distinguir entradas buenas como fiables si se salen un poco de los rangos ya prestablecidos,es decir, nuestro algoritmo sera incapaz de aceptar nuevos vinos validos por sus caracteristicas, si estas no son tal cual como las caracteristicas "preestablecidas" de nuestros vinos

## Para encontrar el equilibrio
Deberemos encontrar un punto medio en el aprendizaje de nuestro modelo en el que no estemos incurriendo en underfitting y tampoco en overfitting.
Subdividiremos nuestro conjunto de datos de entrada para entrenamiento en dos: uno para entrenamiento y otro para testear que el modelo no conocera de antemano. Esta division la haremos del 80% para entrenar y 20% para el testeo. El conjunto de Test tendra muestras de vino diversas en lo posible y una cantidad de muestras de vino suficiente para poder comprobar los resultados una vez entrenado el modelo.

 Para lograr que nuestro modelo de buenos resultados iremos revisando y contrastando nuestro entrenamiento con el conjunto de Test y su tasa de errores.
 ALgunos puntos que tendremos en cuenta:
 ---Cantidad minima de muestras de vino tanto para entrenar el modelo como para validarlo.
 ---Clases de vino variadas y equilibradas en cantidad: En caso de aprendizaje supervisado y suponiendo que tenemos que clasificar diversas clases, es         importante que los datos de entrenamiento esten igualados.
 ---Conjunto de Test de datos. Siempre subdividir nuestro conjunto de datos y mantener una porcion del mismo “oculto” a nuestra maquina entrenada. Esto nos permitira       obtener una valoracion de aciertos/fallos real del modelo y tambien nos permitira detectar facilmente efectos del overfitting /underfitting.


Si nuestro modelo entrenado con el conjunto de train tiene un 90% de aciertos y con el conjunto de test tiene un porcentaje muy bajo, esto señala claramente un problema de overfitting.

Si en el conjunto de Test solo se acierta un tipo de vino o el único resultado que se obtiene es siempre el mismo vino sera que se produjo un problema de underfitting.
