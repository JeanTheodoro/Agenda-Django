import pytest
from django.urls import reverse
from webdev.task.models import Task


@pytest.fixture
def task_delete(db):
    return Task.objects.create(name='Tarefa 1', done=True)

@pytest.fixture
def response(client, task_delete):
    res = client.post(
        reverse('task:delete', kwargs={'task_id':task_delete.id}),     
    )
    return res

def test_delete_task(response):
    assert not Task.objects.exists()
