import numpy as np
import pandas as pd


class TransactionDataSimulator:
    def __init__(self, number_of_customers, number_of_terminals):
        self.number_of_customers = number_of_customers
        self.number_of_terminals = number_of_terminals
        self.random_state = 0

    def generate_customer_profiles_table(self):
        np.random.seed(self.random_state)
        customer_id_properties = []

        for customer_id in range(self.number_of_customers):
            x_customer_id = np.random.uniform(0, 100)
            y_customer_id = np.random.uniform(0, 100)

            mean_amount = np.random.uniform(5, 100)
            std_amount = mean_amount / 2

            mean_number_of_tx_per_day = np.random.uniform(0, 4)
            customer_id_properties.append(
                [customer_id, x_customer_id, y_customer_id, mean_amount, std_amount, mean_number_of_tx_per_day])

        customer_profiles_table = pd.DataFrame(customer_id_properties,
                                               columns=['CUSTOMER_ID', 'x_customer_id', 'y_customer_id',
                                                        'mean_amount', 'std_amount', 'mean_number_of_tx_per_day'])
        return customer_profiles_table

    def generate_terminal_profiles_table(self):
        np.random.seed(self.random_state)
        terminal_id_properties = []

        for terminal_id in range(self.number_of_terminals):
            x_terminal_id = np.random.uniform(0, 100)
            y_terminal_id = np.random.uniform(0, 100)

            terminal_id_properties.append([terminal_id, x_terminal_id, y_terminal_id])

        terminal_profiles_table = pd.DataFrame(terminal_id_properties,
                                               columns=['TERMINAL_ID', 'x_terminal_id', 'y_terminal_id'])
        return terminal_profiles_table
