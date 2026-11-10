"""Validate theme YAML syntax and reject duplicate mapping keys."""

from pathlib import Path

import yaml


class Loader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    seen, result = set(), {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise SystemExit(f"{path}:{key_node.start_mark.line + 1}: duplicate key {key!r}")
        seen.add(key)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
files = sorted(path for path in Path().rglob("*") if path.suffix in (".yaml", ".yml") and ".github" not in path.parts)
if not files:
    raise SystemExit("no YAML files matched: the gate checked nothing")
for path in files:
    print(path)
    with path.open() as source:
        loader = Loader(source)
        try:
            loader.get_single_data()
        finally:
            loader.dispose()
