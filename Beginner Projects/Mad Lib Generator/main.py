import time

# Starting
print("Welcome to the Mad Libs App!")
print("Choose from the below two stories you wish to make:")
print("1. The Best Day Ever.")
print("2. At the Arcade.")
story_choose = int(input("Please choose a story (1 or 2): "))

# Creating functions for each story choice
def story_1(emo, color, weather, cloth, adj, footwear, verb, vehicle, city, direction, adj2, noun, food, restaurant, temp, verb2, animal, furniture, adj3):
    print("Your Story:")
    print(f"One day I woke up feeling {emo}, and I knew it was going to be a special day. The sky was {color}", end=' ')
    print(f"and the weather was {weather}, so I hopped out of bed, put on my {cloth} and my {adj} {footwear},", end=' ')
    print(f"and I was ready to {verb}. Outside, I caught the first {vehicle}, which took me straight to {city}.", end=' ')
    print(f"I went {direction} until I came to a store selling {adj2} {noun}, where I bought the perfect {noun}!", end=' ')
    print(f"Next, I treated myself to a {food} snack at a {restaurant} restaurant. It was very {temp}, but it was still", end=' ')
    print(f"good enough to {verb2}. Finally, I went back home. I fed my {animal}, then sat down on the {furniture},", end=' ')
    print(f"and thought, 'What is a/an {adj3} day!'")
    print("Story Template Credits: https://bit.ly/33s9puR")

def story_2(noun, noun2, verb, noun3, verb2, noun4, noun5, noun6):
    print("Your Story:")
    print(f"When I go to the arcade with my {noun} there are lots of games to play. I spend lots of time there", end=' ')
    print(f"with my friends. In the game X-Men you can be different {noun2} The point of the game is to {verb}", end=' ')
    print(f"every robot. You also need to save people. Then you can go to the next level.", end=' ' + "\n")
    print(f"In the game Star Wars you are Luke Skywalker and you try to destroy every {noun3}", end=' ')
    print(f"In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are", end=' ')
    print(f"{verb2} against." + "\n" + "There are a whole lot of other cool games.", end=' ')
    print(f"When you play some games you win {noun4} for certain scores. Once you're done you can cash in your tickets to get a big", end='')
    print(f"{noun5}. You can save your {noun6} for another time. When I went to this arcade I didn't believe how much fun it would be.", end=' ')
    print(f"So far I have had a lot of fun every time I've been to this great arcade!")
    print("Story Template Credits: https://bit.ly/3GEOx1K")

if story_choose == 1:
    print("You chose the Best Day Ever story.")
    print("Please enter the following words:")
    emo = input("Emotion: ")
    color = input("Color: ")
    weather = input("Weather: ")
    cloth = input("Clothing: ")
    adj = input("Adjective: ")
    footwear = input("Footwear: ")
    verb = input("Verb: ")
    vehicle = input("Vehicle: ")
    city = input("City: ")
    direction = input("Direction: ")
    adj2 = input("Adjective for an object to buy: ")
    noun = input("An object: ")
    food = input("Food: ")
    restaurant = input("Restaurant Type: ")
    temp = input("Weather: ")
    verb2 = input("Verb: ")
    animal = input("Pet: ")
    furniture = input("Furniture to sit: ")
    adj3 = input("Adjective: ")

    print("\n")
    story_1(emo, color, weather, cloth, adj, footwear, verb, vehicle, city, direction, adj2, noun, food, restaurant, temp, verb2, animal, furniture, adj3)

elif story_choose == 2:
    print("You chose the At the Arcade story.")
    print("Please enter the following words:")
    noun = input("Plural Noun: ")
    noun2 = input("Plural Noun: ")
    verb = input("Verb: ")
    noun3 = input("Noun: ")
    verb2 = input("Verb ending with -ing: ")
    noun4 = input("Plural Noun: ")
    noun5 = input("Noun: ")
    noun6 = input("Plural Noun: ")

    print("\n")
    story_2(noun, noun2, verb, noun3, verb2, noun4, noun5, noun6)
else:
    print("Invalid input. Please try again.")

print("\n")
print("\n")
close = input("Write close to exit: ") # Closing the program
if close == "close":
    print("Thank you for using the Mad Libs App!")
    time.sleep(5)
    exit()
else:
    exit()
