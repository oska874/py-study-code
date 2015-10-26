"""
Code illustration: 7.01

Screensaver

Tkinter GUI Application Development Hotshot
""" 


from Tkinter import *
from random import randint

# A class to generate balls with random attributes

class RandomBall:
    
    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas
        self.xpos = randint(10,int(scrnwidth))
        self.ypos = randint(10,int(scrnheight))
        self.xvelocity = randint(6,12)
        self.yvelocity = randint(6,12)
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.radius = randint(40,70)
        r = lambda: randint(0,255)### create a random number from 0-255
        self.color = '#%02x%02x%02x' % (r(),r(),r())
        

    def create_ball(self):
        x1 = self.xpos-self.radius
        y1 = self.ypos-self.radius
        x2 = self.xpos+self.radius
        y2 = self.ypos+self.radius
        self.itm = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color,outline=self.color)
        


    def move_ball(self):
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        if self.ypos >= self.scrnheight - self.radius:
           self.yvelocity = -self.yvelocity # change direction

        if self.ypos <= self.radius :
            self.yvelocity = abs(self.yvelocity)

        if self.xpos >= self.scrnwidth- self.radius or self.xpos <= self.radius:
            self.xvelocity = -self.xvelocity

        self.canvas.move(self.itm, self.xvelocity, self.yvelocity)



# Now our Screen Saver Program
class ScreenSaver:
    balls = []
    
    def __init__(self, num_balls):
        self.root = Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-alpha', 0.3)
        self.root.bind('<Any-KeyPress>', quit)
        self.root.bind('<Any-Button>', quit)
        self.root.bind('<Motion>', quit)
        self.canvas = Canvas(self.root, width=w, height=h)
        self.canvas.pack()
        for i in range(num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(20, self.run_screen_saver)

    def quit(self, event):
        self.root.destroy()



if __name__ == "__main__":
    ScreenSaver(18)  ##18 is the number of balls
    
