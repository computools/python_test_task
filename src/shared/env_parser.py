"""This module uses to manipulate with environment variables"""

import re
from typing import Union


def get_list(pattern: Union[str, None], default: list) -> list:
    """Get list from environment variable separated by characters.
    If not patterns found return default value.
    """
    if not pattern:
        return default

    r = re.split(r", |; |,|;| ", pattern)

    return r if r else default
