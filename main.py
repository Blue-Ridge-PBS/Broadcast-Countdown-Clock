import time
from tkinter import *

### Create the Window
clockWindow = Tk()
clockWindow.attributes('-fullscreen', True)
clockWindow.title("Countdown Timer")
clockWindow.configure(background='black')

### Declare variables
hourString = StringVar()
tenhourString = StringVar()
minuteString = StringVar()
tenminuteString = StringVar()
secondString = StringVar()
tensecondString = StringVar()
Stop_Countdown = StringVar()

### Set strings to default value
hourString.set("0")
tenhourString.set("0")
minuteString.set("0")
tenminuteString.set("0")
secondString.set("0")
tensecondString.set("0")
Stop_Countdown.set("1")

### Boxes to show input
colononebox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", text =":")
colontwobox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", text =":")
hourTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=hourString)
tenhourTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=tenhourString)
minuteTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=minuteString)
tenminuteTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=tenminuteString)
secondTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=secondString)
tensecondTextbox = Label(clockWindow, width=1, font=("Calibri", 350, ""), background = "black", foreground = "white", textvariable=tensecondString)

### Text Placement
colononebox.place(x= 475, y=140)
colontwobox.place(x= 1070, y= 140)
hourTextbox.place(x=300, y=180)
tenhourTextbox.place(x=50, y=180)
minuteTextbox.place(x=895, y=180)
tenminuteTextbox.place(x=645, y=180)
secondTextbox.place(x=1490, y=180)
tensecondTextbox.place(x=1240, y=180)

### Change font color for Countup
def count_up_font():
    colononebox.configure(foreground="red")
    colontwobox.configure(foreground="red")
    tenhourTextbox.configure(foreground="red")
    hourTextbox.configure(foreground="red")
    tenminuteTextbox.configure(foreground="red")
    minuteTextbox.configure(foreground="red")
    tensecondTextbox.configure(foreground="red")
    secondTextbox.configure(foreground="red")

### Font color for running out fo time
def time_run_out():
    colononebox.configure(foreground="yellow")
    colontwobox.configure(foreground="yellow")
    tenhourTextbox.configure(foreground="yellow")
    hourTextbox.configure(foreground="yellow")
    tenminuteTextbox.configure(foreground="yellow")
    minuteTextbox.configure(foreground="yellow")
    tensecondTextbox.configure(foreground="yellow")
    secondTextbox.configure(foreground="yellow")

### Timer 
def runTimer(event):

    #Determine Start or Stop
    if int(Stop_Countdown.get()) == 1:
        Stop_var = int(Stop_Countdown.get())
        Stop_var = 0
        Stop_Countdown.set(Stop_var)

    else: 
        Stop_var = 1
        Stop_Countdown.set(Stop_var)

    #Get your variables     
    try:
        clockTime = (int(tenhourString.get())*10 *3600) + int(hourString.get())*3600 + (int(tenminuteString.get())*10*60) + int(minuteString.get())*60 + int(tensecondString.get())*10 + int(secondString.get())
    except:
        print("Incorrect values")

    #Countdown
    while(clockTime > 0):
               
        Minutes, Seconds = divmod(clockTime, 60)
        
        tenHours = 0
        oneHours = 0
        Hours = 0
        oneMinutes = 0
        tenMinutes = 0
        oneSeconds = 0
        tenSeconds = 0

        if(Minutes > 60):
            Hours, Minutes = divmod(Minutes, 60)
        
        if (Hours > 9):
            oneHours = Hours%10
            tenHours = Hours // 10
        else:
            oneHours = Hours
        
        oneMinutes = Minutes%10
        tenMinutes = Minutes//10

        oneSeconds = Seconds % 10
        tenSeconds = Seconds // 10

        if oneMinutes < 5 and tenMinutes == 0 and oneHours == 0 and tenHours == 0:
            time_run_out()

        hourString.set(oneHours)
        tenhourString.set(tenHours)
        minuteString.set(oneMinutes)
        tenminuteString.set(tenMinutes)
        secondString.set(oneSeconds)
        tensecondString.set(tenSeconds)
        

        ### Update the interface
        clockWindow.update()
        time.sleep(1)   
        clockTime -= 1

        # Break the loop
        if int(Stop_Countdown.get()) == 1:
            break

                
            
    ### Automatically count up
    if clockTime == 0:
        while(clockTime >= -1):
                
            count_up_font()

            Minutes, Seconds = divmod(clockTime, 60)

            tenHours = 0
            oneHours = 0
            Hours = 0
            oneMinute = 0
            tenMinutes = 0
            oneSeconds = 0
            tenSeconds = 0

            if(Minutes > 60):
                Hours, Minutes = divmod(Minutes, 60)
                    
            if (Hours > 9):
                oneHours = Hours % 10
                tenHours = Hours // 10

            else:
                oneHours = Hours
        
            oneMinutes = Minutes%10
            tenMinutes = Minutes//10

            oneSeconds = Seconds % 10
            tenSeconds = Seconds // 10


            hourString.set(oneHours)
            tenhourString.set(tenHours)
            minuteString.set(oneMinutes)
            tenminuteString.set(tenMinutes)
            secondString.set(oneSeconds)
            tensecondString.set(tenSeconds)
        

            ### Update the interface
            clockWindow.update()
            time.sleep(1)   

            clockTime += 1

            if int(Stop_Countdown.get()) == 1:
                break      
    
### Defining how to set the time
#Setting the hours
def hour_up(event):
    try:
        New_Hour = int(hourString.get()) + 1
    except:
        print("Error")

    if New_Hour > 9:
        New_Hour = 0
    hourString.set(New_Hour)

def ten_hour_up(event):
    try:
        New_Hour = int(tenhourString.get()) + 1
    except:
        print("Error")

    if New_Hour > 9:
        New_Hour = 0

    tenhourString.set(New_Hour)
# Setting the minutes
def minute_up(event):
    try:
        New_Minute = int(minuteString.get()) + 1
    except:
        print("Error")

    if New_Minute > 9:
        New_Minute = 0
    minuteString.set(New_Minute)
    
def tenminute_up(event):
    try:
        New_Minute = int(tenminuteString.get()) + 1
    except:
        print("Error")

    if New_Minute > 5:
        New_Minute = 0
    tenminuteString.set(New_Minute)
# Setting the seconds
def second_up(event):
    try:
        New_Second = int(secondString.get()) + 1
    except:
        print("Error")

    if New_Second > 9:
        New_Second = 0
    secondString.set(New_Second)

def tensecond_up(event):
    try:
        New_Second = int(tensecondString.get()) + 1
    except:
        print("Error")

    if New_Second > 5:
        New_Second = 0
    tensecondString.set(New_Second) 

def Clear_command(event):
    hourString.set("0")
    tenhourString.set("0")
    minuteString.set("0")
    tenminuteString.set("0")
    secondString.set("0")
    tensecondString.set("0")
    Stop_Countdown.set("1")
    colononebox.configure(foreground="white")
    colontwobox.configure(foreground="white")
    tenhourTextbox.configure(foreground="white")
    hourTextbox.configure(foreground="white")
    tenminuteTextbox.configure(foreground="white")
    minuteTextbox.configure(foreground="white")
    tensecondTextbox.configure(foreground="white")
    secondTextbox.configure(foreground="white")

### Binding Keys to Events
clockWindow.bind("9", hour_up)
clockWindow.bind("8", ten_hour_up)
clockWindow.bind("5", tenminute_up)
clockWindow.bind("6", minute_up)
clockWindow.bind("2", tensecond_up)
clockWindow.bind("3", second_up)
clockWindow.bind("0", Clear_command)
clockWindow.bind("<Return>", runTimer)

### Keep looping
clockWindow.mainloop()