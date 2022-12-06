import os, time, random

def roll(sides):
  roll = random.randint(1,sides)
  return roll

def health():
  health_val = (((roll(6)*roll(12))/2)+10)
  return health_val

def strength():
  strength_val = ((roll(6)*roll(12))/2+12)
  return strength_val

agility_val = ((roll(8)*roll(10))/2+12)
intelligence_val = ((roll(12)*roll(6))/2+12)
charisma_val = ((roll(10)*roll(8))/2+12)

# Define a dictionary of epic quotes
epic_quotes = {
  "Human": [
    "I am the flame that will never be extinguished!",
    "I will not be broken by the hardships of this world!",
    "I will rise above adversity and conquer all!",
    "I am the future, and the future is bright!"
  ],
  "Elf": [
    "My magic is unmatched by any mortal!",
    "I am the guardian of the forest, and I will not be swayed!",
    "My arrows will find their mark, and my enemies will fall!",
    "I am the embodiment of grace and power!"
  ],
  "Wizard": [
    "My knowledge of the arcane arts is unrivaled!",
    "I am the master of the elements, and they bend to my will!",
    "My spells will shatter the earth and bring forth destruction!",
    "I am the bringer of light, and the keeper of the dark!"
  ],
  "Orc": [
    "I am the terror of the battlefield, and my enemies will tremble before me!",
    "My axe will split the earth and crush my foes!",
    "I will not be stopped, and I will not be defeated!",
    "I am the embodiment of strength and ferocity!"
  ]
}

while True:
  os.system("clear")
  print("Character Builder\n")
  time.sleep(2)
  name = str(input("Name Your Legend: \n"))
  type = str(input("Character Type (Human, Elf, Wizard, Orc): \n"))
  while type not in ['Human', 'Elf', 'Wizard', 'Orc']:
    type = str(input("Invalid character type. Please choose from (Human, Elf, Wizard, Orc): \n"))
  
  print("Your Character is: ",name)
  print("Your character ",name,"belongs to class ",type)  
  print(name,"health is: ",health())
  print(name,"strength is: ",strength())
  print(name,"agility is: ",agility_val)
  print(name,"intelligence is: ",intelligence_val)
  print(name,"charisma is: ",charisma_val)
  epic_quote = random.choice(epic_quotes[type])
  print(name,"'s epic quote is: ",epic_quote)
  ques= str(input("\nWanna build a new character? "))
  if ques =="yes" or ques=="Yes":
    continue
  else:
    exit()
  

