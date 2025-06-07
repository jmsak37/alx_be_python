def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.
    Parameters:
      - num1 (float)
      - num2 (float)
      - operation (str): 'add', 'subtract', 'multiply', or 'divide'
    Returns:
      - float result of the operation, or an error message on division by zero
    """
    op = operation.strip().lower()
    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return f"Error: Unsupported operation '{operation}'"
