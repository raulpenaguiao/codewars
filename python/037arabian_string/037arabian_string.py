
import re

def camelize(str_):
    str = str_[:]
    return  "".join([k.capitalize() for k in re.split(r" |,|:|-|_|'|=|>|<|/|!|\?|;|\.", str)])
