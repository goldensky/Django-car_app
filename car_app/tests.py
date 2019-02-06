from django.test import TestCase

from django.utils import timezone
import random
import time

from .models import TruckModel, TruckNumber, Post


# ./manage.py test      
# https://docs.djangoproject.com/en/2.1/topics/testing/overview/#running-tests

#model_name, max_capacity, model_description
print('Invoke tests')


class TruckModelTests(TestCase):
    random_unique_number = str(int(time.time() *10))
    
    def setUp(self):    
        print('Invoke TruckModelTests')
        
        model_name = 'TT' + self.random_unique_number
        print('model_name = ', model_name)
        model_max_capacity = 140

        TruckModel.objects.create(
            model_name=model_name, 
            max_capacity=model_max_capacity,
            model_description=f'New model {model_name} with max capacity {model_max_capacity}'
        )
        print('\n\nSuccess test model creation\n\n\n')
        
    def test_model(self):
        current_model_name = 'TT' + self.random_unique_number
        current_model = TruckModel.objects.get(model_name=current_model_name)
        self.assertEqual(current_model.model_name, current_model_name)
        self.assertEqual(current_model.max_capacity, 140)



#bort_number, model_name, current_weight, overload    
class TruckNumberTests(TestCase):
    random_unique_number = str(int(time.time() *10))
    
    def setUp(self):    
        print('Invoke TruckNumberTests')
        model_name = 'BELAZ'        
        number_current_weight = 125
        
        truck_number_description='Bort number {} with current weight {}'.format(
            self.random_unique_number, number_current_weight)
    
        new_trunc_number = TruckNumber(
            bort_number= self.random_unique_number, 
            current_weight=number_current_weight,
            truck_number_description=truck_number_description
            )
        new_trunc_number.overload = 0
        new_trunc_number.model_name = model_name
        new_trunc_number.save()
    
        print('\n\nSuccess test number creation  \n\n\n')
        

    def test_number(self):        
        current_number = TruckNumber.objects.get(bort_number=self.random_unique_number)        
        self.assertEqual(current_model.model_name, 'BELAZ')
        self.assertEqual(current_model.current_weight, 125)
    



    