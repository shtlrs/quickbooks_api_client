from enum import Enum


class QuickBooksResource(Enum):
    """
    An enum that holds the difference resource that we might query from Quickbooks
    """

    INVOICE = "invoice"

    PAYMENT = "payment"

    CUSTOMER = "customer"
