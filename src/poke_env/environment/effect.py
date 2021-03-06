# -*- coding: utf-8 -*-
"""This module defines the Effect class, which represents in-game effects.
"""
# pyre-ignore-all-errors[45]

from poke_env.exceptions import UnexpectedEffectException

from enum import Enum, unique, auto


@unique
class Effect(Enum):
    """Enumeration, represent an effect a Pokemon can be affected by."""

    AQUA_RING = auto()
    AROMATHERAPY = auto()
    AROMA_VEIL = auto()
    ATTRACT = auto()
    AUTOTOMIZE = auto()
    BAD_DREAMS = auto()
    BATTLE_BOND = auto()
    BIDE = auto()
    BIND = auto()
    CHARGE = auto()
    CLAMP = auto()
    CONFUSION = auto()
    CRAFTY_SHIELD = auto()
    CURSE = auto()
    CUSTAP_BERRY = auto()
    DANCER = auto()
    DESTINY_BOND = auto()
    DISABLE = auto()
    DISGUISE = auto()
    DOOM_DESIRE = auto()
    ELECTRIC_TERRAIN = auto()
    EMBARGO = auto()
    EMERGENCY_EXIT = auto()
    ENCORE = auto()
    ENDURE = auto()
    FEINT = auto()
    FIRE_SPIN = auto()
    FLASH_FIRE = auto()
    FOCUS_ENERGY = auto()
    FORESIGHT = auto()
    FOREWARN = auto()
    FUTURE_SIGHT = auto()
    GRAVITY = auto()
    GRUDGE = auto()
    GUARD_SPLIT = auto()
    HEAL_BELL = auto()
    HEAL_BLOCK = auto()
    HYDRATION = auto()
    HYPERSPACE_FURY = auto()
    HYPERSPACE_HOLE = auto()
    ILLUSION = auto()
    IMMUNITY = auto()
    IMPRISON = auto()
    INFESTATION = auto()
    INGRAIN = auto()
    INNARDS_OUT = auto
    INSOMNIA = auto()
    IRON_BARBS = auto()
    LASER_FOCUS = auto()
    LEECH_SEED = auto()
    LIMBER = auto()
    LOCK_ON = auto()
    MAGMA_STORM = auto()
    MAGNET_RISE = auto()
    MAGNITUDE = auto()
    MAT_BLOCK = auto()
    MIMIC = auto()
    MIND_READER = auto()
    MIRACLE_EYE = auto()
    MIST = auto()
    MISTY_TERRAIN = auto()
    MUMMY = auto()
    NIGHTMARE = auto()
    OBLIVIOUS = auto()
    OWN_TEMPO = auto()
    PERISH0 = auto()
    PERISH1 = auto()
    PERISH2 = auto()
    PERISH3 = auto()
    PHANTOM_FORCE = auto()
    POWDER = auto()
    POWER_CONSTRUCT = auto()
    POWER_SPLIT = auto()
    POWER_TRICK = auto()
    PROTECT = auto()
    PSYCHIC_TERRAIN = auto()
    PURSUIT = auto()
    QUICK_GUARD = auto()
    ROUGH_SKIN = auto()
    SAFEGUARD = auto()
    SAND_TOMB = auto()
    SHADOW_FORCE = auto()
    SHED_SKIN = auto()
    SKETCH = auto()
    SKILL_SWAP = auto()
    SKY_DROP = auto()
    SLOW_START = auto()
    SMACK_DOWN = auto()
    SNATCH = auto()
    SPEED_SWAP = auto()
    SPITE = auto()
    STICKY_HOLD = auto()
    STICKY_WEB = auto()
    STOCKPILE = auto()
    STOCKPILE1 = auto()
    STOCKPILE2 = auto()
    STOCKPILE3 = auto()
    STRUGGLE = auto()
    SUBSTITUTE = auto()
    SUCTION_CUPS = auto()
    SWEET_VEIL = auto()
    SYNCHRONIZE = auto()
    TAUNT = auto()
    TELEKINESIS = auto()
    THROAT_CHOP = auto()
    TORMENT = auto()
    TRAPPED = auto()
    TRICK = auto()
    TYPEADD = auto()
    TYPECHANGE = auto()
    TYPE_CHANGE = auto()
    UPROAR = auto()
    WATER_BUBBLE = auto()
    WATER_VEIL = auto()
    WHIRLPOOL = auto()
    WIDE_GUARD = auto()
    WIMP_OUT = auto()
    WRAP = auto()
    YAWN = auto()

    def __str__(self) -> str:
        return f"{self.name} (effect) object"

    @staticmethod
    def from_showdown_message(message: str) -> "Effect":
        """Returns the Effect object corresponding to the message.

        :param message: The message to convert.
        :type message: str
        :return: The corresponding Effect object.
        :rtype: Effect
        """
        message = message.replace("item: ", "")
        message = message.replace("move: ", "")
        message = message.replace("ability: ", "")
        message = message.replace(" ", "_")
        try:
            return Effect[message.upper()]
        except KeyError:
            raise UnexpectedEffectException("Unexpected effect '%s' received" % message)
