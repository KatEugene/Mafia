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
        self.immunity = False

    def __str__(self):
        return f"Игрок: {self.name}, Жив: {self.alive}"

    def killed(self):
        self.alive = False

    def get_alive(self):
        return self.alive

    def get_name(self):
        return self.name

    def get_immunity(self):
        return self.immunity

    def set_immunity(self):
        self.immunity = True


class Civilian(Player):
    def __init__(self, name):
        super().__init__(name)


class Mafia(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def kill(player):
        if not player.immunity():
            player.killed()


class DonMafia(Player):
    def __init__(self, name):
        super().__init__(name)


class Maniac(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def kill(player):
        if not player.immunity():
            player.killed()


class Detective(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def check(player):
        if type(player) == DonMafia:
            return "DonMafia"
        elif type(player) == Mafia:
            return "Mafia"
        else:
            return "Civilian"


class Doctor(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def treat(player):
        player.set_immunity()


class NightFly(Player):
    def __init__(self, name):
        super().__init__(name)
        self.night_person = None

    def spend_night(self, player):
        player.set_immunity()
        self.night_person = player


if __name__ == "__main__":
    pass
