# Code Challenge - Strings and Lists
#
# Python file name: fileiochallenge.py
#
# Date: 09-27-230
#
# Programmer's name: Matthew Gutierrez

try:
    with open("animalNames.txt", "r") as animal_names_file:
        names = animal_names_file.read()
        names = names.replace("Names:\n", "Habitat: ").replace("Ryker\n", "Ryker")
        print(names + "\n")

    with open("arrivingAnimals.txt", "r") as arriving_animals_file:
        animals = arriving_animals_file.readlines()
        print("New Animals to the Following Habitats.\n")
        for animal in animals[:16]:
            print(animal.strip())
        print("\nLet's begin!\n")
        print("\n\n Creating Habitats... \n\n")

    with open("fileiochallenge.txt", "w") as output_file:
        output_file.write("Created Habitat Enclosures\n")
        output_file.write("New Animals to the Following Habitats.\n")
        data = names.replace(": \n", ", ").replace("\n\n", ", ").split(",", 52)
        print(data)
        print("\n")
        def out_put_by_hab():
            output_file.write("\n")
            output_file.write(data[0] + "\n")
            for animal in animals[:4]:
                output_file.write(animal.strip() + "\n\n")
            output_file.write(data[12].replace(" L", "L") + "\n")
            for animal in animals[4:8]:
                output_file.write(animal.strip() + "\n\n")
            output_file.write(data[25].replace(" B", "B") + "\n")
            for animal in animals[8:12]:
                output_file.write(animal.strip() + "\n\n")
            output_file.write(data[36].replace(" T", "T") + "\n")
            for animal in animals[12:16]:
                output_file.write(animal.strip() + "\n\n")
        out_put_by_hab()
            
except FileNotFoundError as e:
    print("A file error occurred...")
    print(e)