import os
import re
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding
def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    pattern = r"(?:<category>)([a-zA-Z0-9]+)(?:</category>)"
    check = re.compile(pattern)
    tags = check.findall(content)
    count = Counter(tags)
    return count.most_common(n)
