NAMES = ['arnold schwarzenegger', 'alec baldwin', 'Bob Belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'Bob Belderbos', 'julian sequeira',
         'al pacino', 'Brad Pitt', 'matt damon', 'Brad Pitt']

newlist =[]

def dedup_and_title_case_names(names):
    for i in names:
        a = i.title()
        newlist.append(a)
    return list(set(newlist))
    """Should return a list of names, each name appears only once"""
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split()[-1], reverse=True )

    
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...