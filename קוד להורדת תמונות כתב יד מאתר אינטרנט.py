import os
import requests
import time

# צור תיקייה לשמירת התמונות
folder = "genizah_images"
os.makedirs(folder, exist_ok=True)

# טווח העמודים
start_page = 898610
end_page = 898941

# כתובת בסיס
base_url = "https://talmud.nli.org.il/{}.jpg"

for page_number in range(start_page, end_page + 1):
    print(f"\rמוריד עמוד {page_number}/{end_page}...", end="")  # הודעה מתעדכנת
    url = base_url.format(page_number)
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(folder, f"{page_number}.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"\nבעיה בהורדה של עמוד {page_number}, קוד סטטוס: {response.status_code}")
    
    # השהייה קצרה למען יציבות
    time.sleep(0.1)

print("\nכל ההורדות הסתיימו!")
