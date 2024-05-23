                            Proyecto Urban Grocers 

Script 7 Introducción a la automatización de pruebas
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.
Resumen del script 7

Un compañerp QA Engineer está comprobando la aplicación Urban Grocers para crear kits de productos. Se han creado varias listas de comprobación, un requisito es que el campo name en la solicitud de creación de un kit de productos.

El propósito del proyecto es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.

La documentación requerida para la implementación del proyecto la podemos visualizar en la URL de Urban.Grocers "url/docs/"

para el uso de herramientas requerimos
URL y documentación Urban.Grocers
Github
Linea de comandos cywgin
Programa python (pycharm)

Validamos las listas de comprobación, de las nueve pruebas, podemos destacar lo siguinete
Listas de comprobación 
1. 	El número permitido de caracteres (1): kit_body = { "name": "a"} = prueba aprobada (Respuesta esperada 201, respuesta actual 201)
2. El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} = prueba aprobada (Respuesta esperada 201, respuesta actual 201)
3. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } = Prueba aprobada (Respuesta esperada 400, respuesta actual 400)
4. El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } = Prueba no aprobada (Respuesta esperada 400, status actual 201)
5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } = prueba aprobada (Respuesta esperada 201, respuesta actual 201)
6. 	Se permiten espacios: kit_body = { "name": " A Aaa " } = prueba aprobada (Respuesta esperada 201, respuesta actual 201)
7. 	Se permiten números: kit_body = { "name": "123" } = prueba aprobada (Respuesta esperada 201, respuesta actual 201)
8. El parámetro no se pasa en la solicitud: kit_body = { } = Prueba no aprobada (Respuesta esperada 400, status actual 201)
9. Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } = Prueba no aprobada (Respuesta esperada 400, status actual 201)

Cordialmente

Nilton Cerquera
QA engineer