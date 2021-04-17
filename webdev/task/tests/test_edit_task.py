import pytest
from django.urls import reverse
from webdev.task.models import Task


@pytest.fixture
def task_beggar(db):
    return Task.objects.create(name='Tarefa3', done=False)

@pytest.fixture
def response_task_beggar(client, task_beggar):
    res = client.post(
        reverse('task:detail', kwargs={'task_id':task_beggar.id}), 
        data={'done': 'true', 'name': f'{task_beggar.name}-edit'}
    )
    return res

def test_task_done(response_task_beggar):
    assert Task.objects.first().done

def test_task_status_code(response_task_beggar):
    assert response_task_beggar.status_code == 302


@pytest.fixture
def task_done(db):
    return Task.objects.create(name='Tarefa3', done=True)

@pytest.fixture
def response_task_done(client, task_done):
    res = client.post(
        reverse('task:detail', kwargs={'task_id':task_done.id}), 
        data={'name': f'{task_done.name}-edit'}
    )
    return res

def test_task_beggar(response_task_done):
    assert not Task.objects.first().done

