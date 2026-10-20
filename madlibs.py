import time

print("Enter the fallowing:\n")
spe=input("Species: ")
nam=input("\nName: ")
ver=input("\nVerb-Past Tense: ")
big=input("\nBig object: ")
obj=input("\nNot as big object: ")
pla=input("\nPlace: ")
val=input("\nObject of value: ")
str=input("\nStorage object: ")
too=input("\nTool: ")
tof=input("\nTrue or false: ")
spe=spe.lower()
nam=nam.title()
ver=ver.lower()
big=big.lower()
obj=obj.lower()
pla=pla.title()
val=val.lower()
str=str.lower()
too=too.lower()
tof=tof.lower()

if tof == "true":
    tofequal = "successful"
else:
    tofequal = "not successful"

print("\nHere is your Story")
time.sleep(0.5)
print(f"There once was a {spe} named {nam} who sailed a ship and {ver} under a {big} on the lower deck each night. The {big} was so big that even a {obj} could fit underneath it. Today was no ordinary day, however, since today he was arriving at his favorite place: {pla}. He gifted {pla} the giant {big} and in return, they gave him a {val}. {nam} was unsatified with this gift however, and decided to toss it into a {str}, and never looked back. Until, of course, 11 years later, when they realised how much they really missed the {val}. So, {nam} decided to use a {too} to get it back themselves. {nam} snuck into the headquaters of {pla}, and was {tofequal} in their attempts to aquire a replica of the gift. THE END!")
