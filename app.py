# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from HumanConditions import HumanConditions
import pickle
#import numpy as np
#import pandas as pd

# 2. Create the app object
app = FastAPI()

model=pickle.load(open("NCalModel.pkl","rb"))

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Covid Prediction V1.1'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere

#@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To app file': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_Calories(data:HumanConditions):
    data = data.dict()  
   
    
   
    newData=[Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_0se, Asthma, Chronic_Lung_Disease, Headache, Heart_Disease, Diabetes, Hyper_Tension, Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places, Family_working_in_Public_Exposed_Places, Wearing_Masks, Sanitization_from_Market]
  
    predictedValue = model.predict([newData])
    
# convert numpy 
    converted_prediction=(predictedValue).tolist()[0]
   
    
    return {
        'Covid':converted_prediction
        
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
    
#uvicorn app:app --reload
