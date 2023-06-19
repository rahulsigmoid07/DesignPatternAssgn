# Observer Pattern: Weather Monitoring System
from abc import ABC,abstractmethod
# Subject (Weather Station)
class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_weather_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Observer (Display Device)
class DisplayDevice(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Concrete Observers
class MobileApp(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Mobile App Display: Temperature={}, Humidity={}, Pressure={}"
              .format(temperature, humidity, pressure))


class WebInterface(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Web Interface Display: Temperature={}, Humidity={}, Pressure={}"
              .format(temperature, humidity, pressure))


class DesktopApplication(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Desktop Application Display: Temperature={}, Humidity={}, Pressure={}"
              .format(temperature, humidity, pressure))


# Usage example
if __name__ == "__main__":
    # Create weather station object
    weather_station = WeatherStation()

    # Create display devices (observers)
    mobile_app = MobileApp()
    web_interface = WebInterface()
    desktop_app = DesktopApplication()

    # Register display devices as observers
    weather_station.register_observer(mobile_app)
    weather_station.register_observer(web_interface)
    weather_station.register_observer(desktop_app)

    # Update weather data
    weather_station.set_weather_data(25, 70, 1013)

    # Unregister a display device
    weather_station.unregister_observer(web_interface)

    # Update weather data again
    weather_station.set_weather_data(27, 68, 1012)
