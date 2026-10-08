def output_decorator(parameter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("##########################")
            print("#", parameter)
            print("# input:", args)

            result = func(*args, **kwargs)

            print("# output:", result)
            print("##########################")

            return result
        return wrapper
    return decorator


@output_decorator("Adding")
def add(a, b):
    return a + b


add(4, 3)
add(6,7)