# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:54:17 2023

@author: Abhishek
"""

import instaloader as i
insta=i.Instaloader()
account=input("Enter Instagram id:-")
insta.download_profile(account,profile_pic_only=False)
