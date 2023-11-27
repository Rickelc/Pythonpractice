import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.prompt_label1= tkinter.Label(self.top_frame, text = 'Enter the number of gallons the car holds:')
        self.gallon_entry= tkinter.Entry(self.top_frame, width= 10)
        
        self.prompt_label2= tkinter.Label(self.top_frame, text = 'Enter the number of miles the car can go on a full tank:')
        self.miles_entry= tkinter.Entry(self.top_frame, width= 10)
        
        self.prompt_label1.pack(side='left')
        self.gallon_entry.pack(side='left')
        
        self.prompt_label2.pack(side='left')
        self.miles_entry.pack(side='left')
        
        
        self.calc_button = tkinter.Button(self.bottom_frame,text= 'Calcuate MPG', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def convert(self):
        gallons = float(self.gallon_entry.get())
        miles= float(self.miles_entry.get())
        
        mpg = miles / gallons
        
        tkinter.messagebox.showinfo('Results', 'The car can go' + str(mpg) + 'miles per gallon of gas.')
        
