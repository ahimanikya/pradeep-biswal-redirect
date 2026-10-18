"""Keep existing HTML and extensionless bookmarks returning a normal page."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
template=(root/'index.html').read_text()
for route in json.loads((root/'routes.json').read_text()):
    path=Path(route)
    assert not path.is_absolute() and '..' not in path.parts and path.suffix=='.html'
    for relative in [path,path.with_suffix('')/'index.html']:
        target=root/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(template)
print('Prepared forwarding pages for existing article, book and review addresses.')
