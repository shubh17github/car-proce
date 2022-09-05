
from flask import Flask,request,render_template
from utils.function import car
import numpy as np

app=Flask(__name__)

@app.route('/')

def index ():
    return render_template('car.html')

@app.route('/predict',methods=['GET','POST'])

def pred():

    if request.method=="POST":
        data=request.form
        km_drive=float(data['km'])
        mlg=float(data['mlg'])
        engine=float(data['engine'])
        power=float(data['power'])
        seat=float(data['seat'])
        age=int(data['age'])
        brand=data['brand']
        seller=data['seller']
        fuel=data['fuel']
        transmn=data['transmn']

    car_obj=car(km_drive,mlg,engine,power,seat,brand,seller,fuel,transmn,age)

    result=car_obj.predict()
    return render_template('car.html',prediction=result)

if __name__=="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)
        



