import pytest
from streamflix.catalog import RealVideo


@pytest.fixture(autouse=True)
def reset_real_video_load_count():
    RealVideo.load_count = 0
    yield
    RealVideo.load_count = 0
