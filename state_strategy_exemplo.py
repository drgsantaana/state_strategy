# Estratégias de ataque (Strategy)
class EstrategiaAgressiva:
    def atacar(self):
        print("Atacando com força total!")

class EstrategiaDefensiva:
    def atacar(self):
        print("Defendendo e atacando com cautela.")

class EstrategiaEquilibrada:
    def atacar(self):
        print("Equilíbrio entre ataque e defesa.")

# Estados de saúde do personagem (State)
class EstadoNormal:
    def __init__(self, personagem):
        self.personagem = personagem

    def mudar_estado(self):
        print("Personagem em estado normal.")
        self.personagem.definir_estrategia(EstrategiaEquilibrada())

class EstadoFerido:
    def __init__(self, personagem):
        self.personagem = personagem

    def mudar_estado(self):
        print("Personagem ferido. Mudando para estratégia defensiva.")
        self.personagem.definir_estrategia(EstrategiaDefensiva())

class EstadoCritico:
    def __init__(self, personagem):
        self.personagem = personagem

    def mudar_estado(self):
        print("Personagem em estado crítico! Estratégia agressiva ativada.")
        self.personagem.definir_estrategia(EstrategiaAgressiva())

# Classe principal do Personagem
class Personagem:
    def __init__(self):
        self.estado = EstadoNormal(self)
        self.estrategia = EstrategiaEquilibrada()

    def definir_estado(self, estado):
        self.estado = estado
        self.estado.mudar_estado()

    def definir_estrategia(self, estrategia):
        self.estrategia = estrategia

    def atacar(self):
        self.estrategia.atacar()

# Exemplo de uso
personagem = Personagem()

# Estado normal
personagem.atacar()  # "Equilíbrio entre ataque e defesa."

# Mudar para estado ferido
personagem.definir_estado(EstadoFerido(personagem))
personagem.atacar()  # "Defendendo e atacando com cautela."

# Mudar para estado crítico
personagem.definir_estado(EstadoCritico(personagem))
personagem.atacar()  # "Atacando com força total!"
