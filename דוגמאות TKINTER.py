#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# איך לדעת מהו הפונט וגודל הפונט המשמשים ברירת מחדל בטקינטר
from tkinter import *
from tkinter import font
root=Tk()
print(font.nametofont('TkTextFont').actual())
root.mainloop()


# In[ ]:


# פתיחת קבצים

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()


# In[ ]:


#Change the default Font that will affect in all the widgets
win.option_add( "*font", "lucida 20 bold italic" )
win.resizable(False, False)


# In[ ]:


# אם מוסיפים כוכבית לפני משתנה בתוך רשימת ערכים זה מציג בנפרד כל ערך של המשתנה


# In[ ]:


# https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter

# מסך מלא כולל השמטת שורה עליונה
#ws.attributes('-fullscreen', True)

ws.bind("<F11>", lambda event: ws.attributes("-fullscreen",not ws.attributes("-fullscreen")))
ws.bind("<Escape>", lambda event: ws.attributes("-fullscreen", False))
    
# מסך מלא בלי השמטת שורה עליונה
#ws.state('zoomed')


# In[1]:


# לחצן
# הווידג'ט Button משמש להצגת לחצנים באפליקציה שלך.

import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()


# In[4]:


# הגדרת ווידג'טים עם רקע שקוף

#Import the required libraries
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("700x350")

#Adding transparent background property
win.wm_attributes('-transparentcolor', '#ab23ff')

#Create a Label
Label(win, text= "Hello World!", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 50, ipady=50, padx= 20)

win.mainloop()


# In[5]:





# In[6]:





# In[ ]:


# כל הצבעים שזמינים בטקינטר

import tkinter as tk

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


class ColorChart(tk.Frame):

    MAX_ROWS = 36
    FONT_SIZE = 10

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        r = 0
        c = 0

        for color in COLORS:
            label = tk.Label(self, text=color, bg=color,
                             font=("Times", self.FONT_SIZE, "bold"))
            label.grid(row=r, column=c, sticky="ew")
            r += 1

            if r > self.MAX_ROWS:
                r = 0
                c += 1

        self.pack(expand=1, fill="both")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Named Color Chart")
    app = ColorChart(root)
    root.mainloop()


# In[ ]:





# In[3]:


# סטייל של דברים בעיקר על קומבובוקס

import tkinter as tk
from tkinter import ttk

# variables created for colors
ebg = '#404040'
fg = '#FFFFFF'

root = tk.Tk()

style = ttk.Style()

# Note the code line below.
# Be sure to include this or style.map() won't function as expected.
style.theme_use('alt')

# the following alters the Listbox
root.option_add('*TCombobox*Listbox*Background', ebg)
root.option_add('*TCombobox*Listbox*Foreground', fg)
root.option_add('*TCombobox*Listbox*selectBackground', fg)
root.option_add('*TCombobox*Listbox*selectForeground', ebg)

# the following alters the Combobox entry field
style.map('TCombobox', fieldbackground=[('readonly', ebg)])
style.map('TCombobox', selectbackground=[('readonly', ebg)])
style.map('TCombobox', selectforeground=[('readonly', fg)])
style.map('TCombobox', background=[('readonly', ebg)])
style.map('TCombobox', foreground=[('readonly', fg)])

cb= ttk.Combobox(root, width= 25, values=["Honda", "Hyundai", "Wolkswagon", "Tata", "Renault", "Ford", "Chrevolet", "Suzuki","BMW", "Mercedes"])

cb.pack()

root.mainloop()


# In[4]:


# עיצוב סטייל חדש לקומבובוקס

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': 'gray',
                                       'background': 'green'
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle') 

# show the current styles
# print(combostyle.theme_names())

combo = ttk.Combobox(root, values=['1', '2', '3'])
combo['state'] = 'readonly'
combo.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()


# In[1]:


# סטייל של דברים בעיקר על קומבובוקס

# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "white", background= "orange")

# Add a label widget
label=ttk.Label(win, text= "Select a Car Model",
font= ('Aerial 11'))
label.pack(pady=30)
# Add a Combobox widget
cb= ttk.Combobox(win, width= 25, values=["Honda", "Hyundai", "Wolkswagon", "Tata", "Renault", "Ford", "Chrevolet", "Suzuki","BMW", "Mercedes"])

cb.pack()

win.mainloop()


# In[5]:


# שמירת קבצים בשם

from tkinter import *
from tkinter.filedialog import asksaveasfile

new = Tk()
new.geometry('640x300')
new.title('IoT4Beginners')


def check():
    a = text.get()
    file = asksaveasfile(defaultextension=".txt")
    file.write(a)


text = Entry(new, font=('TimesNewRoman',20))
button = Button(new,text='Save as',font=('Courier',10), width=30,bd=10, command =check)



text.place(x=10,y=10,height=240,width=610)
button.pack(side=BOTTOM)
mainloop()


# In[ ]:


# עוד דוגמא לשמירת קבצים בשם

# importing all files from tkinter
from tkinter import *
from tkinter import ttk

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')

# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)

btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack(side = TOP, pady = 20)

mainloop()


# In[6]:


# כל הסגנונות של טקינטר
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # label
        label = ttk.Label(self, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10,  sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10,  sticky='w')
        # button
        btn = ttk.Button(self, text='Show')
        btn.grid(column=2, row=0, padx=10, pady=10,  sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()


# In[91]:





# In[9]:


# Tkinter OptionMenu
A = ["A", "B", "C"]
from tkinter import *
parent = Tk()
varList = StringVar(parent)
varList.set("Red")
om = OptionMenu(parent, varList, "Yellow", "Pink", "RED", "Brown", "Black", "Blue", *A)
om.pack()
parent.mainloop()


# In[101]:





# In[44]:


# Tkinter Combobox

# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Combobox.html

# https://www.pythontutorial.net/tkinter/tkinter-combobox/

import tkinter as tk
from tkinter import ttk
from calendar import month_name
from datetime import datetime

root = tk.Tk()

# create a combobox
selected_month = StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month, width=5, state='readonly',values=[month_name[m][0:3] for m in range(1, 13)])
month_cb.pack()


# set the current month
current_month = datetime.now().strftime('%b')
month_cb.set(current_month)

root.mainloop()


# In[104]:


# איך לשנות צבעים בקומבובוקס

# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "white")

# Add a label widget
label=ttk.Label(win, text= "Select a Car Model",
font= ('Aerial 11'))
label.pack(pady=30)
# Add a Combobox widget
cb= ttk.Combobox(win, width= 25, values=["Honda", "Hyundai", "Wolkswagon", "Tata", "Renault", "Ford", "Chrevolet", "Suzuki","BMW", "Mercedes"])

cb.pack()

win.mainloop()


# In[11]:


# בד
# הווידג'ט Canvas משמש לציור צורות, כגון קווים, אליפסות, מצולעים ומלבנים, ביישום שלך.

import tkinter as Tkinter

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()


# In[16]:


# כפתור סימון
# הווידג'ט Checkbutton משמש להצגת מספר אפשרויות כתיבות סימון. המשתמש יכול לבחור אפשרויות מרובות בו-זמנית.

import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

from tkinter import *

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()
top.mainloop()


# In[7]:


# כניסה
# יישומון הכניסה משמש להצגת שדה טקסט בשורה אחת לקבלת ערכים ממשתמש.

from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()


# In[1]:


# מסגרת
# הווידג'ט Frame משמש כווידג'ט מיכל לארגון ווידג'טים אחרים.

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()


# In[3]:


# תווית
# הווידג'ט Label משמש כדי לספק כיתוב בשורה אחת עבור ווידג'טים אחרים. זה יכול להכיל גם תמונות.

from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()


# In[65]:


# קופסת רשימה
# הווידג'ט Listbox משמש כדי לספק רשימה של אפשרויות למשתמש.

from tkinter import *
import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

top = Tk()

Lb1 = Listbox(top, selectmode="SINGLE", width=5)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

top.mainloop()


# In[11]:


# כפתור תפריט
# הווידג'ט של כפתור התפריט משמש להצגת תפריטים באפליקציה שלך.

from tkinter import *
import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

# אם רוצים שיתאפשר בחירות מרובות
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label="mayo", variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup", variable=ketchVar )

'''# אם רוצים שיתאפשר בחירה אחת
mayoVar = IntVar() # או סטרינגוואר
mb.menu.add_radiobutton ( label="mayo", variable=mayoVar )
mb.menu.add_radiobutton ( label="ketchup", variable=mayoVar )'''


mb.pack()
top.mainloop()


# In[12]:


# תפריט
# יישומון התפריט משמש כדי לספק פקודות שונות למשתמש. פקודות אלה כלולות בתוך כפתור התפריט.

from tkinter import *

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()


# In[1]:


# הודעה
# יישומון ההודעה משמש להצגת שדות טקסט מרובי שורות לקבלת ערכים ממשתמש.

from tkinter import *

root = Tk()
var = StringVar()
label = Message( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()


# In[6]:


# כפתור רדיו
# הווידג'ט Radiobutton משמש להצגת מספר אפשרויות כלחצני בחירה. המשתמש יכול לבחור רק אפשרות אחת בכל פעם.

from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()


# In[4]:


# סולם
# הווידג'ט Scale משמש כדי לספק ווידג'ט מחוון.

from tkinter import *

def sel():
    selection = "Value = " + str(var.get())
    label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()



# In[1]:


# בר גלילה 
# הווידג'ט של סרגל הגלילה משמש להוספת יכולת גלילה לווידג'טים שונים, כגון תיבות רשימה.

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

menubutton = Menubutton(root, text="Options")
menubutton.pack()
menu = Menu(menubutton, tearoff=0)
menubutton.config(menu=menu)


mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(13):
    mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()


# In[3]:


# טקסט
# יישומון הטקסט משמש להצגת טקסט במספר שורות.

from tkinter import *

def onclick():
    pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()


# In[3]:


# הרמה העליונה
# הווידג'ט Toplevel משמש כדי לספק מיכל חלון נפרד.

from tkinter import *

root = Tk()
top = Toplevel()
top.mainloop()


# In[7]:


# ספיןבוקס
# הווידג'ט Spinbox הוא גרסה של הווידג'ט הסטנדרטי של Tkinter Entry, שניתן להשתמש בו כדי לבחור מתוך מספר קבוע של ערכים.

from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)

w.pack()

mainloop()


# In[54]:


# שימוש בספינבוקס לבחירת תאריך עברי לועזי ושעה

# שימוש בספינבוקס לבחירת שעות דקות ושניות

from tkinter import *


'''def display_selected():
    msg.config(
        text=f'התאריך שנבחר הוא: {greg_day.get()} {greg_month.get()} {greg_year.get()}', 
        font=('sans-serif', 14),
        bg='#D97904'
        )'''

ws = Tk()

# אזור נפרד להזנת תאריך לועזי ושעה
date_time = PanedWindow()

# תאריך לועזי-----------------
# כותרת
Label(date_time, text="תאריך לועזי - גרגוריאני", font=('sans-serif', 15)).grid(column=0, row=0, columnspan=3)

greg_year = IntVar()
Spinbox(
    date_time,
    textvariable=greg_year,
    from_=2000, 
    to=2050,
    wrap=True,
    state = 'normal',
    width=5,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=2, row=1)
Label(date_time, text="בחרו/הזינו שנה").grid(column=2, row=2)

greg_month = IntVar()
Spinbox(
    date_time,
    textvariable=greg_month,
    from_=1, 
    to=12,
    wrap=True,
    state = 'readonly',
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=1, row=1)
Label(date_time, text="בחרו חודש").grid(column=1, row=2)

greg_day = IntVar()
Spinbox(
    date_time,
    textvariable=greg_day,
    state = 'readonly',
    from_=1, 
    to=31,
    wrap=True,
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=0, row=1)
Label(date_time, text="בחרו יום").grid(column=0, row=2)

# הפרדה-------------------------------
Label(date_time, text="                         ").grid(column=3, row=1)

# כותרת
Label(date_time, text="שעה", font=('sans-serif', 15)).grid(column=4, row=0, columnspan=3)

# שעה-----------------------

hours = IntVar()
Spinbox(
    date_time,
    textvariable=hours,
    from_=0, 
    to=23,
    wrap=True,
    state = 'readonly',
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=4, row=1)
Label(date_time, text="בחרו שעה").grid(column=4, row=2)

minutes = IntVar()
Spinbox(
    date_time,
    textvariable=minutes,
    from_=0, 
    to=59,
    wrap=True,
    state = 'readonly',
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=5, row=1)
Label(date_time, text="בחרו דקות").grid(column=5, row=2)

seconds = IntVar()
Spinbox(
    date_time,
    textvariable=seconds,
    state = 'readonly',
    from_=0, 
    to=59,
    wrap=True,
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=6, row=1)
Label(date_time, text="בחרו שניות").grid(column=6, row=2)

# הפרדה-------------------------------
Label(date_time, text="                         ").grid(column=7, row=1)

# תאריך עברי----------------------------------------------

# כותרת
Label(date_time, text="תאריך עברי", font=('sans-serif', 15)).grid(column=8, row=0, columnspan=3)


heb_year = StringVar()
Spinbox(
    date_time,
    textvariable=heb_year,
    value=["שנה"],
    wrap=True,
    state = 'normal',
    width=6,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=8, row=1)
Label(date_time, text="בחרו/הזינו שנה בספרות").grid(column=8, row=2)

heb_month = StringVar()
Spinbox(
    date_time,
    textvariable=heb_month,
    value=['ניסן', 'אייר', 'סיוון', 'תמוז', 'אב', 'אלול', 'תשרי', 'מרחשוון', 'כסלו', 'טבת', 'שבט', 'אדר', 'אדר א', 'אדר ב'],
    wrap=True,
    state = 'readonly',
    width=6,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=9, row=1)
Label(date_time, text="בחרו חודש").grid(column=9, row=2)

heb_day = StringVar()
Spinbox(
    date_time,
    textvariable=heb_day,
    value=['א','ב','ג','ד','ה','ו','ז','ח','ט','י','יא','יב','יג','יד','טו','טז','יז','יח','יט','כ','כא','כב','כג','כד','כה','כו','כז','כח','כט','ל'],
    wrap=True,
    state = 'readonly',
    width=2,
    #command=display_selected,
    font=('sans-serif', 15), 
).grid(column=10, row=1)
Label(date_time, text="בחרו יום").grid(column=10, row=2)

'''msg = Label(
    input_greg,
    text='',
    bg='#D97904'
)
msg.grid(column=2, row=3)'''


date_time.pack()

ws.mainloop()


# In[30]:


# חלון פנד
# PanedWindow הוא יישומון מיכל שעשוי להכיל כל מספר של חלוניות, מסודרות אופקית או אנכית.

from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()





# In[6]:


# לבל פריים
# מסגרת תווית היא ווידג'ט של מיכל פשוט. מטרתו העיקרית היא לשמש כמרווח או מיכל עבור פריסות חלונות מורכבות.

from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()
 
root.mainloop()


# In[13]:





# In[11]:





# In[3]:


# תיבת הודעה
# מודול זה משמש להצגת תיבות הודעות ביישומים שלך.


import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

top = Tkinter.Tk()
def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()


# In[37]:


# שימוש ב אנטר בתור לחצן קלט

from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('pythonguides')
ws.geometry('250x200')

def welMsg(name):
    name = name_Tf.get()
    return messagebox.showinfo('pythonguides', f'Hi! {name}, welcome to pythonguides' )

Label(ws, text='Enter Name & hit Enter Key').pack(pady=20)
name_Tf = Entry(ws)
name_Tf.bind('<Return>',welMsg)
name_Tf.pack()

ws.mainloop()


# In[38]:


help(name_Tf.bind)


# In[1]:


# How to set justification on Tkinter Text box?

# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a text widget
text=Text(win, width=40, height=10)

# justify the text alignment to the center
text.tag_configure("center", justify='center')
text.insert(INSERT, "Welcome to Tutorialspoint...")

# Add the tag from start to end text
text.tag_add("center", 1.0, "end")
text.pack()

win.mainloop()


# In[5]:


# How to run an infinite loop in Tkinter?

# Import the required library
from tkinter import *

# Create an instance of tkinter frame
win=Tk()

# Set the size of the Tkinter window
win.geometry("700x350")

# Define a function to print something inside infinite loop
condition=True

def infinite_loop():
    global condition
    if condition:
        Label(win, text="Infinite Loop!", font="Arial, 25").pack()

       # Call the infinite_loop() again after 1 sec 
        win.after(1000, infinite_loop)

def start():
    global condition
    condition=True

def stop():
    global condition
    condition=False

# Create a button to start the infinite loop
start = Button(win, text= "Start the Loop", font="Arial, 12", command=start).pack()
stop = Button(win, text="Stop the Loop", font="Arial, 12", command=stop).pack()

# Call the infinite_loop function after 1 sec.
win.after(1000, infinite_loop)

win.mainloop()


# In[5]:


# How to stop Tkinter after function?

#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x270")
#Initialize a Label widget
Label(win, text= "This window will get closed after 3 seconds...",
font=('Helvetica 20 bold')).pack(pady=20)
#Automatically close the window after 3 seconds
win.after_cancel(win)
win.after(3000,lambda:win.destroy())
win.mainloop()


# In[ ]:


# איך מעתיקים נתונים ללוח לא קשור דווקא לטקינטר
a = "ddllfkghkjf"
import clipboard
ccc = clipboard.copy(a)
clipboard.paste()


# In[3]:


# לא קשור דווקא לטקינטר
# הדפסת טקסט מודגש או עם קו תחתון

# פונקצייה להדפסת טקסט מודגש
# דוגמא לשימוש: 
#print(bold("יעקב"), "אבינו")
def bold(x):
    BOLD = '\033[1m'
    NORMAL = '\033[0m'
    return BOLD + x + NORMAL

# פונקצייה להדפסת טקסט עם קו תחתון
# דוגמא לשימוש:
# print(bold("יעקב"), "אבינו", underline("וגם אליעזר"))
def underline(x):
    UNDERLINE = '\033[4m'
    NORMAL = '\033[0m'
    return UNDERLINE + x + NORMAL

print(bold("יעקב"), "אבינו", underline("וגם אליעזר"))


# In[ ]:


# איך לבצע פעולה חוזרת בפייתון, אבל לא בטקינטר

import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    sc.enter(3, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()


# In[ ]:


# לא קשור דווקא לטקינטר

# ספליט לפי מספר סימנים

import re

aa = "Hey, Copines is a good song; I like that song"

print(re.split('; |, |\*|\n', aa)) 


# In[6]:


# Python program to create a close button
# using destroy Non-Class method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

root.mainloop()


# In[35]:


# Python program to create a close button
# using quit method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
exit(0)


# In[4]:


# חסימת תגובות קלט משתמש חשוב מאוד

# Import the required library
from tkinter import *

# Create an instance of tkinter frame or widget
win=Tk()
win.geometry("700x350")

# Create a text widget
text=Text(win, font="Calibri, 14")
text.pack(fill= BOTH, expand= True)

# Bind the keys with the event handler
text.bind('<Control-v>', lambda _:'break')
text.bind('<Control-c>', lambda _:'break')
text.bind('<BackSpace>', lambda _:'break')


# חסימת כל תגובה לעכבר וכו של תיבת הטקסט
#txt.bindtags(("txt", "wnd", "all"))

# לחילופין, חסימת שתי תגובות ספציפיות לעכבר עבור תיבת הטקסט
#txt.bind("<Button>", lambda event: "break")
#txt.bind("<Motion>", lambda event: "break")


win.mainloop()


# In[1]:


# Removing all default bindings

import tkinter as tk

root = tk.Tk()
text = tk.Text(root)
text.bindtags((str(text), str(root), "all"))

# Removing specific bindings

text.bind("<Double-1>", lambda event: "break")



# In[ ]:


# Disable Exit (or [ X ]) in Tkinter Window

#Import the tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry of the function
win.geometry("750x250")
def close_win():
    win.destroy()
def disable_event():
    pass
#Create a button to close the window
btn = ttk.Button(win, text ="Click here to Close",command=close_win)
btn.pack()
#Disable the Close Window Control Icon
win.protocol("WM_DELETE_WINDOW", disable_event)
win.mainloop()


# In[1]:


#-------------------------------------
# צריך רישיון שימוש בתוכנה ואם לא אז התוכנה לא פועלת


# פונקצייה לכתיבת קובץ רישיון משולם אם המשתמש הקליד את המילים: רכשתי את התוכנה כדין
def license():
    from tkinter import messagebox as tkMessageBox
    if var123.get() == "156533342":
        file = open("cu_license.txt", "w")
        file.write("התוכנה נרכשה כדין")
        tkMessageBox.showinfo( "רישיון תוכנת כוכבים וזמנים", "כעת ניתן להשתמש בתוכנה בחופשיות")
        On_off.grid(column=1, row=0, columnspan = 2)
        ws.after(1, astro_calculations)
        ws.after(1, C1.set(1))
        lin.destroy()
    else:
        tkMessageBox.showinfo( "רישיון תוכנת כוכבים וזמנים", "טעות בהקלדה, נסה שוב")
        
def nisaion():
    tkMessageBox.showinfo( "רישיון תוכנת כוכבים וזמנים", "התוכנה נפתחה לשימוש פעם אחת")
    On_off.grid(column=1, row=0, columnspan = 2)
    ws.after(1, astro_calculations)
    ws.after(1, C1.set(1))
    file = open("cu_license.txt", "w")
    file.write(line1)
    lin.destroy()


# פתיחת קובץ הרישיון וקריאה של מה שכתוב בו        
with open('cu_license.txt', 'r') as f:
    if f.mode=='r':
        line1 = f.readline()
        line2 = f.readline()

# אם לא כתוב ברישיון שהתוכנה נרכשה כדין, משתנה רישיון שווה אפס, אם התוכנה נרכשה משתנה רישיון שווה אחד
if line1 == 'התוכנה נרכשה כדין':
    rishaion = 1
else:
    rishaion = 0

# במקרה שרישיון שווה אפס, יש להעלים את כפתור הפעלת וכיבוי החישובים            
if rishaion != 1:
    ws.after(1, C1.set(0))
    On_off.grid_forget()
        
if line1 != 'התוכנה נרכשה כדין':
    # פתיחת חלון למשתמש בבקשה שיזין האם רכש את התוכנה כדין
    from tkinter import *
    lin = Toplevel()
    Label(lin, text="לא תעשוק את רעך - ולא תגזול (ויקרא יט,יג) \nאסור להשתמש בתוכנה שלא נרכשה כדין \nמחיר התוכנה 20 שקלים בלבד לכל מחשב \nלרכישה פנה באימייל \nsgbmzm@gmail.com \n\nאם רכשת את התוכנה כדין, הקלד את הסיסמה שקיבלת ברכישה, ולחץ על אישור").pack()
    var123 = StringVar(lin)
    Entry(lin, textvariable=var123, width=9).pack()
    Button(lin, text ="אישור", command = license).pack()
    
    if line2 == "לא בוצע ניסיון":
        Button(lin, text ="לחץ כדי לנסות את התוכנה פעם אחת", command = nisaion, font="david 14 bold").pack()
    
    # החלון הזה יהיה מעל כל החלונות האחרים
    lin.attributes('-topmost',True)
    
    # הגדרה מה לעשות כשהמשתמש לוחץ על אייקון הסגירה של החלון. כרגע מוגדר לסגור את החלון הראשי וממילא גם החלון המשני נסגר
    def disable_event():
        ws.destroy()
    lin.protocol("WM_DELETE_WINDOW", disable_event)
    
    lin.mainloop()


# In[4]:


import tkinter as tk
import tkinter.ttk as ttk


class FormattedSpinbox(ttk.Spinbox):
    """A ttk.Spinbox that displays a float with 2 decimals,
    alongside a '%' character unit
    """
    def __init__(self, master, **kwargs):
        kwargs['command'] = self.command
        super().__init__(master, **kwargs)
    def set(self, value):
        super().set(value)
        self.command()
    def get(self):
        return float(super().get().strip().split()[0])
    def command(self):
        value = self.get()
        self.delete(0, tk.END)
        self.insert(0, f'{float(value): 10.2f} %')


root = tk.Tk()

spinoptions = {'from_': 0, 'to': 100, 'increment': 5}
spinbox = FormattedSpinbox(root, **spinoptions)
spinbox.set(0)  # default value
spinbox.pack()

root.minsize(400, 100)
root.mainloop()


# In[23]:


import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
style = ttk.Style()
style.theme_use('vista')

spinbox = ttk.Spinbox(root, from_=-90, to=90, format_='%1.0f.')
#spinbox.set('{:10.2f} ...'.format(0))  # default value

spinbox.pack()

root.minsize(400, 100)  # make window larger for ease of finding for this simple example
root.mainloop()


# In[28]:


import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("300x150") 

t2 = StringVar()
my_list=['One', 'Two', 'Three', 'Four', 'Five']
sb2 = Spinbox(my_w,values=my_list,  textvariable=t2, width=10)
sb2.grid(row=1,column=2,padx=20)
t2.set('Four')
sb2.delete(0,'end') # replace from 0 position till end
sb2.insert(0,'FOUR') # add string from 0 position
my_w.mainloop()  # Keep the window open


# In[8]:


# מחשבון שמישהו בנה כמדריך לטקינטר

import tkinter as tk

import tkinter.font



def display_result():

    string = txt_display.get()

    try:

        result = eval(string)

    except:

        result = "ERROR"



    txt_display.delete(0, tk.END)

    txt_display.insert(0, str(result))



root = tk.Tk()

root.title("Basic Calculator")



font_buttons = tkinter.font.Font(root, family='Arial', size=20, weight='bold')



for i in range(5):

    root.rowconfigure(i, weight=1)

    root.columnconfigure(i, weight=1)



txt_display = tk.Entry(root, font="Courier 40 bold", justify='right')

txt_display.grid(row=0, column=0, columnspan=5, sticky='NESW')

for num in range(1,10):

    btn = tk.Button(

        root,



        text=str(num),

        font=font_buttons,

        command=lambda x=num: txt_display.insert(tk.END, str(x)))



    btn.grid(column=(num-1)%3, row=(num-1)//3+1, sticky = 'NESW')



btn_0 = tk.Button(root, text="0", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "0"))

btn_0.grid(row=4, column=0, columnspan=2, sticky='NESW')



btn_dot = tk.Button(root, text=".", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "."))

btn_dot.grid(row=4, column=2, sticky='NESW')



btn_plus = tk.Button(root, text="+", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "+"))

btn_plus.grid(row=1, column=3, sticky='NESW')



btn_minus = tk.Button(root, text="-", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "-"))

btn_minus.grid(row=2, column=3, sticky='NESW')



btn_mul = tk.Button(root, text="*", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "*"))

btn_mul.grid(row=3, column=3, sticky='NESW')



btn_div = tk.Button(root, text="/", font=font_buttons,

    command=lambda: txt_display.insert(tk.END, "/"))

btn_div.grid(row=4, column=3, sticky='NESW')



btn_back = tk.Button(root, text="C", font=font_buttons,

    command=lambda: txt_display.delete(0, tk.END))

btn_back.grid(row=1,column=4, sticky='NESW')



btn_equal = tk.Button(root, text="=", font=font_buttons,

    command=display_result)

btn_equal.grid(row=2,column=4, rowspan=3, sticky='NESW')





root.mainloop()


# In[2]:


# העלאת קבצים

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200') 


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    
adhar = Label(
    ws, 
    text='Upload Government id in jpg format '
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)

dl = Label(
    ws, 
    text='Upload Driving License in jpg format '
    )
dl.grid(row=1, column=0, padx=10)

dlbtn = Button(
    ws, 
    text ='Choose File ', 
    command = lambda:open_file()
    ) 
dlbtn.grid(row=1, column=1)

ms = Label(
    ws, 
    text='Upload Marksheet in jpg format '
    )
ms.grid(row=2, column=0, padx=10)

msbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
msbtn.grid(row=2, column=1)

upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



ws.mainloop()


# In[3]:


# לוח שנה לועזי

# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2020, month = 5,
			day = 22)

cal.pack(pady = 20)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Get Date",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()

