import inspect
from typing import Callable


def python_code_markdown(func: Callable) -> str:
    """ Returns markdown for python code. """
    return """
    ```python
    """ + inspect.getsource(func) + """
    ```
    """
