## Características
- Moderna interfaz de usuario
- Varias opciones de café

![image](https://github.com/Mauroquil-bit/CoffeeMachine/assets/75552002/824034d5-b236-40b9-814d-7a1687954eff)


¿Qué puede ser mejor que una taza de café durante un descanso? Un café que no tienes que hacer tú mismo. Basta con pulsar un par de botones de la máquina y se obtiene una taza de energía; Pero primero, debemos enseñarle a la máquina cómo hacerlo. En este proyecto, trabajarás en la programación de un simulador de máquina de café. La máquina funciona con productos típicos: café, leche, azúcar y vasos de plástico; Si se queda sin algo, muestra una notificación. Puedes conseguir tres tipos de café: espresso, capuchino y café con leche. Como nada es gratis, también recauda el dinero.

### Ejemplo de Uso

A continuación se muestra cómo puedes crear una instancia de la máquina de café y realizar algunas acciones básicas:

```python
from coffee_machine import CoffeeMachine

# Crear una instancia de la máquina de café
coffee_machine = CoffeeMachine()

# Realizar acciones
coffee_machine.fill(100, 50, 25, 1)  # Añadir recursos
coffee_machine.buy('1')  # Comprar un espresso
coffee_machine.status()  # Verificar el estado actual
```

## Ejemplo de Definición de Clase

Aquí hay un ejemplo de cómo puedes definir una clase simple en Python. En este caso, creamos una clase `Lampara` que tiene métodos para encender, apagar y mostrar su estado.

```python
class Lampara:
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True
        print("Lámpara encendida")

    def apagar(self):
        self.encendida = False
        print("Lámpara apagada")

    def estado(self):
        if self.encendida:
            print("La lámpara está encendida")
        else:
            print("La lámpara está apagada")
```


### Documentación de Métodos

- `fill(water, milk, coffee, cups)`: Método para rellenar los suministros de la máquina de café.
- `buy(option)`: Método para comprar un café. Las opciones son '1' para espresso, '2' para latte y '3' para cappuccino.
- `status()`: Muestra el estado actual de los suministros de la máquina.
- `take()`: Extrae todo el dinero recaudado por la máquina.

## Instalación

Para clonar este repositorio, usa el siguiente comando en tu terminal:

```bash
git clone https://github.com/Mauroquil-bit/CoffeeMachine.git
```


