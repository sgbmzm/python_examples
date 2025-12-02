from PIL import Image

# פותחים את התמונה המקורית
img = Image.open("cu_splash.jpg")

# שומרים כ-PNG
img.save("cu_splash.png")

print("ההמרה הושלמה! נשמר כ–cu_splash.png")
