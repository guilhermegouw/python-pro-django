import pytest
from django.urls import reverse
from base.django_assertions import assert_contains, assert_template_used


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Video Aperitivo: Motivação</h1>')


def test_video_template(resp):
    assert_template_used(resp, 'aperitivos/video.html')


def test_embeded_video(resp):
    assert_contains(
        resp,
        '<iframe src="https://player.vimeo.com/video/719879800" frameborder="0"></iframe>'
    )
