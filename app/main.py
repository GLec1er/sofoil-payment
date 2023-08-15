from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.models.shemas import PaymentData, RefundData
from app.external_services.megapay import authorize_payment, make_payment, refund_payment

app = FastAPI()
security = HTTPBasic()

external_service_url = "https://api.megapay.com"


@app.get("/")
def read_root():
    return {"message": "Welcome to the payment service"}


@app.post("/authorize-payment")
async def authorize_payment_route(payment_data: PaymentData):
    credentials = HTTPBasicCredentials(username="user", password="1234567890")
    auth_str = f"{credentials.username}:{credentials.password}"
    headers = {"Authorization": f"Basic {auth_str}"}

    payload = payment_data.dict()

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

    payload = payment_data.dict()

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

    payload = refund_data.dict()

    response = await refund_payment(payload, headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Refund failed")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)