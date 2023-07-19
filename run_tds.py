import transaction_data_simulator as tds
tds = tds.TransactionDataSimulator(5, 5)

print(tds.generate_customer_profiles_table())
print(tds.generate_terminal_profiles_table())
