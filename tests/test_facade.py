import pytest
from streamflix.payments import StripeAPI, StripeAdapter, PayPalClient, PayPalAdapter
from streamflix.catalog import RealVideo, ProxyVideo
from streamflix.facade import StreamingFacade


def make_facade():
    return StreamingFacade(StripeAdapter(StripeAPI(merchant_id="acct_123")))


def test_watch_before_subscribing_is_blocked():
    streamflix = make_facade()
    movie = ProxyVideo("Inception", "/videos/inception.mp4")

    with pytest.raises(PermissionError):
        streamflix.watch(movie)


def test_watch_before_subscribing_does_not_load_the_video():
    streamflix = make_facade()
    movie = ProxyVideo("Inception", "/videos/inception.mp4")

    with pytest.raises(PermissionError):
        streamflix.watch(movie)

    assert RealVideo.load_count == 0


def test_subscribe_charges_through_the_payment_processor():
    streamflix = make_facade()

    receipt = streamflix.subscribe(9.99)

    assert receipt == "paid 9.99 EUR via stripe (acct_123)"


def test_watch_after_subscribing_plays_the_video():
    streamflix = make_facade()
    movie = ProxyVideo("Inception", "/videos/inception.mp4")

    streamflix.subscribe(9.99)
    result = streamflix.watch(movie)

    assert result == "Playing 'Inception' from /videos/inception.mp4"


def test_facade_works_with_any_payment_processor():
    streamflix = StreamingFacade(PayPalAdapter(PayPalClient(account_email="user@example.com")))
    movie = ProxyVideo("Interstellar", "/videos/interstellar.mp4")

    streamflix.subscribe(9.99)

    assert streamflix.watch(movie) == "Playing 'Interstellar' from /videos/interstellar.mp4"
