

# Proyecto Urban Routes


Como objetivo principal se verificará el adecuado funcionamiento de esta plataforma de viajes aplicando pruebas automatizadas a través de pytest y selenium Webdriver.

En esta aplicación Web, se tiene como función principal, permitirle al usuario solicitar el servicio de taxi u otro tipo de trasporte, en la cuales se tiene como opción 3 modos de viaje especificos donde cada una tiene opciones de solicitudes específicas relacionadas al modo de trasporte que se elija.




### Descripción del proceso y tecnología utilizada

- Se utilizó como estructura general el patrón de diseño POM (Page Object Model) utilizando como herramienta única Selenium para interactuar con la interfaz de usuario del navegador
- Para el inicio de las pruebas automatizadas se realizó la configuración del repositorio GitHub y se clonó el mismo. 
- El archivo "data.py" se utilizará para almacenar los datos de entrada para las pruebas 
- En el archivo "locators.py" se definirán los localizadores de cada elemento que se probará en las funciones. 
- En "urban_routes_page.py" se ubicarán los métodos necesarios en la clase objetos que interactúan con el navegador y la interfaz de usuario.
- Para las pruebas en la clase se utilizará el archivo "main.py"


##### Lo que se probará

- Configurar la dirección de partida y de llegada
- Seleccionar la tarifa Comfort
- Rellenar el número de teléfono
- Agregar una tarjeta de crédito
- Escribir un mensaje para el controlador
- Pedir una manta y pañuelos
- Pedir 2 helados
- Visualizar modal para busqueda de un taxi

#### Ejecucion de la prueba

    1. Actualizar la URL dentro del archivo data.py
    2. Ejecutar el icono de la flecha verde (Run) en el archivo main.py 
    3. Se verificará el resultado de la ejecución del archivo main.py PASSED [100%]

    