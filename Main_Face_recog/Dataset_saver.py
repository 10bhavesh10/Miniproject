# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:23:15 2022

@author: User
"""

import face_recognition
import cv2
import numpy as np
import pandas as pd
import pickle

all_face_encodings = {}
harish_image = face_recognition.load_image_file("E:\\Damn\\Harish.jpg")
all_face_encodings["Harish"] = face_recognition.face_encodings(harish_image)[0]

arun_image = face_recognition.load_image_file("E:\\Damn\\Arun.jpg")
all_face_encodings["Arun"] = face_recognition.face_encodings(arun_image)[0]

aba_image = face_recognition.load_image_file("E:\\Damn\\Aba.jpg")
all_face_encodings["Aba"] = face_recognition.face_encodings(aba_image)[0]

bhavesh_image = face_recognition.load_image_file("E:\\Damn\\Bhavesh.jpg")
all_face_encodings["Bhavesh"] = face_recognition.face_encodings(bhavesh_image)[0]

raghav_image = face_recognition.load_image_file("E:\\Damn\\Raghav.jpg")
all_face_encodings["Raghav"] = face_recognition.face_encodings(raghav_image)[0]

abhay_image = face_recognition.load_image_file("E:\\Damn\\Abhay.jpg")
all_face_encodings["Abhay"] = face_recognition.face_encodings(abhay_image)[0]

hari_image = face_recognition.load_image_file("E:\\Damn\\Hari.jpg")
all_face_encodings["Hari"] = face_recognition.face_encodings(hari_image)[0]

UPI={}
UPI["Harish"]=str('harishjonsena@okaxis')
UPI["Arun"]=str("9786020894@upi")
UPI["Aba"]=str("abhiabarajith@okicici")
UPI["Bhavesh"]=str("bhaveshpay@upi")
UPI["Raghav"]=str("raghavn753@okicici")
UPI["Abhay"]=str("6309190023@patym")
UPI["Hari"]=str("hariharasudhan8129@okhdfc")

with open('facen.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)
    
with open('upi.dat', 'wb') as g:    
    pickle.dump(UPI, g)
