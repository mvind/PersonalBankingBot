from tkinter import *
from tkinter import filedialog
import os


def main():

    uploadButton = Button(root, text="Select file", command=load_file)
    uploadButton.pack()

    mainloop()

def load_file():
    dir_path = os.getcwd()
    try:
        root.filename = filedialog.askopenfile(initialdir = dir_path ,title='Select file'
                        , filetypes=(("PDF files",".PDF"),('All files','*.*')))
    except:
        print('error')

    print(root.filename)

if __name__ == '__main__':
    root = Tk()
    main()
