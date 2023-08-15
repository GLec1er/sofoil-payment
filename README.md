# sofoil-payment

Welcome to the Payment Service project! This project demonstrates a simple FastAPI application that interacts with an external payment service (megapay.com) to authorize payments, make payments, and process refunds.

## Getting Started

1. Clone the repository:


2. Install the required dependencies:


3. Run the FastAPI application:

The application will be available at http://localhost:8000.

## API Endpoints

- `GET /`: Get a welcome message.

- `POST /authorize-payment`: Authorize a payment using card details.
- Request Body: PaymentData
- Response: Authorization details or error message

- `POST /make-payment`: Make a payment using card details.
- Request Body: PaymentData
- Response: Payment details or error message

- `POST /refund-payment`: Process a refund for a payment.
- Request Body: RefundData
- Response: Refund details or error message

## Models

- PaymentData:
- card_number: 16-digit card number
- expiration_date: Card expiration date (MM/YY)
- cvv: CVV code
- amount: Positive float for payment amount

- RefundData:
- payment_id: Payment ID for refund

## Authentication

The application uses Basic authentication with the token "1234567890".

