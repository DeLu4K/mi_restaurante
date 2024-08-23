# Sistema de Facturación para Restaurante

Este proyecto es una aplicación gráfica desarrollada en Python utilizando la librería Tkinter. El sistema permite gestionar la facturación en un restaurante, con funciones para calcular el costo de comidas, bebidas y postres, generar recibos, y realizar operaciones básicas con una calculadora integrada.

## Características

- **Gestión de Pedidos**: Selecciona los ítems de comida, bebida y postres con su respectiva cantidad.
- **Cálculo Automático**: Calcula automáticamente el subtotal, impuestos y total de la factura.
- **Generación de Recibos**: Genera un recibo detallado que se puede guardar en formato `.txt`.
- **Calculadora Integrada**: Realiza operaciones básicas para cálculos rápidos directamente en la aplicación.
- **Interfaz de Usuario**: Interfaz gráfica sencilla e intuitiva creada con Tkinter.

## Requisitos

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Tkinter**: Esta librería viene preinstalada con Python en la mayoría de las distribuciones, pero si no está instalada, puedes hacerlo ejecutando `pip install tk`.

## Instrucciones de Uso

1. **Clona el repositorio**:
   
    git clone https://github.com/tu_usuario/sistema-facturacion-restaurante.git

3. **Navega al directorio del proyecto**:
    
    cd sistema-facturacion-restaurante
    
4. **Ejecuta la aplicación**:
    
    python mi_restaurante.py
    
5. **Utiliza la aplicación**:
   - Marca las casillas para seleccionar los ítems que deseas añadir al pedido.
   - Ingresa la cantidad correspondiente para cada ítem.
   - Presiona `Total` para calcular el costo total incluyendo impuestos.
   - Presiona `Recibo` para generar un recibo que se mostrará en el área de texto.
   - Puedes guardar el recibo en formato `.txt` utilizando el botón `Guardar`.
   - Utiliza la calculadora integrada para realizar operaciones básicas.

## Estructura del Proyecto

- `sistema_facturacion.py`: Archivo principal que contiene todo el código de la aplicación.
- `recibos/`: Directorio donde se guardan los recibos generados en formato `.txt`.


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor haz un fork del repositorio, crea una rama con tus cambios y abre un pull request.

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.

