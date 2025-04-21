from queue import QueueModel
import math

class MMInf(QueueModel):
    """
    M/M/∞ Queue Model
    - Infinite servers
    - Infinite capacity
    - Infinite population
    - Everyone gets served instantly
    """
    
    def __init__(self, arrival_rate, service_rate):
        """
        Initialize the M/M/∞ queueing model.
        
        Args:
            arrival_rate (float): Average arrival rate (lambda)
            service_rate (float): Average service rate per server (mu)
        """
        super().__init__(arrival_rate, service_rate)
        # For M/M/∞, there's no concept of stability condition since
        # there are infinite servers
        
    def calculate_utilization(self):
        """
        Calculate and return the utilization factor.
        For M/M/∞, this doesn't have the same meaning as in other models
        but we return arrival_rate/service_rate for consistency.
        """
        return self.arrival_rate / self.service_rate
        
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        # For M/M/∞, the probability of idle system follows a Poisson distribution
        # with parameter a = lambda/mu
        a = self.arrival_rate / self.service_rate
        return math.exp(-a)
    
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        if n < 0:
            return 0
            
        # For M/M/∞, the number of customers follows a Poisson distribution
        # with parameter a = lambda/mu
        a = self.arrival_rate / self.service_rate
        return (a**n) * math.exp(-a) / math.factorial(n)
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        # For M/M/∞, this equals lambda/mu
        return self.arrival_rate / self.service_rate
    
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        # For M/M/∞, there's no queue since every customer gets a server immediately
        return 0
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        # For M/M/∞, this equals 1/mu
        return 1 / self.service_rate
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        # For M/M/∞, there's no queue since every customer gets a server immediately
        return 0
        
    def variance_customers(self):
        """Calculate and return the variance of the number of customers in the system."""
        # For Poisson distribution, variance equals mean
        return self.average_customers_in_system() 
        
    def probability_all_servers_busy(self):
        """Calculate and return the probability that all servers are busy (Pw)."""
        # For M/M/∞, this is 0 since there are infinite servers
        # so there's always a free server
        return 0 