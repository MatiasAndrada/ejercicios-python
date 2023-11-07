# CONCURSO

## DISEÑO DEL ALGORITMO Y EXPLICACION DE FORMULAS

Para calcular los diferentes sistemas de medición primero le pregunte cual sist de representación el usuario quería usar. Para asi, luego multiplicarlo por su equivalencia en otra magnitud.

ENTRADA: dimension de la superficie en forma de longitud, anchura y altura o otros parámetros relevantes
PROCESO:  calcular cantidad de metros cúbicos de hormigón  requeridos.
SALIDA: cantidad de hormigon requerida y otros detalles importantes.

## REQUISITOS

● Recibir   las   dimensiones   de   la   superficie   donde   se   utilizará   el   hormigón,   ya  sea  en
 forma de longitud, anchura y altura, o a través de otros parámetros relevantes.
 ● Calcular   de   manera   precisa   la   cantidad   de  metros  cúbicos  de  hormigón  requeridos
 según las dimensiones proporcionadas y otros factores relevantes.
 ●   Presentar  los  resultados  de  manera  clara  y  comprensible  para  el  cliente,  mostrando
 tanto   la   cantidad   de   hormigón   requerida   como   posiblemente   otros   detalles
 importantes.
 ●   Proporcionar  una  interfaz  amigable  e  intuitiva  que  guíe  al  cliente  a  través  del  proceso
 de ingreso de datos y obtención de resultados.
 ●   Ser   capaz   de   manejar   diferentes   unidades   de   medida,   como   metros,   pies,
 centímetros, etc., para adaptarse a las preferencias de los clientes.
 ●   Registrar   el   pedido   del   cliente   en   un   archivo   de   control   para   la  empresa  donde  se
 deberá visualizar el cliente y los metros solicitados.
 ●   Proporcionar   un   archivo   que   podrá  ser  impreso  para  entregárselo  al  cliente  con  los
 datos   ofrecidos,   el   cálculo   realizado   y   el   total   de   metros  de  hormigón  que  le  serán
 entregado

## Descripción de herramientas

Se utilizo las sentencias match para evaluar los diferentes casos de sist de medidas disponibles.
Ademas de sentencia if y elif para los diferentes condicionales y asi lograr la normalización de los datos ingresados para utilizar el sist de metros en todo el sist.

## Pruebas

Se realizo pruebas ingresando los diferentes sist de medición para comprobar su precision.

## Cronograma de desarrollo y lanzamiento

- **Version 1**
La primera version del programa incluyo la normalización de los datos ingresados y la conversión de los mismos a metros.
- **Version 2**
La segunda version incluyo el manejo del sist de archivos para guardar historial de ordenes identificadas por el DNI del cliente.
**Version 3**
- Se incluyo el manejo de excepciones para evitar errores en el programa.
- Se agrego la funcionalidad de que el sistema guarde todas las ordenes en metros independientemente de sist de medida utilizado.

### Participantes

- [x] 1. [Matias Andrada]
- [x] 2. [Emiliano Coronel]
