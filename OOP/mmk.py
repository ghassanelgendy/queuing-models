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
        
        self.rho = self.arrival_rate / (self.num_servers * self.service_rate)
        
        # Validate stability condition
      
    def calculate_utilization(self):
        """Calculate and return the utilization factor (rho)."""
        if hasattr(self, 'num_servers'):
            return self.arrival_rate / (self.num_servers * self.service_rate)
        else:
            return self.arrival_rate / self.service_rate
    
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        sum_terms = sum((self.arrival_rate/self.service_rate)**n / math.factorial(n) for n in range(self.num_servers))
        last_term = (self.arrival_rate/self.service_rate)**self.num_servers / (math.factorial(self.num_servers) * (1 - self.rho))
        return 1.0 / (sum_terms + last_term)
    
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
        lamda = self.arrival_rate
        mu = self.service_rate
        k = self.num_servers
        p0 = self.probability_idle()
        
        return ((lamda/mu)**k * lamda * mu) / (math.factorial(k-1) * (k*mu - lamda)**2) * p0
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        lamda = self.arrival_rate
        mu = self.service_rate
        k = self.num_servers
        p0 = self.probability_idle()
        
        return ((lamda/mu)**k * lamda * mu) / (math.factorial(k-1) * (k*mu - lamda)**2) * p0 + lamda/mu
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        lamda = self.arrival_rate
        mu = self.service_rate
        k = self.num_servers
        p0 = self.probability_idle()
        
        return ((lamda/mu)**k * mu) / (math.factorial(k-1) * (k*mu - lamda)**2) * p0
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        lamda = self.arrival_rate
        mu = self.service_rate
        k = self.num_servers
        p0 = self.probability_idle()
        
        return ((lamda/mu)**k * mu) / (math.factorial(k-1) * (k*mu - lamda)**2) * p0 + 1/mu
    
    def probability_all_servers_busy(self):
        """Calculate and return the probability that all servers are busy (Pw)."""
        k = self.num_servers
        p0 = self.probability_idle()
        
        return (1/math.factorial(k)) * (self.arrival_rate/self.service_rate)**k * (k*self.service_rate/(k*self.service_rate - self.arrival_rate)) * p0
        