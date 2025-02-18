from abc import ABC, abstractmethod

# Interface da Estratégia
class Estrategia(ABC):
    @abstractmethod
    def executar(self, dados):
        pass

# Contexto
class Contexto:
    def __init__(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def executar_estrategia(self, dados):
        return self._estrategia.executar(dados)

# Estratégia concreta para cálculo de imposto padrão
class EstrategiaImpostoPadrao(Estrategia):
    def executar(self, dados):
        return dados * 0.2  # 20% de imposto

# Estratégia concreta para cálculo de imposto reduzido
class EstrategiaImpostoReduzido(Estrategia):
    def executar(self, dados):
        return dados * 0.1  # 10% de imposto

def principal():
    valor = 1000  # Valor sobre o qual o imposto será calculado

    # Usando a estratégia de imposto padrão
    contexto = Contexto(EstrategiaImpostoPadrao())
    print("Imposto Padrão:", contexto.executar_estrategia(valor))

    # Mudando para a estratégia de imposto reduzido
    contexto.definir_estrategia(EstrategiaImpostoReduzido())
    print("Imposto Reduzido:", contexto.executar_estrategia(valor))

if __name__ == "__main__":
    principal()
