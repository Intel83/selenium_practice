def transaction_id_generator():
    """
    Generates a transaction ID of format Txxx
    where xxx is a sequential number from 001 and 999.
    :return:
    """
    for i in range(1, 1000):
        yield f"T{i:03d}"

def transaction_amount_generator():
    """
    Generates a random amount between -1000,00 and 1000,00.
    :return:
    """
    import random
    return round(random.uniform(-1000.00, 1000.00), 2)

def transaction_type_generator():
    """
    Generates a random transaction type from a predefined set.
    :return:
    """
    transaction_types = ("deposit", "withdrawal", "transfer")
    import random
    return random.choice(transaction_types)