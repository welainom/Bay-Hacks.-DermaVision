import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Main window setup
root = tk.Tk()
root.title("DermaVision")
root.geometry("900x650")

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("All Files", "*.*")  # Optionally, allow all file types
        ]
    )


    if file_path:
        process_file(file_path)


def process_file(file_path):
    try:
        # Load the image
        image = Image.open(file_path)
        image_photo = ImageTk.PhotoImage(image)

        # Update the label with the new image
        image_label.config(image=image_photo)
        image_label.image = image_photo  # Keep a reference to avoid garbage collection

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_info():
    info_window = tk.Toplevel(root)
    info_window.title("Information")
    info_window.geometry("600x300")

    mission_label = tk.Label(info_window, text="Our Mission",
                          font=("Serif", 25, "bold"))
    mission_label.pack(padx=0, pady=5)

    info1_label = tk.Label(info_window, text="- Dermatology costs skyrocket day by day.",
                          font=("Serif", 20, "normal"), anchor="w")
    info1_label.place(x=5, y=45)

    info2_label = tk.Label(info_window, text="- Disadvantaged people without access to skincare",
                          font=("Serif", 20, "normal"), anchor="w")
    info2_label.place(x=50, y=75)

    info3_label = tk.Label(info_window, text="- We aim to",
                           font=("Serif", 20, "normal"), anchor="w")
    info3_label.place(x=50, y=105)

    info3b_label = tk.Label(info_window, text="HELP",
                           font=("Serif", 20, "bold"), fg="cyan", anchor="w")
    info3b_label.place(x=156,y=105)

    info4_label = tk.Label(info_window, text="- Ready to",
                            font=("Serif", 20, "normal"), anchor="w")
    info4_label.place(x=5, y=145)

    info4b_label = tk.Label(info_window, text="USE",
                            font=("Serif", 20, "bold"), fg="cyan", anchor="w")
    info4b_label.place(x=100, y=145)

    info4c_label = tk.Label(info_window, text="on",
                           font=("Serif", 20, "normal"), anchor="w")
    info4c_label.place(x=143, y=145)

    info4d_label = tk.Label(info_window, text="ALL",
                            font=("Serif", 20, "bold"), fg="cyan", anchor="w")
    info4d_label.place(x=170, y=145)

    info4c_label = tk.Label(info_window, text="skin",
                            font=("Serif", 20, "normal"), anchor="w")
    info4c_label.place(x=210, y=145)

    info5_label = tk.Label(info_window, text="- Image detection model",
                            font=("Serif", 20, "normal"), anchor="w")
    info5_label.place(x=50, y=175)

    info6_label = tk.Label(info_window, text="- No pricey consultations required",
                           font=("Serif", 20, "normal"), anchor="w")
    info6_label.place(x=50, y=205)

    info7_label = tk.Label(info_window, text="- AI",
                           font=("Serif", 20, "normal"), anchor="w")
    info7_label.place(x=5, y=245)

    info7a_label = tk.Label(info_window, text="DETECTS",
                            font=("Serif", 20, "bold"), fg="cyan", anchor="w")
    info7a_label.place(x=42, y=245)

    info7b_label = tk.Label(info_window, text="and",
                           font=("Serif", 20, "normal"), anchor="w")
    info7b_label.place(x=135, y=245)

    info7c_label = tk.Label(info_window, text="COMMUNICATES",
                            font=("Serif", 20, "bold"), fg="cyan", anchor="w")
    info7c_label.place(x=173, y=245)

    info7d_label = tk.Label(info_window, text="skin anomalies",
                            font=("Serif", 20, "normal"), anchor="w")
    info7d_label.place(x=345, y=245)

#background_image = Image.open("simplegray.jpg")  # Path to your background image
#background_photo = ImageTk.PhotoImage(background_image)

# Create a Label to hold the background image
#background_label = tk.Label(root, image=background_photo)
#background_label.place(relwidth=1, relheight=1)  # Make the image cover the entire window

# Create a frame to hold the labels and image
frame = tk.Frame(root, bg='lightgrey')  # Set a background color for visibility
frame.place(relwidth=1, relheight=1)

# Add labels and button
title_label = tk.Label(frame, text="Scan for Skin Conditions", font=("Lora", 45, "bold"), bg='lightgrey')
title_label.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="n")

upload_label = tk.Label(frame, text="Upload a File:", font=("Lora", 25, "bold"), bg='lightgrey')
upload_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

upload_button = tk.Button(frame, text="Upload", command=upload_file, font=("Arial", 25, "bold"))
upload_button.grid(row=1, column=1, padx=20, pady=20, sticky="e")

image_label = tk.Label(frame)
image_label.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

# Configure grid weights to make sure widgets resize properly
frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# add logo
logo = Image.open("DermaLogo2.png")
image_width, image_height = logo.size
logo = logo.resize((image_width // 6, image_height // 6))
logoImg = ImageTk.PhotoImage(logo)

logo_button = tk.Button(root, image=logoImg, command = open_info)
logo_button.place(x = 15, y = 27)

# Start the Tkinter event loop
root.mainloop()