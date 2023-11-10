# Tutorial from https://fastapi.tiangolo.com/python-types/

def get_full_name(first_name, last_name):
    # no meaningful hints on pressing CTRL+SPACE after first_name.
    return first_name.title()+" "+last_name.title()

print(get_full_name("john","doe"))

def get_full_name_with_type_hints(first_name: str, last_name: str):
    # got meaningful hints for string type on pressing CTRL+SPACE after first_name.
    return first_name.title+" "+last_name.title()

print(get_full_name("john","doe"))

# Generic types with type parameters

def process_items(items: list[str]):
    for item in items:
        print(item)
