import time

import pytest
from collections import namedtuple


@pytest.mark.skip()
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.xfail()
def test_multiply():
    assert 5 * 6 == 31


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


@pytest.mark.run_me_please
def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    time.sleep(0.5)
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    t_task = Task('do_something', 'okken', True, 21)
    time.sleep(0.2)
    t_dict = t_task._asdict()
    expected = {'summary': 'do_something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    t_before = Task('finish book', 'brian', False)
    time.sleep(0.3)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


