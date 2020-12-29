from typing import Dict, Any
import yaml
from jinja2 import Template, Undefined


class NullUndefined(Undefined):
    def __getattr__(
            self,
            key: Any
    ) -> str:
        return ''


def load(
        buffer,
) -> Dict:

    t = Template(buffer, undefined=NullUndefined)

    return yaml.safe_load(t.render(yaml.safe_load(t.render())))
