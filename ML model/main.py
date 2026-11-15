from fastapi import FastAPI
from schemas import inputschema,outputschema
from predict import make_prediction,make_batch_prediction
from typing import List

app=FastAPI()

@app.get('/')
def index():
    return {'message':'welcome to ml prediction API'}

@app.post('/prediction',response_model=outputschema)
def predict(user_input :inputschema):
    # converting the JSON to Dict form using model_dump
    prediction=make_prediction(user_input.model_dump())
    return outputschema(predicted_price=round(prediction,2))


@app.post('batch_prediction',response_model=List[outputschema])
def batch_prediction(user_inputs:List[inputschema]):
    predictions=make_batch_prediction(([x.model_dump() for x in user_inputs]))
    return [outputschema(predicted_price=round(prediction,2)) for prediction in predictions] 