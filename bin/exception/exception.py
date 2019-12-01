class BPException(Exception):
    pass


class BPProjectInitializationException(BPException):
    """
    Raise Exception for all the product service related errors
    """
    pass


class BPProductException(BPException):
    """
    Raise Exception for all the product service related errors
    """
    pass
