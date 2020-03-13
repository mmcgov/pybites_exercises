class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first separated by a whitespace
           and using title case for both.
        """
        f_name = self.first_name.title()
        l_name = self.last_name.title()
        return f'{f_name} {l_name}'

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        f_name = self.first_name[0].lower()
        l_name = self.last_name[:8].lower()
        return f'{f_name}{l_name}'

    # TODO 3: you code
    #
    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    def __str__(self):
        f_name = self.first_name.title()
        l_name = self.last_name.title()
        uf_name = self.first_name[0].lower()
        ul_name = self.last_name[:8].lower()
        return f'{f_name} {l_name} ({uf_name}{ul_name})' 


    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return self.__class__.__name__
