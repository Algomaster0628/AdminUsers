#making a empty dictionary
Storeddata = {}
#setting a flag to indicate polling is active 
polling_active = True
#letting the user input data 
while polling_active == True:
   name = input('Enter Your Name:')
   dream = input('Enter Your dream:')
   
  #storing data in dictionary
   Storeddata[name] = dream
  #finding out if anyone els want to takr the poll or not
   repeat = input("would you like another person to respond? (yes/no)")
   if repeat == "no":
     polling_active = False
   else:
     continue
#polling is complete.show results
print('---Poll Results---')
for name,dream in Storeddata.items():
  print(name.title() + ":" + dream)