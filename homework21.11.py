def make_logger(level):

    def logger(message):
        return f"[{level}] {message}"
    return logger

print(make_logger("Error")("This is an ERROR message"))
