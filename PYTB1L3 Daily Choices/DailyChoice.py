print('Het wordt ochtond. En je alarm gaat af. SNOOZE of OPSTAAN')

choice = input()
if choice == "SNOOZE":
    print ("Je slaapt door.")

elif choice == "OPSTAAN":
    print("Je staat en bent fris")

else:
    print(choice , "Is geen goede keuzen")

print("Zodra je op bent heb je 2 keuzens. ETEN of NIET ETEN")

choice2 = input()

if choice2 == "ETEN":
    print("Je maakt een broodje en eet het")

elif choice2 == "NIET ETEN":
    print("Je eet niks. Je hebt toch nog niet zo veel honger")

else:
    print(choice2 , "Wasn't a right choice")

print('Je gaat naar school. Kies je de FIETS of de BUS')

choice3 = input()
if choice3 == "FIETS":
   print('Je gaat fietsen. Je komt buitenadem op school')

elif choice3 == "BUS":
   print('Je neemt de bus. Je komt net optijd op school')

else: 
   print(choice3 , "Wasn't a right choice")

print("Je hebt pauze. Ga je eten van THUIS eten of van de KANTINE")

choice4 = input()
if choice4 == "THUIS":
   print('Je eet je broodjes van thuis')

elif choice4 == "KANTINE":
   print('Je eet een broodje uit de kantine')

else:
   print(choice4 , "Wasn't the right choice")

print("Je komt thuis na school. Ga je GAMEN of HUISWERK")

choice5 = input()

if choice5 == "GAMEN":
   print('Je gaat gamen tot je gaat slapen')

elif choice5 == "HUISWERK":
   print('Je gaat huiswerk maken tot je gaat slapen')

else:
   print(choice5 , "Wasn't a good choice")

print('Toen viel je in slaap')