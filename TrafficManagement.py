from agents.TrafficSignalAI import TrafficSignalAI
from agents.VehicleRoutingAI import VehicleRoutingAI
from agents.EmergencyVehicleAI import EmergencyVehicleAI

class TrafficManagementSystem:
    def __init__(self):
        self.signal_agent = TrafficSignalAI()
        self.routing_agent = VehicleRoutingAI()
        self.emergency_agent = EmergencyVehicleAI(self.signal_agent, self.routing_agent)

    def simulate(self, traffic_density, emergency_vehicle_route=None):
        """
        Simulate the traffic management system
        """
        result = ""

        if emergency_vehicle_route:
            # If an emergency vehicle is detected, prioritize its route
            emergency_route = self.emergency_agent.prioritize_emergency_vehicle(emergency_vehicle_route)
            result += f"Emergency Vehicle Route: {emergency_route}\n"

        # Simulate traffic signal behavior
        signal_action = self.signal_agent.simulate(traffic_density)
        result += f"Traffic Signal Action: {'Green' if signal_action == 0 else 'Red'}\n"

        # Simulate vehicle routing decision
        route_choice = self.routing_agent.choose_route('Route_A')
        result += f"Optimal Route for Vehicle: {route_choice}\n"

        return result
