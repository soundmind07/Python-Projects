import pywhatkit as pw
import cv2
txt="""
Python is dynamically typed general purpose programming language that supports an object oriented as well as functional approach.
it is an interpreted and high level programming language. it is platform independent and has big library support.
"""
pw.text_to_handwriting(txt,save_to="demo1.jpeg")
print("END")
