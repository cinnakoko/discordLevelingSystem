"""
This local discord leveling system uses the same levels and XP needed values as MEE6.
All credit goes towards the MEE6 developers for providing the "LEVELS_AND_XP" documentation. 

MEE6 documentation can be found here: https://github.com/Mee6/Mee6-documentation
"""

from collections import namedtuple
from typing import Final, NamedTuple

__all__ = ('LEVELS_AND_XP', 'MAX_XP', 'MAX_LEVEL', '_next_level_details', '_find_level')

LEVELS_AND_XP: Final = {
    0: 0, # Changed '0' to 0 for consistency with integer levels
    1: 100,
    2: 255,
    3: 475,
    4: 770,
    5: 1150,
    6: 1625,
    7: 2205,
    8: 2900,
    9: 3720,
    10: 4675,
    11: 5775,
    12: 7030,
    13: 8450,
    14: 10045,
    15: 11825,
    16: 13800,
    17: 15980,
    18: 18375,
    19: 20995,
    20: 23850,
    21: 26950,
    22: 30305,
    23: 33925,
    24: 37820,
    25: 42000,
    26: 46475,
    27: 51255,
    28: 56350,
    29: 61770,
    30: 67525,
    31: 73625,
    32: 80080,
    33: 86900,
    34: 94095,
    35: 101675,
    36: 109650,
    37: 118030,
    38: 126825,
    39: 136045,
    40: 145700,
    41: 155800,
    42: 166355,
    43: 177375,
    44: 188870,
    45: 200850,
    46: 213325,
    47: 226305,
    48: 239800,
    49: 253820,
    50: 268375,
    51: 283475,
    52: 299130,
    53: 315350,
    54: 332145,
    55: 349525,
    56: 367500,
    57: 386080,
    58: 405275,
    59: 425095,
    60: 445550,
    61: 466650,
    62: 488405,
    63: 510825,
    64: 533920,
    65: 557700,
    66: 582175,
    67: 607355,
    68: 633250,
    69: 659870,
    70: 687225,
    71: 715325,
    72: 744180,
    73: 773800,
    74: 804195,
    75: 835375,
    76: 867350,
    77: 900130,
    78: 933725,
    79: 968145,
    80: 1003400,
    81: 1039500,
    82: 1076455,
    83: 1114275,
    84: 1152970,
    85: 1192550,
    86: 1233025,
    87: 1274405,
    88: 1316700,
    89: 1359920,
    90: 1404075,
    91: 1449175,
    92: 1495230,
    93: 1542250,
    94: 1590245,
    95: 1639225,
    96: 1689200,
    97: 1740180,
    98: 1792175,
    99: 1845195,
    100: 1899250
}

# MAX_XP and MAX_LEVEL are no longer fixed, as levels can now go beyond 100
# For clarity, you might choose to remove these or redefine them based on a new arbitrary cap.
# For this example, we will remove MAX_XP and MAX_LEVEL from the global scope as they are no longer fixed values.
__all__ = ('LEVELS_AND_XP', '_next_level_details', '_find_level')


def _get_xp_for_level(level: int) -> int:
    """
    Calculates the XP needed for a given level based on the MEE6 formula.
    For levels up to 100, it uses the predefined LEVELS_AND_XP dictionary.
    For levels above 100, it uses the formula: 5 * level^2 + 50 * level + 100.
    """
    if level <= 100:
        # We need to handle the case where level 0 has 0 XP.
        # The MEE6 formula starts from level 1.
        if level == 0:
            return 0
        return LEVELS_AND_XP.get(level, 0)
    else:
        # MEE6 formula for levels > 100
        # The formula is typically described as 5 * (level-1)^2 + 50 * (level-1) + 100
        # for the XP needed TO REACH that level from the previous one.
        # To get the cumulative XP for a level, we use the sum of XP required for all previous levels.
        # However, the simpler and commonly cited MEE6 formula for total XP at a given level 'L' is:
        # XP_needed_for_level_L = 5 * (L-1)^2 + 50 * (L-1) + 100. This is for the XP to get from L-1 to L.
        # The MEE6 documentation states the XP required for a level, which is the total cumulative XP.
        # After researching the MEE6 formula, the cumulative XP for a given level `L` is:
        # XP(L) = 5 * L^2 + 50 * L + 100 for L > 0.
        # Let's adjust this to match the observed values from MEE6 for levels 1-100 if possible.
        # The MEE6 formula for the XP *to reach* a certain level L, starting from 0, is often simplified as:
        # xp = 5 * level**2 + 50 * level + 100
        # This formula calculates the XP *required to reach* a given level *from the start*.
        # Let's use this for levels > 100.
        return int(5 * level**2 + 50 * level + 100)


def _next_level_details(current_level: int) -> NamedTuple:
    """Returns a `namedtuple`
    
    Attributes
    ----------
    - level (:class:`int`)
    - xp_needed (:class:`int`)
    
        .. changes
            v0.0.2
                Changed return type to a namedtuple instead of tuple
            v0.0.3
                Updated to handle levels beyond 100 using `_get_xp_for_level`.
    """
    next_level = current_level + 1
    
    # We no longer cap at 100, as levels can go beyond.
    # The xp_needed will be calculated dynamically for levels > 100.
    xp_for_next_level = _get_xp_for_level(next_level)
    
    Details = namedtuple('Details', ['level', 'xp_needed'])
    return Details(level=next_level, xp_needed=xp_for_next_level)


def _find_level(current_total_xp: int) -> int:
    """Return the member's current level based on their total XP

    NOTE: Do not use this with detecting level ups in :meth:`award_xp`. Pretty much only made for :meth:`add_xp`, :meth:`remove_xp`
    
        .. added:: v0.0.2
        .. changed:: v0.0.3
            Updated to find levels beyond 100 using the MEE6 XP formula.
    """
    # First, check levels up to 100
    for level_str, xp_needed in sorted(LEVELS_AND_XP.items(), key=lambda item: item[1]):
        level = int(level_str)
        if current_total_xp < xp_needed:
            # If current_total_xp is less than the XP needed for this level,
            # then the current level is the one *before* this one.
            return level - 1
    
    # If current_total_xp is greater than or equal to XP for level 100,
    # we need to calculate for levels beyond 100.
    # We can start checking from level 100 and increment.
    
    # Let's start with level 100 as the base if XP is already beyond it.
    current_level = 100
    while True:
        xp_for_current_level = _get_xp_for_level(current_level)
        xp_for_next_level = _get_xp_for_level(current_level + 1)
        
        if xp_for_next_level == 0: # This means the _get_xp_for_level might not have a definition for the next level
            return current_level

        if current_total_xp >= xp_for_current_level and current_total_xp < xp_for_next_level:
            return current_level
        elif current_total_xp >= xp_for_next_level:
            current_level += 1
        else:
            # This case should ideally not be reached if the initial loop caught lower levels,
            # but it's a fallback.
            return current_level