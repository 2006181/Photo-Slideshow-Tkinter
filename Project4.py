import tkinter as tk 
import time 
from PIL import Image, ImageTk

# Main Application Window 
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("1000x800")

# List of Image Paths 
image_paths= [
    r"C:\Users\Rahul gupta\Downloads\1771446828182.jpg",
    r"C:\Users\Rahul gupta\Downloads\1771446828187.jpg",
    r"C:\Users\Rahul gupta\Downloads\1771446827499.jpg",
    r"C:\Users\Rahul gupta\Downloads\1771446827729.jpg",
    r"C:\Users\Rahul gupta\Downloads\1771446827839.jpg",
]

image_size= (700, 700)
images= []
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)  #Adding each image in the list

# Convert PIL Images into Tkinter Compatible Image 
final_images= []
for img in images:
    photo= ImageTk.PhotoImage(img) 
    final_images.append(photo)

# Label widget to keep photuuu 
image_label= tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function 
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

#Button 
play_button= tk.Button(
    root,
    text= "Play the Slideshow",
    font=("Arial", 17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()
