import pyjokes
import pyttsx3

joke =pyjokes.get_joke()

engine=pyttsx3.init()
engine.say("welcome joke for customer")
engine.runAndWait()
print(joke,'\n\n')
engine.say(joke )
engine.runAndWait()
print ("Welcome to My Grocery store Sir.......!")
engine.say("Welcome to My Grocery store Sir")
engine.runAndWait()
print ("We have Jam,Bread and Eggs...")
engine.say("We have Jam,Bread and Eggs")
engine.runAndWait()
print ("Select items you want to buy ......")
engine.say("Select items you want to buy ")
engine.runAndWait()
print ("""
    ______________________________________________________________________________________
   |                              |                           |                           |             
   |    1) Mitchell's Fruit jam   |     2) Fruit  Bread       |        3)    Eggs         |
   |         ( 500_gram )         |        ( 800_gram )       |           ( 12/pis )      |
   |         Rs: 800 only         |        Rs: 200 only       |          Rs: 400 only     |
   |                              |                           |                           |
   |          ADD To Cart         |        ADD To Cart        |          ADD To Cart      |
   |                              |                           |                           | 
   |______________________________|___________________________|___________________________|
""")


print ("(....Enter only Number please....)")
engine.say("Enter only Number please")
engine.runAndWait()

scan = 'y'
total=0
while scan=='y'or scan=='Y' :
   num99=int (input("-->"))
   if num99==1:
       total+=800
   elif num99==2:
       total+=200
   elif num99==3:
       total+=400
   print ("Anything else Sir? If not, press key (N); otherwise, press key (Y), please....")
   engine.say("Anything else Sir? If not, press key N; otherwise, press key Y, please.")
   engine.runAndWait()
   scan= input("-->")



print ("Your Total Purchase Amount is :",total,"Rs...only")
bb=str(total)

engine.say(f"Your Total Purchase Amount is {total}")
engine.runAndWait()



