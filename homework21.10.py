def make_config(key,value):

    def config():
        return {key:value}
    return config

print(make_config("username","Bob")())
