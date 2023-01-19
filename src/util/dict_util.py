def to_dict(obj):
    d = {}
    for k, v in obj.dict().items():
        if hasattr(v, "value"):
            d[k] = v.value
        else:
            d[k] = v
    return d
