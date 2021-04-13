import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.task.models import Task

@pytest.fixture
def resposta(client, db):
    res = client.get(reverse('task:home'))
    return res

def test_status_code(resposta):
    assert resposta.status_code == 200


def test_form_present(resposta):
    assertContains(resposta, '<form')

def test_button_save_present(resposta):
    assertContains(resposta, '<button type="submit"')

@pytest.fixture
def list_task_beggar(db):    
    task = [
        Task(name='Tak 1', done=False),
        Task(name='Tak 2', done=False),
        ]
    Task.objects.bulk_create(task)
    return task


@pytest.fixture
def response_list_task(client, list_task_beggar):    
    resp = client.get(reverse('task:home'))
    return resp

def response_with_list_task(list_task_beggar,  response_list_task):
    for task in response_list_task:
        assertContains(response_list_task, task.name)