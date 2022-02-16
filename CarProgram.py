import CarClass as c

def main():
    car = c.Car("2015 ModelX", "Tesla")
    print( "Accelerating the car's speed after accelerate.")
    
    for i in range(5):
        car.accelerate()
        print (car.get_speed())
        
    print ("Decelerating the car's speed after brake.")
    for i in range(5):
        car.brake()
        print (car.get_speed())

main()
    