

from __future__ import print_function
# from abstractgameunit import AbstractGameUnit
from gameunit import AbstractGameUnit
from gameutils import print_bold


class Knight(AbstractGameUnit):
    """
    Class that represents the game character 'Knight'

    The player instance in the game is a Knight Instance.
    Other Knight instances are considered as 'friends' of the player
    and is indicated by the attribute 'self.unit_type'.
    """
    def __init__(self, name='Jibreel'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """
        Print basic information about this character
        """
        print("I'm a Knight")

    def acquire_hut(self, hut):
        """
        Fight thte combat (command line) to acquire the hut

        ..todo:: acquire_hut method can be refactored.
                 Example: Can you use self.enemy instead of
                calling hut.occupant every time?
        """
        # refactor
        print_bold("Entering hut %d..." % hut.number, end=' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit) and
                    hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'

        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')
            while continue_attack:
                continue_attack = input("......continue attack? (y/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() == 'unoccupied':
                print_bold("Hut is occupied")
            else:
                print_bold("Friend Sighted!!!")
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """
        Abandon the Battle.
        """
        print_bold("Running Away...")
        self.enemy = None


if __name__ == "__main__":
    # Inherits from ABC
    k = Knight()
    k.info()
