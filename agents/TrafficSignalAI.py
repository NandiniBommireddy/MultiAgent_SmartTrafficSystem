import random

class TrafficSignalAI:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, num_actions=2):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.num_actions = num_actions  # Number of actions: 0 = Green, 1 = Red
        self.q_table = {}  # For storing state-action values

    def get_state(self, traffic_density):
        """
        Defines states based on traffic density.
        For simplicity, we can classify traffic density into buckets
        """
        return int(traffic_density / 10)  # Example: traffic density in ranges

    def choose_action(self, state):
        """
        Epsilon-greedy strategy: explore vs exploit
        """
        if state not in self.q_table:
            self.q_table[state] = [0] * self.num_actions  # Initialize actions for that state

        epsilon = 0.1  # Exploration factor
        if random.random() < epsilon:
            return random.choice(range(self.num_actions))  # Explore
        else:
            return self.q_table[state].index(max(self.q_table[state]))  # Exploit best action

    def update_q_value(self, state, action, reward, next_state):
        """
        Update the Q-value using the Q-learning update rule
        """
        if next_state not in self.q_table:
            self.q_table[next_state] = [0] * self.num_actions

        max_future_q = max(self.q_table[next_state])  # Max Q value for next state
        current_q = self.q_table[state][action]
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[state][action] = new_q

    def simulate(self, traffic_density):
        """
        Simulates traffic signal decision-making
        """
        state = self.get_state(traffic_density)
        action = self.choose_action(state)
        
        # Assume rewards based on congestion. Reducing congestion gives positive rewards.
        reward = -traffic_density if action == 0 else traffic_density  # Red/Green actions reward
        next_state = state  # Same state after action
        
        # Update Q-value based on the action and reward
        self.update_q_value(state, action, reward, next_state)
        
        return action
