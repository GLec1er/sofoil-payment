from pydantic import BaseModel, PositiveFloat, constr


class PaymentData(BaseModel):
    card_number: constr(min_length=16, max_length=16)
    expiration_date: constr(min_length=5, max_length=5)
    cvv: constr(min_length=3, max_length=4)
    amount: PositiveFloat


class RefundData(BaseModel):
    payment_id: str
