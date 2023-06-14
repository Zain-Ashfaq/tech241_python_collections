
my_hero_story = {
    "start": "Once upon a time there lived a man named Peter.",
    "middle": "After drinking radioactive water, Peter became Water Man who has water-manipulating powers.",
    "end": "Using his newfound abilities, Water Man protected the town and became a symbol of hope."
}


print(my_hero_story)

print(type(my_hero_story))

print(my_hero_story.keys())

print(my_hero_story.values())

print(my_hero_story["start"])
print(my_hero_story["middle"])
print(my_hero_story["end"])


my_hero_story["hero"] = "Water Man"


print(my_hero_story)


for key, value in my_hero_story.items():

    print(f"{key} : {value}")
