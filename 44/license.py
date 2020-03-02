import secrets
import string


def gen_key(*, parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase + string.digits
    keys = list()
    for part in range(parts):
        keys.append(''.join(secrets.choice(alphabet) \
                    for i in range(chars_per_part)))
    return '-'.join(keys)
