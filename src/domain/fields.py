from pydantic import constr

username = constr(
    min_length=3,
    max_length=32,
    pattern=r'^[a-zA-Z0-9_]+$'
)
