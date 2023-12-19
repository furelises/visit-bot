character_description = {
    "name": "Harry James Potter",
    "age": 11,
    "description": "He lives in the 4 Privet Drive, Little Whinging.He doesn`t know he is a wizard "
                   "and wants to go to the primary school(because his cousin bullies him."
}

contacts = {
    "email": "if you know Harry Potter`s email please call me :)",
    "ministry_of_magic": "62442"
}
project = {"project": "https://github.com/furelises/visit-bot.git"}
photo = 'images.jpg'


def contacts_to_str() -> str:
    a = 'Menu\n'
    for i in contacts:
        b = f'{i} : {contacts[i]}\n'
        a = a + b
    return a


def character_description_str() -> str:
    a = 'Menu\n'
    for i in character_description:
        b = f'{i} : {character_description[i]}\n'
        a = a + b
    return a


def project_to_str() -> str:
    a = 'Menu\n'
    for i in project:
        b = f'{i} : {project[i]}\n'
        a = a + b
    return a


def get_photo():
    a = open(photo, 'rb')
    return a
