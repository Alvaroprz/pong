# pong

Versión del clásico juego Pong hecho con Python y pygame

## Cómo empezar a jugar

1. Crear un entorno virtual: `python3 -m venv env`
2. Activar el entorno recién creado: `source ./env/bin/activate`
3. Instalar las dependencias: `pip install -r requirements.txt`
4. Arrancar el juego: `python pong.py`

## Como crear un entorno virtual

Para crear un entorno virtual con el nombre _env_ necesito utilizar
un módulo de Python que se llama `venv`.

```
# en windows
python -m venv env

# en mac/linux
python3 -m venv env
```

Evidentemente, podemos usar cualquier nombre para
ponerle al entorno virtual. De aquí en adelante,
utilizaré _env_ como nombre de entorno, pero puedes
usar el que quieras.

## Cómo activar el entorno virtual

Cuando se crea un entorno virtual, se preparan unos
scripts con utilidades para activar el entorno y
un enlace simbólico a la versión de Python que se va
a usar y su versión correspondiente del gestor de paquetes
`pip`.

Para activarlo, es necesario ejecutar el script de activación
de la siguiente manera:

```
# en windows
.\env\Scripts\activate

# en mac/linux
source ./env/bin/activate
```

Si el entorno se ha activado correctamente, veremos en el
prompt del terminal el nombre del entorno activo entre
paréntesis. En este caso veremos `(env)`.

## Gestor de paquetes: pip

- Instalar un paquete nuevo: `pip install <nombre-del-paquete>`
- Listar los paquetes instalados: `pip list`
- Listar paquetes en fromato de dependencias: `pip freeze`

## Como desactivar el entorno virtual

Con el entorno virtual activado simplemente basta con
ejecutar el siguiente comando:

```
deactivate
```

## Cómo eliminar un entorno virtual

Basta con eliminar el directorio que se ha creado al
inicializar el entorno virtual. Esto elimina el entorno
y todas las dependencias instaladas en él.
