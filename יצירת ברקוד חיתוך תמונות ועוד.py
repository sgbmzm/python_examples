#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import string

# יצירת פונקציה ליצירת סיסמה אקראית
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# יצירת 20 סיסמאות אקראיות והדפסתן
passwords = [generate_password(20) for _ in range(20)]
for password in passwords:
    print(password)


# In[ ]:





# In[ ]:


# חשוב מאוד הקוד שאיתו יצרתי את כל הברקודים לפרוייקט דנא

import string
import random
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import os

# יצירת פונקציה ליצירת סיסמה אקראית
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# הגדרת סוג הברקוד המבוקש: קוד128
code128 = barcode.get_barcode_class('code128')

# יצירת רשימה ריקה לאחסון ברקודים
barcode_images = []


def reverse_text(text):
    return text[::-1]

# עשר פעמים
for i in range(10):
    # יצירת סיסמה רנדומלית באורך 20 תווים באמצעות הפונקצייה שהוגדרה לעיל
    password = generate_password(20)
    # שם קובץ התמונה
    filename = f'barcode_{i+1}.jpeg'
    
    # Write to a file-like object:
    rv = BytesIO()
    code128(password, writer=ImageWriter()).write(rv)
    barcode_image = Image.open(rv)
    
    # יצירת תמונה חדשה עם טקסט מסביר על הברקוד
    img_with_text = Image.new("RGB", (barcode_image.width, barcode_image.height + 100), background_color)
    draw = ImageDraw.Draw(img_with_text)
    text = "2024" + " " + reverse_text('סיסמת השתתפות במחקר דנ"א כוהנים')
    font = ImageFont.truetype("arial.ttf", 30)
    text_width, text_height = draw.textsize(text, font=font)
    x_position = (barcode_image.width - text_width) // 2
    y_position = 10
    draw.text((x_position, y_position), text, fill=(0, 0, 0), font=font)
    
    # הדבקת הברקוד בתוך התמונה עם הטקסט
    img_with_text.paste(barcode_image, (0, 100))
    barcode_images.append(img_with_text)
    

# קביעת נתיב לתיקייה בה ישמרו הקבצים
save_path = os.path.expanduser("~/Desktop/barcode_images")

# בדיקה אם התיקייה לא קיימת - אם לא, ניצור אותה
if not os.path.exists(save_path):
    os.makedirs(save_path)
    
# שמירת כל תמונת הברקודים בקבצים נפרדים
for i, img_with_text in enumerate(barcode_images):
    file_path = os.path.join(save_path, f"barcode_{i+1}.jpg")
    img_with_text.save(file_path)


# In[ ]:


# חיתוך תמונות

#Import required Image library
from PIL import Image

#Create an Image Object from an Image
im = Image.open('images/elephant.jpg')

#Display actual image
#im.show()

#left, upper, right, lowe
#Crop
cropped = im.crop((1000,500,5000,5300))

#Display the cropped portion
#cropped.show()

#Save the cropped image
cropped.save('images/croppedBeach1.jpg')

