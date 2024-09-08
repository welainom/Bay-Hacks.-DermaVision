import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np

# Specify the directory where the image will be saved
save_directory = '/Users/williamliu/PycharmProjects/pythonProject/UserImage/Image/'
fixed_image_name = 'uploaded_image.jpg'  # This is the fixed name for the uploaded image

# Define your class names
class_names = [
    'Acne',
    'Carcinoma',
    'Eczema',
    'Keratosis',
    'Milia',
    'Rosacea'
]

# Load your trained model
model = load_model("FinalModel.keras", compile=False)

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Directory where you will be processing the uploaded image
dataset_dir = '/Users/williamliu/PycharmProjects/pythonProject/UserImage'

# Prediction function
def p():
    dataset = image_dataset_from_directory(
        dataset_dir,
        labels='inferred',
        label_mode='int',
        image_size=(224, 224),
        batch_size=32,
        shuffle=True
    )
    predicted_class = None
    for images, labels in dataset:
        processed_image = images

        predictions = model.predict(processed_image)

        predicted_class_idx = np.argmax(predictions, axis=-1)
        predicted_class = class_names[predicted_class_idx[0]]

    return predicted_class

# Upload image function
def upload_image():
    # Open file dialog for user to select an image
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
    )

    if file_path:
        # Define the save path using a fixed name
        save_path = os.path.join(save_directory, fixed_image_name)

        # Remove any previous image with the same name to ensure a fresh upload
        if os.path.exists(save_path):
            os.remove(save_path)

        # Copy the new image to the save directory
        shutil.copyfile(file_path, save_path)

        # Open and display the uploaded image
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Resize image to fit in the UI
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Make the prediction and update the label with the result
        predicted_class = p()
        print(predicted_class)

# Create the main application window
root = tk.Tk()
root.title("Skin Condition Predictor")
root.geometry("500x600")

# Create a label to show the uploaded image
image_label = tk.Label(root, text="No Image Uploaded")
image_label.pack(pady=20)

# Create a label to show the status of the image upload
label = tk.Label(root, text="Upload an Image", font=("Arial", 12))
label.pack(pady=10)

# Create the upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Create a label to show the prediction result
message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
