
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade:
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor):
      # TODO: store the payment processor and start unsubscribed
      pass

    def subscribe(self, monthly_fee: float) -> str:
      # TODO: charge `monthly_fee` through the payment processor, mark the
      # account as subscribed, and return the processor's receipt string.
      pass

    def watch(self, video: Video) -> str:
      # TODO: if not subscribed, raise PermissionError("subscription required").
      # Otherwise delegate to `video.play()` and return its result.
      pass
