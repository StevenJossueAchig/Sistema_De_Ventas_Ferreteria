# Sistema De Ventas Para Una Ferreteria
Sitema de ventas para una Ferreteria

Sistema para el manejo de inventario y venta los precios y cantidad de cada producto son numeros decimales y enteros respectivamente, en el caso de los demas ademas datos son cadenas de caracteres, para el ingreso de texto, cada opción lleva a una funcionalidad diferente que solventa las necesidades de una ferreteria, como la venta de productos, agregación de productos, busqueda de un producto entre otros. El esquema de negocio ha sido tomado de https://www.100plandenegocios.com/plan-de-negocios-de-una-ferreteria#descripcion


## Requisitos

Se requieren las siguientes bibliotecas:

* [memory_profiler](https://pypi.org/project/memory-profiler/)

* [PyInstaller](https://pyinstaller.org/en/stable/)

Si desea usar [@profile](https://pypi.org/project/memory-profiler/), ejecutar el programa desde una terminal, buscando el archivo .py y porterior ejeceutar el comando [python -m memory_profiler product.py](https://pypi.org/project/memory-profiler/), posterior haga uso del programa al momento de finalizar el programa automaticamente se capturara la complejidad de espacio de cada una de las funciones a las que se les ha agregado [@profile](https://pypi.org/project/memory-profiler/).

## Uso

```
usage: product.py [option] [datos]

C:\Users\legio\OneDrive\Escritorio\Sistema_De_Ventas_Ferretieria\code>
C:\Users\legio\OneDrive\Escritorio\Sistema_De_Ventas_Ferretieria\code>python -m memory_profiler product.py

Sistema de ventas Ferreteria: Manejo de un inventario y el proceso para ventas de una ferreteria.

Arguments:
  -datos   datos de un producto.
```
### Formato de los datos de entrada

**Nombre:** El nombre del producto solo debe hacer referencia al producto, no más especificaciones eso se ingresará en la descripción del producto.

**Fecha de caducidad:** La manera de ingresar la fecha será en el formato: **DD-MM-AA**. Examples: **24-04-2023**, **19-09-2023**

**Precio:** the time must always be represented under the 24h system, that is, the number of hours that have elapsed since midnight. The 12h format is not allowed. Format: **HH:MM**, where **HH** and **MM** should be composed of two digits, respectively. Examples: **12:30, 21:10, 09:05, 00:00 (midnight).**

**Cantidad:** the time must always be represented under the 24h system, that is, the number of hours that have elapsed since midnight. The 12h format is not allowed. Format: **HH:MM**, where **HH** and **MM** should be composed of two digits, respectively. Examples: **12:30, 21:10, 09:05, 00:00 (midnight).**

**Descripción:** the time must always be represented under the 24h system, that is, the number of hours that have elapsed since midnight. The 12h format is not allowed. Format: **HH:MM**, where **HH** and **MM** should be composed of two digits, respectively. Examples: **12:30, 21:10, 09:05, 00:00 (midnight).**

En caso de usar [@profile](https://pypi.org/project/memory-profiler/) agregar en cada función encima de donde se define, para poder ejecutar el comando python -m memory_profiler product.py, caso contrario no funcionará.


## Ejemplo

```
$ python pico_y_placa.py -p EBA-0234 -d 2021-04-23 -t 15:15
The vehicle with plate EBA-0234 CAN be on the road on 2021-04-23 at 15:15.

$ python pico_y_placa.py -p EBA-0234 -d 2021-04-27 -t 17:00
The vehicle with plate EBA-0234 CANNOT be on the road on 2021-04-27 at 17:00.
```


## Licencia

Este proyecto está autorizado bajo la Licencia MIT; consulte el archivo de [Licencia](Licencia) para mas detalles.
