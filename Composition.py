#composition is a class that exists inside of another class

class Car:
    def __init__(self,make,model,year,engine):
        self.make = make
        self.model =model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"{str(self.year)} {self.make} {self.model} with an {self.engine} engine"

#to access a composite class you need to call the place it's saved inside the class

class Engine:
    def __init__(self,configuration,displacement,horsepower,torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def __repr__(self) -> str:
        return f"{self.configuration} {str(self.displacement)}dsp {str(self.horsepower)}HP {str(self.torque)}T"

    def ignite(self):
        print("vroom vroom :D")

    

mycar = Car("Bear","Mauling",392,Engine("V8",5.8,326,344))
print(mycar)
mycar.engine.ignite()