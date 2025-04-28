import math
from abc import ABC, abstractmethod

class QueueModel(ABC):
    """Base class for all queueing models."""
    
    def __init__(self, arrival_rate, service_rate):
        """
        Initialize the queueing model.
        
        Args:
            arrival_rate (float): Average arrival rate (lambda)
            service_rate (float): Average service rate (mu)
        """
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.rho = self.calculate_utilization()
        
    def calculate_utilization(self):
        """Calculate and return the utilization factor (rho)."""
        return self.arrival_rate / self.service_rate
    
    @abstractmethod
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        pass
        
    @abstractmethod
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        pass
    
    @abstractmethod
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        pass
    
    @abstractmethod
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        pass
    
    @abstractmethod
    def probability_idle(self):
        """Calculate and return the probability that the system is idle."""
        pass
    
    @abstractmethod
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        pass
        
    @abstractmethod
    def probability_all_servers_busy(self):
        """Calculate and return the probability that all servers are busy (Pw)."""
        pass
