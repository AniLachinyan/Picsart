def read_file(file_name):
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    return content

def write_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()

def append_file(file_name, content):
    file = open(file_name, 'a')
    file.write(content)
    file.close()

def delete_file(file_name):
    try:
        file = open(file_name, 'w')
        file.truncate(0)
        file.close()
        return f"{file_name} has been deleted."
    except IOError:
        return f"{file_name} does not exist or cannot be deleted."

file_operations = {
    "read": read_file,
    "write": write_file,
    "append": append_file,
    "delete": delete_file
}

def file_manager(file_name, operation, content=None):
    if operation in file_operations:
        if operation in ["write", "append"]:
            if content is None:
                raise ValueError(f"Content is required for {operation} operation.")
            return file_operations[operation](file_name, content)
        else:
            return file_operations[operation](file_name)
    else:
        raise ValueError(f"Unsupported file operation: {operation}")

print(file_manager('example.txt', 'write', 'Hello, World!'))
print(file_manager('example.txt', 'append', '\nThis is appended text.'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'delete'))

