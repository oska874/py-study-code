"""
Code illustration: 6.05

Adding Features of 'delete_object', 'fill_object', 'move_to_top', 'drag_item'

ATTRIBUTED ADDED HERE:
selected_objected

ATTRIBUTES MODIFIED HERE:
all_toolbar_functions (added 4 new items to the tuple- 'delete_object', 'fill_object', 'move_to_top', 'drag_item')


METHODS MODIFIED:
mouse_down


NEW METHODS ADDED:
fill_object
fill_object_options
delete_object
delete_object_options
move_to_top
move_to_top_options
drag_item
drag_item_update_xy
drag_item_options

Tkinter GUI Application Development Hotshot
""" 



from Tkinter  import *
import tkFileDialog
import tkMessageBox
import Image
import ImageTk
from tkColorChooser import askcolor

import ttk

import framework



class GUI(framework.GUIFramework):
    background = 'white'
    foreground = 'red'
    currentobject = None
    filename = 'untitled'
    currentobject = None
    startx = 0
    starty = 0
    lastx = 0
    lasty = 0
    all_toolbar_functions = ('draw_line', 'draw_rectangle', 'draw_oval', 'draw_brush', 'delete_object', 'fill_object', 'move_to_top', 'drag_item')
    selected_toolbar_func_index = 0 # draw_line
    arrow='none'
    width=1.0
    dash = None
    fill = 'red'
    outline = 'black'
    
    selected_objected        = None

    
    def __init__(self, root):
       self.root = root
       self.create_menu()
       self.create_top_bar()
       self.create_tool_bar()
       self.create_drawing_canvas()
    
    def delete_object(self,x0,y0,x1,y1):
        self.canvas.delete(self.selected_objected)
        
    
    def delete_object_options(self):
        pass
    

    def fill_object(self,x0,y0,x1,y1):
        if self.selected_objected == self.canvas:
            self.canvas.config(bg=self.fill)
        else:
            self.canvas.itemconfig(self.selected_objected, fill=self.fill)
        
    
    def fill_object_options(self):
        self.fill_options_combobox()



    
    def move_to_top(self,x0,y0,x1,y1):
        self.canvas.tag_raise(self.selected_objected)
        
        
    
    def move_to_top_options(self):
        pass
    
    
    def drag_item(self,x0,y0,x1,y1):
        if not self.all_toolbar_functions[self.selected_toolbar_func_index] == 'drag_item':
            self.canvas.bind( "<Button1-Motion>", self.mouse_down_motion)
            return
        self.currentobject = self.canvas.move(self.selected_objected, x1-x0,y1-y0)
        self.canvas.bind("<B1-Motion>", self.drag_item_update_xy)

        
    def drag_item_update_xy(self, event):
        self.startx, self.starty = self.lastx, self.lasty
        self.lastx, self.lasty = event.x, event.y
        self.drag_item(self.startx, self.starty,self.lastx, self.lasty)
    
    def drag_item_options(self):
        pass
        

     
    
    
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
        self.topbar = Frame(self.root, height=25, relief=RAISED)
        self.topbar.pack(fill=X,side=TOP, pady=2)
        
    
    def create_tool_bar(self):
        self.toolbar = Frame(self.root, width=50, relief=RAISED)
        self.toolbar.pack(fill=Y,side=LEFT, pady=3)
        self.create_tool_bar_buttons()
        self.create_color_pallete()
        self.curcoordlabel = Label(self.toolbar, text = 'x: 0  \ny: 0 ')
        self.curcoordlabel.grid(row=13, column=1, columnspan=2, pady=5, padx=1, sticky='w')

    def create_tool_bar_buttons(self):
        for i, item in enumerate(self.all_toolbar_functions):
            tbicon = PhotoImage(file='icons/'+item+'.gif')
            self.button = Button(self.toolbar, image=tbicon, command=lambda i=i: self.selected_tool_bar_item(i))
            self.button.grid(row=i/2, column=1+i%2, sticky='nsew')
            self.button.image = tbicon

    def selected_tool_bar_item(self, i):
            self.selected_toolbar_func_index = i
            self.remove_options_from_topbar()
            self.show_selected_tool_icon_in_topbar()
            opt = self.all_toolbar_functions[self.selected_toolbar_func_index]+'_options'
            fnc = getattr(self, opt)
            fnc()

                
    def create_color_pallete(self):
        self.colorpallete = Canvas(self.toolbar, height=55, width =55)
        self.colorpallete.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.backgroundpallete = self.colorpallete.create_rectangle(15, 15,48, 48,tags="backgroundpallete", outline=self.background, fill=self.background)
        self.foregroundpallete = self.colorpallete.create_rectangle(1, 1,33, 33,tags="foregroundpallete", outline=self.foreground, fill=self.foreground)
        self.colorpallete.tag_bind(self.backgroundpallete, "<Button-1>", self.set_background_color)
        self.colorpallete.tag_bind(self.foregroundpallete, "<Button-1>", self.set_foreground_color)
        
        
    def set_background_color(self, event=None):
        self.background = askcolor()[-1]
        try:self.set_fill()
        except:pass
        try:self.set_outline()
        except:pass
        self.colorpallete.itemconfig(self.backgroundpallete, outline=self.background, fill=self.background) 
    
    def set_foreground_color(self, event=None):
        self.foreground = askcolor()[-1]
        try:self.set_fill()
        except:pass
        try:self.set_outline()
        except:pass
        self.colorpallete.itemconfig(self.foregroundpallete,outline=self.foreground, fill=self.foreground) 
        

    def show_selected_tool_icon_in_topbar(self):
        Label(self.topbar,text='Selected Tool:').pack(side=LEFT)
        photo = PhotoImage(file='icons/'+self.all_toolbar_functions[self.selected_toolbar_func_index]+'.gif')
        label = Label(self.topbar, image=photo)
        label.image = photo 
        label.pack(side=LEFT)
    
    def remove_options_from_topbar(self):
        for child in self.topbar.winfo_children():
            child.destroy()        
        
    def width_options_combobox(self):
            Label(self.topbar,text='Width:').pack(side=LEFT)
            self.widthcmbobx = ttk.Combobox(self.topbar, state='readonly', width=3)
            self.widthcmbobx.pack(side=LEFT)
            self.widthcmbobx['values'] = (1.0, 2.0, 3.0,4.0,5.0,6.0,7.0,8.0,9.0, 10.0)
            self.widthcmbobx.bind('<<ComboboxSelected>>', self.set_width)
            self.widthcmbobx.set(self.width)

    def fill_options_combobox(self):
            Label(self.topbar,text='Fill:').pack(side=LEFT)
            self.fillcmbobx = ttk.Combobox(self.topbar, state='readonly', width=5)
            self.fillcmbobx.pack(side=LEFT)
            self.fillcmbobx['values'] = ('none', 'fg','bg', 'black', 'white' )
            self.fillcmbobx.bind('<<ComboboxSelected>>', self.set_fill)
            self.fillcmbobx.set(self.fill)
            
    def set_fill(self, event=None):
        fl = self.fillcmbobx.get()
        if fl == 'none': self.fill = '' #transparent
        elif fl == 'fg': self.fill = self.foreground
        elif fl == 'bg': self.fill = self.background
        else: self.fill = fl
            


    def outline_options_combobox(self):
            Label(self.topbar,text='Outline:').pack(side=LEFT)
            self.outlncmbobx = ttk.Combobox(self.topbar, state='readonly', width=5)
            self.outlncmbobx.pack(side=LEFT)
            self.outlncmbobx['values'] = ('none', 'fg','bg', 'black', 'white' )
            self.outlncmbobx.bind('<<ComboboxSelected>>', self.set_outline)
            self.outlncmbobx.set(self.outline)
            
    def set_outline(self, event=None):
        outln = self.outlncmbobx.get()
        if outln == 'none': self.outline = ''#transparent
        elif outln == 'fg': self.outline = self.foreground
        elif outln == 'bg': self.outline = self.background
        else: self.outline = outln




    def dash_options_combobox(self):
            Label(self.topbar,text='Dash:').pack(side=LEFT)
            self.dashcmbobx = ttk.Combobox(self.topbar, state='readonly', width=5)
            self.dashcmbobx.pack(side=LEFT)
            self.dashcmbobx['values'] = ('none','small', 'medium', 'large' )
            self.dashcmbobx.bind('<<ComboboxSelected>>', self.set_dash)
            self.dashcmbobx.current(0)

            
    def arrow_options_combobox(self):
            Label(self.topbar,text='Arrow:').pack(side=LEFT)
            self.arrowcmbobx = ttk.Combobox(self.topbar, state='readonly', width=5)
            self.arrowcmbobx.pack(side=LEFT)
            self.arrowcmbobx['values'] = ('none', 'first', 'last', 'both')
            self.arrowcmbobx.bind('<<ComboboxSelected>>', self.set_arrow)
            self.arrowcmbobx.current(0)
            
        
    
    def set_width(self, event):
        self.width = float(self.widthcmbobx.get())

    def set_arrow(self, event):
        self.arrow = self.arrowcmbobx.get()

    def set_dash(self, event):
        '''Dash takes value from 1 to 255'''
        if self.dashcmbobx.get() == 'none':
            self.dash = None
        elif self.dashcmbobx.get() == 'small':
            self.dash = 1
        elif self.dashcmbobx.get() == 'medium':
            self.dash = 15
        elif self.dashcmbobx.get() == 'large':
            self.dash = 255
        
   
    def draw_line_options(self):
            self.fill_options_combobox()
            self.width_options_combobox()
            self.arrow_options_combobox()
            self.dash_options_combobox()  

    def draw_rectangle_options(self):
        self.fill_options_combobox()
        self.outline_options_combobox()
        self.width_options_combobox()

         
    def draw_oval_options(self):
        self.fill_options_combobox()
        self.outline_options_combobox()
        self.width_options_combobox()

         
    def draw_brush_options(self):
        self.fill_options_combobox()
        self.width_options_combobox()
        
    
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
        self.canvas.bind( "<Button-1>", self.mouse_down)
        self.canvas.bind( "<Button1-Motion>", self.mouse_down_motion)
        self.canvas.bind( "<Button1-ButtonRelease>", self.mouse_up)
        self.canvas.bind( "<Motion>", self.show_current_coordinates)
        
    
    def mouse_down(self, event):
        self.currentobject = None
        self.lastx = self.startx = self.canvas.canvasx(event.x)
        self.lasty = self.starty = self.canvas.canvasy(event.y)
        if self.all_toolbar_functions[self.selected_toolbar_func_index] in ['fill_object', 'delete_object', 'move_to_top', 'drag_item']: # work on selected objected
            try:
                self.selected_objected = self.canvas.find_closest(self.startx,self.starty)[0]
            except:
                self.selected_objected = self.canvas

 
    def mouse_down_motion(self, event):
        self.lastx = self.canvas.canvasx(event.x)
        self.lasty = self.canvas.canvasy(event.y)
        if self.selected_toolbar_func_index:
            self.canvas.delete(self.currentobject)
            self.execute_method()
            

    def mouse_up(self, event):
        self.lastx = self.canvas.canvasx(event.x)
        self.lasty = self.canvas.canvasy(event.y)
        self.canvas.delete(self.currentobject)
        self.currentobject = None
        self.execute_method()
        

    def execute_method(self):
        fnc = getattr(self,self.all_toolbar_functions[self.selected_toolbar_func_index])
        fnc(self.startx, self.starty,self.lastx, self.lasty)


        
    def show_current_coordinates(self, event=None):
        lx = self.canvas.canvasx(event.x)
        ly = self.canvas.canvasy(event.y)
        cord =  'x: %d \ny: %d '%(lx, ly)
        self.curcoordlabel.config(text=cord)

    
   

    def draw_line(self, x, y, x2, y2):
        self.currentobject = self.canvas.create_line(x,y,x2,y2,fill= self.fill, arrow=self.arrow, width=self.width, dash=self.dash )
    
    
    def draw_rectangle(self, x, y, x2, y2):
        self.currentobject = self.canvas.create_rectangle(x, y,x2, y2, outline=self.outline, fill=self.fill, width=self.width)



    def draw_oval(self, x, y, x2, y2):
        self.currentobject =  self.canvas.create_oval(x, y, x2, y2,outline=self.outline, fill=self.fill, width=self.width)


    
    def draw_brush(self, x, y, x2, y2):
        if not self.all_toolbar_functions[self.selected_toolbar_func_index] == 'draw_brush':
            self.canvas.bind( "<Button1-Motion>", self.mouse_down_motion)
            return
        self.currentobject = self.canvas.create_line(x,y,x2,y2,fill=self.fill, width=self.width)

        self.canvas.bind("<B1-Motion>", self.draw_brush_update_xy)
    
 
    def draw_brush_update_xy(self, event):
        self.startx, self.starty = self.lastx, self.lasty
        self.lastx, self.lasty = event.x, event.y
        self.draw_brush(self.startx, self.starty,self.lastx, self.lasty)    
    
    
    
    
    
        
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
