"""Process the device status JSON file to generate a tree of a device status."""

import json
from pathlib import Path
import re
import sys
from typing import Any, Callable

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


def prepare_attribute_name(attribute: str) -> str:
    """Prepare attribute name."""
    return {
        "dmv": "DATA_MODEL_VERSION",
        "drlcStatus": "DEMAND_RESPONSE_LOAD_CONTROL_STATUS",
        "di": "DEVICE_ID",
        "n": "DEVICE_NAME",
        "mnhw": "HARDWARE_VERSION",
        "mnml": "MANUFACTURER_DETAILS_LINK",
        "mnmn": "MANUFACTURER_NAME",
        "mndt": "MANUFACTURE_DATE",
        "mnmo": "MODEL_NUMBER",
        "mnfv": "OCF_FIRMWARE_VERSION",
        "mnos": "OS_VERSION",
        "pH": "PH",
        "pi": "PLATFORM_ID",
        "mnpv": "PLATFORM_VERSION",
        "icv": "SPEC_VERSION",
        "mnsl": "SUPPORT_LINK",
        "st": "SYSTEM_TIME",
        "vid": "VENDOR_ID",
    }.get(
        attribute, re.sub(r"(?<!^)(?=[A-Z])", "_", attribute).upper().replace("-", "")
    )


def prepare_command_name(command: str) -> str:
    """Prepare command name."""
    return (
        re.sub(r"(?<!^)(?=[A-Z])", "_", command)
        .upper()
        .replace("DRLC", "DEMAND_RESPONSE_LOAD_CONTROL")
    )


def main() -> int:  # pylint: disable=too-many-locals, too-many-statements  # noqa: PLR0912 PLR0915
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
        name = prepare_attribute_name(attribute)
        file += f'    {name} = "{attribute}"\n'

    file += "\n"
    file += "CAPABILITY_ATTRIBUTES: dict[Capability, list[Attribute]] = {\n"

    for ns in ORDER:
        for cap in sorted(capability_attributes[ns]):
            attr2 = capability_attributes[ns][cap]
            file = render_capability(
                file, cap, attr2, "Attribute", prepare_attribute_name
            )
        file += "\n"

    for ns, attr in capability_attributes.items():
        if ns in ORDER:
            continue
        for cap in sorted(attr):
            attr2 = attr[cap]
            file = render_capability(
                file, cap, attr2, "Attribute", prepare_attribute_name
            )
        file += "\n"
    file += "}\n"
    Path("src/pysmartthings/attribute.py").write_text(file, encoding="utf-8")
    command_file = '"""Command model."""\n'
    command_file += "from enum import StrEnum\n"
    command_file += "from pysmartthings.capability import Capability\n"
    command_file += "class Command(StrEnum):\n"
    command_file += '    """Command model."""\n'
    for command in sorted(
        commands,
        key=lambda x: re.sub(r"(?<!^)(?=[A-Z])", "_", x)
        .upper()
        .replace("-", "")
        .lower(),
    ):
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", command).upper()
        command_file += f'    {name} = "{command}"\n'
    command_file += "\n"
    command_file += "CAPABILITY_COMMANDS: dict[Capability, list[Command]] = {\n"

    for ns in ORDER:
        for cap in sorted(capability_commands[ns]):
            attr2 = capability_commands[ns][cap]
            command_file = render_capability(
                command_file,
                cap,
                attr2,
                "Command",
                lambda x: re.sub(r"(?<!^)(?=[A-Z])", "_", x).upper(),
            )
        command_file += "\n"

    for ns, attr in capability_commands.items():
        if ns in ORDER:
            continue
        for cap in sorted(attr):
            attr2 = attr[cap]
            command_file = render_capability(
                command_file,
                cap,
                attr2,
                "Command",
                lambda x: re.sub(r"(?<!^)(?=[A-Z])", "_", x).upper(),
            )
    command_file += "}\n"
    Path("src/pysmartthings/command.py").write_text(command_file, encoding="utf-8")
    return 0


def render_capability(
    file: str,
    capability: str,
    attributes: list[str],
    class_name: str,
    name_fn: Callable[[str], str],
) -> str:
    """Render capability."""
    capability_name = prepare_capability_name(capability)
    file += f"    Capability.{capability_name}: ["
    first = True
    for attribute in sorted(attributes, key=prepare_attribute_name):
        print(attribute)
        if first:
            first = False
        else:
            file += ", "
        name = name_fn(attribute)
        file += f"{class_name}.{name}"
    file += "],\n"
    return file


if __name__ == "__main__":
    sys.exit(main())
