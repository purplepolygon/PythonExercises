# Validate 4 and 6 digit pin numbers


import re


def validate_pin(pin):
    if re.match(r'^[0-9]{4}\n|^[0-9]{6}\n', pin):  # Obscure use case when str contains new line
        return False

    if re.match(r"^[0-9]{4}$|^[0-9]{6}$", pin):
        return True

    else:
        return False


validate_pin('235253')
