from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
import webbrowser
import platform

def app():
    def showChart():
        img = Image.open("C:\\Users\\Ashwin\\Desktop\\Programming Portfolio\\Finished Projects\\bmi-calc\\img\\bmi-chart.png")
        img.show()

    def showHelp():
        webbrowser.open("https://www.google.com/search?q=what+is+BMI&sxsrf=ALiCzsaktVrWGWJaUF78bFI1qFg4gHzsgQ%3A1655312297031&source=hp&ei=qA-qYue_O4vKtQa2pbPYBg&iflsig=AJiK0e8AAAAAYqoduV3Fk8Pu86M1qfT2x92klMWwDv5q&ved=0ahUKEwjns9Dr9q_4AhULZc0KHbbSDGsQ4dUDCAk&uact=5&oq=what+is+BMI&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6DQguEMcBENEDEOoCECc6BAgAEEM6CggAELEDEIMBEEM6DgguEIAEELEDEIMBENQCOhEILhCABBCxAxCDARDHARCjAjoFCAAQkQI6CAgAELEDEIMBOgsIABCABBCxAxCDAToICAAQgAQQyQM6CAguELEDEIMBOggIABCABBCxA1C3DlijH2CJImgBcAB4AIABcYgBgwiSAQM5LjKYAQCgAQGwAQo&sclient=gws-wiz")

    def showAbout():
        os = platform.platform()
        messagebox.showinfo(title="About", message=f"BMI Calculator                                          \nAuthor: Ashwin Ravuru Kalyan\nVersion: 1.1.0\nOperating System: {os}")

    window = Tk()
    window.geometry("700x350")
    window.resizable(False, False)
    window.iconbitmap("C:\\Users\\Ashwin\\Desktop\\Programming Portfolio\\Finished Projects\\bmi-calc\\icon\\favicon.ico")
    window.title("BMI Calculator")

    tabControl = ttk.Notebook(window)
    customaryTab = ttk.Frame(tabControl)
    metricTab = ttk.Frame(tabControl)
    tabControl.add(customaryTab, text="Customary                                                                                              ")
    tabControl.add(metricTab, text="Metric                                                                                                      ")
    tabControl.pack(expand=1, fill="both")

    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Window                          ", command=newWindow)
    filemenu.add_command(label="BMI Chart", command=showChart)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Show Help                        ", command=showHelp)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=showAbout)
    menubar.add_cascade(label="Help", menu=helpmenu)

    titleLabel = Label(window, font=("Times New Roman", 25), text="BMI Calculator").place(x=250, y=30)
    resultLabel = Label(window, font=("Times New Roman", 15), text="Your BMI is:").place(x=200, y=240)

    # Metric Tab Code Start ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    heightLabelCm = Label(metricTab, font=("Times New Roman", 11), text="Height (cm)").place(x=165, y=100)
    weightLabelKg = Label(metricTab, font=("Times New Roman", 11), text="Weight (kg)").place(x=165, y=125)

    heightEntryCm = Entry(metricTab, width=34)
    heightEntryCm.insert(0, "170")
    heightEntryCm.place(x=250, y=100)

    weightEntryKg = Entry(metricTab, width=34)
    weightEntryKg.insert(0, "65")
    weightEntryKg.place(x=250, y=125)

    def bmiCalcMetric():
        try:
            height = float(heightEntryCm.get())
            weight = float(weightEntryKg.get())
            heightMeters = height/100
            heightMetersSq = heightMeters**2    
            bmi = weight/heightMetersSq
            bmiRounded = round(bmi, 2)

        except ZeroDivisionError:
            messagebox.showerror(title="Error", message="Cannot divide by zero. Please enter a value above zero for your height and weight.")
        
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid number.                                                ")

        if  bmi < 18.5:
            bmiResult = Label(metricTab, font=("Times New Roman", 15), foreground="#3477eb", text=f"{bmiRounded}, underweight                                                                                           ").place(x=320, y=216)
        elif bmi >= 18.5 and bmi <= 24.9:
            bmiResult = Label(metricTab, font=("Times New Roman", 15), foreground="#10eb2a", text=f"{bmiRounded}, healthy                                                                                           ").place(x=320, y=216)
        elif bmi >= 25 and bmi <= 29.9:
            bmiResult = Label(metricTab, font=("Times New Roman", 15), foreground="#ebc310", text=f"{bmiRounded}, overweight                                                                                           ").place(x=320, y=216)
        elif  bmi > 30:
            bmiResult = Label(metricTab, font=("Times New Roman", 15), foreground="#fa0505", text=f"{bmiRounded}, obese                                                                                           ").place(x=320, y=216)

    calcButtonMetric = Button(metricTab, text="        Calculate        ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=bmiCalcMetric).place(x=297, y=169)

    # Metric Tab Code End / Customary Tab Code Start ---------------------------------------------------------------------------------------------------------------------------------------------
    
    heightLabelFt = Label(customaryTab, font=("Times New Roman", 11), text="Height (ft)").place(x=165, y=100)
    heightLabelIn = Label(customaryTab, font=("Times New Roman", 11), text="Height (in)").place(x=165, y=125)
    weightLabelLbs = Label(customaryTab, font=("Times New Roman", 11), text="Weight (lbs)").place(x=165, y=150)

    heightEntryFt = Entry(customaryTab, width=34)
    heightEntryFt.insert(0, "5")
    heightEntryFt.place(x=250, y=100)

    heightEntryIn = Entry(customaryTab, width=34)
    heightEntryIn.insert(0, "8")
    heightEntryIn.place(x=250, y=125)

    weightEntryLbs = Entry(customaryTab, width=34)
    weightEntryLbs.insert(0, "150")
    weightEntryLbs.place(x=250, y=150)

    def bmiCalcCustomary():
        try:
            heightFt = int(heightEntryFt.get())
            heightIn = float(heightEntryIn.get())
            height = (heightFt*12)+heightIn
            weight = float(weightEntryLbs.get())
            bmi = (weight*703)/(height**2)
            bmiRounded = round(bmi, 2)
        except ZeroDivisionError:
            messagebox.showerror(title="Error", message="Cannot divide by zero. Please enter a value above zero for your height and weight.")
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid number.                                                ")

        if  bmi < 18.5:
            bmiResult = Label(customaryTab, font=("Times New Roman", 15), foreground="#3477eb", text=f"{bmiRounded}, underweight                                                                                           ").place(x=320, y=216)
        elif bmi >= 18.5 and bmi <= 24.9:
            bmiResult = Label(customaryTab, font=("Times New Roman", 15), foreground="#10eb2a", text=f"{bmiRounded}, healthy                                                                                           ").place(x=320, y=216)
        elif bmi >= 25 and bmi <= 29.9:
            bmiResult = Label(customaryTab, font=("Times New Roman", 15), foreground="#ebc310", text=f"{bmiRounded}, overweight                                                                                           ").place(x=320, y=216)
        elif  bmi > 30:
            bmiResult = Label(customaryTab, font=("Times New Roman", 15), foreground="#fa0505", text=f"{bmiRounded}, obese                                                                                           ").place(x=320, y=216)

    calcButtonMetric = Button(customaryTab, text="        Calculate        ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=bmiCalcCustomary).place(x=297, y=182)

    # Customary Tab Code End ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    window.config(menu=menubar)
    window.mainloop()

def newWindow():
    app()

app()