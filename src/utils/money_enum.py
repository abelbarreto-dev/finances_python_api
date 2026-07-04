from enum import Enum


class MoneyType(Enum):
    PAYMENT = "PAYMENT"
    RECEIPT = "RECEIPT"
    TRANSFER = "TRANSFER"


class MoneyMethod(Enum):
    CASH = "CASH"
    PIX = "PIX"
    DOC = "DOC"
    TED = "TED"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    CHECK = "CHECK"
    BANK_SLIP = "BANK_SLIP"
    OTHER = "OTHER"
