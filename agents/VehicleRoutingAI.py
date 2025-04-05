import random

class VehicleRoutingAI:
    def __init__(self):
        self.routes = ['Route_A', 'Route_B', 'Route_C', 'Route_D']
        self.route_conditions = {'Route_A': 0, 'Route_B': 0, 'Route_C': 0, 'Route_D': 0}  # Traffic conditions (0 = clear, 1 = congested)

    def get_current_traffic(self, route):
        """Return traffic condition for a specific route (0 = clear, 1 = congested)"""
        return self.route_conditions[route]

    def choose_route(self, current_route):
        """AI-based decision for optimal route selection"""
        # Check traffic condition of available routes
        available_routes = [route for route in self.routes if self.get_current_traffic(route) == 0]
        
        if not available_routes:  # If all routes are congested, take the least congested one
            available_routes = [min(self.routes, key=lambda route: self.route_conditions[route])]
        
        # Choose a route randomly or based on traffic
        return random.choice(available_routes)

    def update_traffic_conditions(self, route, condition):
        """Update traffic conditions for a route"""
        self.route_conditions[route] = condition
