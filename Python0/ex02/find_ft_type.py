def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type != int and obj_type != str:
        print(obj_type.__name__.capitalize(), ":", obj_type)
    elif obj_type == str:
        print("Brian is in the kitchen :", obj_type)
    elif obj_type == int:
        print("Type not found")
    return 42
