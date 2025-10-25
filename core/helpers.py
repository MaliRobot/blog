# Compatibility shim for legacy imports in old migrations
# Allows `import core.helpers` to resolve to the real implementation
# in apps.core.helpers without modifying historical migration files.
from apps.core.helpers import RandomFileName

__all__ = ["RandomFileName"]
