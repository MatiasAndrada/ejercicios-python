# CONSIGNA DE EJERCICIO
## CASO: CRM
Una empresa de nuestra ciudad ofrece a sus clientes un
producto CRM (Sistema de Gestión de Relaciones con el
Cliente - Customer Relationship Management). 
Los clientes(empresas de cualquier rubro) pueden optar por dos
modalidades de soporte:
A) Abono fijo con tope de horas
B) Pago a demanda según las horas requeridas.

Cuando un cliente realiza un ticket de soporte por alguna
eventualidad con el CRM, un responsable de 1er nivel de
atención evalúa la solicitud y consulta el contrato del cliente
para conocer la modalidad de soporte contratada. 
Si la solicitud no corresponde a una acción de soporte, le
contesta al cliente que debe realizar un pedido de desarrollo
de nuevas funcionalidades y cierra el ticket como
improcedente.
Si la solicitud corresponde a una acción de soporte, analiza la solicitud
para derivarla al área correspondiente (infraestructura, desarrollo,
redes, seguridad).
Un empleado del área asignada toma el ticket y resuelve lo solicitado.
Al finalizar registra las horas insumidas, cierra el ticket como resuelto
y lo deriva a Administración.
El Responsable de Administración consulta las horas registradas en el
ticket, verifica la modalidad contratada de soporte por el cliente y, si
el cliente posee un abono fijo actualiza la cantidad de horas
consumidas en el mes. Si la modalidad es pago a demanda o la
cantidad de horas insumidas supera el tope de horas del abono fijo,
calcula el total a cobrar al cliente, confecciona y le envía la factura
correspondiente.

### EVALUACIÓN
#### Proceso central: 
- Venta de soporte.
- Venta de CRM(Este vamos a analizar).

### MODELOS 

#### CLIENTE

#### TICKET

### MÉTODOS  
- Crear ticket.
- Consultar contrato del cliente 

### A IMPLEMENTAR
1. El cliente cuando crea un ticket el programa evalúa la solicitud y consulta el contrato del cliente para conocer su modalidad contratada.
2. Si la solicitud no corresponde a una acción retorna un mensaje "realizar un pedido de desarrollo
de nuevas funcionalidades" y cierra el ticket.
3. Si la solicitud si corresponde la analiza para llevarla al area correspondiente (infraestructura, desarrollo,
redes, seguridad).
3. Un empleado de esa area toma el ticket y resuelve lo solicitado. Al finalizar cierra el ticket como resuelto y deriva a administración.
4. Este responsable de administración consulta las horas registradas en el ticket, verifica su modalidad contratada por el cliente, y si posee un abono fijo actualiza las horas consumidas en el mes.  
5. Si es bajo demanda y la cantidad de horas insumidas supera el tope de horas de abono fijo, calcula cuanto cobrar al cliente, confecciona y envía la factura correspondiente 