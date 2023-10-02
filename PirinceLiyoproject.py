from tkinter import*
from typing import Optional, Tuple, Union
from customtkinter import*
from PIL import Image
import customtkinter



class first_frame(CTkFrame):
   def __init__(self, master, width, title):
      super().__init__(master,width )
      self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
    
      CTkLabel(self,text=title, font=('Courier', 18, 'bold'),justify=CENTER).grid(row=0, column=2,sticky=(NSEW),columnspan=2,pady=10)

      CTkLabel(self, text="Menu : ", padx=10).grid(row=1, column=0,sticky="w")

      CTkLabel(self, text="Customer Name" ).grid(row=1, column=4,sticky="we",pady=20 )   


#Main App Class
class App(CTk):
   def __init__(self, title ):
      super().__init__()
      self.title(title)    
       #set the theme of the app
      customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
       #set the appearance mode
      customtkinter.set_appearance_mode("system")  # default
      self.geometry()
      #config grid layout on the window
      self.grid_columnconfigure((0,1), weight=1)
      self.grid_rowconfigure(0,weight=1)
     

      self.frame_one = first_frame(self, 300, "Place Pizza Order")
      self.frame_one.grid(row=0, column=0, sticky=(NSEW), padx=10, pady=20)
       #name entry
      self.name = CTkEntry(self.frame_one, width=200, height=30, placeholder_text="customer name")
      self.name.grid(row=1, column=5,sticky="WE", padx=10,pady=20)
       # Pizza size options
      CTkLabel(self.frame_one, text="Pizza Size : ", padx=10).grid(row=2, column=0,sticky="w") 
      img1 = CTkImage(Image.open("images/Samall_pizza.png"),size=(150, 150))
      img2 = CTkImage(Image.open("images/Large_pizza.png"),size=(180, 180))
      img3 = CTkImage(Image.open("images/Large_pizza.png"),size=(200, 200))

      CTkLabel(self.frame_one, image=img1).grid(row=3, column=0,pady=0,padx=(10,10),sticky=W)
      CTkLabel(self.frame_one, image=img2).grid(row=3, column=1,pady=(0,30),padx=(0,10),sticky=W)
      CTkLabel(self.frame_one, image=img3).grid(row=3, column=2,pady=(0,50),padx=(0,10),sticky=W) 
      
      self.size_var = StringVar(value="medium")
      CTkRadioButton(self.frame_one, text="Small", variable=self.size_var, value="small").grid(row=4, column=0,pady=0,padx=(10,10),sticky=NW)
      CTkRadioButton(self.frame_one, text="Medium", variable=self.size_var, value="medium").grid(row=4, column=1,pady=0,padx=(0,10),sticky=NW)
      CTkRadioButton(self.frame_one, text="Large", variable=self.size_var, value="large").grid(row=4, column=2,pady=0,padx=(0,10),sticky=NW)

      # Toppings options
      self.toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Beef"]
      self.toppings_vars = []
      CTkLabel(self.frame_one, text="Toppings:").grid(row=5, column=0,sticky=W, padx=10, pady=(10,0))
      img1 = CTkImage(Image.open("images/Samall_pizza.png"),size=(200,100))
      img2 = CTkImage(Image.open("images/Large_pizza.png"),size=(200,100))
      img3 = CTkImage(Image.open("images/Large_pizza.png"),size=(200,100))
      img4 = CTkImage(Image.open("images/Samall_pizza.png"),size=(200,100))
      img5 = CTkImage(Image.open("images/Large_pizza.png"),size=(200,100))
      img6 = CTkImage(Image.open("images/Large_pizza.png"),size=(200,100))

      CTkLabel(self.frame_one, image=img1).grid(row=6, column=0,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img2).grid(row=6, column=1,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img3).grid(row=6, column=2,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img4).grid(row=6, column=3,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img5).grid(row=6, column=4,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img6).grid(row=6, column=5,sticky=EW,pady=(10,0),padx=10)
      #
      for i in range(len(self.toppings)):
         var = IntVar(value=0)
         self.toppings_vars.append(var)

         customtkinter.CTkCheckBox (self.frame_one, text=self.toppings[i], variable=self.toppings_vars[i]).grid(row=7, column= i, sticky="we",padx=10, pady=10)
       #submit button
      CTkButton(self.frame_one, text="Submit Order", command=self.submit).grid(row=8, column=0, sticky=SW, padx=10,pady=10)  

      # Frame number 2
      self.frame_two = CTkScrollableFrame(self,width= 300)
      self.frame_two.grid_columnconfigure(0, weight=1)

      self.frame_two.grid(row=0, column=1, sticky=(NSEW), pady=20)
      CTkLabel(self.frame_two,text="your order", font=('Courier', 18, 'bold'),justify=CENTER).grid(row=0, column=0,sticky=(NSEW),pady=10)
     
      #Submit button
   def submit(self):
         customer_name = self.name.get()
         size = self.size_var.get()
         selected_toppings = [ self.toppings[i] for i in range(len(self.toppings)) if  self.toppings_vars[i].get() == 1]
         prints_name =CTkLabel(self.frame_two, text=f"{customer_name}")
         prints_name.grid(row=1,column=0, padx=10,pady=10, sticky="ew")
         note =CTkLabel(self.frame_two, text=f"your order is: ")
         note.grid(row=2, column=0, sticky=W)
         print_pizza_size = CTkLabel(self.frame_two,text=f"Pizza Size: {size}")
         print_pizza_size.grid(row=3, column=0, sticky=W)

         print_toppins = CTkLabel(self.frame_two,text=f"Topping List: pizza with toppings: {', '.join( selected_toppings)}", wraplength=100)
         print_toppins.grid(row=4, column=0, sticky=W)

        
   
     
   
     







app = App('Pizza Order')
app.mainloop()