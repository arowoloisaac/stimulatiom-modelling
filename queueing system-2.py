import random


class Customer:
    def __init__(self, name, account_number, arrival_time):
        self.name = name
        self.account_number = account_number
        self.arrival_time = arrival_time


class Bank:
    def __init__(self, num_tellers, service_time_mean):
        self.num_tellers = num_tellers
        self.service_time_mean = service_time_mean
        self.queue = []
        self.tellers = [0] * num_tellers
        self.next_arrival_time = self.get_next_arrival_time()

    def get_next_arrival_time(self):
        return random.expovariate(1)

    def get_next_service_time(self):
        return random.expovariate(1 / self.service_time_mean)

    def add_customer_to_queue(self, customer):
        self.queue.append(customer)

    def serve_customer(self, teller_index):
        if len(self.queue) > 0:
            customer = self.queue.pop(0)
            service_time = self.get_next_service_time()
            self.tellers[teller_index] = service_time
            print("Serving customer:", customer.name, "at teller", teller_index, "for", service_time, "minutes.")
        else:
            print("No customers in queue for teller", teller_index)

    def update_tellers(self):
        for i in range(self.num_tellers):
            if self.tellers[i] > 0:
                self.tellers[i] -= 1

    def run_simulation(self, num_customers):
        arrival_time = 0
        for i in range(num_customers):
            if i == 0:
                arrival_time = self.next_arrival_time
            else:
                arrival_time += self.get_next_arrival_time()
                self.next_arrival_time = arrival_time
            customer = Customer("Customer " + str(i+1), i+1, arrival_time)
            self.add_customer_to_queue(customer)
            print("Customer", customer.name, "arrived at time", customer.arrival_time)
            self.update_tellers()
            for j in range(self.num_tellers):
                if self.tellers[j] == 0:
                    self.serve_customer(j)


# Example usage:
bank = Bank(num_tellers=3, service_time_mean=3)
bank.run_simulation(num_customers=20)
