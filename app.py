def greet(gcp):
    """
    Function to greet a user by name.
    Args:
        name (str): The name of the user.
    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
