def greet(name, verbose=False):
    if verbose:
        print("Entering greet()")

    print("Hello", name)
    print("Welcome!")

    return True


#fixed

def greet(name, verbose=False):
    if verbose:
        logging.info("Entering greet()")

    logging.info("Hello", name)
    logging.info("Welcome!")

    return True