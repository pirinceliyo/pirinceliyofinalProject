from tkinter import*
from typing import Optional, Tuple, Union
from customtkinter import*
from PIL import Image
import customtkinter


class PrintRecipe(CTkToplevel):
       def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="your recipe")
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky=EW)
      




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
      #frame price
      priceFrame = CTkFrame(self.frame_one, width=200)
      priceFrame.grid(row=3, column=4, sticky=NSEW, columnspan=3, rowspan=3, padx=10)
      #frame price element
      CTkLabel(priceFrame, text="Pricing").grid(row=0, column=1, sticky=EW, padx=30, pady=5)
      CTkLabel(priceFrame, text="Pizza:").grid(row=1, column=0 , sticky=W, padx=10, pady=5 )
      CTkLabel(priceFrame, text="Small pizza").grid(row=2, column=0 , sticky=W, padx=10, pady=5)
     
      self.pricesmall =CTkLabel(priceFrame, text="9.88")
      self.pricesmall.grid(row=2, column=1 , sticky=W, padx=10, pady=5)
      CTkLabel(priceFrame, text="Meduim pizza:").grid(row=3, column=0 , sticky=W, padx=10, pady=5)
      pricemeduim = CTkLabel(priceFrame, text="9.88")
      pricemeduim.grid(row=3, column=1 , sticky=W, padx=10, pady=5)
      CTkLabel(priceFrame, text="Large pizza:").grid(row=4, column=0 , sticky=W, padx=10, pady=5)
      pricelarge = CTkLabel(priceFrame, text="10.88")
      pricelarge.grid(row=4, column=1 , sticky=W, padx=10, pady=5)

      CTkLabel(priceFrame, text="Topping:").grid(row=1, column=5, sticky=EW, padx=5, pady=2)
      CTkLabel(priceFrame, text="Pepperoni:").grid(row=2, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="0.75").grid(row=2, column=6 , sticky=W, padx=5, pady=5)
      CTkLabel(priceFrame, text="Mushrooms").grid(row=3, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="1.00").grid(row=3, column=6 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="Onions:").grid(row=4, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="0.50").grid(row=4, column=6 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="Green peppers:").grid(row=5, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="0.75").grid(row=5, column=6 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="Baccon:").grid(row=6, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="0.65").grid(row=6, column=6 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="Beef:").grid(row=7, column=5 , sticky=W, padx=5, pady=2)
      CTkLabel(priceFrame, text="1.50").grid(row=7, column=6 , sticky=W, padx=5, pady=2)

       #name entry
      self.name = CTkEntry(self.frame_one, width=200, height=30, placeholder_text="customer name")
      self.name.grid(row=1, column=5,sticky="WE", padx=10,pady=20)
       # Pizza size options
      CTkLabel(self.frame_one, text="Pizza Size : ", padx=10).grid(row=2, column=0,sticky="w") 
      img1 = CTkImage(Image.open("images/Samall_pizza.png"),size=(150, 150))
      img2 = CTkImage(Image.open("images/Large_pizza.png"),size=(180, 180))
      img3 = CTkImage(Image.open("images/Large_pizza.png"),size=(200, 200))

      CTkLabel(self.frame_one, image=img1,text="").grid(row=3, column=0,pady=0,padx=(10,10),sticky=W)
      CTkLabel(self.frame_one, image=img2,text="").grid(row=3, column=1,pady=(0,30),padx=(0,10),sticky=W)
      CTkLabel(self.frame_one, image=img3,text="").grid(row=3, column=2,pady=(0,50),padx=(0,10),sticky=W) 
      
      self.size_var = StringVar(value="medium")
      CTkRadioButton(self.frame_one, text="Small", variable=self.size_var, value="small").grid(row=4, column=0,pady=0,padx=(10,10),sticky=NW)
      CTkRadioButton(self.frame_one, text="Medium", variable=self.size_var, value="medium").grid(row=4, column=1,pady=0,padx=(0,10),sticky=NW)
      CTkRadioButton(self.frame_one, text="Large", variable=self.size_var, value="large").grid(row=4, column=2,pady=0,padx=(0,10),sticky=NW)

      # Toppings options
      self.toppings = ["Pepperoni", "Mushrooms", "Onions", "Green Peppers", "Bacon", "Beef"]
      self.toppings_vars = []
      CTkLabel(self.frame_one, text="Toppings:").grid(row=5, column=0,sticky=W, padx=10, pady=(10,0))
      img1 = CTkImage(Image.open("images/pepperonoi.JPG"),size=(200,100))
      img2 = CTkImage(Image.open("images/mushrooms.JPG"),size=(200,100))
      img3 = CTkImage(Image.open("images/onion.JPG"),size=(200,100))
      img4 = CTkImage(Image.open("images/greenpepper.JPG"),size=(200,100))
      img5 = CTkImage(Image.open("images/bacon.JPG"),size=(200,100))
      img6 = CTkImage(Image.open("images/beef.JPG"),size=(200,100))

      CTkLabel(self.frame_one, image=img1,text="").grid(row=6, column=0,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img2,text="").grid(row=6, column=1,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img3,text="").grid(row=6, column=2,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img4,text="").grid(row=6, column=3,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img5,text="").grid(row=6, column=4,sticky=EW,pady=(10,0),padx=10)
      CTkLabel(self.frame_one, image=img6,text="").grid(row=6, column=5,sticky=EW,pady=(10,0),padx=10)
      #
      for i in range(len(self.toppings)):
         var = IntVar(value=0)
         self.toppings_vars.append(var)

         customtkinter.CTkCheckBox (self.frame_one, text=self.toppings[i], variable=self.toppings_vars[i]).grid(row=7, column= i, sticky="we",padx=10, pady=10)
       #submit button
      CTkButton(self.frame_one, text="Submit Order", command=self.submit).grid(row=8, column=0, sticky=SW, padx=10,pady=10)  
      CTkButton(self.frame_one, text="Quit", command= self.destroy, fg_color="red",font=("Arial", 14, 'bold')).grid(row=8, column=5, sticky=SE, padx=10,pady=10)  

      # Frame number 2
      self.frame_two = CTkFrame(self,width= 300)
      self.frame_two.grid_columnconfigure(0, weight=1)
 

      self.frame_two.grid(row=0, column=1, sticky=(NSEW), pady=20, padx=10)
      CTkLabel(self.frame_two,text="your order", font=('Courier', 18, 'bold'),justify=CENTER).grid(row=0, column=0,sticky=(EW),pady=10, padx=30)

      self.toplevel_window = None

     
     
      #Submit button
   def submit(self):
         customer_name = self.name.get()
         size = self.size_var.get()
         selected_toppings = [ self.toppings[i] for i in range(len(self.toppings)) if  self.toppings_vars[i].get() == 1]
         prints_name =CTkLabel(self.frame_two, text=f"{customer_name}")
         prints_name.grid(row=1,column=0, padx=10,pady=10, sticky="ew")
         note =CTkLabel(self.frame_two, text=f"your order is: ")
         note.grid(row=2, column=0, sticky=W, padx=10)
         print_pizza_size = CTkLabel(self.frame_two,text=f"Pizza Size: {size}")
         print_pizza_size.grid(row=3, column=0, sticky=W, padx=10)

         print_toppins = CTkLabel(self.frame_two,text=f"Topping List: {', '.join( selected_toppings)}")
         print_toppins.grid(row=4, column=0, sticky=EW, padx=10)

         CTkButton(self.frame_two, text="Print recipe", command= self.open_print).grid(row=6, column=0, sticky=EW, pady=10, padx=10)

   
   def open_print(self):
      size = self.size_var.get()
      if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = PrintRecipe(self)  # create window if its None or destroyed
      else:
            self.toplevel_window.focus()  # if window exists focus it

     

           
           
   
     
   
     







app = App('Pizza Order')
app.resizable(True, True)
app.mainloop()