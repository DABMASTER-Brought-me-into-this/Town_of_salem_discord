class Game:
    def __init__(self, players):
        self.players = players
        self.is_day = True
        self.dead_players = []
        self.num_living = len(players)

    def turn_night(self):
        self.is_day = False

    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Mafioso" or killer.role.__class__.__name__ == "Godfather":
                message = f"{target.name} was killed by the mafia."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."




        else:
            message = "Your target's defense is too high."
            recipient = killer
        return [message, recipient]

class Player:
    def __init__(self, name, role, number):
        self.name = name