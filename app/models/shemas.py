from pydantic import BaseModel


class PaymentData(BaseModel):
    merchant_key: str
    operation: str
    methods: list[str]
    order: dict
    cancel_url: str
    success_url: str
    customer: dict
    billing_address: dict
    recurring_init: str
    hash: str


class RefundData(BaseModel):
    merchant_key: str
    payment_id: str
    amount: float
    operation_hash: str


class RecurringData(BaseModel):
    merchant_key: str
    order_number: str
    amount: float
    description: str
    recurring_init_trans_id: str
    recurring_token: str
    session_hash: str


class TransactionStatusData(BaseModel):
    merchant_key: str
    payment_id: str
    operation_hash: str
