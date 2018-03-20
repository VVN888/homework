from collections import namedtuple


def return_namedtuple(*field_names):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_tuple = func(*args, **kwargs)
            if type(original_tuple) is tuple:
                new_named_tuple = namedtuple('new_named_tuple', list(field_names))
                return new_named_tuple(*original_tuple)
        return wrapper
    return decorator
