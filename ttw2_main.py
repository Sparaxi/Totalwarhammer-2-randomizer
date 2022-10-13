# here it imports modules and all necessary data for the function Lords to work.
import random

from ttw2_main_DB import (

#races
High_elves, Dark_elves, Vampire_count, Lizardmen,
Skaven, Tomb_kings, Vampire_coast, The_empire,
Dwarfs,Greenskins,Chaos,Woodelves,Bretonia,Norsca, Race,
#lords
HighElf_lord, Vampire_lord, DarkElf_lord, Lizard_lord,
Skaven_Lord, TombKing_lord, VampireLord_Coast, Empire_Lord,
Dwarf_lord, Greenskin_lord, Chaos_lord, Woodelf_Lord, Bretonia_lord,
Norsca_lord
)

# this function controls the randomizer, it gathers all information from database.py and randomizes it here for the final result.
def Lords(Race):
    random.choice(Race)
    Race = random.choice(Race)
    #main code this is what makes everything work.
    if Race == High_elves:
        print("High elf lord:", random.choice(HighElf_lord))
    elif Race == Vampire_count:
        print("Vampire Lord:", random.choice(Vampire_lord))
    elif Race == Dark_elves:
        print("Dark elf lord:", random.choice(DarkElf_lord))
    elif Race == Skaven:
        print("Skaven lord:", random.choice(Skaven_Lord))
    elif Race == Tomb_kings:
        print("Tomb king lord:", random.choice(TombKing_lord))
    elif Race == Lizardmen:
        print("Lizard lord:", random.choice(Lizard_lord))
    elif Race == Vampire_coast:
        print("Vampire coast lord:", random.choice(VampireLord_Coast))
    elif Race == The_empire:
        print("Empire lord:", random.choice(Empire_Lord))
    elif Race == Dwarfs:
        print("Dwarf lord:", random.choice(Dwarf_lord))
    elif Race == Greenskins:
        print("Greenskin lord:", random.choice(Greenskin_lord))
    elif Race == Chaos:
        print("Chaos lord:", random.choice(Chaos_lord))
    elif Race == Woodelves:
        print("Woodelf lord:", random.choice(Woodelf_Lord))
    elif Race == Bretonia:
        print("Bretonia lord:", random.choice(Bretonia_lord))
    elif Race == Norsca:
        print("Norsca Lord:", random.choice(Norsca_lord))

    else: random.choice(Race)

#here it prints out the final result for i in range() is how many results there have to be printed.
x=int(input('how many times do you want to roll the dice?:')) #
for i in range (0,x):
    Lords(Race)

print("Press any key to exit")
if input() == exit():
    print("Goodbye")
