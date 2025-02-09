"""Process the device status JSON file to generate a tree of a device status."""

import json
from pathlib import Path
import re
import sys

from treelib import Tree

from pysmartthings.models import Attribute, Capability


def main() -> int:
    """Run the script."""
    if len(sys.argv) != 2:
        print("Usage: python process_device_status.py <filename>")
        return 1
    filename = sys.argv[1]
    print(f"Processing {filename}")
    with Path(filename).open(encoding="utf-8") as file:
        data = json.load(file)
    components = data["components"]
    tree = Tree()
    found_capabilities = {}
    found_attributes = {}
    tree.create_node(filename, "root")
    for component_name, capabilities in components.items():
        tree.create_node(component_name, component_name, parent="root")
        for capability_name, attributes in capabilities.items():
            if capability_name not in Capability:
                found_capabilities[capability_name] = re.sub(
                    r"(?<!^)(?=[A-Z])", "_", capability_name
                ).upper()
            tree.create_node(
                capability_name,
                f"{component_name}-{capability_name}",
                parent=component_name,
            )
            for attribute in attributes:
                if attribute not in Attribute:
                    found_attributes[attribute] = re.sub(
                        r"(?<!^)(?=[A-Z])", "_", attribute
                    ).upper()
                tree.create_node(
                    attribute,
                    f"{component_name}-{capability_name}-{attribute}",
                    parent=f"{component_name}-{capability_name}",
                )
    print(tree.show(stdout=False))
    if found_capabilities:
        print("\nFound capabilities:")
        for capability_name, slug in found_capabilities.items():
            print(f'{slug} = "{capability_name}"')
    if found_attributes:
        print("\nFound attributes:")
        for attribute_name, slug in found_attributes.items():
            print(f'{slug} = "{attribute_name}"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
