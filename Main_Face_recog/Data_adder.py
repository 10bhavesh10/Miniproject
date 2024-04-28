# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:43:19 2022

@author: User
"""

import face_recognition
import pickle

''' Run for the first time to create the file

with open('facen.dat', 'wb') as f:
    all_face_encodings = {}
    pickle.dump(all_face_encodings, f)
    
with open('upi.dat', 'wb') as g:
    UPI={}
    pickle.dump(UPI, g)
'''
with open('facen.dat', 'rb') as f:
    all_face_encodings=pickle.load(f)
    
with open('upi.dat', 'rb') as g:    
    UPI=pickle.load(g)
    
image = face_recognition.load_image_file("image.jpg")    
all_face_encodings["Name"]=face_recognition.face_encodings(image)[0]

UPI["Name"]=str('cristianoronaldo@okicici')

with open('facen.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)
    
with open('upi.dat', 'wb') as g:    
    pickle.dump(UPI, g)