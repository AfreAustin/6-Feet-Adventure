# 6 Feet Adventure by AfreAustin and JoSky21
# Created for Hacklarious 09-10/5/2020
# Adventure Game set during the pandemic

from tkinter     import *
from collections import OrderedDict
import os
import sys
import random

def main():
    root = Tk()
    root.geometry("800x600")
    
    app = Window(root)
    app.configure(bg = '#898282')

    root.mainloop()

# GUI
class Window(Frame):

    # main window / master widget
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        self.shoplist = {'Bread': 2, 
                          'Fruit Bag': 1, 
                          'Can': 6, 
                          'Lbs Meat': 8, 
                          'Water': 1, 
                          'Toilet Paper Rolls': 8, 
                          'Clean': 2, 
                          'Paper Towel Rolls': 2, 
                          'Medicines': 3, 
                          'Games': 2} 
        self.cart  = []
        self.funds = 100.00
        self.area  = ""
        self.infct = 0
        self.event = ""
        self.ori_time = 480
        self.timer = 0
        
        self.pack()
        self.init_window()
        self.init_labels()
        self.init_events(self.shoplist,
                         self.cart,
                         self.funds,
                         self.area, 
                         self.infct,
                         self.event,
                         self.ori_time,
                         self.timer)

    # window frame
    def init_window(self):

        self.master.title("6 Feet Adventure")
        self.pack(fill = BOTH, expand = 1)

       # Menu Bar
        dropdown = Menu(self.master)
        self.master.config(menu = dropdown)

       # File Menu
        file = Menu(dropdown)
        file.add_command(label   = "Exit",
                         command = self.master.destroy)
        dropdown.add_cascade(label = 'File', menu = file)

    # window labels
    def init_labels(self):
        
        # Title
        title = Label(self, bg = '#beb5b5',
                      text = "6 Feet Adventure",
                      relief = GROOVE)
        title.config( font = ('CopperplateGothicLight', '25', 'bold') )
        title.place(relx = 0.30, rely = 0.01)

        # Exit Button
        exitButton = Button(self, bg = '#f44040', fg = 'black',
                            text = " EXIT ", 
                            command = self.master.destroy )
        exitButton.place(relx = 0.81, rely = 0.015)
        
        # Credits
        credits = Label(self, bg = '#898282',
                        text = ("_" * 153) + 
                                "\n created by AfreAustin and JoSky21")
        credits.place(relx = 0.015, rely = 0.90)
        
    # game
    def init_events(self, shoplist, cart, funds, area, 
                    infct, event, ori_time, timer):

        # inventory window
        list = ""
        for i in shoplist:
            list += "\n " + str(shoplist[i]) + " " + i
        
        InventL = Label(self, bg = 'yellow',
                        text = " Shopping List \n\n" + list,
                        height = 15, width = 30, relief = RAISED )
        InventL.place(relx = 0.70, rely = 0.10)

    #-------------------------------------------------------------------#    

        # events window
        events = Label(self, bg = "white",
                       text = " You are in the main hub" +
                              "\n 1: Corner Store" +
                              "\n 2: Gas Station"  +
                              "\n 3: Drug Store"   +
                              "\n 4: Supermarket",
                       height = 7, width = 27, relief = RIDGE)
        events.config(font = ("Times", 25))
        events.place(relx = 0.05, rely = 0.10)  

    #-------------------------------------------------------------------# 

        # current time
        def displayTime(ori_time, timer):
            time_dis = ori_time + timer              # minutes
            hours    = time_dis // 60
            minutes  = time_dis % 60
            ori_time = time_dis
            return ori_time

        # advances time
        def incrementTimer(timer):
            timer += 10
            return timer

        # checks infection
        def infection(ori_time, infct):
            
            # determines if infected
            if  (infct <= 5):
                infection = random.randint(0, 15)
            elif(infct <= 9  and infct > 5):
                infection = random.randint(0, 8)
            elif(infct <= 13 and infct > 9):
                infection = random.randint(0, 5)
            else:
                infection = random.randint(0, 3)

            # determines game state
            if(infection == 0):
                state = "You are infected"
            else:
                state = "You are still healthy"
            return state

        # Stats Window
        time   = displayTime(ori_time, timer)
        health = infection(ori_time, infct)
        
        statsL = Label(self, bg = '#3f423f', fg = '#06f706',
                       text = "Time: "                   + str(time)  +
                              "\n Monies: "              + str(funds) + "\n" +
                              "\n People Around: "       + str(infct)  + "\n" +
                              "\n Health: "              + health,
                       height = 8, width = 30, 
                       relief = SUNKEN, justify = CENTER)
        statsL.place(relx = 0.70, rely = 0.60)

    #-------------------------------------------------------------------#    
        entryL= Label(self, bg = 'white',
                      text = "Enter Choice Number:    ",
                      relief = RAISED, justify = CENTER)
        entryL.config(font = ("Times",25))
        entryL.place(relx = 0.055, rely = 0.60)

        entry = Entry(self, font = ("Times", 26),
                      width = 9, 
                      relief = SUNKEN, justify = CENTER)
        entry.place(relx = 0.45, rely = 0.60)
        
        s = entry.get()
        print(s)

    #-------------------------------------------------------------------# 

        #def mainHub():
         #   while(True):
          #      choice = 0
                
           #     try:
            #        choice = int(input("Choose where do you wish to go: "))
        
             #   except:
              #      print("A")

        # Ending Conditions
        if(ori_time >= 1200):
                print("The time is up" + 
                      "\n Your game is over." +
                      "\n Congratulations on surviving this long.")
                sys.exit()
        if(health == "You are infected"):
            event = health
        if(funds <= 0):
            print("You have no money. You poor soul.")
            sys.exit()

main()