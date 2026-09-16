
from .payments import StripeAPI, StripeAdapter
from .catalog import ProxyVideo
from .facade import StreamingFacade


def main():
    stripe = StripeAPI(merchant_id="acct_stream42")
    processor = StripeAdapter(stripe)
    streamflix = StreamingFacade(processor)

    movie = ProxyVideo("Inception", "/videos/inception.mp4")

    try:
        print(streamflix.watch(movie))
    except PermissionError as e:
        print("Blocked:", e)

    print(streamflix.subscribe(9.99))
    print(streamflix.watch(movie))
    print(streamflix.watch(movie))  # served from the already-loaded video


if __name__ == "__main__":
    main()
