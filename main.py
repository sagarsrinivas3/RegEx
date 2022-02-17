filenames = ['nov-12', 'november-11', 'oct-18', 'Nov-22']


import re

# List of Meta Characters
# .        Matches any single character
# \        Escapes one of the meta characters to treat it as a regular character
# [...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
# +        Matches the preeceding element one or more times
# ?        Matches the preeceding element zero or one time
# *        Matches the preeceding element zero or more times
# {m,n}    Matches the preeceding element at least m and not more than n times
# ^        Matches the beginning of a line or string
# $        Matches the end of a line or string
# [^...]   Matches a single character or a range that is not contained within the brackets
# ?:...|..."Or" operator
# ()       Matches an optional expression



# extract all email ids
Sentence = "Hi!! There, I'm abcd and email id is abcd@gmail.com and alternate emailid is xyz.12@examle.com"
pattern = re.compile("[^ ]+@[^ ]+\.[A-Za-z]+")
matches = pattern.findall(Sentence)
print(matches)


# extract urls ending with .com
urlsList = ['http://google.com', 'https://bnmit.org', 'http://yahoo.com', 'https://mymail.in', 'http://www.redit.com']

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
string_url = "\n".join(urlsList)
print(string_url)
match = pattern.findall(string_url)
print(match)


# extract ip with 3 digit start with 12
ip = ["141.122.124.321","145,145.134.1", "553.954.129.771"]
ip_string = "\n".join(ip)
print(ip_string)

pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}.[0-9]{3}")
match = pattern.findall(ip_string)
print(match)


#Write a regular expression that returns all the list items that contain the word Delhi.
data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com", 
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar delhi 3456 ants"
]

pattern = re.compile("Delhi", re.IGNORECASE)
outList = []
for sen in data:
  if pattern.findall(sen):
    outList.append(sen)
print(outList)