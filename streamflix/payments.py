
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """
    Target interface. StreamFlix only ever talks to this.
    """

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Charge `amount` (in EUR) and return a human-readable receipt."""
        raise NotImplementedError


# --- Third-party SDKs (given, do not modify) --------------------------------
# These are stand-ins for real vendor libraries: their interfaces don't match
# `PaymentProcessor`, and we can't change them.

class StripeAPI:
    """Fake Stripe SDK. Works in integer cents and needs a merchant id."""

    def __init__(self, merchant_id: str):
        self.merchant_id = merchant_id

    def charge_cents(self, cents: int) -> dict:
        if cents <= 0:
            raise ValueError("cents must be positive")
        return {"id": f"ch_{cents}", "status": "succeeded"}


class PayPalClient:
    """Fake PayPal SDK. Works with string amounts and an account email."""

    def __init__(self, account_email: str):
        self.account_email = account_email

    def send_payment(self, amount_str: str, currency: str) -> str:
        if float(amount_str) <= 0:
            raise ValueError("amount must be positive")
        return f"PP-{amount_str}-{currency}"


# --- Adapters (implement these) ---------------------------------------------

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: StripeAPI):
      # TODO: store the wrapped StripeAPI instance
      pass

    def pay(self, amount: float) -> str:
      # TODO: convert `amount` (EUR) to integer cents, call self._stripe.charge_cents,
      # and return "paid {amount:.2f} EUR via stripe ({merchant_id})"
      pass


class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal: PayPalClient):
      # TODO: store the wrapped PayPalClient instance
      pass

    def pay(self, amount: float) -> str:
      # TODO: call self._paypal.send_payment with amount formatted to 2 decimals and
      # currency "EUR", and return "paid {amount:.2f} EUR via paypal ({account_email})"
      pass
