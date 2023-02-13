from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Open the image
def open_image():
    global img
    root.filename = filedialog.askopenfilename()
    img = Image.open(root.filename)
    return img


# Add watermark to the image
def add_watermark():
    global img
    draw = ImageDraw.Draw(img)
    text = watermark_text.get()
    font = ImageFont.truetype("arial.ttf", 20)
    draw.textlength(text)
    width, height = img.size
    x = width / 8
    y = height / 1.1
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))


# Save the new image
def save_image():
    global img
    img.save("watermarked.jpg")


# Create GUI Platform
root = Tk()
root.title("Watermark Creator")
root.config(padx=100, pady=50, bg="#A7727D")

# Create GUI Components
title = Label(text="WaterMark Your Pictures", fg="#EDDBC7", bg="#A7727D", font=("Courier", 30, "bold"))
title.grid(column=0, row=0)
upload_button = Button(root, text="Upload Picture", padx=20, pady=5, fg="#EDDBC7", bg="#A7727D", command=open_image)
upload_button.grid(column=0, row=1)

watermark_label = Label(text="Enter Your Watermark", fg="#A7727D")
watermark_label.grid(column=0, row=2)
watermark_text = Entry(root, bg="#EDDBC7")
watermark_text.grid(column=0, row=3)
add_watermark_button = Button(root, text="Add Watermark", padx=17, fg="#EDDBC7", bg="#A7727D", command=add_watermark)
add_watermark_button.grid(column=0, row=4)

save_button = Button(root, text="Save Picture", padx=27, fg="#EDDBC7", bg="#A7727D", command=save_image)
save_button.grid(column=0, row=5)

root.rowconfigure(1, pad=20)
root.rowconfigure(3, pad=20)
root.rowconfigure(5, pad=20)

root.mainloop()