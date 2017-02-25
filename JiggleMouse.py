#Python Script to Jiggle Mouse Every 10 Minutes
#Keeps Computer From Going To Sleep
#Currently No Windows Support, Only Linux
#Original Code To Move Mouse From Here: http://danielbaggio.blogspot.com/2009/03/python-mouse-move-in-5-lines-of-code.html

#Import Libraries
import time
from Xlib import X, display

#Makes The Mouse Move After Ten Minutes
def Main():
    #Print Starting Message
    print("Starting JiggleMouse")
    print("Ctrl + C to exit")

    #Moves The Mouse
    try:
        while True:
            d = display.Display()
            s = d.screen()
            root = s.root
            root.warp_pointer(300,300)
            d.sync()

            root.warp_pointer(301,301)
            d.sync()

            time.sleep(600) #Sleeps for 10 Minutes(600 seconds)

    #Gets Rid of Error Screen When Exiting
    except KeyboardInterrupt:
        print("\nGoodbye :)")

#Call Main
Main()
