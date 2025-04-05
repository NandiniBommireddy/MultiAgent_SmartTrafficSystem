# MultiAgent_SmartTrafficSystem
Multi-Agent Smart Traffic System
Overview
The Multi-Agent Smart Traffic System is an AI-powered solution to optimize urban traffic management. It uses a combination of traffic signal agents, vehicle routing agents, and emergency vehicle prioritization to improve overall traffic flow, reduce congestion, and ensure quick responses for emergency vehicles. The system dynamically adjusts traffic signals, routes vehicles, and integrates an AI-based toll pricing system to handle different traffic conditions.

--Features
AI-powered Traffic Signals: Traffic signals adjust dynamically based on traffic density to reduce congestion.

Emergency Vehicle Prioritization: Emergency vehicles are prioritized in the system to ensure they can reach their destination without delays.

Vehicle Routing: Vehicles are routed through the least congested routes in real-time.

AI-based Toll Pricing: Toll prices adjust dynamically based on congestion levels.

Simulations: Simulate different traffic scenarios like rush hour, accidents, and roadblocks.

Human-in-the-Loop: User-friendly interface for interacting with the system and controlling the simulations.

--Components
TrafficSignalAI: Handles dynamic adjustment of traffic signals based on traffic density.

VehicleRoutingAI: Decides optimal routes for vehicles based on current traffic conditions.

EmergencyVehicleAI: Prioritizes emergency vehicles by adjusting traffic signals and routes.

TollPricingAI: Calculates toll prices based on congestion levels.

TrafficManagementSystem: Coordinates the overall simulation and integrates all the components.

--Installation
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/multiagent_smarttraffic_system.git
cd multiagent_smarttraffic_system
2. Set up a virtual environment (optional but recommended):
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Running the Application
1. Start the Flask server:
bash
Copy
Edit
python app.py
The server will start and the app will be accessible at http://127.0.0.1:5000/.

2. Interact with the simulation:
Open the browser and navigate to http://127.0.0.1:5000/. You can enter traffic density, choose an emergency route (optional), and submit to simulate the traffic management system.

--How it Works
Traffic Simulation: When a user submits the form, the server runs a simulation based on the traffic density and emergency vehicle route.

Signal Management: The TrafficSignalAI agent simulates the traffic signal decision-making process based on the traffic density.

Route Selection: The VehicleRoutingAI agent determines the optimal route based on the current traffic conditions.

Emergency Vehicle Prioritization: The EmergencyVehicleAI agent adjusts the routes and traffic signals to prioritize emergency vehicles.

Toll Pricing: The TollPricingAI agent adjusts toll prices based on the current congestion levels.

--Example Usage
To simulate a scenario with a traffic density of 50 and prioritize emergency vehicles on Route A:

Enter a traffic density of 50 in the input field.

Select Route_A in the "Emergency Vehicle Route" dropdown.

Click "Simulate" to see the results.

The output will show the traffic signal action (Green/Red), the optimal route for vehicles, and the prioritized emergency vehicle route.
