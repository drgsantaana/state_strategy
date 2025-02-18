class State:
    def handle(self, context):
        raise NotImplementedError("Subclasses must implement this method")

class NovoPedidoState(State):
    def handle(self, context):
        print("Novo pedido recebido. Transicionando para o estado Processando.")
        context.state = ProcessandoPedidoState()

class ProcessandoPedidoState(State):
    def handle(self, context):
        print("Pedido está sendo processado. Transicionando para o estado Enviado.")
        context.state = PedidoEnviadoState()

class PedidoEnviadoState(State):
    def handle(self, context):
        print("Pedido foi enviado. Transicionando para o estado Entregue.")
        context.state = PedidoEntregueState()

class PedidoEntregueState(State):
    def handle(self, context):
        print("Pedido foi entregue. Não há mais transições.")

class PedidoContext:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)

if __name__ == "__main__":
    pedido = PedidoContext(NovoPedidoState())
    pedido.request()  # Novo pedido recebido. Transicionando para o estado Processando.
    pedido.request()  # Pedido está sendo processado. Transicionando para o estado Enviado.
    pedido.request()  # Pedido foi enviado. Transicionando para o estado Entregue.
    pedido.request()  # Pedido foi entregue. Não há mais transições.