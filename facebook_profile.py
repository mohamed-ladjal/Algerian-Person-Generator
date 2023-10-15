import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import csv
import random
import os


class UserInterface:
    
    def __init__(self, master):
        root.geometry("600x400")
        self.master = master
        master.title("User Information")
        self.first_name = ""
        self.last_name = ""
        self.username = ""
        self.email = ""
        self.password = ""
        self.gender = ""
        self.birthdate = ""
        self.phone_number = ""
        self.image_path = ""
        self.prev_image=""
        
        # set background color and font style
        bg_color = "#f2f2f2"
        font_style = ("Helvetica", 12)
        
        # create labels for user information
        self.name_label = tk.Label(master, text="Name:", bg=bg_color, font=font_style)
        self.username_label = tk.Label(master, text="Username:", bg=bg_color, font=font_style)
        self.email_label = tk.Label(master, text="Email:", bg=bg_color, font=font_style)
        self.gender_label = tk.Label(master, text="Gender:", bg=bg_color, font=font_style)
        self.dob_label = tk.Label(master, text="Date of Birth:", bg=bg_color, font=font_style)
        self.phone_label = tk.Label(master, text="Phone:", bg=bg_color, font=font_style)
        
        # create labels for user information values
        self.name_value_label = tk.Label(master, text="Mohamed Laadjel", font=font_style)
        self.username_value_label = tk.Label(master, text="Mouh_laad", font=font_style)
        self.email_value_label = tk.Label(master, text="mohamed.laadjle2019@gmail.com", font=font_style)
        self.gender_value_label = tk.Label(master, text="Male", font=font_style)
        self.dob_value_label = tk.Label(master, text="march 3, 2001", font=font_style)
        self.phone_value_label = tk.Label(master, text="(+213) 06 99479120", font=font_style)
        
        # create and display image
        self.img = Image.open("1.jpg")
        self.img = self.img.resize((150, 150), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label = tk.Label(master, image=self.img, bg=bg_color)
       
        
        # add labels to grid
        self.img_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
        
        self.name_label.grid(row=0, column=1, padx=10, pady=5, sticky="W")
        self.name_value_label.grid(row=0, column=2, padx=10, pady=5, sticky="W")
        
        self.username_label.grid(row=1, column=1, padx=10, pady=5, sticky="W")
        self.username_value_label.grid(row=1, column=2, padx=10, pady=5, sticky="W")
        
        self.email_label.grid(row=2, column=1, padx=10, pady=5, sticky="W")
        self.email_value_label.grid(row=2, column=2, padx=10, pady=5, sticky="W")
        
        self.gender_label.grid(row=3, column=1, padx=10, pady=5, sticky="W")
        self.gender_value_label.grid(row=3, column=2, padx=10, pady=5, sticky="W")
        
        self.dob_label.grid(row=4, column=1, padx=10, pady=5, sticky="W")
        self.dob_value_label.grid(row=4, column=2, padx=10, pady=5, sticky="W")
        
        self.phone_label.grid(row=5, column=        1, padx=10, pady=5, sticky="W")
        self.phone_value_label.grid(row=5, column=2, padx=10, pady=5, sticky="W")
        
        # set background color of all labels
        for label in [self.name_label, self.username_label, self.email_label, self.gender_label, self.dob_label, self.phone_label,
                      self.name_value_label, self.username_value_label, self.email_value_label, self.gender_value_label, self.dob_value_label, self.phone_value_label]:
            label.configure(bg=bg_color)
        # create refresh button
        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh)
        self.refresh_button.grid(row=6, column=2, padx=10, pady=10, columnspan=2, sticky="WE")

    def get_random_picture_path(self):
        if self.gender == 'Female':
            folder_path='ww\pic'
        else :
            folder_path='bb\pic'
        # Get a list of all the files in the folder
        files = os.listdir(folder_path)

        # Filter the list to only include image files
        image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.jfif')]

        # Choose a random image file from the list
        if image_files:
            file_name = random.choice(image_files)
            file_path = os.path.join(folder_path, file_name)
            self.image_path= file_path

    def generate_algerian_phone_number(self):
        # Choose a random mobile network code
        network_codes = ["05", "06", "07"]
        mobile_network_code = random.choice(network_codes)

        # Generate a random subscriber number
        subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])

        # Concatenate the parts to form the phone number
        phone_number = f"(+213) {mobile_network_code} {subscriber_number}"
        self.phone_number = phone_number

    def generate_gender(self):
        genders = ['Male', 'Female']
        self.gender = random.choice(genders)

    def generate_username(self):
        unique_numbers = random.sample(range(1000, 10000), 4)
        self.username = (self.first_name[0] + self.last_name).lower() + "_"+str(unique_numbers[0])

    def generate_name_from_csv(self):
        if self.gender == 'Female':
            filename='ww\ww.csv'
        else :
            filename='bb\wb.csv'
        # Read in the data from the CSV file
        names = []
        probabilities = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                names.append(row[1])
                probabilities.append(float(row[0]))

        # Generate a name based on the probabilities
        name = random.choices(names, weights=probabilities)[0]
        self.first_name = name
       
    def generate_last_name_from_csv(self):
        filename='lastNames.csv'
        # Read in the data from the CSV file
        names = []
        probabilities = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                names.append(row[0])
                probabilities.append(float(row[1]))

        # Generate a name based on the probabilities
        name = random.choices(names, weights=probabilities)[0]
        self.last_name = name
    def generate_birthdate(self, start_date, end_date):
        # Convert start_date and end_date to datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the range of days between start_date and end_date
        delta = end_date - start_date
        delta_days = delta.days

        # Generate a random number of days within the range
        random_days = random.randrange(delta_days)

        # Add the random number of days to start_date to get the birthdate
        birthdate = start_date + timedelta(days=random_days)

        # Format the birthdate as a string and save it to the instance variable
        self.birthdate = birthdate.strftime('%B %d, %Y') 
        
    def refresh(self):
       
        # update user information values here, for example:
        self.generate_gender()
        self.generate_name_from_csv()
        self.generate_last_name_from_csv()
        self.generate_username()
        self.generate_algerian_phone_number()
        self.get_random_picture_path()
        self.generate_birthdate('1950-01-01', '2005-12-31')
        self.name_value_label.configure(text=self.first_name + " " + self.last_name)
        self.username_value_label.configure(text=self.username)
        self.email_value_label.configure(text=self.username+"@gmail.com")
        self.gender_value_label.configure(text=self.gender)
        self.dob_value_label.configure(text=self.birthdate)
        self.phone_value_label.configure(text=self.phone_number)
        
        # reload image
        self.img = Image.open(self.image_path)
        self.img = self.img.resize((150, 150), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label.configure(image=self.img)
    
 
root = tk.Tk()
ui = UserInterface(root)
root.mainloop()

