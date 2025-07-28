import os
def insert_driver_path():
    """
    Inserts the ChromeDriver path into the system PATH environment variable.
    This is necessary for Selenium to locate the ChromeDriver executable.
    """
    import sys
    if sys.platform.startswith('win'):
        # For Windows, we use a semicolon to separate paths
        sep = ';'
    else:
        # For Unix-like systems, we use a colon
        sep = ':'

    # Assuming CHROMEDRIVER_PATH is set in the environment variables
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path:
        os.environ["PATH"] += sep + chromedriver_path
    else:
        raise EnvironmentError("CHROMEDRIVER_PATH environment variable is not set.")