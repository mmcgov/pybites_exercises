import re

pattern = re.compile(r'(,){2,}')


def get_users(passwd: str) -> dict:
    """Split password output by newline,
 mport      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    results = dict()
    passwd = re.sub(pattern, ' ', passwd).split('\n')[1:-1]
    for entry in passwd:
        entry = entry.split(':')
        results[entry[0].strip()] = entry[4].replace(',','').strip() \
                                    if entry[4] else 'unknown'
    return results



