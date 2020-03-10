import re

def generate_affiliation_link(url):
    num = re.search("dp/(.+)", url).group(1).split('/')[0]
    return f'http://www.amazon.com/dp/{num}/?tag=pyb0f-20'
