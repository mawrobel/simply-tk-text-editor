from tkinter import *


class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        mybar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        mybar.config(command=text.yview)
        text.config(yscrollcommand=mybar.set)
        mybar.pack(side=RIGHT, fill=BOTH)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file=file, mode='r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def gettext(self):
        return self.text.get('1.0', END + '-1c')


if __name__ == "__main__":
    root = Tk()
    if len(sys.argv) > 1:
        root.title(sys.argv[1])
        st = ScrolledText(file=sys.argv[1])
    else:
        root.title("Lorem")
        st = ScrolledText(file='Lorem')


    def show(event):
        print(str(st.gettext()))


    root.bind('<Key-Escape>', show)

    root.mainloop()
