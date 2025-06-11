"""
This local discord leveling system uses the same levels and XP needed values as MEE6.
All credit goes towards the MEE6 developers for providing the "LEVELS_AND_XP" documentation. 

MEE6 documentation can be found here: https://github.com/Mee6/Mee6-documentation
"""

from collections import namedtuple
from typing import Final, NamedTuple

__all__ = ('LEVELS_AND_XP', 'MAX_XP', 'MAX_LEVEL', '_next_level_details', '_find_level')

LEVELS_AND_XP: Final = {
    '0': 0,
    '1': 100,
    '2': 255,
    '3': 475,
    '4': 770,
    '5': 1150,
    '6': 1625,
    '7': 2205,
    '8': 2900,
    '9': 3720,
    '10': 4675,
    '11': 5775,
    '12': 7030,
    '13': 8450,
    '14': 10045,
    '15': 11825,
    '16': 13800,
    '17': 15980,
    '18': 18375,
    '19': 20995,
    '20': 23850,
    '21': 26950,
    '22': 30305,
    '23': 33925,
    '24': 37820,
    '25': 42000,
    '26': 46475,
    '27': 51255,
    '28': 56350,
    '29': 61770,
    '30': 67525,
    '31': 73625,
    '32': 80080,
    '33': 86900,
    '34': 94095,
    '35': 101675,
    '36': 109650,
    '37': 118030,
    '38': 126825,
    '39': 136045,
    '40': 145700,
    '41': 155800,
    '42': 166355,
    '43': 177375,
    '44': 188870,
    '45': 200850,
    '46': 213325,
    '47': 226305,
    '48': 239800,
    '49': 253820,
    '50': 268375,
    '51': 283475,
    '52': 299130,
    '53': 315350,
    '54': 332145,
    '55': 349525,
    '56': 367500,
    '57': 386080,
    '58': 405275,
    '59': 425095,
    '60': 445550,
    '61': 466650,
    '62': 488405,
    '63': 510825,
    '64': 533920,
    '65': 557700,
    '66': 582175,
    '67': 607355,
    '68': 633250,
    '69': 659870,
    '70': 687225,
    '71': 715325,
    '72': 744180,
    '73': 773800,
    '74': 804195,
    '75': 835375,
    '76': 867350,
    '77': 900130,
    '78': 933725,
    '79': 968145,
    '80': 1003400,
    '81': 1039500,
    '82': 1076455,
    '83': 1114275,
    '84': 1152970,
    '85': 1192550,
    '86': 1233025,
    '87': 1274405,
    '88': 1316700,
    '89': 1359920,
    '90': 1404075,
    '91': 1449175,
    '92': 1495230,
    '93': 1542250,
    '94': 1590245,
    '95': 1639225,
    '96': 1689200,
    '97': 1740180,
    '98': 1792175,
    '99': 1845195,
    '100': 1899250
}

MAX_XP: Final = None
MAX_LEVEL: Final = None

def xp_for_level(level: int) -> int:
    """Returns the XP needed to reach a given level."""
    if str(level) in LEVELS_AND_XP:
        return LEVELS_AND_XP[str(level)]
    # Example formula for levels above 100:
    base = LEVELS_AND_XP['100']
    # Increase XP needed by 5% per level after 100
    extra = 1.05 ** (level - 100)
    return int(base * extra)


def _next_level_details(current_level: int) -> NamedTuple:
<<<<<<< Updated upstream
    """Returns a `namedtuple`
    
    Attributes
    ----------
    - level (:class:`int`)
    - xp_needed (:class:`int`)
    
        .. changes
            v0.0.2
                Changed return type to a namedtuple instead of tuple
    """
    temp = current_level + 1
    key = str(temp)
    if key in LEVELS_AND_XP:
        val = LEVELS_AND_XP[key]
    else:
        # Calculate XP needed for levels beyond the predefined ones
        val = LEVELS_AND_XP['100'] + (temp - 100) * 50000  # Example increment
=======
    """Returns a namedtuple with the next level and its XP needed."""
    next_level = current_level + 1
    val = xp_for_level(next_level)
>>>>>>> Stashed changes
    Details = namedtuple('Details', ['level', 'xp_needed'])
    return Details(level=next_level, xp_needed=val)

<<<<<<< Updated upstream
def _find_level(current_total_xp: int) -> int: # type: ignore / this WILL return an `int` unless the user intentionally changed the values by altering the code 
    """Return the members current level based on their total XP

    NOTE: Do not use this with detecting level ups in :meth:`award_xp`. Pretty much only made for :meth:`add_xp`, :meth:`remove_xp`
    
        .. added:: v0.0.2
    """
    for level, xp_needed in LEVELS_AND_XP.items():
        if current_total_xp < xp_needed:
            return int(level) - 1
    # Calculate level for XP beyond the predefined ones
    base_xp = LEVELS_AND_XP['100']
    if current_total_xp >= base_xp:
        extra_levels = (current_total_xp - base_xp) // 50000
        return 100 + extra_levels
    return 0

def get_xp_for_level(level: int) -> int:
    """Returns the total XP needed to reach the given level.
    
    Parameters
    ----------
    level: :class:`int`
        The level for which to get the XP.
    
    Returns
    -------
    :class:`int`
        The total XP needed to reach the given level.
    """
    if level <= 100:
        key = str(level)
        if key in LEVELS_AND_XP:
            return LEVELS_AND_XP[key]
        else:
            raise ValueError(f"Level {level} is not defined in LEVELS_AND_XP.")
    else:
        # Calculate XP needed for levels beyond the predefined ones
        return LEVELS_AND_XP['100'] + (level - 100) * 50000  # Example increment

# Example usage:
# xp_needed = get_xp_for_level(105)
# print(f"XP needed for level 105: {xp_needed}")


=======
def _find_level(current_total_xp: int) -> int:
    """Return the current level based on total XP (works for unlimited levels)."""
    # First, check for levels in the static table
    levels = [int(lvl) for lvl in LEVELS_AND_XP.keys()]
    levels.sort()
    for lvl in levels:
        if current_total_xp < LEVELS_AND_XP[str(lvl)]:
            return max(lvl - 1, 0)
    # If XP is higher than table, use the formula
    lvl = 100
    while True:
        xp_needed = xp_for_level(lvl + 1)
        if current_total_xp < xp_needed:
            return lvl
        lvl += 1
>>>>>>> Stashed changes
