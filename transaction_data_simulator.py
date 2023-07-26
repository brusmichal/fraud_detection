import numpy as np
import pandas as pd


class TransactionDataSimulator:
    def __init__(self, number_of_customers, number_of_terminals):
        self.number_of_customers = number_of_customers
        self.number_of_terminals = number_of_terminals
        self.random_state = 0
        self.customers_table = None
        self.terminals_table = None

    def generate_customers_table(self):
        np.random.seed(self.random_state)
        customers = []

        for customer_id in range(self.number_of_customers):
            x_customer = np.random.uniform(0, 100)
            y_customer = np.random.uniform(0, 100)

            mean_amount = np.random.uniform(5, 100)
            std_amount = mean_amount / 2

            mean_number_of_tx_per_day = np.random.uniform(0, 4)
            customers.append(
                [customer_id, x_customer, y_customer, mean_amount, std_amount, mean_number_of_tx_per_day])

        self.customers_table = pd.DataFrame(customers,
                                            columns=['CUSTOMER_ID', 'x_customer', 'y_customer',
                                                     'mean_amount', 'std_amount', 'mean_number_of_tx_per_day'])
        return self.customers_table

    def generate_terminals_table(self):
        np.random.seed(self.random_state)
        terminals = []

        for terminal_id in range(self.number_of_terminals):
            x_terminal = np.random.uniform(0, 100)
            y_terminal = np.random.uniform(0, 100)

            terminals.append([terminal_id, x_terminal, y_terminal])

        self.terminals_table = pd.DataFrame(terminals,
                                            columns=['TERMINAL_ID', 'x_terminal', 'y_terminal'])
        return self.terminals_table
