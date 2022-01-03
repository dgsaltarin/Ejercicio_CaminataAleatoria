# Ejercicio_CaminataAleatoria
En este ejercicio veremos cómo hacer una simulación de una caminata aleatoria.
## Descripción
Para este ejercicio estarémos viendo de manera básica cómo se puede simular una caminata aleatoria. Imagina una caminata aleatoria, como un punto (x,y) en el plano el cuál puede moverse en el siguiente momento x+1 a los puntos y+1 o y-1 con una probabilidad p y 1-p respectivamente, es decir que va dando pasos de 1 hacia un lado u otro en cada momento basado en una probabilidad. Ahora, lo que tú tendrás que hacer es simular esto, imagina un apostador que empieza en el momento 0 con $20 y para el siguiente momento apuesta 1 de sus 20 con otra persona, si pierde, entonces en el momento 1 tendría $19, si gana, entonces tendría $21. Si suponemos que tiene el 50% de probabilidades de ganar o perder, entonces crea una gráfica donde puedas ver el resultado de esta interacción y termine hasta que el apostador se quede sin dinero o llegue a $30. Ahora repite este experimento muchas veces y responde ¿Cuántas veces llegó a cero sin que haya llegado a $30? ¿Cómo cambia tu resultado si ahora el apostador tiene 51% de probabilidades de perder?

## Bonus
Expande tu código de tal manera que ahora el movimiento aleatorio igual se vea reflejado en x (En este caso no podemos semejar este movimiento a las apuestas, pero sin embargo se parece más al movimiento de una partícula en dos dimensiones)

## Solución
Dentro de la solución del ejercicio se incluye un método que permite simular una caminata aleatoria, asemejando el movimiento a una seríe de apuestas. Adicionalmente se incluye un método que permite simular las caminatas aleatorias en dos dimensiones, sin embargo ya no podemos hacer la semejanza con las apuestas.


## Skills
Para resolver el ejercicio se utiliza el lenguaje python, junto con la librería de matplotlib:
- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [Matplotlib](https://matplotlib.org/)

## Resultados

### Caminata Aleatoria 1D:
Un ejemplo del resultado gráfico de simular una caminata aleatoria se puede ver a continuación:
![myplot2](https://user-images.githubusercontent.com/53949337/147934027-63e28e45-86bf-4211-8f3e-234e1eca0a4b.png)

Luego de hacer muchas simulaciones, aproximadamente de cada 100 intentos el apostador puede llegar en promedio 30 veces a 0 antes de llegar a 30, cuando se incrementa la probabilidad de perder el 51%, el apostar puede llegar en promedio al 0 unas 40 veces antes de llegar a 30 por primera vez.

### Caminata Aleatoria 2D:
El siguiente resultado corresponde a la somulación de una caminata aleatoria en dos dimensiones con un número de iteaciones igual a 1000.      
![myplot3](https://user-images.githubusercontent.com/53949337/147934147-67777d59-38fb-47cd-8bda-2932d11c8bde.png)

