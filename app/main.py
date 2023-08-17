from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.models.shemas import PaymentData, RefundData, RecurringData, TransactionStatusData
from app.external_services.megapay import authorize_payment, make_payment, refund_payment, get_transaction_status

app = FastAPI()
security = HTTPBasic()

external_service_url = "https://mega-pay.online/"


@app.get("/")
def read_root():
    return {"message": "Welcome to the payment service"}


@app.post("/authorize-payment")
async def authorize_payment_route(payment_data: PaymentData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = {
        "merchant_key": payment_data.merchant_key,
        "operation": "purchase",
        "methods": ["card"],
        "order": {
            "number": payment_data.order_number,
            "amount": str(payment_data.amount),
            "currency": payment_data.currency,
            "description": payment_data.description
        },
        "cancel_url": payment_data.cancel_url,
        "success_url": payment_data.success_url,
        "customer": {
            "name": payment_data.customer_name,
            "email": payment_data.customer_email
        },
        "billing_address": {
            "country": payment_data.billing_country,
            "state": payment_data.billing_state,
            "city": payment_data.billing_city,
            "address": payment_data.billing_address,
            "zip": payment_data.billing_zip,
            "phone": payment_data.billing_phone
        },
        "recurring_init": payment_data.recurring_init,
        "hash": payment_data.session_hash
    }

    response = await authorize_payment(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Payment authorization failed")


@app.post("/make-payment")
async def make_payment_route(payment_data: PaymentData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = {
        "merchant_key": payment_data.merchant_key,
        "operation": "purchase",
        "methods": ["card"],
        "order": {
            "number": payment_data.order_number,
            "amount": str(payment_data.amount),
            "currency": payment_data.currency,
            "description": payment_data.description
        },
        "cancel_url": payment_data.cancel_url,
        "success_url": payment_data.success_url,
        "customer": {
            "name": payment_data.customer_name,
            "email": payment_data.customer_email
        },
        "billing_address": {
            "country": payment_data.billing_country,
            "state": payment_data.billing_state,
            "city": payment_data.billing_city,
            "address": payment_data.billing_address,
            "zip": payment_data.billing_zip,
            "phone": payment_data.billing_phone
        },
        "recurring_init": payment_data.recurring_init,
        "hash": payment_data.session_hash
    }

    response = await make_payment(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Payment failed")


@app.post("/refund-payment")
async def refund_payment_route(refund_data: RefundData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = {
        "merchant_key": refund_data.merchant_key,
        "payment_id": refund_data.payment_id,
        "amount": str(refund_data.amount),
        "hash": refund_data.operation_hash
    }

    response = await refund_payment(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Refund failed")


@app.post("/recurring-payment")
async def recurring_payment_route(recurring_data: RecurringData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = {
        "merchant_key": recurring_data.merchant_key,
        "order": {
            "number": recurring_data.order_number,
            "amount": str(recurring_data.amount),
            "description": recurring_data.description
        },
        "recurring_init_trans_id": recurring_data.recurring_init_trans_id,
        "recurring_token": recurring_data.recurring_token,
        "hash": recurring_data.session_hash
    }

    response = await make_payment(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Recurring payment failed")


@app.post("/get-transaction-status")
async def get_transaction_status_route(status_data: TransactionStatusData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = {
        "merchant_key": status_data.merchant_key,
        "payment_id": status_data.payment_id,
        "hash": status_data.operation_hash
    }

    response = await get_transaction_status(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to get transaction status")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
