from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfile
from quitter import Quitter
from Scrolledtext import ScrolledText


class SimpleEditor(ScrolledText):
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save', command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut', command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find', command=self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 9, 'normal'))
        self.filetypes = [('txt', '*.txt'), ('All files', '*')]

    def onSave(self):
        filename = asksaveasfile(filetype=self.filetypes)
        if filename:
            alltext = self.gettext()
            open(file=filename.name, mode='w').write(alltext)

    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def onFind(self):
        target = askstring('Edytor', 'wyszukaj')
        if target:
            where = self.text.search(target, INSERT, END)
            if where:
                print(where)
                pastit = where + ('+%dc' % len(target))
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()
    else:
        SimpleEditor().mainloop()
