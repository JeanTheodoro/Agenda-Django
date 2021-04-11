import pytest
from django.urls import reverse
from webdev.task.models import Task


@pytest.fixture
def resposta(client, db):
    res = client.post(reverse('task:home'), data={'name': 'Tarefa'})
    return res

def test_tarefa_exists_database(resposta):
    assert Task.objects.exists()

def test_tarefa_redirect_after_save(resposta):
    assert resposta.status_code == 302

@pytest.fixture
def response_data_invalid(client, db):
    res = client.post(reverse('task:home'), data={'nome': ' '})
    return res


def test_tarefa_no_exists_database(response_data_invalid):
    assert not Task.objects.exists()

def test_tarefa_page_data_invalid(response_data_invalid):
    assert response_data_invalid.status_code == 400