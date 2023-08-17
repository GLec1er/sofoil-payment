import httpx


async def authorize_payment(payload, headers):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{external_service_url}/authorize-payment", json=payload, headers=headers)
        return response


async def make_payment(payload, headers):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{external_service_url}/make-payment", json=payload, headers=headers)
        return response


async def refund_payment(payload, headers):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{external_service_url}/refund-payment", json=payload, headers=headers)
        return response


async def get_transaction_status(payload, headers):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{external_service_url}/payment/status", json=payload, headers=headers)
        return response
