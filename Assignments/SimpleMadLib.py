'''
long long ago in the lands of {place1} ther lived a {being = adjective1 + creature1}.
this {being} dispised {noun1}, for {noun1} liked to {adverb1} {verb1} with its {noun2}.
the {noun2} was {being}'s most {adjective2} thing in its collection.
without {noun2} {being} would get more {adjective3} that {adjective1}.
when that happens {place1} will merge with {place2} and become the most {adjective4} {propper_noun} of them all.
{verb ending with ing} the {noun3} once and for all."
'''

#introduction
print("hello, welcome to my mad lib\nfor it you will need:\n2 places\n4 adjectives\n1 creature\n3 nouns\n1 propper noun\n1 adverb\n1 verb\n1 verb ending in ing\n\nwords")

#places
place1 = input("place 1:")
place2 = input("place 2:")

#the being (adjective+creature)
adjective1 = input("adjective 1:")
being = adjective1+" "+input("creature:")

#other adjectives
adjective2 = input("adjective 2:")
adjective3 = input("adjective 3:")
adjective4 = input("adjective 4:")

#nouns
noun1 = input("noun 1:")
noun2 = input("noun 2:")
noun3 = input("noun 3:")
propper_noun = input("propper noun:")

#verbs
verb = input("verb:")
verbing = input("verb that ends with ing:")

#adverb
adverb = input("adverb:")

#finished madlib
print(f"long long ago in the lands of {place1} there lived a {being}.\nthis {being} despised {noun1} for {noun1} liked {adverb} {verb} with its {noun2}.\nthe {noun2} was {being}'s most {adjective2} thing in its collection.\nwithout {noun2} {being} would get more {adjective3} that {adjective1}.\nwhen that happens {place1} will merge with {place2} and become the most {adjective4} {propper_noun} of them all\n{verbing} the {noun3} once and for all.")