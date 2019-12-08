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


class BPSupplierException(BPException):
    """
    Raise Exception for all the supplier service related errors
    """
    pass


class BPLocationException(BPException):
    """
    Raise Exception for all the location service related errors
    """
    pass


class BPBrandException(BPException):
    """
    Raise Exception for all the location service related errors
    """
    pass