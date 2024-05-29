
class Ticket:

    def __init__(self, id, title, description, dateEmit, state):
        self.id = id,
        self.title = title,
        self.description = description,
        self.createdAt = dateEmit,
        self.state = state
        self.closeAt = "" # Esto no se inicializa con un valor de parámetros desde el constructor ya que se define con el método closeTicket

    def __str__(self):
        print(f"Id: {self.id} \n Titulo: {self.title} \n Descripción: {self.description} \n Estado: {self.state} Tiempo de emisión: {self.createdAt} \n Tiempo de expiración: {self.closeAt} ")
