import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.event import FileSystemEventHandler

from_dir = "C:\Users\dr_ar\downloads"


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print (f"Oops! Someone deleted {event.src_path}!")
    def on_modified(self, event):
        print (f"Someone modified {event.src_path}!")
    def on_deleted(self, event):
        print (f"Someone moved {event.src_path}!")

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()