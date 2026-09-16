import pytest
from streamflix.payments import StripeAPI, PayPalClient, StripeAdapter, PayPalAdapter


def test_stripe_adapter_pays_and_formats_receipt():
    stripe = StripeAPI(merchant_id="acct_123")
    adapter = StripeAdapter(stripe)

    receipt = adapter.pay(12.3)

    assert receipt == "paid 12.30 EUR via stripe (acct_123)"


def test_stripe_adapter_converts_euros_to_cents():
    stripe = StripeAPI(merchant_id="acct_123")
    adapter = StripeAdapter(stripe)

    # 12.34 EUR must reach the Stripe SDK as 1234 cents, not 1233 or 1235.
    receipt = adapter.pay(12.34)

    assert "12.34" in receipt


def test_paypal_adapter_pays_and_formats_receipt():
    paypal = PayPalClient(account_email="seller@example.com")
    adapter = PayPalAdapter(paypal)

    receipt = adapter.pay(9.5)

    assert receipt == "paid 9.50 EUR via paypal (seller@example.com)"


@pytest.mark.parametrize("amount", [0, -5.0])
def test_adapters_reject_non_positive_amounts(amount):
    stripe_adapter = StripeAdapter(StripeAPI(merchant_id="acct_123"))
    paypal_adapter = PayPalAdapter(PayPalClient(account_email="seller@example.com"))

    with pytest.raises(ValueError):
        stripe_adapter.pay(amount)
    with pytest.raises(ValueError):
        paypal_adapter.pay(amount)
