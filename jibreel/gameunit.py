

from __future__ import print_function
import random
from abc import ABC, abstractmethod
from gameutils import print_bold, weighted_random_selection
from gameuniterror import HealthMeterException


class AbstractGameUnit(ABC):
    """a base class for creating various game characters"""
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """information on the unit (overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """the main logic to determine injured unit and amount of injury

        .. todo:: check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("attack! ", end='')
        self.show_health(end='  ')
        enemy.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            # todo: do you see a bug here? it can exceed max hit points!
            self.health_meter += heal_by

        # raise a custom exception
        if self.health_meter > self.max_hp:
            raise HealthMeterException("health_meter > max_hp!")

        print_bold("you are healed!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """show the remaining hit points of the player and the enemy"""
        # todo: what if there is no enemy?
        msg = "health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
