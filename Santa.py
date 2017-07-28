def introduction():
  print " "
  print "Santa's Sibling"
  print "by Robyn and DeeAnne"
  print " "
  print "You were just a baby when you were dropped off at the orphonage."
  print "You don't even how get there, but you need to get out right now."
  waiter()
  print "blah, blah, blah"
  return

def waiter():
  raw_input("Press Enter to continue")
  print " "
  return

def game():
  orphanage = raw_input("Do you leave the orphanage (y/n)?")
  if orphanage == "n" or orphanage == "N":
    print "Bye you spineless coward!  There is nothing else for you to accomplish!"
  else:
    print "Be careful not to caught. Good luck"
    game2()
  return

def game2():
  print "You go out into the world and quickly reallize it isn't much better."
  print "you can only get food by pan handling and stealing which are not your"
  print "favorite activities"
  waiter()
  print "An old lady appears and asks the following question:"
  print "Do you know who your brother is?"
  print "You think what??? What is this lady talking about?"
  print "As far as you know you don't have a brother."
  waiter()
  print "The old lady turns and walks away."
  print "You yell wait. You tell her that she doesn't know what she is talking about!"
  print "She turns and says that his name is St. Nick, aka Santa Claus!"
  print "You look down, and when you look up, she is gone."
  waiter()
  print "The more you process the information, the more angry you get."
  print "After the beatings from the nuns, at the orphanage you struggled for every little thing."
  print "It seems if you want to live the good life, you have to give gifts to"
  print "little boys and girls.  I need to to kill this Santa Claus person!  You begin your journey!"
  waiter()
  print "Now the big decision, should I use a (g)un or a (k)nife: "
  killer = raw_input("Choose g or k:")
  if killer == "g" or killer == "G":
    print "Get them quick and from a distance!"
  else:
    print "You want to feel the life drain out of their body!"
  waiter()
  yourMind = raw_input("Should you (A)bandon your path or (F)ind Santa Claus")
  if yourMind == "a" or yourMind == "A":
    print "You go back to your sorry, miserable existance you call a life"
  else:
    print "You are sick!"
    game3()
  return

def game3():
  waiter()
  print "You wonder through the city and find a teenage.  He looks haggart and hungry."
  print "Now you have a big decision:"
  feedKid = raw_input("Should I (f)eed him or (i)gnore him? (f/i)")
  if feedKid == "i" or feedKid =="I":
    print "You just don't have the resources to spare."
    oldLady()
  else:
    print "Hey kid, come with me. I'll get you a bite to eat. I know "
    print "the perfect place to dine and dash"
  waiter()
  print "The kid asks to join you."
  print "Is this a good idea? I mean afterall, how do you explain to someone:"
  print "You want to kill Santa!"
  join = raw_input("Do you let him (j)oin your, or (n)ot?")
  if join == "n" or join == "N":
    print "Sorry kid, I do not have room for you!"
    oldLady()
  else:
    print "Sure kid, let us go further"
    print "Now get this straight, I am going to kill Santa Claus."
    print "If you can take it, fine, if not, I am going to kill you as well"
    print "I have one more decision for you to make:  Do you want to "
  transport = raw_input("be a (p)ickpocket to get your fare, or hop on (t)rain and be a hobo: (p/t)")
  if transport == "t" or transport == "T":
    print "So you want to ride the rails"
    oldLady()
  else:
    print "Well we have some traing to do to make you a great pickpocket."
  return

def oldLady():
  print "The game will continue from here"
  print "end here"
  
  return
  

# Santa's Sibling
# by Robyn and DeeAnne
# Interactive fiction
# Plot Rebirth
# Character is the person who makes the decisions
#
print "Hello World"
print "What is your name:"
name = raw_input()
# Ask what gender they are
print "What is your gender (F/M):"
gender = raw_input()
if gender == "m" or gender == "M" or gender == "Male":
  # Assume the person is male
  gender = "m"
  print "You are so handsome!"
else:
  # Assume the person is female
  gender = "f"
  print "You are so pretty!"
# Ask user if they live in the city or country
print "Do you live in (C)ity or (R)ural, enter the first letter?"
WhereLive = raw_input()
if WhereLive == "C" or WhereLive == 'c':
  # Live in the city
  WhereLive = "c"
  print "Ok, you live in the city."
else:
  # Live in the country
  WhereLive = "r"
  print "Ok, you live on the farm."
  
# call the introduction
introduction()
# run the game
game()

