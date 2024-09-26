cars = ["Ford", "Volvo", "BMW", "Mitsubishi", "Toyota", "Lamborghini", "Rolls Royce"]
cars.append("Honda")
print(f"The cars in the list are: {cars}")
cars[-1] = "Austin Martin"
cars[2] = "Chevy"
print(f"The list of cars are now: {cars}")
cars.insert(2, "Jeep")
print(f"The list of cares are now: {cars}")
cars.remove("Jeep")
print(f"The list of cares are now: {cars}")
check = ("Toyota" in cars)
print(f"The statement that Toyota is in the list is {check}")