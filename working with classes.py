class car:
    def __init__(self, make, model, year, color):
        self.model = model
        self.year = year
        self.make = make
        self.color = color


#for useless model of car '''def get_model(self):
 #   return self'''

#to encapsulate model in line 9, put an underscore -> self.__model


    def drive(self):
        print('this ' + self.model + ' is driving')
        

    def stop(self):
        print('This ' + self.model + ' is stopped')

car_1 = car('Chevy', 'corvette', 2012, 'blue')
car_1.drive()

         