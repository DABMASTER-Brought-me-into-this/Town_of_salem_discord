
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class PlagueBearer:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 0
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True:
          target.infect = True
          self.kill_count += 1
          if target.infected == targetoftarget:
            self.kill_count += 1
            if self.kill_count > 4:
              self.become_pestilence = True
              recipient = "user"
              message = "You have become Pestilence"
        else:
          recipient = "user"
          message = f"{target} is infected"

roles = ['Jailor', 'Mayor', 'Retributionist', 'Veteran', 'Godfather', 'Mafioso', 'Ambusher', 'Juddgernut', 'PlagueBearer', 'Pestilence', 'Pirate', 'Werewolf', 'Coven Leader', 'Necromancer',  'Medusa', 'Poisioner', 'Hex Master', 'Potion Master']

def kill(self, target, killer):
  pass
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class Pestilence:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 1000
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True:
          kill(target, killer="Pestilence")

roles = ['Jailor', 'Mayor', 'Retributionist', 'Veteran', 'Godfather', 'Mafioso', 'Ambusher', 'Juddgernut', 'PlagueBearer', 'Pestilence', 'Pirate', 'Werewolf', 'Coven Leader', 'Necromancer',  'Medusa', 'Poisioner', 'Hex Master', 'Potion Master']

def kill(self, target, killer):
  pass
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class Pirate:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.can_role_block = False
        self.control_immunity = True
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True:
          kill(target, killer="Pirate")
        else:
          recipient = "user"
          message = f"{target}'s defense is too high"

roles = ['Jailor', 'Mayor', 'Retributionist', 'Veteran', 'Godfather', 'Mafioso', 'Ambusher', 'Juddgernut', 'PlagueBearer', 'Pestilence', 'Pirate', 'Werewolf', 'Coven Leader', 'Necromancer',  'Medusa', 'Poisioner', 'Hex Master', 'Potion Master']

def kill(self, target, killer):
  pass
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class Werewolf:
    def init(self, game_object):
        self.faction = "Coven"
        if game_object.full_moon == True:
          self.can_kill = True
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 0
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True and self.can_kill == True:
          kill(target, killer="Werewolf")
        elif self.can_kill != True:
          recipient = "user"
          message = "You can't kill, because it isnt a full moon"
        else:
          recipient = "user"
          message = "You did not preform your night ability"

roles = ['Jailor', 'Mayor', 'Retributionist', 'Veteran', 'Godfather', 'Mafioso', 'Ambusher', 'Juddgernut', 'PlagueBearer', 'Pestilence', 'Pirate', 'Werewolf', 'Coven Leader', 'Necromancer',  'Medusa', 'Poisioner', 'Hex Master', 'Potion Master']

def kill(self, target, killer):
  pass
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class CovenLeader:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True and target.control_immunity == False:
          target.control = True
        else:
          recipient = "user"
          message = "Target was immune to control"

roles = ['Jailor', 'Mayor', 'Retributionist', 'Veteran', 'Godfather', 'Mafioso', 'Ambusher', 'Juddgernut', 'PlagueBearer', 'Pestilence', 'Pirate', 'Werewolf', 'Coven Leader', 'Necromancer',  'Medusa', 'Poisioner', 'Hex Master', 'Potion Master']

def kill(self, target, killer):
  pass
class Jailor:
    def __init__(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 100
        self.limit = 3
        self.voting_power =1
        self.game_object = game_object

    def use_abil(self, target):
        target.targer_captured = True
        if target.targer_captured == True:
          self.can_kill = True 
          if self.want_kill == True:
            kill(target, killer="Jailor") 
          
class Mayor:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 1
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, name):
        if self.limit == 0:
            self.voting_power = 3
            message = f"The mayor has revealed himself as {name}"
            self.limit = 0
        
        else:
          recipient = "user"
          message = "You have already revealed yourself -_-"

class Retributionist:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 0
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          target.resseruct = True
        else:
          recipient = "user"
          message = "Breh he aint dead your ability is RESSERUCTING the DEAD not the alive"

class Veteran:
    def init(self, game_object):
        self.faction = "Town"
        self.is_sus = False
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.game_object = game_object
    def use_abil(self, target):
        self.want_to_resseruct_d_ded = False
        if self.want_to_resseruct_d_ded == True:
          self.attack = 10000000000000000
          self.defense = 1000000000000000000
          self.limit -= 1
          if self.limit == 0:
            recipient = "user"
            message = "You do not have this ability anymore"
                   
class Godfather:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus = True
        self.defense = 0
        self.attack = 0
        self.limit = 3
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, "Mafioso")
        elif target.defense > self.attack:
          recipient = "user"
          message = "Target had too high defense"
        else:
          self.want_use_abile = False

class Ambusher:
    def init(self, game_object):
        self.faction = "Mafia"
        self.is_sus =  True
        self.defense = 0
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if target.visted == True:
          kill(target.visitor, killer="Ambusher")
        else:
          recipient = "user"
          message = f"No one Visited your {target}"

class Juddgernut:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target):
        if self.want_use_abile == True:
          kill(target, killer="Juddgernut")
          self.kill_count += 1
          if self.kill_count > 2:
            self.attack = 10000000000000000
        else:
          recipient = "user"
          message = f"{target} had too much defense"

class Necromancer:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        if game_object.night >2:
          self.inherit_necrom = True
        self.attack = 0
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True and self.inherit_necrom == True:
          kill(target, killer = "Necromancer")
        else:
          recipient = "user"
          message = "Your target defense was too high or you do not have Necromazer"

class Medusa:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = True
        self.defense = 20
        if game_object.night >2:
          self.inherit_necrom = True
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        if self.inherit_necrom == True:
          self.is_sus = False
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True:
          kill(target, killer = "Medusa")
        else:
          recipient = "user"
          message = "Your target defense was too high"

class Poisioner:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = True
        self.defense = 0
        if game_object.night >2:
          self.inherit_necrom = True
        self.attack = 20
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        if self.inherit_necrom ==  True:
          self.is_sus =  False
        self.game_object = game_object
    def use_abil(self, target, game_object):
        if self.want_use_abile == True and self.inherit_necrom == True:
          kill(target, killer = "Poisioner")
          if game_object.target.live_after_attack > 1:
              kill(target, killer="Poisioner")
        else:
          recipient = "user"
          message = "Your target defense was too high"

class HexMaster:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 0
        if game_object.night >2:
          self.inherit_necrom = True
        self.attack = 1000000000000000000000000000000000000000000000000000000000
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
        if self.inherit_necrom == True:
          self.is_sus = False
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True and self.inherit_necrom == True:
          kill(target, killer = "HexMaster")
        
class PotionMaster:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = False
        self.defense = 20
        if game_object.night >2:
          self.inherit_necrom = True
        self.attack = 0
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
        if self.inherit_necrom == True:
          self.is_sus = False
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True and self.want_to_kill == True:
          kill(target, killer = "Potion Master")
        elif self.want_use_abile == True and self.want_to_heal == True:
          heal(target, killer = "Potion Master")
        elif self.want_use_abile == True and self.want_to_reveal == True:
          recipient = "everyone"
          message = reveal(target, killer = "Potion Master")
        else:
          recipient = "user"
          message = "You did not use your night ability"
 

class Mafioso:
    def init(self, game_object):
        self.faction = "Coven"
        self.kill_count = 0
        self.is_sus = True
        self.defense = 0
        self.attack = 100
        self.limit = 'Infinite'
        self.voting_power = 1
        self.want_use_abile = False
        self.game_object = game_object
    def use_abil(self, target, targetoftarget):
        if self.want_use_abile == True:
          kill(target, killer = "Mafioso")
        else: 
            recipient = "user"
            message = f"{target}'s defense too high"
