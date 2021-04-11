import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def resposta(client):
    res = client.get(reverse('task:home'))
    return res

def test_status_code(resposta):
    assert resposta.status_code == 200


def test_form_present(resposta):
    assertContains(resposta, '<form')

def test_button_save_present(resposta):
    assertContains(resposta, '<button type="submit"')

    