PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names_of_invitees = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
for name in names_of_invitees:
    name = name.strip()
    personalized_content = content.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w") as file:
        file.write(personalized_content)