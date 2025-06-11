# מחשבון עומק השמש הקובע לסוף בין השמשות
# יש להזין קו רוחב גיאוגרפי ואת מספר הדקות אחר השקיעה ביום השיוויון הקובע את תחילת הלילה
# הכל כאן מבוסס על חישוב ביום השיוויון וברגע השיוויון
# נבנה בעזרת GPT לפי הוראות של הרב ד"ר שי ואלטר

import math

# נתונים
phi_deg = 31.03          # קו רוחב של המיקום בדוגמא כאן סדום
delta_deg = 0            # נטיית השמש באביב
h_shkia_deg = -0.833333  # גובה השמש בשקיעה נראית
extra_minutes = 72       # זמן לאחר השקיעה
minutes_per_degree = 4   # יחס של זמן לשעה זוויתית

# המרה לרדיאנים
phi = math.radians(phi_deg)
h_shkia = math.radians(h_shkia_deg)

# שלב 1: חשב את זווית השעה בשקיעה נראית (h = -0.8333)
cos_H = math.sin(h_shkia) / math.cos(phi)
H_rad = math.acos(cos_H)
H_deg = math.degrees(H_rad)

# שלב 2: הוספת 72 דקות לזווית השעה
H2_deg = H_deg + extra_minutes / minutes_per_degree
H2_rad = math.radians(H2_deg)

# שלב 3: חישוב גובה השמש עבור H = 108.56
sin_h2 = math.cos(H2_rad) * math.cos(phi)
h2_rad = math.asin(sin_h2)
h2_deg = math.degrees(h2_rad)

print(H_deg, H2_deg, h2_deg)

