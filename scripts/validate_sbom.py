"""Validate the training SBOM against package.json."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sbom_path = ROOT / "sbom_fixture.json"
manifest_path = ROOT / "package.json"


def main():
    try:
        sbom = json.loads(sbom_path.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Validation failed: {error}")
        return 1

    if sbom.get("bomFormat") != "CycloneDX":
        print("Validation failed: SBOM format must be CycloneDX.")
        return 1

    if not isinstance(sbom.get("specVersion"), str):
        print("Validation failed: missing specification version.")
        return 1

    components = sbom.get("components")

    if not isinstance(components, list):
        print("Validation failed: components must be a list.")
        return 1

    dependencies = {}
    dependencies.update(manifest.get("dependencies", {}))
    dependencies.update(manifest.get("devDependencies", {}))

    sbom_components = {}

    for component in components:
        required = ("type", "name", "version", "purl")

        if not isinstance(component, dict) or any(
            not component.get(field) for field in required
        ):
            print("Validation failed: a component has missing fields.")
            return 1

        sbom_components[component["name"]] = component["version"]

    if sbom_components != dependencies:
        print("Validation failed: SBOM does not match package.json.")
        print("Manifest:", dependencies)
        print("SBOM:", sbom_components)
        return 1

    print("SBOM validation passed.")
    print(f"Format: {sbom['bomFormat']}")
    print(f"Specification version: {sbom['specVersion']}")
    print(f"Components validated: {len(components)}")
    print("All components match package.json.")
    print("Note: This is a training fixture, not a full official schema validation.")

    return 0


if __name__ == "__main__":
    sys.exit(main())