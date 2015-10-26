"""
Code illustration: 9.01
Demo of Available Cursors

Tkinter GUI Application Development Hotshot
""" 


from Tkinter import *

all_cursors = ['X_cursor' , 'arrow' , 'based_arrow_down' , 'based_arrow_up' , 
               'boat' , 'bogosity' , 'bottom_left_corner' , 'bottom_right_corner' , 
               'bottom_side' , 'bottom_tee' , 'box_spiral' , 'center_ptr' , 'circle' ,
                'clock' , 'coffee_mug' , 'cross' , 'cross_reverse' , 'crosshair' , 
                'diamond_cross' , 'dot' , 'dotbox' , 'double_arrow' , 'draft_large', 
                'draft_small' , 'draped_box' , 'exchange' , 'fleur' , 'gobbler' , 
                'gumby' , 'hand1' , 'hand2' , 'heart' , 'icon' , 'iron_cross' , 
                'left_ptr' , 'left_side' , 'left_tee' , 'leftbutton' , 'll_angle' ,
                 'lr_angle' , 'man' , 'middlebutton' , 'mouse' , 'pencil' , 'pirate' , 
                 'plus' , 'question_arrow' , 'right_ptr' , 'right_side' , 'right_tee' ,
                    'rightbutton' , 'rtl_logo' , 'sailboat' , 'sb_down_arrow' , 
                    'sb_h_double_arrow' , 'sb_left_arrow' , 'sb_right_arrow' , 
                    'sb_up_arrow' , 'sb_v_double_arrow' , 'shuttle' , 'sizing' ,
                     'spider' , 'spraycan' , 'star' , 'target' , 'tcross' , 
                     'top_left_arrow' , 'top_left_corner' , 'top_right_corner' , 
                     'top_side' , 'top_tee' , 'trek' , 'ul_angle' , 'umbrella' ,
                      'ur_angle' , 'watch' , 'xterm']


root= Tk()
root.title('Hover Over White Area for Cursor Sample')
for i, item in enumerate(all_cursors):
    r, c = i % 10, i // 10 * 2
    Label(text=item).grid(row=r, column=c)
    Label(width=3, height=3, cursor=item, bg='white').grid(row=r, column=c+1)
root.mainloop()