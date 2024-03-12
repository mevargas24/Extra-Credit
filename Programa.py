import random
from Criatura import Criatura
from Jugador import Jugador
from Location import Location, Ruta, Ciudad
from Batalla import Batalla


def add_attack(self, attack):
        self.attacks.append(attack)
def choose_attack(self):
        return random.choice(self.attacks)
def choose_starter(self, starter):
        self.starter = starter
def start_battle(self):
        print("¡Comienza la batalla!")
        while self.jugador.starter.health > 0 and self.oponente.health > 0:
            player_attack = self.player.starter.choose_attack()
            oponente_attack = self.oponente.choose_attack()
            print(f"{self.player.starter.name} usa {player_attack}!")
            print(f"{self.oponente.name} usa {oponente_attack}!")
            # Lógica para calcular daño y actualizar la salud de los combatientes
        if self.player.starter.health <= 0:
            print("¡Has perdido la batalla!")
        else:
            print("¡Has ganado la batalla!")
def encounter(self):
        print(f"Te encuentras con un {self.creature.name} salvaje!")
def heal_starter(self):
        print("Tu starter ha sido curado.")

def battle_leader(self, leader):
        print(f"¡Te enfrentas al líder {leader.name}!")

def next_location(self):
        pass

def previous_location(self):
        pass
creature1 = Criatura("Dragón", "Fuego")
creature1.add_attack("Aliento de Fuego")
creature1.add_attack("Garra de Dragón")
creature1.add_attack("Cola Ardiente")

creature2 = Criatura("Hada", "Hada")
creature2.add_attack("Beso Encantado")
creature2.add_attack("Poder Mágico")
creature2.add_attack("Danza de las Hadas")



