import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
class TodoList(tk.Tk):
    count=1
    def __init__(self):
        self.win=tk.Tk()
        self.win.geometry("400x400")
        self.win.title("TodoList")
        self.win.resizable(0,0)
    def create_widgets(self):
        # Init StringVariables
        self.item=tk.StringVar()
        # Init Widgets 
        self.listbox=tk.Listbox(self.win,width=65)
        self.welcome_label=ttk.Label(self.win,text="Welcome To TodoList!")
        self.add_item_label=ttk.Label(self.win,text="Add Item :")
        self.add_item_entry=ttk.Entry(self.win,textvariable=self.item)
        self.add_item_button=ttk.Button(self.win,text="Add Item!",command=self.add_item)
        self.clear_list_button=ttk.Button(self.win,text="Clear List",command=self.clear_list)
        # Menu
        self.menu=tk.Menu(self.win)
        self.about=tk.Menu(self.menu,tearoff=False)
        self.about.add_command(label="About",command=self.help_window)
        # Pack Widgets
        self.welcome_label.pack()
        self.listbox.pack()
        self.add_item_label.pack()
        self.add_item_entry.pack()
        self.add_item_button.pack(pady=5)
        self.clear_list_button.pack(pady=5)
        # Config 
        self.win.config(menu=self.menu)
        self.menu.add_cascade(label="Help",menu=self.about)
        self.win.mainloop()
    def add_item(self):
        item=self.item.get()          
        if item:
            self.listbox.insert(tk.END,f"{self.count} : {item}")
            self.count+=1
        else:
            mbox.showerror("Error","Invalid Item Name")
    def clear_list(self):
        user_input=mbox.askyesno("Warning","Are You Sure Want To Clear TodoList?")
        if user_input:
            self.listbox.delete(0,tk.END)
        else:
            return
    def help_window(self):
        self.help=tk.Toplevel(self.win)
        self.help.title("About")
        self.help_text=tk.Text(self.help)
        self.help_text.pack(expand=True,fill=tk.BOTH)
        msg="""TodoList\nCopyright Abhimanyu Sharma\nCoded in 100% Pure Python, Using The Tkinter GUI Toolkit\nAlso Check Out My Other Softwares :\nVisit :\nhttps://angry-dijkstra-87d8ed.netlify.app/\nSource Code :\nhttps://github.com/N1nja0p/Todo-List-Tkinter"""
        self.help_text.insert(tk.END,msg)
        self.help_text.config(state=tk.DISABLED)
if __name__ == "__main__":
    app=TodoList()
    app.create_widgets()