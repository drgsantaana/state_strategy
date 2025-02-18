from __future__ import annotations
from abc import ABC, abstractmethod


class Contexto:
    """
    O Contexto define a interface de interesse para os clientes. Ele também mantém
    uma referência a uma instância de uma subclasse de Estado, que representa o estado atual
    do Contexto.
    """

    _estado = None
    """
    Uma referência ao estado atual do Contexto.
    """

    def __init__(self, estado: Estado) -> None:
        self.mudar_para(estado)

    def mudar_para(self, estado: Estado):
        """
        O Contexto permite mudar o objeto Estado em tempo de execução.
        """

        print(f"Contexto: Mudança para {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self

    """
    O Contexto delega parte de seu comportamento ao objeto Estado atual.
    """

    def requisicao1(self):
        self._estado.tratar1()

    def requisicao2(self):
        self._estado.tratar2()


class Estado(ABC):
    """
    A classe base Estado declara métodos que todos os Estados Concretos devem
    implementar e também fornece uma referência de volta ao objeto Contexto,
    associado ao Estado. Esta referência de volta pode ser usada pelos Estados para
    mudar o Contexto para outro Estado.
    """

    @property
    def contexto(self) -> Contexto:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Contexto) -> None:
        self._contexto = contexto

    @abstractmethod
    def tratar1(self) -> None:
        pass

    @abstractmethod
    def tratar2(self) -> None:
        pass


"""
Estados Concretos implementam vários comportamentos, associados a um estado do
Contexto.
"""


class EstadoConcretoA(Estado):
    def tratar1(self) -> None:
        print("EstadoConcretoA trata a requisição1.")
        print("EstadoConcretoA quer mudar o estado do contexto.")
        self.contexto.mudar_para(EstadoConcretoB())

    def tratar2(self) -> None:
        print("EstadoConcretoA trata a requisição2.")


class EstadoConcretoB(Estado):
    def tratar1(self) -> None:
        print("EstadoConcretoB trata a requisição1.")

    def tratar2(self) -> None:
        print("EstadoConcretoB trata a requisição2.")
        print("EstadoConcretoB quer mudar o estado do contexto.")
        self.contexto.mudar_para(EstadoConcretoA())


if __name__ == "__main__":
    # O código do cliente.

    contexto = Contexto(EstadoConcretoA())
    contexto.requisicao1()
    contexto.requisicao2()