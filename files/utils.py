import uuid


def generate_unique_name(original_name: str):
    file_type = original_name[-3:]
    new_name = f'{str(uuid.uuid4()).replace('-', '')}.{file_type}'
    return new_name