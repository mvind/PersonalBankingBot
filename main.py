import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from scrapper import scrape

class MainApp():
        def __init__(self, master):
            self.loaded = False
            self.lonseddler = [] # Should only contain one element

            self.master = master
            self.master.title('PersonalBankingBot')

            self.frame = tk.Frame(self.master)
            self.frame.pack()

            # Canvas
            self.can = tk.Canvas(self.frame, width=400, height=400)

            # Buttons
            self.findbutton = tk.Button(self.frame, text='Select file', command=self.load_file)
            self.findbutton.pack()

            self.analyzebutton = tk.Button(self.frame, text='Get data', command=self.serve_data)
            self.analyzebutton.pack()

            #self.scrollbar.config(command=self.can.yview)
            #self.scrollbar.pack(side="right",fill="y")
            self.can.pack()


        def load_file(self):
            dir_path = os.getcwd()

            try:
                file = filedialog.askopenfilename(initialdir = dir_path ,title='Select file'
                                         , filetypes=(("PDF files",".PDF"),('All files','*.*')))

            except:
                print('Error load file')

            raw_data = scrape(file)
            print(raw_data)
            self.lonseddler.append(raw_data)# Add lonseddel path to file list.
            self.loaded = True



        def serve_data(self):
            self.can.delete(all)
            try:
                self.can.create_text(50, 10, text='Data found: ')
                x = 10
                y = 35
                for item in self.lonseddler[0]:
                    self.can.create_text(x,y,text=item, anchor='nw')
                    y+= 20
                self.can.configure(scrollregion= self.can.bbox(all))
            except IndexError:
                messagebox.showerror('Error', 'No file selected')
                #print('No file selected')

        
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
