"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request
import re

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    for line in open(tempfile):
        if 'True' in line:
            yield re.search(r'/(.*),' ,line).group(1)


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    Stats = namedtuple('Stats', 'user, challenge')
    challenges = list()
    users = [x for x in gen_files() if x not in IGNORE]
    for line in open(tempfile):
        if any(word in re.search(r'/(.*),' ,line).group(1) for word in IGNORE):
            continue
        elif 'True' in line:
                challenges.append(re.search(r'^(.*)/' ,line).group(1))
    challenges = Counter(challenges)
    users = Counter(users)
    high_user = users.most_common(1)[0][0]
    high_challenge = challenges.most_common(1)[0]
    return Stats(user=high_user, challenge=high_challenge)
