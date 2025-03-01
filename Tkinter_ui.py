import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
from main import generate_caption

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        img = ImageTk.PhotoImage(image)
        image_label.config(image=img)
        image_label.image = img
        caption = generate_caption(file_path)
        caption_label.config(text=f"Caption: {caption}")
    elif file_path:
        print("filepath does not exist or not found")

# created ui window
root = tk.Tk()
root.title("Image Caption Generator")

# UI elements
image_label = Label(root)
image_label.pack()
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()
caption_label = Label(root, text="Caption: ", wraplength=300)
caption_label.pack()

root.mainloop()
