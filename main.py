import customtkinter
from PIL import Image

import customtkinter


class Det(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Use relheight and relwidth for placement
        self.date = customtkinter.CTkLabel(self, text='Tuesday 15 October')
        self.date.place(relx=0.05, relwidth=0.9)  # 90% width, 5% padding from left

        self.time = customtkinter.CTkLabel(self, text='19:00',)
        self.time.place(relx=0.05,  relwidth=0.9,rely=0.2)  # Positioned below the date

        self.price = customtkinter.CTkLabel(self, text='$234', font=("System", 14))
        self.price.place(relx=0.05, relwidth=0.9,rely=0.35)  # Positioned below the time

        self.book = customtkinter.CTkButton(self, text='Book')
        self.book.configure(fg_color='#B99EFF', text_color='#190745')
        self.book.place(relx=0.05,rely=0.63,relheight=0.3,  relwidth=0.9)  # Positioned below the price, book button takes 15% height




class Flight(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Use relheight and relwidth for placement
        self.fro = customtkinter.CTkLabel(self, text='DXB')
        self.fro.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.8)  # Takes 25% width and 80% height

        self.details = Det(master=self, fg_color='#3603B7')
        self.details.place(relx=0.35, rely=0.045, relwidth=0.35, relheight=0.94)  # 35% width, placed in the middle

        self.tor = customtkinter.CTkLabel(self, text='SHJ')
        self.tor.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.8)  # Positioned on the right with 25% width



class FlightsContainer(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Use relheight and relwidth for the container
        self.headlabel = customtkinter.CTkLabel(self, text='Flights', font=('System', 24))
        self.headlabel.place(relx=0.05, rely=0.05, relwidth=0.9)  # Positioned at the top with 90% width

        # Loop through multiple flights and place them using relheight/relwidth
        for i in range(3):
            self.flight = Flight(master=self)
            self.flight.configure(fg_color='#6E39F6', corner_radius=14)
            self.flight.place(relx=0.05, rely=0.2 + i * 0.25, relwidth=0.9,
                              relheight=0.23)  # Position each flight below the previous


# Create the main window
root = customtkinter.CTk()
root.geometry("600x600")

# Create the Flights container
flights_container = FlightsContainer(master=root)
flights_container.place(relx=0, rely=0, relwidth=1, relheight=1)  # Take up the full window size

root.mainloop()


class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.logo_img = customtkinter.CTkImage(light_image=Image.open('img.png'),size=(100,100))
        self.label = customtkinter.CTkLabel(self , image=self.logo_img, text='')
        self.label.grid(row=0, column=0, padx=20,sticky='nsew')
        self.flightFram = Flightscontainer(master = self)
        self.flightFram.configure(fg_color='transparent' )
        self.flightFram.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.configure(fg_color='#23094f')
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bind("<Configure>", self.resize_font)

    def resize_font(self, event):
        # Dynamically calculate the font size based on window dimensions
        window_width = event.width
        window_height = event.height

        # Adjust the font size based on window size (choose a scaling factor)
        new_font_size = int(min(window_width, window_height) / 20)

        # Apply the new font size to the label
        self.label.configure(font=("Arial", new_font_size))


    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()