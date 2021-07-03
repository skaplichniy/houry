import schedule
import time
from playsound import playsound

def job():
    playsound('/Users/skaplichniy/PycharmProjects/houry/beep.wav')


schedule.every().hour.at(":00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

