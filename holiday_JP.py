#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:55:30 2021

@author: hiroakikato
"""
import datetime
import jpholiday

def isBizDay(DATE):
    Date = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if Date.weekday() >= 5 or jpholiday.is_holiday(Date):
        return 0
    else:
        return 1

holiday = isBizDay(datetime.date.today().strftime('%Y%m%d'))

if holiday == 0:
    print("weekend or holiday")
else:
    print("weekday")