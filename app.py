from time import sleep
from datetime import datetime
while True:
    print(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}: App is working ...")
    sleep(60)
