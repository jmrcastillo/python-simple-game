

from knight import Knight
from gameuniterror import GameUnitError

# See the module docstring for details.
if __name__ == '__main__':
    print("Creating a Knight..")
    knight = Knight("Sir Bar")
    # Assume the Knight has sustained injuries in the combat.
    knight.health_meter = 10
    knight.show_health()
    try:
        # Heal the knight by 100 hit points. This will raise an
        # exception as the Knight can have upto 40 hit points.
        knight.heal(heal_by=100, full_healing=False)

    except GameUnitError as e:
        # Print the information about the error
        print(e)
        print(e.error_message)

    knight.show_health()
