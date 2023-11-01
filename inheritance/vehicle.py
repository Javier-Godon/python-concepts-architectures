from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass


class Car(Vehicle):

    def __init__(self, model: str):
        self.model = model

    def start_engine(self):
        print(f"Starting the engine of: {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of: {self.model}")

    def accelerate(self):
        print(f"Accelerating the : {self.model}")

    def brake(self):
        print(f"Applying car brakes of: {self.model}")


class VwGolf(Car):

    def __init__(self, model: str):
        super().__init__(model)

    def start_engine(self):
        print(f"Starting the engine of a VwGolf model: {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of a VwGolf model: {self.model}")

    def accelerate(self):
        print(f"Accelerating the VwGolf model : {self.model}")

    def brake(self):
        print(f"Applying car brakes of a VwGolf model: {self.model}")
