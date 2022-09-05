

import numpy as np
import config
import pickle
import json

class car():

    def __init__(self,km_driven,mileage,engine,max_power,seats,brand_name,seller_type,fuel_type,transmission_type,car_Age):
        " this function for accepting the user input"

        self.km_drive=km_driven
        self.mlg=mileage
        self.engine=engine
        self.power=max_power
  
        self.seat=seats
        self.brand=brand_name
        self.seller=seller_type
        self.fuel=fuel_type
        self.xmn=transmission_type
        self.age=car_Age


    def load_model(self):

        with open(config.model_file_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.col_dict_path,'r') as file:
            self.col_dict=json.load(file)

    def predict (self):

        self.load_model()

        array=np.zeros(len(self.col_dict['column']))

        array[0]=self.km_drive
        array[1]=self.mlg
        array[2]=self.engine
        array[3]=self.power
        array[4]=self.seat
        array[47]=self.age

        brand_value='brand_name_'+self.brand
        brand_index=self.col_dict['column'].index(brand_value)
        array[brand_index]=1

        seller_value='seller_type_'+self.seller
        seller_index=self.col_dict['column'].index(seller_value)
        array[seller_index]=1

        fuel_value='fuel_type_'+self.fuel
        fuel_index=self.col_dict['column'].index(fuel_value)
        array[fuel_index]=1

        trans_type_value='transmission_type_'+self.xmn
        trans_type_index=self.col_dict['column'].index(trans_type_value)
        array[trans_type_index]=1


        result=self.model.predict([array])

        return result[0]

       

        

