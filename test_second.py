import pytest


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

    print("\nerror no happens")


if __name__ == '__main__':
    pytest.main()
