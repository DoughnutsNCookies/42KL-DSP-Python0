def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object}", type(None))
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object}", type(float("NaN")))
    elif isinstance(object, bool) and not object:
        print(f"Fake: {object}", type(object))
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object}", type(0))
    elif isinstance(object, str) and not object:
        print(f"Empty: {object}", type(''))
    else:
        print("Type not Found")
        return 1
    return 0
