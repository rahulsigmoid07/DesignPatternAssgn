# DesignPatternAssgn
### Weather Monitoring System
The subject is a weather station that collects temperature, humidity, and pressure data, and the observers are display devices that show the weather data.
The code consists of the following classes:
1. WeatherStation: This is the subject class that maintains the weather data and the list of observers. It has methods to register and unregister observers, notify observers of any changes, and set the weather data.
2. DisplayDevice: This is the abstract observer class that defines the update method that must be implemented by the concrete observers. It is an abstract class because it contains an abstract method.
3. 'MobileApp', 'WebInterface', and 'DesktopApplication': These are the concrete observer classes that implement the update method to display the weather data.<br/>

<img width="623" alt="Screenshot 2023-06-19 at 10 52 46 PM" src="https://github.com/rahulsigmoid07/DesignPatternAssgn/assets/123542137/323087cd-6cf3-406c-be9a-f3d18c6fc7b2">

The code demonstrates how to use the Observer Pattern to notify multiple observers of changes to the subject. It creates a weather station object, display devices (observers), and registers the display devices as observers of the weather station. It then updates the weather data and notifies the observers of the changes. Finally, it unregisters one of the display devices and updates the weather data again.

###  vehicle manufacturing system
This code demonstrates the Factory Design Pattern, which is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. In this example, the factory creates different types of vehicles, such as cars, motorcycles, and trucks.
The code consists of the following classes:
1. Vehicle: This is the abstract superclass that defines the common properties of all vehicles. It has an abstract method display_details that must be implemented by the concrete subclasses.
2. 'Car', 'Motorcycle', and 'Truck': These are the concrete subclasses that extend the Vehicle class and implement the display_details method to display the details of the specific type of vehicle.
3. VehicleFactory: This is the factory class that creates the different types of vehicles based on the input. <br/>

<img width="595" alt="Screenshot 2023-06-19 at 10 52 28 PM" src="https://github.com/rahulsigmoid07/DesignPatternAssgn/assets/123542137/bae9eecf-9ac4-4594-833c-6327f06e04ee">

The code demonstrates how to use the Factory Design Pattern to create objects without exposing the instantiation logic to the client. It creates a VehicleFactory object and uses it to create different types of vehicles. The VehicleFactory class decides which type of vehicle to create based on the input, and returns the appropriate object.
