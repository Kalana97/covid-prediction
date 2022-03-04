# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: rash
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class HumanConditions(BaseModel):
    Breathing_Problem: int
    Fever: int
    Dry_Cough: int
    Sore_throat: int
    Running_0se: int
    Asthma: int
    Chronic_Lung_Disease: int
    Headache: int
    Heart_Disease: int
    Diabetes: int
    Hyper_Tension: int
    Abroad_travel: int
    Contact_with_COVID_Patient: int
    Attended_Large_Gathering: int
    Visited_Public_Exposed_Places: int
    Family_working_in_Public_Exposed_Places: int
    Wearing_Masks: int
    Sanitization_from_Market: int
    
    
