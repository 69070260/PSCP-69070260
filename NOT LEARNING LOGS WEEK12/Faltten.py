"""โปรแกรม Flatten"""

import ast

data = ast.literal_eval(input())
result = []

def flatten(items):
    """Flatten nested lists into a single list."""
    for item in items:
        if isinstance(item, list):
            flatten(item)
        else:
            result.append(item)

flatten(data)
result.sort(reverse=True)
print(result)
