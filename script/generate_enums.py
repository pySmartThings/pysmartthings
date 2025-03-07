"""Process the device status JSON file to generate a tree of a device status."""

import json
from pathlib import Path
import re
import sys
from typing import Any

ORDER = ["standard", "custom", "samsungce", "samsungvd", "samsungim"]


def prepare_capability_name(capability_name: str) -> str:
    """Prepare capability name."""
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", capability_name).upper()
    for k, v in {
        ".": "_",
        "SAMSUNGCE": "SAMSUNG_CE",
        "SAMSUNGVD": "SAMSUNG_VD",
        "SAMSUNGIM": "SAMSUNG_IM",
        "P_H_": "PH_",
        "ZW_MULTI": "ZWAVE_MULTI",
        "CUSTOM_SOUNDMODE": "CUSTOM_SOUND_MODE",
        "CUSTOM_TVSEARCH": "CUSTOM_TV_SEARCH",
        "CUSTOM_PICTUREMODE": "CUSTOM_PICTURE_MODE",
        "CUSTOM_LAUNCHAPP": "CUSTOM_LAUNCH_APP",
        "SYNTHETIC_LIGHTING_EFFECT_CIRCADIAN": "SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT",
        "SYNTHETIC_LIGHTING_EFFECT_FADE": "SYNTHETIC_FADE_LIGHTNING_EFFECT",
    }.items():
        name = name.replace(k, v)
    return name


def main() -> int:  # noqa: PLR0912  # noqa: PLR0915
    """Run the script."""
    attributes = set()
    commands = set()
    capability_attributes: dict[str, Any] = {}
    capability_commands: dict[str, Any] = {}
    root = Path("capabilities/json")
    for namespace in root.iterdir():
        for js in namespace.iterdir():
            with js.open(encoding="utf-8") as f:
                data = json.load(f)
            ns = data["id"].split(".")[0] if "." in data["id"] else "standard"
            if ns not in capability_attributes:
                capability_attributes[ns] = {}
                capability_commands[ns] = {}
            capability_attributes[ns][data["id"]] = []
            capability_commands[ns][data["id"]] = []
            for attribute in data["attributes"]:
                attributes.add(attribute)
                capability_attributes[ns][data["id"]].append(attribute)
            capability_commands[data["id"]] = []
            for command in data["commands"]:
                commands.add(command)
                capability_commands[ns][data["id"]].append(command)
    file = '"""Attribute model."""\n'
    file += "from enum import StrEnum\n"
    file += "from pysmartthings.capability import Capability\n"
    file += "class Attribute(StrEnum):\n"
    file += '    """Attribute model."""\n'
    for attribute in sorted(
        attributes,
        key=lambda x: re.sub(r"(?<!^)(?=[A-Z])", "_", x)
        .upper()
        .replace("-", "")
        .lower(),
    ):
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", attribute).upper().replace("-", "")
        file += f'    {name} = "{attribute}"\n'

    file += "\n"
    file += "CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {\n"

    for ns in ORDER:
        for capability in sorted(capability_attributes[ns]):
            attributes = capability_attributes[ns][capability]
            capability_name = prepare_capability_name(capability)
            file += f"    Capability.{capability_name}: ["
            first = True
            for attribute in sorted(attributes):
                if first:
                    first = False
                else:
                    file += ", "
                name = (
                    re.sub(r"(?<!^)(?=[A-Z])", "_", attribute).upper().replace("-", "")
                )
                file += f"Attribute.{name}"
            file += "],\n"
        file += "\n"

    for ns, capability in capability_attributes.items():
        if ns in ORDER:
            continue
        for cap, attributes in capability.items():
            capability_name = prepare_capability_name(cap)
            file += f"    Capability.{capability_name}: ["
            first = True
            for attribute in sorted(attributes):
                if first:
                    first = False
                else:
                    file += ", "
                name = (
                    re.sub(r"(?<!^)(?=[A-Z])", "_", attribute).upper().replace("-", "")
                )
                file += f"Attribute.{name}"
            file += "],\n"
        file += "\n"
    file += "}\n"
    Path("src/pysmartthings/attribute.py").write_text(file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
