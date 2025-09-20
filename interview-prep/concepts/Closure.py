def outer_function(name):
    def inner_function():
        print("Hello, " + name)
    return inner_function

closure = outer_function("bro")
closure()
