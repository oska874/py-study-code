"""
Code illustration: 6.01

Creating the Overall Structure for our Drawing Program

Tkinter GUI Application Development Hotshot
""" 



from Tkinter  import *
import tkFileDialog
import tkMessageBox
import Image
import ImageTk
from tkColorChooser import askcolor
import framework


class GUI(framework.GUIFramework):
    background = 'white'
    foreground = 'red'
    currentobject = None
    filename = 'untitled'
    
    def __init__(self, root):
       self.root = root
       self.create_menu()
       self.create_top_bar()
       self.create_tool_bar()
       self.create_drawing_canvas()
       
    
    def create_menu(self):
        self.menubar = Menu(self.root)
        self.menuitems = (
                       'File- &New/Ctrl+N/self.new_file, &Open/Ctrl+O/self.open_file, Save/Ctrl+S/self.save, SaveAs//self.save_as, Sep, Exit/Alt+F4/self.close', 
                       'Edit- Undo/Ctrl+Z/self.undo, Sep',
                       'About- About//self.about'
                       )
        self.build_menu()
        self.root.config(menu=self.menubar)
    
    def create_top_bar(self):
        self.topbar = Frame(self.root, height=25, relief=RAISED, bg='yellow')
        self.topbar.pack(fill=X,side=TOP, pady=2)
        
    
    def create_tool_bar(self):
        self.toolbar = Frame(self.root, width=50, relief=RAISED, bg='grey')
        self.toolbar.pack(fill=Y,side=LEFT, pady=3)
        self.create_tool_bar_buttons()
        self.create_color_pallete()
        self.curcoordlabel = Label(self.toolbar, text = 'x: 0  \ny: 0 ')
        self.curcoordlabel.grid(row=13, column=1, columnspan=2, pady=5, padx=1, sticky='w')

    def create_tool_bar_buttons(self):
        for i in range(8):
            self.button = Button(self.toolbar, text=i, command=lambda i=i: self.selected_tool_bar_item(i))
            self.button.grid(row=i/2, column=1+i%2, sticky='nsew')

    def selected_tool_bar_item(self, i):
        print 'You selected {}'.format(i)
              
    def create_color_pallete(self):
        self.colorpallete = Canvas(self.toolbar, height=55, width =55)
        self.colorpallete.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.backgroundpallete = self.colorpallete.create_rectangle(15, 15,48, 48,tags="backgroundpallete", outline=self.background, fill=self.background)
        self.foregroundpallete = self.colorpallete.create_rectangle(1, 1,33, 33,tags="foregroundpallete", outline=self.foreground, fill=self.foreground)
        self.colorpallete.tag_bind(self.backgroundpallete, "<Button-1>", self.set_background_color)
        self.colorpallete.tag_bind(self.foregroundpallete, "<Button-1>", self.set_foreground_color)
        
        
    def set_background_color(self, event=None):
        self.background = askcolor()[-1]
        self.colorpallete.itemconfig(self.backgroundpallete, outline=self.background, fill=self.background) 
    
    def set_foreground_color(self, event=None):
        self.foreground = askcolor()[-1]
        self.colorpallete.itemconfig(self.foregroundpallete,outline=self.foreground, fill=self.foreground) 
        
        
    
    
    
    def create_drawing_canvas(self):
        cnvsframe=Frame(self.root,width=900,height=900)
        cnvsframe.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.canvas = Canvas(cnvsframe, background="white", width=500,height=500,scrollregion=(0,0,800,800))
        hbar=Scrollbar(cnvsframe,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(cnvsframe,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=RIGHT, expand=YES, fill=BOTH)

        
    def new_file(self):
        self.canvas.delete(ALL)
        self.root.title('untitled')
    
    def open_file(self):
        self.filename = tkFileDialog.askopenfilename(master = self.root,
                                   filetypes = [('All Files',('*.jpg', '*.png', '*.tif', '*.gif')),
                                                ('jpeg','*.jpg'),('png','*.png'),('tiff','*.tif'), ('gif','*.gif')],title="Open...")
        if not self.filename: return
        self.root.title(self.filename)
        self.img = Image.open(self.filename)
        self.image = ImageTk.PhotoImage(self.img)
        self.currentobject = self.canvas.create_image(10, 10, anchor=NW, image=self.image)
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))


    
    def undo(self, event=None):
        self.canvas.delete(self.currentobject)
    
    
    def save(self):
        if self.filename == 'untitled':
            self.save_as()
        else:
            self.actual_save()
            

    def save_as(self):
        try:
            self.filename = tkFileDialog.asksaveasfilename(master = self.root,filetypes = [('All Files',('*.ps', '*.ps'))], title="Save...")
        except:pass
        self.actual_save()
        
    def actual_save(self):    
        self.canvas.postscript(file=self.filename, colormode='color')
        self.root.title(self.filename)

    def about(self, event=None):
        tkMessageBox.showinfo("About","Tkinter GUI Application\n Development Hotshot")


    def close(self, event=None):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()



if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
