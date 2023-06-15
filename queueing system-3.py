import numpy as np
import heapq


class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time


class Teller:
    def __init__(self, index):
        self.index = index
        self.is_available = True
        self.current_customer = None
        self.time_to_finish = 0


class BankQueue:
    def __init__(self, num_tellers, arrival_rate, service_rate):
        self.num_tellers = num_tellers
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.tellers = [Teller(i) for i in range(num_tellers)]
        self.queues = [[] for _ in range(num_tellers)]
        self.customers = []
        self.current_time = 0

    def generate_customer(self):
        arrival_time = self.current_time + np.random.poisson(self.arrival_rate)
        service_time = np.random.exponential(self.service_rate)
        return Customer(arrival_time, service_time)

    def process_event(self, customer):
        # Find the teller with the shortest queue
        queue_lengths = [len(q) for q in self.queues]
        shortest_queue_index = np.argmin(queue_lengths)

        if queue_lengths[shortest_queue_index] == 0:
            # Serve the customer immediately
            self.current_time = customer.arrival_time
            self.queues[shortest_queue_index].append(customer)
            self.tellers[shortest_queue_index].is_available = False
            self.tellers[shortest_queue_index].current_customer = customer
            self.tellers[shortest_queue_index].time_to_finish = self.current_time + customer.service_time
            print(f"Customer {len(self.customers) + 1} arrived at time {customer.arrival_time:.2f}, "
                  f"assigned to teller {shortest_queue_index + 1}")
        else:
            # Add the customer to the shortest queue
            earliest_available = self.queues[shortest_queue_index][-1].arrival_time + self.queues[shortest_queue_index][
                -1].service_time
            self.current_time = max(earliest_available, customer.arrival_time)
            self.queues[shortest_queue_index].append(customer)
            if self.tellers[shortest_queue_index].is_available:
                self.tellers[shortest_queue_index].is_available = False
                self.tellers[shortest_queue_index].current_customer = customer
                self.tellers[shortest_queue_index].time_to_finish = self.current_time + customer.service_time
                print(f"Customer {len(self.customers) + 1} arrived at time {customer.arrival_time:.2f}, "
                      f"assigned to teller {shortest_queue_index + 1}")
            else:
                print(f"Customer {len(self.customers) + 1} arrived at time {customer.arrival_time:.2f}, "
                      f"assigned to teller {shortest_queue_index + 1}, "
                      f"wait time: {self.current_time - customer.arrival_time:.2f}")

        self.customers.append(customer)

    def simulate(self, num_customers):
        for _ in range(num_customers):
            customer = self.generate_customer()
            self.process_event(customer)
            for t in self.tellers:
                if not t.is_available:
                    if self.current_time >= t.time_to_finish:
                        t.is_available = True
                        t.current_customer = None
                        t.time_to_finish = 0
                        print(f"Teller {t.index + 1} finished serving customer at time {self.current_time:.2f}")
                    else:
                        print(f"Teller {t.index + 1} is busy until time {t.time_to_finish:.2f}")
            for t in self.tellers:
                if t.is_available and all(len(q) == 0 for q in self.queues):
                    print(f"Teller {t.index + 1} is available")
                    break

    def average_wait_time(self):
        wait_times = [
            max(0, (c.arrival_time - start_time) * 60)
            for c, start_time in zip(self.customers, [q[0].arrival_time for q in self.queues])
        ]
        return np.mean(wait_times)


if __name__ == "__main__":
    num_tellers = 2
    arrival_rate = 1  # Average time between customer arrivals (Poisson distribution)
    service_rate = 1  # Average service time per customer (Exponential distribution)
    num_customers = 10

    bank_queue = BankQueue(num_tellers, arrival_rate, service_rate)
    bank_queue.simulate(num_customers)

    print(f"\nAverage wait time: {bank_queue.average_wait_time():.2f} minutes")