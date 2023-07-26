import transaction_data_simulator as tds
tds = tds.TransactionDataSimulator(5, 5)

print(tds.generate_customers_table())
print(tds.generate_terminals_table())
