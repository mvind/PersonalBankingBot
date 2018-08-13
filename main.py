import tkinter as tk
from tkinter import filedialog
import os
from scrapper import scrape

class MainApp():
        def __init__(self, master):
            self.master = master
            self.master.title('PersonalBankingBot')

            self.frame = tk.Frame(self.master)
            self.frame.pack()

            self.button = tk.Button(self.frame, text='Select file', command=self.load_file)
            self.button.pack()

        def load_file(self):
            dir_path = os.getcwd()

            try:
                file = filedialog.askopenfilename(initialdir = dir_path ,title='Select file'
                                         , filetypes=(("PDF files",".PDF"),('All files','*.*')))
            except:
                print('Error load file')

            #self.lonseddeler.append(file) # Add lonseddel path to file list.

            print(scrape(file))

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
