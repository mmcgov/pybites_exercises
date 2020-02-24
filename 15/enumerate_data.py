names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    j=0
    res=list()
    max_len = len(max(names, key=len))
    for c, value in enumerate(names, 1):
        dis = 4+max_len-len(value)
        print(f'{c}. '+f'{value}'+' '*dis+f'{countries[j]:<}')
        j+=1
