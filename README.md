# Queueing Theory Models

This project provides an object-oriented implementation of various queueing theory models using Python. The implementation uses inheritance to share common functionality across models.

## Models Implemented

| Model | Servers | Capacity | Population | Description |
|-------|---------|----------|------------|-------------|
| M/M/1 | 1 | Infinite | Infinite | Basic queue |
| M/M/1/K | 1 | K (finite) | Infinite | Finite buffer queue, customers blocked when full |
| M/M/1/m | 1 | Up to m in system | Finite (m) | Finite source, arrival rate depends on how many are already in system |
| M/M/k | k | Infinite | Infinite | Multiple servers |
| M/M/∞ | ∞ | Infinite | Infinite | Everyone gets served instantly |

## Key Features

- Object-oriented design with inheritance
- Abstract base class for common functionality
- Accurate calculation of key performance measures
- Easy to extend for additional queueing models

## Performance Measures Calculated

Each model calculates the following performance measures:

- Utilization factor (ρ)
- Probability of system being idle (P₀)
- Probability of n customers in the system (Pₙ)
- Average number of customers in the system (L)
- Average number of customers in the queue (Lq)
- Average time spent in the system (W)
- Average time spent in the queue (Wq)

Some models provide additional metrics specific to their characteristics.

## Usage

See the `example.py` file for demonstration of how to use each model:

```python
# Example for M/M/1 model
from mm1 import MM1

# Create model with arrival rate 5 customers/hour and service rate 8 customers/hour
model = MM1(5, 8)

# Calculate performance measures
print(f"Utilization factor: {model.rho}")
print(f"Average number of customers in system: {model.average_customers_in_system()}")
print(f"Average waiting time in queue: {model.average_time_in_queue()}")
```

## Requirements

- Python 3.6 or higher
- Math module (part of Python's standard library)

## License

This project is open-source and available under the MIT License. 