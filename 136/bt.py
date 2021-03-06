"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum
from collections import defaultdict


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7



blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}



# complete :
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """
    try:
        if isinstance(donor, Bloodtype):
            donor = donor.value
        if type(donor) == str:
            donor = blood_type_text[donor].value
        if type(donor) == int:
            if donor>7 or donor<0:
                raise ValueError
            donor = donor
        else:
            raise TypeError
    except KeyError:
        raise ValueError

    try:
        if isinstance(recipient, Bloodtype):
            recipient = recipient.value
        if type(recipient) == str:
            recipient = blood_type_text[recipient].value
        if type(recipient) == int:
            if recipient>7 or recipient<0:
                raise ValueError
            recipient = recipient
        else:
            raise TypeError
    except ValueError:
        raise ValueError
   
    blood_dict = defaultdict(list)
    blood_dict = { 0: [0, 1, 2, 3, 4, 5, 6, 7],
                   1: [1, 3, 5, 6, 7],
                   2: [2, 3, 6, 7],
                   3: [3, 6, 7],
                   4: [4, 6, 7],
                   5: [5, 6, 7],
                   6: [6, 7],
                   7: [7]}


    if donor == 0:
        if recipient in blood_dict[0]:
            return True
        else:
            return False
    if donor == 1:
        if recipient in blood_dict[1]:
            return True
        else:
            return False
    if donor == 2:
        if recipient in blood_dict[2]:
            return True
        else:
            return False
    if donor == 3:
        if recipient in blood_dict[3]:
            return True
        else:
            return False
    if donor == 4:
        if recipient in blood_dict[4]:
            return True
        else:
            return False
    if donor == 5:
        if recipient in blood_dict[5]:
            return True
        else:
            return False
    if donor == 6:
        if recipient in blood_dict[6]:
            return True
        else:
            return False
    if donor == 7:
        if recipient in blood_dict[7]:
            return True
        else:
            return False

# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )
