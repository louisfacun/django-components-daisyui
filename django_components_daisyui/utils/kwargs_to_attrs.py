from typing import Any


def kwargs_to_attrs(attrs_dict_in: dict[str, Any]) -> dict[str, Any]:
    attrs_dict = {}
    for key, value in attrs_dict_in.items():
        if value is None or value is False:
            continue
        if value is True:
            attrs_dict[key.replace("_", "-")] = True
        else:
            attrs_dict[key.replace("_", "-")] = value
    return attrs_dict
