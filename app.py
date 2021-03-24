from LearningClasses import vehicle
from LearningClasses import fruits
from LearningClasses import bank

my_car = vehicle.Vehicle("Volswagen",
                         "Polo",
                         (135,135,135),
                         False)

print(my_car.getBrand())
print(my_car.getModel())
print(my_car.getColor())
print(my_car.getEle())

my_ingredients = fruits.Fruit("Apple", (255,0,0), True)

print(my_ingredients.getMakejam())

my_bankdetails = bank.Bank(10391123, "Ayush Yadav", 20.03)

print(my_bankdetails.getAccno())
print(my_bankdetails.getName())
print(my_bankdetails.getDeposit())