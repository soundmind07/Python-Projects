# made a desktop notifier using python.


from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital and recharges body as well thus increasing productivity.",
            timeout=5  # display time
            )
        time.sleep(10)  # wait time. 



# to run file in background use pythonw file.py format.


