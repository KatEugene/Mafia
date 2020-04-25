# IN PROGRESS
# Game "Mafia"
# Version 2.0
# Created by Katasonov Eugene

from Data import list_of_players
from random import choice


class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def killed(self):
        self.alive = False

    def alive(self):
        return self.alive

    def name(self):
        return self.name


class Civilian(Player):
    def __init__(self, name):
        super().__init__(name)


class Mafia(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def kill(player):
        player.killed()


class DonMafia(Player):
    pass


class Maniac(Player):
    pass


class Detective(Player):
    pass


class Doctor(Player):
    pass


class NightFly(Player):
    pass
