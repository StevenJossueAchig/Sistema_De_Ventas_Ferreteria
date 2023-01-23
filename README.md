# Sistema De Ventas Para Una Ferretieria
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

**Plate:** following the [Ecuador car license plate format](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Ecuador), the parameter “Plate” should have this format: **XXX-YYYY**  (commercial, government, official, and private vehicles) or **XX-YYYY** (diplomatic service and temporary hospitalization vehicles), where **X** is a capital letter, and **Y** is a digit. Examples: **EBA-0234**, **CC-0012.**

**Date:** considering the [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601), the parameter “Date” should have the following format: **YYYY-MM-DD**. Examples: **2021-04-24**, **2020-09-10.**

**Time:** the time must always be represented under the 24h system, that is, the number of hours that have elapsed since midnight. The 12h format is not allowed. Format: **HH:MM**, where **HH** and **MM** should be composed of two digits, respectively. Examples: **12:30, 21:10, 09:05, 00:00 (midnight).**

To use the [abstract Public Holidays API](https://www.abstractapi.com/holidays-api) add the flag -o or --online. Otherwise, the predicator will use the class “HolidayEcuador” to check if a date is a holiday or not.


## Example

```
$ python pico_y_placa.py -p EBA-0234 -d 2021-04-23 -t 15:15
The vehicle with plate EBA-0234 CAN be on the road on 2021-04-23 at 15:15.

$ python pico_y_placa.py -p EBA-0234 -d 2021-04-27 -t 17:00
The vehicle with plate EBA-0234 CANNOT be on the road on 2021-04-27 at 17:00.
```

## Automated Testing

To perform automated testing using the _unittest_ framework run: `python test.py`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
