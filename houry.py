import schedule
import time
from playsound import playsound


# Find the sound
def beep():
    playsound('beep.wav')


# Schedule the time (every hour at :00)
schedule.every().hour.at(":00").do(beep)


# Loop the hole thing
while True:
    schedule.run_pending()
    time.sleep(1)
