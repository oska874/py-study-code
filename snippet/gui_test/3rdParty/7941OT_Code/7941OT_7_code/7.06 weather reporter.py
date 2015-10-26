"""
Code illustration: 7.06

Weather Reporter

Tkinter GUI Application Development Hotshot
""" 
# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import urllib
import datetime
import json
from PIL import ImageTk
import tkMessageBox

class WeatherReporter:
    def __init__(self, root):
        self.root = root
        self.top_frame()
        self.display_frame()
        
    def top_frame(self):
        topfrm = Frame(self.root)
        topfrm.grid(row=1, sticky='w')
        Label(topfrm, text='Enter Location').grid(row=1, column=2, sticky='w')
        self.enteredlocation = StringVar()
        Entry(topfrm, textvariable=self.enteredlocation).grid(row=1, column=3, sticky='w')
        ttk.Button(topfrm, text='Show Weather Info', command= self.show_weather_button_clicked).grid(row=1, column=4, sticky='w')
        
    def display_frame(self):
        displayfrm = Frame(self.root)
        displayfrm.grid(row=2, sticky='ew', columnspan=5)
        self.canvas = Canvas(displayfrm, height='410', width='300', background='black', borderwidth=5)
        self.canvas.create_rectangle( 5, 5,305,415, fill='#F6AF06')  
        self.canvas.grid(row=2, sticky='w', columnspan=5)
    
    def show_weather_button_clicked(self):
        if not self.enteredlocation.get():
            return
        self.canvas.delete(ALL)
        self.canvas.create_rectangle( 5, 5,305,415, fill='#F6AF06')  
        data = self.get_weather_data()
        data =self.json_to_dict(data)
        self.display_final(data)

        
    def display_final(self, data):
        try:
            data['name']
        except:
            tkMessageBox.showerror('Name not found', 'Unable to fetch record - Name not found') 
            return
        self.canvas.create_text( 30, 30, text=data['name'], fill='white', font="Purisa 16", anchor=NW) 
        self.canvas.create_text( 245, 35, text='Latitude :  '+'%.3f'%(float(data['lat'])), fill='white', font="Purisa 10")  
        self.canvas.create_text( 245, 53, text='Longitude: '+ '%.3f'%(float(data['lon'])), fill='white', font="Purisa 10")  
        self.canvas.create_text( 30, 50, text='Country : '+ str(data['country']), fill='white', font="Purisa 10", anchor=NW)
        self.canvas.create_text( 155, 80, text=self.time_stamp_to_data(data['dt']), fill='white', font="Purisa 10") 
        
        self.canvas.create_text( 85,105, text='NOW', fill='white', font="Purisa 14")
        iconname = "weatherimages/%s.png" %data['icon'].lower()
        self.img = ImageTk.PhotoImage(file=iconname)
        self.canvas.create_image( 140, 105, image=self.img)  
        
        self.canvas.create_text( 220, 105, text=data['description'], fill='white', font="Purisa 8") 
        
        #temperature
        tempr = float(data['temp'])/10.0
        self.canvas.create_text( 85,155, text='Temperature', fill='white', font="Purisa 14")
        self.canvas.create_text( 87,175, text=str('%.2f'%(float(data['temp_min'])/10.0))+u' \u2103'.encode('utf-8')+ ' ~ ' + str('%.2f'%(float(data['temp_max'])/10.0))+u' \u2103'.encode('utf-8'), fill='white', font="Purisa 9")
        self.canvas.create_text( 225, 140, text=str(tempr)+u' \u2103'.encode('utf-8'), fill='white', font="Purisa 18") #celcius
        self.canvas.create_text( 225, 180, text=str(self.celcius_to_fahrenheit(tempr))+u' \u2109'.encode('utf-8'), fill='white', font="Purisa 18") #fahrenheit
        
        #humidity
        self.canvas.create_text( 95,215, text='Relative Humidity', fill='white', font="Purisa 12")
        self.canvas.create_text( 198, 215, text=data['humidity']+' %' ,fill='white', font="Purisa 12") #rh
        
        #Wind Speed
        self.canvas.create_text( 77,235, text='Wind Speed', fill='white', font="Purisa 12")
        self.canvas.create_text( 205, 235, text=data['speed']+' m/s ' ,fill='white', font="Purisa 12") #rh
        #Wind Degree
        self.canvas.create_text( 80,255, text='Wind Degree', fill='white', font="Purisa 12")
        self.canvas.create_text( 223, 255, text=data['deg']+' degrees' ,fill='white', font="Purisa 12") #rh
        
        #atmoshpheric pressure
        self.canvas.create_text( 80,275, text='Pressure(at.)', fill='white', font="Purisa 12")
        self.canvas.create_text( 225, 275, text=data['pressure']+' millibars' ,fill='white', font="Purisa 12") #rh
        
        #rain in last 3 hours
        if data.has_key('3h'):
            self.canvas.create_text( 83,293, text='Rain (Last 3h)', fill='white', font="Purisa 12")
            self.canvas.create_text( 200, 293, text=data['3h']+' mm' ,fill='white', font="Purisa 12") #rain
        
        #clouds
        self.canvas.create_text( 58,310, text='Clouds', fill='white', font="Purisa 12")
        self.canvas.create_text( 200, 310, text=data['all']+' %' ,fill='white', font="Purisa 12") #clouds
        
        #sunrise
        self.canvas.create_text( 60,328, text='Sunrise', fill='white', font="Purisa 12")
        self.canvas.create_text( 200, 328, text=self.time_stamp_to_time(data['sunrise']) ,fill='white', font="Purisa 12") 
        
        #sunsettime_stamp_to_data
        self.canvas.create_text( 59,343, text='Sunset', fill='white', font="Purisa 12")
        self.canvas.create_text( 200, 343, text=self.time_stamp_to_time(data['sunset']) ,fill='white', font="Purisa 12") 

        
    def time_stamp_to_time(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S'))        
        #poweredby Openweather.org
        self.canvas.create_text( 159,378, text='Powered by:', fill='white', font="Purisa 12")
        self.canvas.create_text( 159,398, text='www.openweathermap.org', fill='white', font="Purisa 12")

        
    def time_stamp_to_data(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S'))
        
    def celcius_to_fahrenheit(self, c):
         return (float(c) * 9.0/5) + 32
        
        
    
    
    def get_weather_data(self):
        try:
            apiurl = 'http://api.openweathermap.org/data/2.5/weather?q=%s'%self.enteredlocation.get()
            data =  urllib.urlopen(apiurl)
            jdata= data.read()
            return jdata
        except IOError as e:
             tkMessageBox.showerror('Unable to connect', 'Unable to connect %s'%e) 
            
        
    def json_to_dict(self, jdata):
        mydecoder = json.JSONDecoder()
        decodedjdata = mydecoder.decode(jdata)
        flatteneddict = {}
        for key, value in decodedjdata.items():
            if key == 'weather':
                for ke,va in value[0].items():
                        flatteneddict[str(ke)] = str(va).upper() 
                continue
            try:
                for k,v in value.items():
                        flatteneddict[str(k)] = str(v).upper()
            except:
                flatteneddict[str(key)] = str(value).upper()
        return flatteneddict       
    

        





def main():
    root=Tk()
    WeatherReporter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()