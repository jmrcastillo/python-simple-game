

import random
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from gameutils import print_bold


class AttackOfTheOrcs:
    """Main class to play attack of the Orcs game"""

    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        """Return a list of occupant types for all huts.
        .. todo::

            Prone to bugs if self.huts is not populated.
            Chapter 2 talks about catching exceptions
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print(" 1. Fight with the enemy.")
        print(" 2. Bring all the huts in the village under your control")
        print("----------------------------------------------------------")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants())
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")

            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid Input, args: %s \n" % e.args)
                continue

            try:
                if self.huts[idx - 1].is_acquired:
                        print("You have already acquired this hut. Try again."
                              "<INFO: You can Not get healed in already " /
                              "acquired hut.")
                else:
                    verifying_choice = False

            except IndexError:
                print("Invalid input : ", idx)
                print("Number should be in range 1-5. Try again")
                continue

        return idx

    def _occupy_huts(self):
        """Randomly occupy thte huts with one of: friend, enemy or 'None'"""
        for i in range(5):
            choice_list = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_list)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def setup_game_scenario(self):
        """Create player and huts and then randomly pre occupy huts"""
        self.player = Knight()
        self._occupy_huts()
        self.show_game_mission()
        self.player.show_health(bold=True)

    def play(self):
        """
        Workhorse method to play the game
        """
        # Create a Knight instance , create huts and preoccupy them
        # with a game character instance (or leave empty)
        self.setup_game_scenario()
        acquired_hut_counter = 0
        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold("Your Lose :( Better Luck Next Time!!!")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations!!! You Win!!!")


if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()
