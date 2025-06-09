#!/usr/bin/env python
# coding: utf-8

# In[1]:


# מיקום גיאוגרפי נקרא bluffton
# ephemeris זה מידע על הכוכבים
# topos זה קוי הרוחב והאורך של המיקום הגיאוגרפי המבוקש
# t זה הזמן


# In[18]:





# In[10]:


23 * 0.75


# In[18]:





# In[2]:


# המרות

# דוגמא לנוסחה להמרה ממעלות עם דקות ושניות קשת - למעלות עשרוני
#-19:42:54.7
# 19.715182237343605
# מינוס 19 מעלות
# 19 + (42 / 60) + ((54.7 / 60) / 60 )
#-19.07
# דקות קשת הם 60
# שניות קשת הם 60
#התוצאה 19.715194444444442

# דוגמא לנוסחה להמרה ממעלות עשרוני - למעלות עם דקות ושניות קשת
# בדוגמא זו לוקחים בכל פעם את שתי הספרות הראשונות של התוצאה
# 19.715194444444442
# 715194444444442 * 60 = 42911666666666520
# 911666666666520 * 60 = 54699999999991200
# 19:42:54.6999999999


# זו דוגמא לנוסחה להמרת רדיאנים למעלות
5.644654750823975 / pi * 180.0

# וזו דוגמא להמרת מעלות לרדיאנים
323.4148940306831 * pi / 180.0


# In[ ]:


# פונקצייה לחישוב זריחות ושקיעות השמש ששימשה בעבר לחישוב שעות זמניות וכרגע אין בה צורך אלא לשימור
def calculate_SR_SS(time,location,location_timezone,horizon=0):
    
    # הגדרת תחילת וסוף התאריכים לחישוב זריחות ושקיעות
    time_midday = time.replace(hour=12, minute=0, second=0, microsecond=0)
    time_minus_1_midday = time_midday - dt.timedelta(days=1)
    time_plus_1_midday = time_midday + dt.timedelta(days=1)
    
    ts = load.timescale()
    t0 = ts.from_datetime(time_minus_1_midday)
    t1 = ts.from_datetime(time_plus_1_midday)
    
    # הגדרת זריחה ושקיעה
    sun_rise_set = almanac.risings_and_settings(eph, eph["sun"], location, horizon_degrees=horizon, radius_degrees=0)
    
    # חיפוש הזריחה והשקיעה המבוקשים בין שני התאריכים
    sun_rise_set_times, y = almanac.find_discrete(t0, t1, sun_rise_set)
    
    # פירוט הזמנים כולל אפשרות למחיקת מיקרו שניות מזמני השקיעה והזריחה
    Yesterday_SS = sun_rise_set_times[0].astimezone(location_timezone)#.replace(microsecond=0)
    Today_SR = sun_rise_set_times[1].astimezone(location_timezone)#.replace(microsecond=0)
    Today_SS = sun_rise_set_times[2].astimezone(location_timezone)#.replace(microsecond=0)
    tomorrow_SR = sun_rise_set_times[3].astimezone(location_timezone)#.replace(microsecond=0) 
    
    return Yesterday_SS,Today_SR,Today_SS,tomorrow_SR


# In[2]:


# סקייפילד
from skyfield.api import N, S, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield.earthlib import refraction
from skyfield import almanac
from skyfield.units import Angle
from skyfield.nutationlib import iau2000b_radians

from skyfield.searchlib import find_discrete

# השורה הזו חשובה מאוד והיא מועתקת מתוך ספריית האלמנך
find_discrete

# תאריכים
import datetime as dt
from datetime import datetime, timedelta, date
from pytz import timezone

# חישובים
from numpy import cos, zeros_like, arccos





###### אם יש שגיאה שאומרת שיש קובץ פתוח בזיכרון, צריך לה ####

# חישוב אורך ראשון של הירח ואחוזי התאורה שלו עבור תאריך מסויים
# ותוך כדי כך חישוב מקום השמש האמיתי ומקום הירח האמיתי

# יבוא החבילות הנדרשות
from skyfield.api import N, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield import almanac
import datetime as dt
from pytz import timezone


# הגדרת הזמן
ts = load.timescale()
t = ts.utc(2024, 12, 19, 8, 43, 15)

#----------------------------
# טעינת קובץ הנתונים מנאסא, מהאינטרנט או מהמחשב

#--------
# הקדמה לצורך הסתמכות על תעודת אבטחה בנטפרי שנמצאת בכונן סי
import certifi

def my_where():
    return r'C:\netfree.crt'

certifi.where = my_where
#---------------------

#####  חשוב מאוד!!! כדי שלא יצטרכו להוריד שוב מהאינטרנט את קובץ הנתונים מנאס"א, הוא חייב להיות בדיוק באותה תיקייה שבה נמצא קובץ פייתון או ג'ופיטר,  ####

# קבלת המידע מנאס"א על כל כוכבי הלכת
# השורה הבאה מורידה את הקובץ מהאינטרנט :
eph = load('de441s.bsp')
# אם אין חיבור לאינטרנט יש להוריד את הקובץ בדרך אחרת, לשים אותו במיקום כלשהוא במחשב ולהכניס את מיקום הכתובת בסוגריים בין המרכאות:
#eph = load_file(r'C:\de421.bsp')

# זו הכתובת שממנה מורידים את הקובץ
#(https://ssd.jpl.nasa.gov/ftp/eph/planets/bsp/de421.bsp)
    
#---------------------------------------

# הגדרות משנים מתוך קובץ הנתונים מנאסא
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# הגדרת כדור הארץ השמש והירח
e = earth.at(t)
s = e.observe(sun).apparent()
m = e.observe(moon).apparent()

# חישוב מקום השמש האמיתי ומקום הירח האמיתי 
slon = s.frame_latlon(ecliptic_frame)[1]
mlon = m.frame_latlon(ecliptic_frame)[1]

# מציאת אורך הירח באצעות הפחתת מקום הירח ממקום השמש במודולו 360 מעלות
phase = (mlon.degrees - slon.degrees) % 360.0

moon_first_lon = (mlon.degrees - slon.degrees) % 360.0
# חישוב אחוזי התאורה של הירח על בסיס מיקום הירח
percent = 100.0 * m.fraction_illuminated(sun)

phase_angle = m.phase_angle(sun)

# הדפסות

print('מקום השמש האמיתי (0°–360°): {0:.3f}'.format(slon.degrees))
print('מקום הירח האמיתי (0°–360°): {0:.2f}'.format(mlon.degrees))
print('אורך ראשון של הירח (0°–360°): {0:.2f}'.format(phase))
print('אחוזי התאורה של הירח: {0:.2f}%'.format(percent))
#print('Phase (0°–360°): {0:.1f}'.format(phase))
#print('Percent illuminated: {0:.1f}%'.format(percent))

print(m.phase_angle(sun))

print(m.fraction_illuminated(sun))


# סגירת קובץ הנתונים מנאסא כדי שיוכל לפעול במחברת אחרת
#eph.close()

t


# In[5]:





# In[42]:


ts = load.timescale(builtin=False)


# In[ ]:


https://datacenter.iers.org/products/eop/rapid/standard/finals2000A.all


# In[43]:


help(load.download)


# In[49]:


# לתחנת החלל ולויינים
from skyfield.api import load, wgs84
import math

ts = load.timescale()
stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)

by_name = {sat.name: sat for sat in satellites}
iss = by_name['ISS (ZARYA)']


eph = load('de441.bsp')
bluffton = wgs84.latlon(+40.8939, -83.8917)
t0 = ts.utc(2024, 1, 23)
t1 = ts.utc(2024, 1, 24)

t, events = iss.find_events(bluffton, t0, t1, altitude_degrees=30.0)
sunlit = iss.at(t).is_sunlit(eph)
event_names = 'rise above 30°', 'culminate', 'set below 30°'

for ti, event, sunlit_flag in zip(t, events, sunlit):
    name = event_names[event]
    state = ('in shadow', 'in sunlight')[sunlit_flag]
    iss_topocentric = (iss - bluffton).at(ti)
    alt, az, distance = iss_topocentric.altaz()
    iss_phase_angle = eph['earth'].at(ti).observe(eph['earth'] + iss).apparent().phase_angle(eph['sun'])
    distance_to_satellite = distance.km  # This is in KM
    iss_phase_angle = eph['earth'].at(ti).observe(eph['earth'] + iss).apparent().phase_angle(eph['sun'])
    pa = iss_phase_angle.radians  # Convert the phase angle to radians
    intrinsic_magnitude = -1.8  # -1.8 is std. mag for iss
    term_1 = intrinsic_magnitude
    term_2 = 5.0 * math.log10(distance_to_satellite / 1000.0)
    arg = math.sin(pa) + (math.pi - pa) * math.cos(pa)
    term_3 = -2.5 * math.log10(arg)
    apparent_magnitude = term_1 + term_2 + term_3
    magnitude = apparent_magnitude

    print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name, state,"; magnitude:", round(magnitude,1))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


eph.close()


# In[ ]:


from datetime import datetime
from dateutil.tz import gettz

# Create a datetime object for a specific date and time
date = datetime(2023, 1, 1, 12, 0, 0)  # Example: January 1, 2023 at 12:00 PM

# Get the timezone object for Israel using the zoneinfo database
timezone = gettz('Israel')

# Convert the datetime object to the Israel timezone
date_with_timezone = date.astimezone(timezone)

# Print the result
print(date_with_timezone)


# In[6]:


eph.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


try:
    # השורה הבאה מורידה את הקובץ מהאינטרנט :
    eph = load('de440.bsp')
except OSError:
    netfree_crt_url = "https://netfree.link/netfree-ca.crt"
    netfree_crt_path = cu_dir_path+"\netfree-ca.crt"
    urlretrieve(netfree_crt_url, netfree_crt_path)
    certifi.where = rf'{netfree_crt_path}'
    eph = load('de440.bsp')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:


import locale

default_encoding = locale.getpreferredencoding()

print(default_encoding)


# In[73]:


# נסיון לאין היה הירח נוטה
from skyfield.api import N, E, load, wgs84
from skyfield.trigonometry import position_angle_of

ts = load.timescale()
t = ts.utc(2022, 1, 1, 18)

eph = load('de440.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']
location = earth + wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)

b = location.at(t)
m = b.observe(moon).apparent()
s = b.observe(sun).apparent()
ss = position_angle_of(m.altaz(), s.altaz()).degrees

ss = int(ss) -180 if ss > 180 else int(ss) + 180

point_start = ss-45
point_end = ss+45


# In[74]:


f"{point_start/6:2.01f} - {point_end/6:2.01f}"


# In[1]:


import sun_moon_test


# In[76]:


ss


# In[2]:


help(position_angle_of)


# In[ ]:


# ניסיון לחישוב ליקוי חמה שאני כתבתי

# חישוב אלונגציה בלי לכלול בחשבון את המיקום הגיאוגרפי נותן תוצאה טובה
from skyfield.api import N, S, E, W, wgs84, load
from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima, find_minima,find_discrete
from pytz import timezone

ts = load.timescale()
t0 = ts.utc(2019)
t1 = ts.utc(2024)

eph = load('de440.bsp')

modiin_illit_israel = wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)

Illinois_usa = wgs84.latlon(40.197303, -89.626094 * E, elevation_m=0) # Illinois

location = modiin_illit_israel

def elongation_at(t):
    bluffton = eph['earth'] + location
    sun = bluffton.at(t).observe(eph['sun']).apparent()
    moon = bluffton.at(t).observe(eph['moon']).apparent()
    moon_elongation = sun.separation_from(moon).degrees
    return moon_elongation

elongation_at.step_days = 27.0

times, elongations = find_minima(t0, t1, elongation_at)

for t, elongation_degrees in zip(times, elongations):
    if elongation_degrees < 1:
        print('{}  {:4.5f}° elongation'.format(
            t.astimezone(timezone("israel")), elongation_degrees))


# In[ ]:


# אלונגציה

from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima

ts = load.timescale()
t0 = ts.utc(2019)
t1 = ts.utc(2022)

eph = load('de440s.bsp')
sun, earth, venus = eph['sun'], eph['earth'], eph['venus']

def elongation_at(t):
    e = earth.at(t)
    s = e.observe(sun).apparent()
    v = e.observe(venus).apparent()
    return s.separation_from(v).degrees

elongation_at.step_days = 15.0

times, elongations = find_maxima(t0, t1, elongation_at)

for t, elongation_degrees in zip(times, elongations):
    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
    _, vlon, _ = e.observe(venus).apparent().frame_latlon(ecliptic_frame)
    is_east = (vlon.degrees - slon.degrees) % 360.0 < 180.0
    direction = 'east' if is_east else 'west'
    print('{}  {:4.1f}° {} elongation'.format(
        t.utc_strftime(), elongation_degrees, direction))


# In[ ]:


A = wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)


# In[ ]:





# In[ ]:


# חישוב אלונגציה נוכחית

from skyfield.api import N, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima

time = load.timescale().now()
#time = load.timescale().utc(2017, 8, 21, 18, 26, 40)


# חישוב מיקום הצופה בתוספת כדור הארץ עצמו
bluffton = eph['earth'] + wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0) # מודיעין עילית,ישראל
#bluffton = eph['earth'] + wgs84.latlon(40.197303, -89.626094 * E, elevation_m=0) # Illinois

# חישוב לפי כדור הארץ כולל מיקום הצופה
sun = bluffton.at(time).observe(eph['sun']).apparent()
moon = bluffton.at(time).observe(eph['moon']).apparent()

# חישוב לפי כדור הארץ בלי לקחת בחשבון את מיקום הצופה כך זה בדוגמא המקורית של סקייפילד
#sun = eph['earth'].at(time).observe(eph['sun']).apparent()
#moon = eph['earth'].at(time).observe(eph['moon']).apparent()

# זו אלונגציה אמיתית שלוקחת בחשבון גם את רוחב הירח
# אבל אלונגציה על המילקה שהרמב"ם קורא לה אורך ראשון אינה לוקחת בחשבון את רוחב הירח
elongation_degrees = sun.separation_from(moon).degrees
elongation_radians = sun.separation_from(moon).radians
elongation_degrees


# In[ ]:


A = 0.5 * (1.0 + cos(elongation_radians))
B = 100 * A
B


# In[ ]:


0.9989793583851071


# In[ ]:


# פונקצייה שמחשבת אלונגציה אמיתית בין השמש לבין הירח או כוכב אחר
# הפונקצייה צריכה לקבל רק נתונים של סקייפילד: גוף מיקום וזמן
def elongation(body,location,time):

    # חישוב אלונגציה אמיתית לכוכבים וזמנים
    # חישוב מיקום הצופה בתוספת כדור הארץ עצמו

    bluffton = eph['earth'] + location

    # חישוב לפי כדור הארץ כולל מיקום הצופה
    sun = bluffton.at(time).observe(eph['sun']).apparent()
    body_body = bluffton.at(time).observe(eph[body]).apparent()

    # חישוב לפי כדור הארץ בלי לקחת בחשבון את מיקום הצופה כך זה בדוגמא המקורית של סקייפילד
    #sun = eph['earth'].at(time).observe(eph['sun']).apparent()
    #moon = eph['earth'].at(time).observe(eph['moon']).apparent()

    # זו אלונגציה אמיתית שלוקחת בחשבון גם את רוחב הירח
    # אבל אלונגציה על המילקה שהרמב"ם קורא לה אורך ראשון אינה לוקחת בחשבון את רוחב הירח
    elongation = sun.separation_from(body).degrees
    
    # חישוב קו-אורך השמש 
    _, slon, _ = eph['earth'].at(time).observe(eph["sun"]).apparent().frame_latlon(ecliptic_frame)
    
    # חישוב קו-אורך הגוף
    _, body_lon, _ = eph['earth'].at(time).observe(eph[body]).apparent().frame_latlon(ecliptic_frame)
    
    phase = (body_lon - slon) % 360.0
    east_or_west = 'מערב' if phase>180 else 'מזרח'
    
    return elongation,east_or_west


# In[ ]:


# חישוב הקוטר הזוויתי של כוכב בדקות קשת

import numpy as np
from skyfield.api import Angle, load

ts = load.timescale()
time = ts.utc(2003, 10, 26, 14, 56, 30)

#time = ts.now()

body = "moon"

eph = load('de440s.bsp')

# קוטר משווני של כל אחד מכוכבי הלכת
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html
if body == "sun":
    Equatorial_radius_km = 696342.0
elif body == "moon":
    Equatorial_radius_km = 1738.1
elif body == "venus":
    Equatorial_radius_km = 6051.8 
elif body == "JUPITER BARYCENTER":
    Equatorial_radius_km = 71492.0
elif body == "MARS BARYCENTER":
    Equatorial_radius_km = 3396.2
elif body == "SATURN BARYCENTER":
    Equatorial_radius_km = 60268.0
elif body == "mercury":
    Equatorial_radius_km = 2440.5


_, _, distance = eph['earth'].at(time).observe(eph[body]).apparent().radec()
apparent_diameter = Angle(radians=np.arcsin(Equatorial_radius_km / distance.km) * 2.0)

if body in ["sun", "moon"]:
    print('{:.6f} arcminutes'.format(apparent_diameter.arcminutes()))
else:
    print('{:.6f} arcseconds'.format(apparent_diameter.arcseconds()))


# In[ ]:


moon_precent = 1.783997 # 1.5% from 100
precent = moon_precent / 100 # exemple 1.5 / 100
arcminutes_crescent_moon = apparent_diameter.arcminutes() * precent
arcminutes_crescent_moon


# In[ ]:


precent


# In[ ]:


_precent = 1.5 
present_100 = _precent / 100
31.48 * present_100


# In[ ]:


moon_precent = 1.5 # 1.5% from 100
present = moon_precent / 100 # exemple 1.5 / 100
31.48 * precent


# In[ ]:


31.48 * 0.015


# In[ ]:


def percentage(part, whole):
    return 100 * float(part)/float(whole)

percentage(present, apparent_diameter.arcminutes())


# In[ ]:


# דוגמא לחיפוש אירוע נקודתי מותאם אישית: שמש באזימוט 180 או 360 שזו עוד דרך למציאת חצות היום והלילה ודרך זו עובדת גם בקטבים

# יבוא החבילות הנדרשות
from skyfield.api import N, S, E, W, wgs84, load
from skyfield.searchlib import find_discrete

# טעינת קובץ הנתונים מנאס"א
eph = load('de440.bsp')

# הגדרת המיקום הגיאוגרפי
location = wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)

# הגדרת פונקצייה של מה שרוצים לחפש: שמש באזימוט 180 נכון או לא נכון
def sun_az_180_and_360(t):
    return (eph['earth'] + location).at(t).observe(eph['sun']).apparent().altaz()[1].degrees <= 180.0 

# הגדרת מספר הימים או השעות שביניהם צריך לעשות את החיפוש
sun_az_180_and_360.step_days = 0.04 

# הגדרת טווח התאריכים שבו צריך לחפש את האירוע
ts = load.timescale()
t0 = ts.utc(2022, 10, 22, 6 ,12 ,50)
t1 = ts.utc(2022, 10, 23, 6 ,12 ,40)

# קריאה לפונקציית פינד דיסקרייט שמחפשת את האירוע שמוגדר בפונקצייה שלעייל בטווח הזמן שלעייל
t, values = find_discrete(t0, t1, sun_az_180_and_360)

# הדפסת הנתונים שנמצאו
for ti, vi in zip(t, values):
    print(ti.utc_strftime('%Y-%m-%d %H:%M:%S'), vi)


# In[ ]:





# In[ ]:


t0 = ts.utc(2022, 12, 9, 6)
t1 = ts.utc(2022, 12, 10, 6)

#t0 = ts.utc(2020, 2, 1)
#t1 = ts.utc(2020, 2, 2)
f = almanac.risings_and_settings(eph, eph['Moon'], bluffton)
t, y = almanac.find_discrete(t0, t1, f)

for ti, yi in zip(t, y):
    print(ti.utc_iso(), 'Rise' if yi else 'Set')


# In[11]:


# יבוא החבילות הנדרשות
from skyfield.api import N, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield import almanac
import datetime as dt
from pytz import timezone

# הגדרת הזמן
ts = load.timescale()

# חישוב תקופות אמיתיות, בשעון גריניץ
eph = load('de441_part-1.bsp')
t0 = ts.utc(-3758, 1, 1)
t1 = ts.utc(-3758, 12, 31)
t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))

for yi, ti in zip(y, t):
    print(yi, almanac.SEASON_EVENTS[yi], ti.utc_iso(' '))
    print("delta_t:", round(ti.delta_t, 1), "seconds")
    print("UT1:", ti.ut1_calendar())
    print(f'יום יוליאני: {ti.tdb :02.6f}')
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(day_names[int((ti.tdb % 7 + 1) % 7)])
    #print(ti.whole())
    
#    print(yi, almanac.SEASON_EVENTS[yi], ti.astimezone(zone))
    

# סגירת קובץ הנתונים מנאסא כדי שיוכל לפעול במחברת אחרת
eph.close()


# In[6]:


from pyluach import dates
birth_heb = dates.HebrewDate(1, 1, 19)


# In[10]:


birth_heb.to_greg()


# In[9]:


birth_heb.hebrew_date_string()


# In[41]:


import math
# מבינה מלאכותית לבדוק
# Define the date variables for 22 March -3759 Gregorian calendar
Y = -3758  # Adjusting to make -3759 equivalent to astronomical notation (-3758)
M = 3
D = 22

# Calculate Julian Day (JD) based on the Gregorian calendar formula
JD_gregorian = (367 * Y 
                - math.floor(7 * (Y + math.floor((M + 9) / 12)) / 4) 
                - math.floor(3 * (math.floor((Y + (M - 9) / 7) / 100) + 1) / 4)  # Gregorian adjustment
                + math.floor(275 * M / 9) 
                + D 
                + 1721028.5)

JD_gregorian


# In[ ]:


import datetime as dt
from pytz import timezone
from skyfield import almanac
from skyfield.api import N, E, W, wgs84, load

# Figure out local midnight.
zone = timezone('Israel')
now = zone.localize(dt.datetime.now())
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
next_midnight = midnight + dt.timedelta(days=1)

ts = load.timescale()
t0 = ts.from_datetime(midnight)
t1 = ts.from_datetime(next_midnight)
eph = load('de440s.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0) 
f = almanac.dark_twilight_day(eph, bluffton)
times, events = almanac.find_discrete(t0, t1, f)


previous_e = f(t0).item()
for t, e in zip(times, events):
    tstr = str(t.astimezone(zone))[:16]
    if previous_e < e:
        print(tstr, ' ', almanac.TWILIGHTS[e], 'starts')
    else:
        print(tstr, ' ', almanac.TWILIGHTS[previous_e], 'ends')
    previous_e = e
    
zone.zone


# In[ ]:


bluffton = [wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0), "מודיעין עילית"]


# In[ ]:


a = ["מודיעין עילית",
    "ירושלים",
    "בני ברק",
    "ביתר"]
a


# In[9]:


# חישוב ירח חדש מלא ורבעים

eph = load('de441s.bsp')
t0 = ts.utc(2022, 12, 7)
t1 = ts.utc(2022, 12, 20)
t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))

print(t.utc)
print(y)
print([almanac.MOON_PHASES[yi] for yi in y])

t = ts.utc(2025, 5, 25)
phase = almanac.moon_phase(eph, t)
print('Moon phase: {:.1f} degrees'.format(phase.degrees))


# In[15]:


from skyfield.api import load
from skyfield import almanac

#eph = load('de421.bsp')
ts = load.timescale()
t = ts.utc(2025, 5, 28)

phase = almanac.moon_phase(eph, t)
percent = phase.degrees / 360 * 100

print('Moon cycle progress: {:.1f}%'.format(percent))


# In[12]:


# חישוב התקבצות וניגוד    

'''עבור כוכבי הלכת החיצוניים מאדים, צדק, שבתאי, אורנוס, וכל שאר הגופים מחוץ למסלולנו, 0 פירושו רגע החיבור עם השמש ו-1 פירושו רגע ההתנגדות.
מכיוון שהירח נע מזרחה על פני השמים שלנו ביחס לשמש, לא מערבה, הפלט מתהפך בהשוואה לכוכבי הלכת החיצוניים: 0 פירושו רגע ההתנגדות או ירח מלא, בעוד ש-1 פירושו רגע החיבור או ירח חדש.
כוכבי הלכת הפנימיים מרקורי ונוגה חווים רק קשרים עם השמש מנקודת המבט שלנו, לעולם לא ניגודים, כאשר 0 מציין צירוף נחות ו-1 צירוף עליון'''


'''# אם רוצים להדפיס את כל המיקומים של ירח חדש במערך
for i in range(len(y)):
    if y[i] == 1:
        print(t[i].astimezone(israel))

# אם רוצים להדפיס רק את המיקום הראשון של התקבצות וניגוד במערך
for i in y:
    if y[i] == 0:
        hitkabzut = t[i].astimezone(location_timezone)
    if y[i] == 1:
        nigud = t[i].astimezone(location_timezone)'''

t0 = ts.utc(94, 1, 20)
t1 = ts.utc(94, 2, 8)
f = almanac.oppositions_conjunctions(eph, eph['moon'])
t, y = almanac.find_discrete(t0, t1, f)

print(t.utc_iso())
print(t.ut1_strftime())
print(t.utc_strftime())
print(y)


# In[3]:


# חישוב זריחה ושקיעה
# יבוא והגדרות
from pytz import timezone

israel = timezone('Israel')
utc = timezone('utc')

eph = load('de441s.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)
t0 = ts.ut1(500, 3, 21, 1)
t1 = ts.ut1(500, 3, 22, 1)
t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))

print(t.ut1_strftime())
asd = t.ut1_calendar()
print(t.utc_strftime())
print(y)
print(t.astimezone(israel))
print(t.astimezone(israel) - timedelta(seconds=int(t[0].delta_t)))

print(t[0].astimezone(israel))
#type(t - t.delta_t


print()
print()
print(t[0].ut1_calendar())
a = t[0]
print(a.tai_strftime())
print(a.tdb_strftime())
print(a.tt_strftime())
print(a.ut1_strftime())
print(a.utc_strftime())



# In[13]:





# In[ ]:





# In[38]:





# In[39]:





# In[29]:





# In[36]:


def cu_to_skyfield_time(cu_time):
    
    # המרת הזמן בחזרה מאיזור הזמן המקומי לאיזור הזמן של גריניץ כי כל חישובי סקייפילד הם במקור רק על אזור זמן גריניץ
    # אולי צריך להוסיף קודם בדיקה האם קיים איזור זמן כלומר שזה לא none###########
    cu_time = cu_time.astimezone(timezone('utc'))
        
    global is_ut1
       
    return ts.ut1(cu_time.year, cu_time.month, cu_time.day, cu_time.hour, cu_time.minute, cu_time.second+cu_time.microsecond/1e6) if is_ut1 else ts.from_datetime(cu_time)

def skyfield_to_cu_time(skyfield_time, requested_timezone):
    
    global is_ut1
    
    timescale="ut1_astimzone" if is_ut1 else "utc_astimzone"
    
    if timescale == "ut1_astimzone":
        a = skyfield_time.ut1_calendar()
        return datetime(a[0], a[1], a[2], a[3], a[4], int(a[5]), int((a[5] % 1) * 1e6), tzinfo=pytz.utc).astimezone(requested_timezone)

    elif timescale == "utc_astimzone":
        return skyfield_time.astimezone(requested_timezone)


# In[33]:


is_ut1 = False

import pytz
tt = datetime(*(2, 2, 3, 4, 5, 6, 758736), tzinfo=pytz.utc)

asd = cu_to_skyfield_time(tt)


# In[44]:


asd.utc


# In[34]:





# In[35]:


skyfield_to_cu_time(asd, timezone('utc'))


# In[47]:


t[0].


# In[85]:


a= (500, 3, 21, 3, 43, 25.435523843978444)


# In[87]:


datetime(a[0], a[1], a[2], a[3], a[4], int(a[5]), int((a[5] % 1) * 1e6), tzinfo=pytz.utc).astimezone(israel)


# In[62]:


rrr = (tt.year,tt.month,tt.day,tt.hour,tt.minute,tt.second,tt.microsecond)


# In[56]:


rrr


# In[72]:


aaaa = ts.ut1(1,2,3,4,5,6,7,8,9)


# In[ ]:


aaaa.astimezone(israel)


# In[52]:





# In[57]:





# In[11]:


from datetime import datetime
import pytz

# צור אובייקט datetime
dt = datetime(1, 1, 1, 1, 1, 1, tzinfo=pytz.utc)


# In[58]:


year = 2024
time = skyfield_to_cu_time(ts.now(), location_timezone)




# In[60]:


import pytz
(datetime(1900, 1, 1, tzinfo=pytz.utc) + timedelta(seconds=60)).astimezone(timezone('Israel'))


# In[57]:


from datetime import datetime, timedelta
import pytz

transit_mean = (datetime(1900, 1, 1, tzinfo=pytz.utc) + timedelta(seconds=100)).astimezone(pytz.timezone('Israel'))
print(transit_mean)


# In[54]:


timezone('Israel'))transit_mean


# In[9]:


datetime(*(1,1,1,1,1,1)).astimezone(israel)


# In[24]:


from datetime import datetime

# המחרוזת שאתה רוצה להמיר
a = '0023-03-21 03:43:55 UT1'

# ממיר את המחרוזת לפורמט datetime
date_time_obj = datetime.strptime(a, '%Y-%m-%d %H:%M:%S UT1')

# הדפסה של המשתנה החדש בפורמט שלך
new_format = date_time_obj.strftime('%Y-%m-%d %H:%M:%S UT1')
print(new_format)  # אמור להדפיס: 0023-03-21 03:43:55 UT1


# In[70]:


# יצירת מילון לאחסון המידע
data = {2023: {"jerusalem": datetime(1,1,1)}}


# In[76]:


data[year]


# In[71]:


year = 2023
location = "jerusalem"
transit_mean = datetime(1,1,1)


# In[72]:


if year in data.keys() and location == data[year][location]:
    print("ddd")


# In[40]:


ts = load.timescale(builtin=False)


# In[8]:


173 - -21


# In[9]:


-173 - +21


# In[10]:


173 - +21


# In[32]:





# In[ ]:





# In[61]:





# In[62]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[48]:





# In[38]:





# In[44]:


ss = [transits[41],transits[306]]


# In[29]:





# In[32]:





# In[ ]:





# In[27]:


##### מחשבון לחישוב השפעת גובה במטרים על זריחה ושקיעה
# התוצאה שונה ממה שכתוב בתוכנת סול אט אומברה אבל אני יודע שהבעיה היא בסול אט אומברה 
# אבל המציאות המדוייקת היא כמו לוחות חי באינטרנט וכמו שראיתי בעין ולגובה 320 מטר האיחור הוא 0.522 מעלות וזה מתאים פה לאיחור עבור גובה 265 מטר ולא ברור למה
# לכן למעשה אם מחשבים כאן צריך להפחית 17.3 אחוז מהגובה האמיתי ועל זה לעשות את החישוב
# ואם מחשבים בסול אט אומברה צריך להפחית 31 אחוז מהגובה האמיתי ועל זה לעשות את החישוב, כדי שהוא יצא מתאים לאמת
# אבל החישוב המתמטי הטהור נותן תוצאה כמו כאן ולא כמו במציאות. השאלה למה המציאות שונה, האם בגלל שהרפרקציה בגובה יורדת?
from numpy import arccos
from skyfield.units import Angle

# When does the Sun rise in the ionosphere’s F-layer, 300km up?
altitude_m = 320 

# חישוב גובה אחרי הורדה של 17.3 אחוז
altitude_m_17 = altitude_m - (altitude_m * (17.3/100))

earth_radius_m = 6378136.6
side_over_hypotenuse = earth_radius_m / (earth_radius_m + altitude_m_17)
h = Angle(radians = -arccos(side_over_hypotenuse))
# עד כאן התוצאה הייתה עבור שקיעה גיאומטרית. אבל השקיעה של סוף עיגול השמש בגובה הנל כולל רפרקציה היא כך
alt_rise_set = h.degrees - -0.833
print(f'The horizon from {int(altitude_m)} meters up is at %.3f degrees' % h.degrees)
print(round(alt_set,3))


# In[18]:


# בדיקות חשובות מאוד של משוואת הזמן


# סקייפילד
from skyfield.api import N, S, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield.earthlib import refraction
from skyfield import almanac
from skyfield.units import Angle
from skyfield.nutationlib import iau2000b_radians

from skyfield.searchlib import find_discrete

# השורה הזו חשובה מאוד והיא מועתקת מתוך ספריית האלמנך
find_discrete

# תאריכים
import datetime as dt
from datetime import datetime, timedelta, date
from pytz import timezone

# חישובים
from numpy import cos, zeros_like, arccos


eph = load('de441s.bsp')

utc = timezone('utc')

location_timezone = utc

location = wgs84.latlon(0 * N, 0 * E)

ts = load.timescale(delta_t=0.0)

target_time = datetime(100,1,17) 

time = utc.localize(target_time)

# הגדרת הזמן לשעה שש בבוקר
time_6 = time.replace(hour=6, minute=0, second=0, microsecond=0)
    
# חישוב חצות היום והלילה בחיפוש בין שש בבוקר לשש בבוקר למחורת: נזכיר כי הזמן הוא כבר בשעון מקומי
meridian_transit = almanac.meridian_transits(eph, eph["sun"], location)
transit, y = almanac.find_discrete(ts.from_datetime(time_6), ts.from_datetime(time_6 + dt.timedelta(hours=24)), meridian_transit)
day_transit = transit[0].astimezone(location_timezone)
night_transit = transit[1].astimezone(location_timezone)


# הגדרת תאריך ההתחלה והסיום של השנה הגרגוריאנית המבוקשת, בשעון מקומי
datetime_greg_year_start = location_timezone.localize(datetime(target_time.year, 1, 1, 0, 0 ,0))
datetime_greg_year_end = location_timezone.localize(datetime(target_time.year, 12, 31, 23, 59 ,59))

# חישוב חצות היום והלילה עבור כל יום מימי השנה המבוקשת
transits, y = almanac.find_discrete(ts.from_datetime(datetime_greg_year_start), ts.from_datetime(datetime_greg_year_end), meridian_transit)
# איסוף כל חצות היום בלבד לפי השעה בשעון גריניץ עבור כל אחד מימי השנה לתוך מערך חדש
transits = [transits[i].utc for i in range(len(transits)) if y[i] == 1]

# המרה של שעת חצות היום של כל יום מימי השנה מ-שעות דקות ושניות - ל-שניות
total_seconds = sum(time.hour * 3600 + time.minute * 60 + time.second for time in transits)

# חישוב ממוצע של מספר השניות שזה בעצם חישוב של חצות ממוצע עבור כל השנה
average_seconds = total_seconds // len(transits)

# הפיכת הזמן שהתקבל לזמן פייתון (תחילת יממת שנת 1900 זה לא בדווקא)
mean_time = datetime(1900, 1, 1) + timedelta(seconds=average_seconds)

# Convert mean time back to string format
mean_time_str = mean_time.strftime('%H:%M:%S')

# חישוב חצות מקומי אמיתי של היום המבוקש בשעון גריניץ
transit_utc = day_transit.astimezone(timezone('utc'))

# שעון גריניץ של חצות הממוצע
transit_mean = transit_utc.replace(hour=mean_time.hour, minute=mean_time.minute, second=mean_time.second, microsecond=mean_time.microsecond)


delta_t = ts.from_datetime(day_transit).delta_t

transit_12 = transit_utc.replace(hour=12, minute=0, second=0, microsecond=0)

# בדיקת פער הזמן כלומר הדלתא בין שעה מקומית ממוצעת של חצות לבין השעה 12 בצהריים ובדיקה האם יש להוסיף דקות או להפחית דקות
if transit_mean < transit_12:
    error_delta_t = transit_12-transit_mean
    seconds_error_delta_t = error_delta_t.total_seconds()
    str_error_delta_t = f'+{str(error_delta_t)[2:7]}'
else:
    error_delta_t = transit_mean-transit_12
    seconds_error_delta_t = - error_delta_t.total_seconds()
    str_error_delta_t = f'-{str(error_delta_t)[2:7]}'

repaired_delta_t = delta_t + seconds_error_delta_t # חיבור כולל בתוכו חיסור כשיש מינוס

print("original_delta_t",delta_t)
print("seconds_eror_delta_t", seconds_error_delta_t)
print("repaired_delta_t",repaired_delta_t)
print("transit_utc",transit_utc)
print("transit_mean",transit_mean)


# בדיקת פער הזמן כלומר הדלתא בין שעת חצות המקומי לשעת חצות הממוצע שזה משוואת הזמן, ובדיקה האם משוואת הזמן מוסיפה דקות או מפחיתה דקות
if transit_utc < transit_mean:
    equation_of_time = transit_mean-transit_utc
    seconds_equation_of_time = equation_of_time.total_seconds()
    str_equation_of_time = f'+{str(equation_of_time)[2:7]}'
else:
    equation_of_time = transit_utc-transit_mean
    seconds_equation_of_time = - equation_of_time.total_seconds()
    str_equation_of_time = f'-{str(equation_of_time)[2:7]}'

print("str_equation_of_time",str_equation_of_time)


# In[ ]:


# בדיקות חשובות מאוד של פער דלטא-טי

# סקייפילד
from skyfield.api import N, S, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield.earthlib import refraction
from skyfield import almanac
from skyfield.units import Angle
from skyfield.nutationlib import iau2000b_radians

from skyfield.searchlib import find_discrete

# השורה הזו חשובה מאוד והיא מועתקת מתוך ספריית האלמנך
find_discrete

# תאריכים
import datetime as dt
from datetime import datetime, timedelta, date
from pytz import timezone

# חישובים
from numpy import cos, zeros_like, arccos


eph = load('de441s.bsp')

utc = timezone('utc')

location_timezone = utc

location = wgs84.latlon(0 * N, 0 * E)

ts = load.timescale(delta_t=0.0)

# יצירת מילון לאחסון תוצאות
results_dict = {}


# לולאה על כל שנה מ-2 עד 2999
for year in range(600, 800, 5):
    # יצירת תאריך ל-17 ליוני בשנה הנוכחית
    target_time = datetime(year, 6, 17)

    time = utc.localize(target_time)

    # הגדרת הזמן לשעה שש בבוקר
    time_6 = time.replace(hour=6, minute=0, second=0, microsecond=0)

    # חישוב חצות היום והלילה בחיפוש בין שש בבוקר לשש בבוקר למחורת: נזכיר כי הזמן הוא כבר בשעון מקומי
    meridian_transit = almanac.meridian_transits(eph, eph["sun"], location)
    transit, y = almanac.find_discrete(ts.from_datetime(time_6), ts.from_datetime(time_6 + dt.timedelta(hours=24)), meridian_transit)
    day_transit = transit[0].astimezone(location_timezone)
    night_transit = transit[1].astimezone(location_timezone)


    # הגדרת תאריך ההתחלה והסיום של השנה הגרגוריאנית המבוקשת, בשעון מקומי
    datetime_greg_year_start = location_timezone.localize(datetime(target_time.year, 1, 1, 0, 0 ,0))
    datetime_greg_year_end = location_timezone.localize(datetime(target_time.year, 12, 31, 23, 59 ,59))

    # חישוב חצות היום והלילה עבור כל יום מימי השנה המבוקשת
    transits, y = almanac.find_discrete(ts.from_datetime(datetime_greg_year_start), ts.from_datetime(datetime_greg_year_end), meridian_transit)
    # איסוף כל חצות היום בלבד לפי השעה בשעון גריניץ עבור כל אחד מימי השנה לתוך מערך חדש
    transits = [transits[i].utc for i in range(len(transits)) if y[i] == 1]

    # המרה של שעת חצות היום של כל יום מימי השנה מ-שעות דקות ושניות - ל-שניות
    total_seconds = sum(time.hour * 3600 + time.minute * 60 + time.second for time in transits)

    # חישוב ממוצע של מספר השניות שזה בעצם חישוב של חצות ממוצע עבור כל השנה
    average_seconds = total_seconds // len(transits)

    # הפיכת הזמן שהתקבל לזמן פייתון (תחילת יממת שנת 1900 זה לא בדווקא)
    mean_time = datetime(1900, 1, 1) + timedelta(seconds=average_seconds)

    # Convert mean time back to string format
    mean_time_str = mean_time.strftime('%H:%M:%S')

    # חישוב חצות מקומי אמיתי של היום המבוקש בשעון גריניץ
    transit_utc = day_transit.astimezone(timezone('utc'))

    # שעון גריניץ של חצות הממוצע
    transit_mean = transit_utc.replace(hour=mean_time.hour, minute=mean_time.minute, second=mean_time.second, microsecond=mean_time.microsecond)


    delta_t = ts.from_datetime(day_transit).delta_t

    transit_12 = transit_utc.replace(hour=12, minute=0, second=0, microsecond=0)

    # בדיקת פער הזמן כלומר הדלתא בין שעה מקומית ממוצעת של חצות לבין השעה 12 בצהריים ובדיקה האם יש להוסיף דקות או להפחית דקות
    if transit_mean < transit_12:
        error_delta_t = transit_12-transit_mean
        seconds_error_delta_t = error_delta_t.total_seconds()
        str_error_delta_t = f'+{str(error_delta_t)[2:7]}'
    else:
        error_delta_t = transit_mean-transit_12
        seconds_error_delta_t = - error_delta_t.total_seconds()
        str_error_delta_t = f'-{str(error_delta_t)[2:7]}'

    repaired_delta_t = delta_t + seconds_error_delta_t # חיבור כולל בתוכו חיסור כשיש מינוס
    
    # עדכון המילון בערך המתוקן של דלטא_טי עבור השנה המתאימה
    results_dict[year] = repaired_delta_t
    
    #print("original_delta_t",delta_t)
    #print("seconds_eror_delta_t", seconds_error_delta_t)
    #print("repaired_delta_t",repaired_delta_t)
    #print("transit_utc",transit_utc)
    #print("transit_mean",transit_mean)

results_dict


# In[ ]:





# In[ ]:





# In[ ]:


# חישובי זריחה ושקיעה עבור כל כוכב לכת
# כדי לקבל חישוב לפי מרכז השמש צריך להגדיר את רדיוס על 0 
# כדי לקבל אופק של שקיעה וזריחה נראים כולל רפרקציה צריך להגדיר הוריזון של מינוס 0.833

eph = load(r'C:\de421.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)
t0 = ts.utc(2022, 8, 15)
t1 = ts.utc(2022, 8, 16)
f = almanac.risings_and_settings(eph, eph['sun'], bluffton, horizon_degrees= 0, radius_degrees= 0)
t, y = almanac.find_discrete(t0, t1, f)

# for ti, yi in zip(t, y):
#    print(ti.astimezone(zone), 'Rise' if yi else 'Set')
    

print(f' זריחה: {t[0].astimezone(zone)}')
print(f' שקיעה: {t[1].astimezone(zone)}')


#--------------------------------------------------------

# זריחה ושקיעה גיאומטריים של השמש

eph = load(r'C:\de421.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)
t0 = ts.utc(2022, 8, 15)
t1 = ts.utc(2022, 8, 16)
f = almanac.risings_and_settings(eph, eph['sun'], bluffton, horizon_degrees= 0, radius_degrees= 0)
t, y = almanac.find_discrete(t0, t1, f)
  
print(f' זריחה גיאומטרית שמש: {t[0].astimezone(zone)}')
print(f' שקיעה גיאומטרית שמש: {t[1].astimezone(zone)}')


# זריחה ושקיעה מישוריים נראים של השמש

eph = load(r'C:\de421.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)
t0 = ts.utc(2022, 8, 15)
t1 = ts.utc(2022, 8, 16)
f = almanac.risings_and_settings(eph, eph['sun'], bluffton, horizon_degrees= -0.833, radius_degrees= 0)
t, y = almanac.find_discrete(t0, t1, f)
  
print(f' זריחה מישורית שמש: {t[0].astimezone(zone)}')
print(f' שקיעה מישורית שמש: {t[1].astimezone(zone)}')


# זריחה ושקיעה מישוריים נראים של הירח
# יש לשים לב שעבור הירח כנראה שתמיד המיקום ה[0] הוא שקיעה והמיקום ה[1] הוא זריחה???
eph = load(r'C:\de421.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)
t0 = ts.utc(2022, 8, 15)
t1 = ts.utc(2022, 8, 16)
f = almanac.risings_and_settings(eph, eph['moon'], bluffton, horizon_degrees= -0.833, radius_degrees= 0)
t, y = almanac.find_discrete(t0, t1, f)
  
print(f' זריחה גיאומטרית ירח: {t[1].astimezone(zone)}')
print(f' שקיעה גיאומטרית ירח: {t[0].astimezone(zone)}')


# In[ ]:


# חישוב חצות היום והלילה
from skyfield.api import N, S, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield.earthlib import refraction
from skyfield import almanac
from skyfield.units import Angle
from skyfield.nutationlib import iau2000b_radians

from skyfield.searchlib import find_discrete

ts = load.timescale()
eph = load_file('441ss.bsp')
bluffton = wgs84.latlon(31.940826 * N, 35.037057 * E)



# יבוא והגדרות
from pytz import timezone

israel = timezone('Israel')
utc = timezone('utc')

# המרה מתאריך ושעה מקומיים בישראל, לתאריך ושעה בגריניץ
time = israel.localize(datetime(400, 10, 4, 21, 21, 21))


# הגדרת הזמן לשעה שש בבוקר
time_6 = time.replace(hour=6, minute=0, second=0, microsecond=0)

ts = load.timescale()

# חישוב חצות היום והלילה בחיפוש בין שש בבוקר לשתיים בלילה: נזכיר כי הזמן הוא כבר בשעון מקומי
meridian_transit = almanac.meridian_transits(eph, eph["sun"], location)
transit, y = almanac.find_discrete(ts.from_datetime(time_6), ts.from_datetime(time_6 + dt.timedelta(hours=20)), meridian_transit)
day_transit = transit[0].astimezone(location_timezone)
night_transit = transit[1].astimezone(location_timezone)

#t0 = israel.localize(datetime(2023, 10, 4, 6, 0, 0))
#t1 = israel.localize(datetime(2023, 10, 5, 2, 0, 0))
#t0 = ts.from_datetime(t0)
#t1 = ts.from_datetime(t1)

#t0 = utc.localize(datetime(400, 10, 4, 6, 0, 0))
#t1 = utc.localize(datetime(400, 10, 5, 2, 0, 0))
#t0 = ts.from_datetime(t0)
#t1 = ts.from_datetime(t1)

print("t0", t0.utc_strftime('%Y-%m-%d %H:%M'))
print("t1", t1.utc_strftime('%Y-%m-%d %H:%M'))


#t0 = ts.utc(200, 10, 4, 6)
#t1 = ts.utc(200, 10, 5, 2)
f = almanac.meridian_transits(eph, eph['sun'], bluffton)
t, y = almanac.find_discrete(t0, t1, f)

print(t.utc_strftime('%Y-%m-%d %H:%M'))
print(y)
print([almanac.MERIDIAN_TRANSITS[yi] for yi in y])

t


# In[ ]:


# מציאת מיקום של גוף שמיימי אזימוט וגובה

# יבוא החבילות הנדרשות
from skyfield.api import load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield import almanac
from skyfield.api import N,S,E,W, wgs84

eph = load('de421.bsp')

# הגדרות משתנים מתוך קובץ הנתונים מנאסא
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']


# Altitude and azimuth in the sky of a
# specific geographic location
bluffton = earth + wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)
# boston = earth + wgs84.latlon(42.3583 * N, 71.0603 * W, elevation_m=43)
#astro = bluffton.at(ts.utc(1980, 3, 1)).observe(sun)
astro = bluffton.at(ts.now()).observe(sun)
app = astro.apparent()

alt, az, distance = app.altaz()
# תיקון למספר מוזר שיוצא כאשר השמש בגובה 0 מעלות
if alt.degrees < 0.0001:
    alt.degrees = 0.0

print(f'alt: {alt.degrees}')
print(f'az: {az.degrees}')
print(f'dist: {distance}')
print("")
print(alt.dstr())
print(az.dstr())
print(f'dist: {distance}')



ha, dec, distance = app.hadec()

print("")

print('Hour Angle:', ha)
print('Declination:', dec, )
print('Distance:', distance)
print(ts.now().astimezone(israel))


# In[ ]:


# מציאת מיקום של גוף שמיימי אזימוט וגובה, בתאריך ושעה מסויימים במיקום גיאוגרפי מסויים
##################### משודרג מאוד לא למחוק!!!!!!! ##########


#------------------------------------------------

# ראשית, המרה מתאריך ושעה מקומיים בישראל, לתאריך ושעה בגריניץ ולהיפך

# יבוא והגדרות
from pytz import timezone

israel = timezone('Israel')
utc = timezone('utc')

# המרה מתאריך ושעה מקומיים בישראל, לתאריך ושעה בגריניץ
israel_time = israel.localize(datetime(2022, 8, 18, 21, 21, 21))
utc_time_from_israel_time = israel_time.astimezone(utc)

# המרה מתאריך ושעה בשעון גריניץ, לתאריך ושעה בשעון ישראל
utc_time = utc.localize(datetime(2018, 10, 15, 2, 23, 45))
israel_time_from_utc_time = utc_time.astimezone(israel)

#------------------------------------------------------------


# יבוא החבילות הנדרשות
from skyfield.api import load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield import almanac
from skyfield.api import N,S,E,W, wgs84
import datetime


eph = load_file(r'C:\de421.bsp')

# הגדרות משתנים מתוך קובץ הנתונים מנאסא
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# הגדרת הזמן
ts = load.timescale()
t = ts.utc(utc_time_from_israel_time)

# Altitude and azimuth in the sky of a
# specific geographic location
bluffton = earth + wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0)
# boston = earth + wgs84.latlon(42.3583 * N, 71.0603 * W, elevation_m=43)
#astro = bluffton.at(ts.utc(1980, 3, 1)).observe(sun)
#astro = bluffton.at(ts.now()).observe(sun)
astro = bluffton.at(t).observe(sun)
app = astro.apparent()

alt, az, distance = app.altaz()
print(f'alt: {alt.degrees}')
print(f'az: {az.degrees}')
print(f'dist: {distance}')


ha, dec, distance = app.hadec()

print("")

print('Hour Angle:', ha)
print('Declination:', dec, )
print('Distance:', distance)


# In[ ]:


# מציאת מיקום של גוף שמיימי עלייה ישרה ונטייה

# Apparent RA/Dec.

# The “d =” line from the previous example,
# rewritten to give each position a name.

barycentric = earth.at(t)
astrometric = barycentric.observe(sun)
apparent = astrometric.apparent()
d = apparent.distance()


# הגדרת הזמן 
ts = load.timescale()
#t = ts.utc(2022, 8, 10, 5, 52)
t = ts.now()

# עלייה והטיה נכון לכאורה לצורך תצפית בטלסקופ וכן בסול אט אומברה
ra, dec, distance = apparent.radec('date')

# עלייה וירידה ימין אסטרומטרית
#ra, dec, distance = apparent.radec()

print('RA:', ra)
print('Dec:', dec)
print('Distance:', distance)


# In[ ]:


# חישוב זריחה ושקיעה באמצעות קביעת רפרקציה אישית

from skyfield.earthlib import refraction

#r = refraction(0.0, temperature_C=15.0, pressure_mbar=1030.0)
r = refraction(0.0, temperature_C=14.4, pressure_mbar=998.7)
print('Arcminutes refraction for body seen at horizon: %.2f\n' % (r * 60.0))

f = almanac.risings_and_settings(eph, eph['Sun'], bluffton, horizon_degrees=-r)
t, y = almanac.find_discrete(t0, t1, f)

for ti, yi in zip(t, y):
    print(ti.utc_iso(), 'Rise' if yi else 'Set')


# In[ ]:


# ניסיון עריכה שלי לפונקצציה מובנית של כל הדמדומים

# יבוא החבילות הנדרשות
from skyfield.api import N, E, W, wgs84, load, load_file
from skyfield.framelib import ecliptic_frame
from skyfield import almanac
import datetime as dt
from pytz import timezone
from skyfield.nutationlib import iau2000b_radians
from numpy import cos, zeros_like

ephemeris = load_file('de440.bsp')
topos = wgs84.latlon(31.940826 * N, 35.037057 * E, elevation_m=0) 

def dark_twilight_day(ephemeris, topos):
    """Build a function of time returning whether it is dark, twilight, or day.

    The function that this returns will expect a single argument that is
    a :class:`~skyfield.timelib.Time` and will return:

    | 0 — Dark of night.
    | 1 — Astronomical twilight.
    | 2 — Nautical twilight.
    | 3 — Civil twilight.
    | 4 — Sun is up.

    """
    sun = ephemeris['sun']
    topos_at = (ephemeris['earth'] + topos).at

#    def is_it_dark_twilight_day_at(t):
#        """Return whether the Sun is up, down, or whether there is twilight."""
#        t._nutation_angles_radians = iau2000b_radians(t)
#        degrees = topos_at(t).observe(sun).apparent().altaz()[0].degrees
#        r = zeros_like(degrees, int)
#        r[degrees >= -18.0] = 1
#        r[degrees >= -12.0] = 2
#        r[degrees >= -6.0] = 3
#        r[degrees >= -0.8333] = 4
#        return r

# זו חלופה שלי שכוללת מציאת דמדומים הלכתיים    
    def is_it_dark_twilight_day_at(t):
        """Return whether the Sun is up, down, or whether there is twilight."""
        t._nutation_angles_radians = iau2000b_radians(t)
        degrees = topos_at(t).observe(sun).apparent().altaz()[0].degrees
        r = zeros_like(degrees, int)
        r[degrees >= -25.9] = 1
        r[degrees >= -19.75] = 2
        r[degrees >= -18.0] = 3
        r[degrees >= -15.99] = 4
        r[degrees >= -15.194] = 5
        r[degrees >= -12.0] = 6
        r[degrees >= -10.2] = 7
        r[degrees >= -8.5] = 8
        r[degrees >= -6.0] = 9
        r[degrees >= -4.61] = 10
        r[degrees >= -4.37] = 11
        r[degrees >= -4.239] = 12
        r[degrees >= -3.65] = 13
        r[degrees >= -1.37] = 14
        r[degrees >= -0.8333] = 15
        r[degrees >= 0.0] = 16
        r[degrees >= +1.5] = 17
        return r

    is_it_dark_twilight_day_at.step_days = 0.04  # catch days at least an hour long
    return is_it_dark_twilight_day_at


TWILIGHTS = {
    0: 'Night',
    1: 'Alot Hashachar and Tzet Hacochavim -25.9',
    2: '-19.75',
    3: 'Astronomical twilight -18.0',
    4: '-15.99',
    5: '-15.194',
    6: 'Nautical twilight -12.0',
    7: '-10.2',
    8: '-8.5',
    9: 'Civil twilight -6.0',
    10: '-4.61',
    11: '-4.37',
    12: '-4.239',
    13: '-3.65',
    14: '-1.37',
    15: '-0.8333',
    16: '0.0',
    17: '+1.5',
}


ss = dark_twilight_day(ephemeris, topos)


zone = timezone('Israel')
now = zone.localize(dt.datetime.now())
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
next_midnight = midnight + dt.timedelta(days=1)

ts = load.timescale()
t0 = ts.from_datetime(midnight)
t1 = ts.from_datetime(next_midnight)
#eph = load_file(r'C:\de421.bsp')
#bluffton = wgs84.latlon(40.8939 * N, 83.8917 * W)
#f = almanac.dark_twilight_day(eph, bluffton)
times, events = almanac.find_discrete(t0, t1, ss)



previous_e = ss(t0).item()
for t, e in zip(times, events):
    tstr = str(t.astimezone(zone))[:19]
    if previous_e < e:
        print(tstr, ' ', TWILIGHTS[e], 'starts')
    else:
        print(tstr, ' ', TWILIGHTS[previous_e], 'ends')
    previous_e = e


# In[ ]:


previous_e


# In[ ]:


times[2].astimezone(zone)


# In[ ]:


a = "Ss"


# In[ ]:


a


# In[ ]:




