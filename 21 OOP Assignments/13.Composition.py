class Engine:
    def start(self):
        print("Engine Started")
        
class Car:
    def __init__(self, engine):
        self.engine = engine
    def start_car(self):
        self.engine.start()

x = Engine()
y = Car(x).start_car()
