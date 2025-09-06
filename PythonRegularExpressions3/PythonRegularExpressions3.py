import sys
import re

def endBMatch(txt):
    patterns = 'a.*?b$'
    if(re.search(patterns,txt)):
        return True
    else:
        return False

print(endBMatch("appleb"))
print(endBMatch("appleBaby"))
print(endBMatch("abcbdedfeb"))

def upperLowerMatch(txt):
    patterns = '^[A-Z]+[a-z]+$'
    if(re.search(patterns,txt)):
        return True
    else:
        return False

print(upperLowerMatch("aB"))
print(upperLowerMatch("Ba"))

def textMatch(txt):
    patterns = '^[a-z]+_[a-z]+$'
    if(re.search(patterns,txt)):
        return True
    else:
        return False

print(textMatch("aaa_bbb"))
print(textMatch("aaa_Bbb"))










