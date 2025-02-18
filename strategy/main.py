from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Contexto():
    """
    O Contexto define a interface de interesse para os clientes.
    """

    def __init__(self, estrategia: Estrategia) -> None:
        """
        Normalmente, o Contexto aceita uma estratégia através do construtor, mas
        também fornece um setter para alterá-la em tempo de execução.
        """

        self._estrategia = estrategia

    @property
    def estrategia(self) -> Estrategia:
        """
        O Contexto mantém uma referência a um dos objetos Estrategia. O
        Contexto não conhece a classe concreta de uma estratégia. Ele deve funcionar
        com todas as estratégias através da interface Estrategia.
        """

        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: Estrategia) -> None:
        """
        Normalmente, o Contexto permite substituir um objeto Estrategia em tempo de execução.
        """

        self._estrategia = estrategia

    def executar_alguma_logica_de_negocio(self) -> None:
        """
        O Contexto delega algum trabalho ao objeto Estrategia em vez de
        implementar várias versões do algoritmo por conta própria.
        """

        # ...

        print("Contexto: Ordenando dados usando a estratégia (não tenho certeza de como ela fará isso)")
        resultado = self._estrategia.fazer_algoritmo(["a", "b", "c", "d", "e"])
        print(",".join(resultado))

        # ...


class Estrategia(ABC):
    """
    A interface Estrategia declara operações comuns a todas as versões suportadas
    de algum algoritmo.

    O Contexto usa essa interface para chamar o algoritmo definido pelas
    Estratégias Concretas.
    """

    @abstractmethod
    def fazer_algoritmo(self, dados: List):
        pass


"""
Estratégias Concretas implementam o algoritmo seguindo a interface base Estrategia.
A interface as torna intercambiáveis no Contexto.
"""


class EstrategiaConcretaA(Estrategia):
    def fazer_algoritmo(self, dados: List) -> List:
        return sorted(dados)


class EstrategiaConcretaB(Estrategia):
    def fazer_algoritmo(self, dados: List) -> List:
        return reversed(sorted(dados))


if __name__ == "__main__":
    # O código do cliente escolhe uma estratégia concreta e a passa para o contexto.
    # O cliente deve estar ciente das diferenças entre as estratégias para
    # fazer a escolha certa.

    contexto = Contexto(EstrategiaConcretaA())
    print("Cliente: A estratégia está definida para ordenação normal.")
    contexto.executar_alguma_logica_de_negocio()
    print()

    print("Cliente: A estratégia está definida para ordenação reversa.")
    contexto.estrategia = EstrategiaConcretaB()
    contexto.executar_alguma_logica_de_negocio()