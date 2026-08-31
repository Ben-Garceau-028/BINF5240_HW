
# EXERCISE 1.2
# Program input
cars = 100
people_per_car = 4 #dash to equal
drivers = 30
passengers = 90 #double equals

#Compute the dependent values
cars_not_driven = cars - drivers # would have to be minus
cars_driven = drivers # only one driver per car
carpool_capacity = cars_driven * people_per_car #
average_people_per_car = ( drivers + passengers ) // cars_driven # passengers is the variable # use double // for integer
people_in_last_car = ( drivers + passengers - 1 ) % people_per_car + 1 #changed minus 1, plus 1

# Output the results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.") # have to use cars not driven
print("We can transport", carpool_capacity, "people today.") # carpool capacity is people per car
print("We have", passengers, "to carpool today.") # not including drivers
print("We need to put about", average_people_per_car, "in each car.")
print("There are", people_in_last_car, "people in the last car.")

#Exercise 1.2: Write-Up
#Regarding the program input, it is all corrected to make containers or variables that consist of integers rather than decimals
    #as all variables should be expressed through whole numbers.
#Regarding the dependent variables,
    #the calculations were corrected to better represent their variables(i.e cars not driven would nt add the cars and the drivers, but would rather subtract.
#cars driven have to equal the amount of drivers.
    #Carppol capacity is the amount of cars multiplied by the number of people per car.
#The average people/car can be calculated by total individuals(drivers and passengers) by the amount of cars being driven, rounded to the nearest whole number.
#Overall, we corrected both mathematical and logical mistakes in the code. ***
