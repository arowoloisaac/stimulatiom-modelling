import numpy as np
import heapq


class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time


class BankQueue:
    def __init__(self, num_tellers, arrival_rate, service_rate):
        self.num_tellers = num_tellers
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = []
        self.customers = []
        self.teller = [0] * num_tellers
        self.current_time = 0

    def generate_customer(self):
        arrival_time = self.current_time + np.random.poisson(self.arrival_rate)
        service_time = np.random.exponential(self.service_rate)
        return Customer(arrival_time, service_time)

    def process_event(self, customer):
        # If there is an available teller, the customer is served immediately
        if len(self.queue) < self.num_tellers:
            self.current_time = customer.arrival_time
            heapq.heappush(self.queue, customer.arrival_time + customer.service_time)
            print(f"Customer {len(self.customers) + 1} arrived at time {customer.arrival_time:.2f}")
        # If all tellers are busy, the customer waits in the queue
        else:
            earliest_available = heapq.heappop(self.queue)
            self.current_time = max(earliest_available, customer.arrival_time)
            heapq.heappush(self.queue, self.current_time + customer.service_time)
            print(f"Customer {len(self.customers) + 1} arrived at time {customer.arrival_time:.2f} and is waiting")

        self.customers.append(customer)

    def simulate(self, num_customers):
        for _ in range(num_customers):
            customer = self.generate_customer()
            self.process_event(customer)
            if len(self.queue) > 0:
                print(f"Teller is busy until time {self.queue[0]:.2f}")
            else:
                print("Teller is available")

    def average_wait_time(self):
        wait_times = [
            max(0, c.arrival_time - start_time)
            for c, start_time in zip(self.customers, self.queue)
        ]
        return np.mean(wait_times)


if __name__ == "__main__":
    num_tellers = 3
    arrival_rate = 1  # Average time between customer arrivals (Poisson distribution)
    service_rate = 2  # Average service time per customer (Exponential distribution)
    num_customers = 10

    bank_queue = BankQueue(num_tellers, arrival_rate, service_rate)
    bank_queue.simulate(num_customers)

    print(f"\nAverage wait time: {bank_queue.average_wait_time():.2f} minutes")

