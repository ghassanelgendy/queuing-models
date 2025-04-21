from mm1 import MM1
from mm1k import MM1K
from mm1m import MM1m
from mmk import MMk
from mminf import MMInf

def print_model_results(model, model_name):
    """Print the results for a queueing model."""
    print(f"\n{model_name} Model Results:")
    print(f"P0 - Probability that system is idle: {model.probability_idle():.4f}")
    
    # Print probability distribution for a few values
    print("Pn - Probability of n customers in the system:")
    for n in range(5):
        print(f"P({n}) = {model.probability_n_customers(n):.4f}")
        
    print(f"L - Average number of customers in the system: {model.average_customers_in_system():.4f}")
    print(f"Lq - Average number of customers in the queue: {model.average_customers_in_queue():.4f}")
    print(f"W - Average time spent in the system: {model.average_time_in_system():.4f}")
    print(f"Wq - Average time spent in the queue: {model.average_time_in_queue():.4f}")
    print(f"Pw - Probability that all servers are busy: {model.probability_all_servers_busy():.4f}")
    print(f"p - Utilization factor of each server: {model.rho:.4f}")

def main():
    # Parameters
    arrival_rate = float(input("Enter the arrival rate (cx per hour): "))  
    service_rate = float(input("Enter the service rate (cx per hour): "))       # 8 customers served per hour
    
    print("Queuing Models Example")
    print("======================")
    print(f"Arrival rate (λ): {arrival_rate} customers/hour")
    print(f"Service rate (μ): {service_rate} customers/hour")
    
    # M/M/1 model
    try:
        mm1_model = MM1(arrival_rate, service_rate)
        print_model_results(mm1_model, "M/M/1")
    except ValueError as e:
        print(f"\nM/M/1 Model: {e}")
    
    # M/M/1/K model (finite buffer)
    capacity = 10
    mm1k_model = MM1K(arrival_rate, service_rate, capacity)
    print_model_results(mm1k_model, f"M/M/1/{capacity}")
    print(f"Probability of rejection: {mm1k_model.probability_rejection():.4f}")
    
    # M/M/1/m model (finite source)
    population_size = 20
    arrival_rate_per_source = 0.5  # Each source generates 0.5 customers per hour
    mm1m_model = MM1m(arrival_rate_per_source, service_rate, population_size)
    print_model_results(mm1m_model, f"M/M/1/{population_size}")
    print(f"Effective arrival rate: {mm1m_model.effective_arrival_rate():.4f}")
    
    # M/M/k model (multiple servers)
    num_servers = 3
    try:
        mmk_model = MMk(arrival_rate * 2, service_rate, num_servers)  # Increased arrival rate for illustration
        print_model_results(mmk_model, f"M/M/{num_servers}")
    except ValueError as e:
        print(f"\nM/M/{num_servers} Model: {e}")
    
    # M/M/∞ model (infinite servers)
    mminf_model = MMInf(arrival_rate, service_rate)
    print_model_results(mminf_model, "M/M/∞")
    print(f"Variance of customers in system: {mminf_model.variance_customers():.4f}")

if __name__ == "__main__":
    main() 