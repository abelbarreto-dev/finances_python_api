from enum import Enum


class InvoiceStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELED = "CANCELED"
    CONTINUED = "CONTINUED"


class InvoiceType(Enum):
    CASH = "CASH"
    PIX = "PIX"
    DOC = "DOC"
    TED = "TED"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    CHECK = "CHECK"
    BANK_SLIP = "BANK_SLIP"
    OTHER = "OTHER"
