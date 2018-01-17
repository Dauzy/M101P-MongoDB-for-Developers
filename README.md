# Inicilizar el proyecto

###Creaamos un entorno virtual y instalamos las librerias necesarias.
```
$ python3 -m venv mBlog
$ pip install -r requirements.txt
```

###Inicializamos el contenedor de mongo para correr nuestra BD.

```
$ sudo docker run --name mongodev -v $PWD:/data/db -d mongo

```

