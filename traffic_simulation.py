# traffic_simulation.py

from TrafficSignalAI import TrafficSignalAI
from VehicleRoutingAI import VehicleRoutingAI
from EmergencyVehicleAI import EmergencyVehicleAI
from TrafficManagement import TrafficManagementSystem

if __name__ == "__main__":
    tms = TrafficManagementSystem()
    
    # Test traffic density simulation
    traffic_density = 50  # Arbitrary value, can be changed to test different conditions
    emergency_route = 'Route_A'  # Choose a route to prioritize for emergency vehicles

    # Simulate with no emergency vehicle
    print(tms.simulate(traffic_density))
    
    # Simulate with an emergency vehicle
    print(tms.simulate(traffic_density, emergency_vehicle_route=emergency_route))
