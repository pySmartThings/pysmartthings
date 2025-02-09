"""Sort the Attribute enum."""

from pysmartthings.models import Attribute


def main() -> int:
    """Run the script."""
    attributes = {attr.name: attr for attr in Attribute}
    attributes = dict(sorted(attributes.items()))
    print("class Attribute(StrEnum):")
    print('    """Attribute model."""')
    print()
    for name, attribute in attributes.items():
        print(f'    {name} = "{attribute.value}"')
    return 0


if __name__ == "__main__":
    main()
