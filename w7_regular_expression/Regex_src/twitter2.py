import re

url = input("URL: ").strip()

"""
re.sub(pattern, repl, string, count=0, flags=0)
to substitute a pattern with sth else
pattern = RegEx, 
repl = str that we can replace the pattern with 
string = str taht we want to do the sub on.
"""

username = re.sub(r"(https?://)?(www.)?twitter\.com/", "", url)
print(f"Username: {username}")