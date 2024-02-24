# The bar


En un bar se controla la entrada de personas diaria durante una cantidad determinada
de días. En lo adelante, la administración del bar se refiere a la cantidad de personas que entran, en
relación a la media durante ese período, por ejemplo si un día entran 5 personas más que la media
calculada se registra como 5, si entran 10 personas menos que la media ya calculada se registra −10.
Esta media no se actualiza.
La administración del bar tiene un registro de la asistencia durante n días consecutivos, que ha sido
registrada de la forma antes mencionada, y se ha visto que la asistencia al bar en la segunda mitad
analizada fue la misma cada día.
El due˜no del bar va a hacerle una auditoría a la administración para saber si todo marcha bien.
La auditoría se lleva a cabo de la siguiente forma: El administrador le diría un número k, y el dueño
obtendrá la suma de las n − k + 1 posibles secuencias de k días consecutivos. Esto es, para todo i
entre 1 y n − k + 1, obtendrá la suma:

$$
a_i + a_{i + 1} + \dots + a_{i+k−1}.
$$


Por ejemplo si se registró como asistencia [−1, 0, 1, 2, 2] (nótese que los dos últimos elementos
conforman la segunda mitad, tomando parte entera por debajo, y son todos iguales), para k = 3, el
dueño tendrá como suma los números 0, 3 y 5.
Si todas las sumas obtenidas resultan positivas con respecto a la media anterior el dueño concluirá
que el bar marcha bien, de lo contrario, despide al administrador.
El administrador lo contrata a usted para que lo ayude, como científico que se considera, a determinar
qué valor de k debe elegir el administrador para que el dueño del bar no lo despida.