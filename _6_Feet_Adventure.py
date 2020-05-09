# 6 Feet Adventure by AfreAustin and JoSky21
# Created for Hacklarious 09-10/5/2020
# Adventure Game set during the pandemic

from tkinter import *
import os
from sys import exit

def main():
    root = Tk()
    root.geometry("800x600")
    
    app = Window(root)
    app.configure(bg = '#beb5b5')
    
    root.mainloop()

# GUI
class Window(Frame):

    # main window / master widget
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        
        self.pack()
        self.init_window()
        self.init_labels()
        self.init_events()
        self.init_invent()
        self.init_Cstats()
        
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
        title = Label(self, bg = 'white',
                      text = "6 Feet Adventure",
                      relief = RAISED)
        title.config( font = ('CopperplateGothicLight', '25', 'bold') )
        title.place(relx = 0.30, rely = 0.01)

        # Exit Button
        exitButton = Button(self, bg = '#f44040', fg = 'black',
                            text = " EXIT ", 
                            command = self.master.destroy )
        exitButton.place(relx = 0.90, rely = 0.015)
        
        # Credits
        credits = Label(self, bg = '#beb5b5',
                        text = ("_" * 153) + 
                                "\n created by AfreAustin and JoSky21")
        credits.place(relx = 0.015, rely = 0.90)

    # events window
    def init_events(self):

        events = Label(self, bg = 'white',
                       text = "EVENTS",
                       height = 30, width = 70)
        events.place(relx = 0.05, rely = 0.10)
    
    # inventory window
    def init_invent(self):

        item0, item1, item2, item3, item4 = 2, 1, 6, 1, 8
        item5, item6, item7, item8, item9 = 8, 2, 4, 3, 2

        InventL = Label(self, bg = 'yellow',
                        text = " Shopping List " + "\n\n" +
                               "\n" + str(item0) + " Bread " +  
                               "\n" + str(item1) + " Fruit Bag " + 
                               "\n" + str(item2) + " Canned Food " + 
                               "\n" + str(item3) + " Water Pack "
                               "\n" + str(item4) + " Lbs Meat "
                               "\n" + str(item5) + " Toilet Paper Rolls "
                               "\n" + str(item6) + " Cleaning Solutions "
                               "\n" + str(item7) + " Paper Towel Rolls "
                               "\n" + str(item8) + " Medicine "
                               "\n" + str(item9) + " Games ",
                        height = 15, width = 30)
        InventL.place(relx = 0.70, rely = 0.10)

    # stats window
    def init_Cstats(self):

        monies = 100;

        statsL = Label(self, bg = '#3f423f', fg = '#06f706',
                       text = "Monies: +" + str(monies) + "\n"+
                              "\n Current People: A Shit Ton" +
                              "\n Chance of Infection: Fucked ", 
                       height = 8, width = 30)
        statsL.place(relx = 0.70, rely = 0.60)

main()