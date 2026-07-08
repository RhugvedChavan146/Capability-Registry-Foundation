import re

SEMVER_PATTERN = r"^\d+\.\d+\.\d+$"


def validate_version(version):

    return bool(re.match(SEMVER_PATTERN, version))


def validate_required(module):

    return all([
        module.name,
        module.description,
        module.category,
        module.version,
        module.author
    ])