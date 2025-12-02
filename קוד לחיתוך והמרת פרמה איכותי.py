import os
from PIL import Image

input_folder = r"C:\Users\HP\Desktop\סדר טהרות"
output_folder = r"C:\Users\HP\Desktop\סדר טהרות_jpg"
os.makedirs(output_folder, exist_ok=True)

'''
# חיתוך שוליים טוב עבור צילום מסך של 7000 X 7000
crop_left = 1250
crop_right = 1250
crop_top = 770
crop_bottom = 950


# חיתוך שוליים טוב עבור צילום מסך של 4000 X 4000
crop_left = 750
crop_right = 750
crop_top = 550
crop_bottom = 600
'''

# חיתוך שוליים טוב עבור צילום מסך של 6000 X 6000
crop_left = 1071
crop_right = 1071
crop_top = 660
crop_bottom = 814


for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # המרה ל־RGB כדי למנוע שגיאת RGBA
        img = img.convert("RGB")

        w, h = img.size

        cropped = img.crop((
            crop_left,
            crop_top,
            w - crop_right,
            h - crop_bottom
        ))
        
        # גודל סופי רצוי
        final_width = 3821
        final_height = 4592

        # שינוי גודל סופי
        cropped = cropped.resize((final_width, final_height), Image.LANCZOS)

        out_name = os.path.splitext(filename)[0] + ".jpg"
        out_path = os.path.join(output_folder, out_name)

        cropped.save(out_path, "JPEG", quality=30)

        print("✔ נשמר:", out_path)
