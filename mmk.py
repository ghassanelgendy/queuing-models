from queue import QueueModel
import math

class MMk(QueueModel):
    """
    M/M/k Queue Model
    - k servers
    - Infinite capacity
    - Infinite population
    - Multiple server queue
    """
    
    def __init__(self, arrival_rate, service_rate, num_servers):
        """
        Initialize the M/M/k queueing model.
        
        Args:
            arrival_rate (float): Average arrival rate (lambda)
            service_rate (float): Average service rate per server (mu)
            num_servers (int): Number of servers (k)
        """
        # Store num_servers before calling super() to make it available in calculate_utilization
        self.num_servers = num_servers
        
        super().__init__(arrival_rate, service_rate)
        
        # For M/M/k, we use a different definition of utilization
        self.rho = self.arrival_rate / (self.num_servers * self.service_rate)
        
        # Validate stability condition
        if self.rho >= 1:
            raise ValueError("System is unstable: arrival rate must be less than total service rate")
    
    def calculate_utilization(self):
        """Calculate and return the utilization factor (rho)."""
        if hasattr(self, 'num_servers'):
            return self.arrival_rate / (self.num_servers * self.service_rate)
        else:
            return self.arrival_rate / self.service_rate
    
    def erlang_c(self):
        """Calculate and return the Erlang C formula (probability all servers are busy)."""
        a = self.arrival_rate / self.service_rate
        k = self.num_servers
        
        # Calculate the sum term in the denominator
        sum_term = 0
        for n in range(k):
            sum_term += (a**n) / math.factorial(n)
        
        # Calculate the Erlang C formula
        numerator = (a**k) / math.factorial(k)
        denominator = numerator * (1 / (1 - self.rho)) + sum_term
        
        return numerator / denominator
    
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        a = self.arrival_rate / self.service_rate
        k = self.num_servers
        
        sum_term = 0
        for n in range(k):
            sum_term += (a**n) / math.factorial(n)
            
        return 1 / (sum_term + (a**k) / (math.factorial(k) * (1 - self.rho)))
    
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        if n < 0:
            return 0
            
        a = self.arrival_rate / self.service_rate
        k = self.num_servers
        p0 = self.probability_idle()
        
        if n <= k:
            return (a**n) / math.factorial(n) * p0
        else:
            return (a**n) / (math.factorial(k) * (k**(n-k))) * p0
    
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        a = self.arrival_rate / self.service_rate
        return self.erlang_c() * a * self.rho / (1 - self.rho)
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        return self.average_customers_in_queue() + (self.arrival_rate / self.service_rate)
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        return self.average_customers_in_queue() / self.arrival_rate
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        return self.average_time_in_queue() + (1 / self.service_rate) 