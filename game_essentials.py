class Game:
    def __init__(self, players):
        self.players = players
        self.is_day = True
        self.num_living = len(players)

    def turn_night(self):
        self.is_day = False

    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Mafioso" or killer.role.__class__.__name__ == "Godfather":
                message = f"{target.name} was killed by the mafia."
                recipient = "everyone"
                del self.players[self.players.index(target)]
            elif killer.role.__class__.__name__ == "Janitor":
                message = f"{target.name} was cleaned"
                recipient = "everyone"
                del self.players[self.players.index(target)]

        else:
            message = "Your target's defense is too high."
            recipient = killer
        return [message, recipient]
