def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    results = dict()
    passwd = passwd.split('\n')[1:-1]
    for entry in passwd:
        entry = entry.split(':')
        results[entry[0].strip()] = entry[4].replace(',','').strip()
    return results


