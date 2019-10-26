import signal
from contextlib import contextmanager


TIME_LIMIT = 5 # seconds per test


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out after {0} seconds!".format(seconds))

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


@contextmanager
def ignore(*errs):
    try:
        yield
    except tuple(errs):
        pass


def test_0001():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0001 import solution
        assert solution() == 233168


def test_0002():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0002 import solution
        assert solution() == 4613732


def test_0003():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0003 import solution
        assert solution() == 6857


def test_0004():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0004 import solution
        assert solution() == 906609


def test_0005():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0005 import solution
        assert solution() == 232792560


def test_0006():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0006 import solution
        assert solution() == -1


def test_0007():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0007 import solution
        assert solution() == -1


def test_0008():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0008 import solution
        assert solution() == -1


def test_0009():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0009 import solution
        assert solution() == -1


def test_0010():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0010 import solution
        assert solution() == -1


def test_0011():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0011 import solution
        assert solution() == -1


def test_0012():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0012 import solution
        assert solution() == -1


def test_0013():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0013 import solution
        assert solution() == -1


def test_0014():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0014 import solution
        assert solution() == -1


def test_0015():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0015 import solution
        assert solution() == -1


def test_0016():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0016 import solution
        assert solution() == -1


def test_0017():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0017 import solution
        assert solution() == -1


def test_0018():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0018 import solution
        assert solution() == -1


def test_0019():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0019 import solution
        assert solution() == -1


def test_0020():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0020 import solution
        assert solution() == -1


def test_0021():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0021 import solution
        assert solution() == -1


def test_0022():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0022 import solution
        assert solution() == -1


def test_0023():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0023 import solution
        assert solution() == -1


def test_0024():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0024 import solution
        assert solution() == -1


def test_0025():
    with time_limit(TIME_LIMIT), ignore(ImportError):
        from problem_0025 import solution
        assert solution() == -1


def test_0026():
    with ignore(ImportError):
        from problem_0026 import solution
        assert solution() == -1
