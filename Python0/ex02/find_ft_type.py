def all_thing_is_obj(object: any) -> int:
    if isinstance(object, int) is False and isinstance(object, str) is False:
        print(type(object).__name__.capitalize(), ":", type(object))
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :", type(object))
    elif isinstance(object, int):
        print("Type not found")
    return 42
