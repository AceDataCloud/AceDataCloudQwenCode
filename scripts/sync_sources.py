"""Rebuild Qwen marketplace snapshots from the independently pinned extension sources."""
import io
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = {"qwen-extension.json", "QWEN.md", "README.md", "README_zh_Hans.md", "LICENSE"}
PREFIX = {"commands", "readme", "assets", "_assets", "skills", "agents", "workflows"}


def selected(path):
    p = PurePosixPath(path)
    return not p.is_absolute() and ".." not in p.parts and (path in INCLUDE or p.parts[0] in PREFIX)


def unpack(service, archive):
    root = ROOT / "extensions" / service["slug"]
    root.mkdir(exist_ok=True, parents=True)
    members = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as tar:
        for member in tar:
            path = PurePosixPath(member.name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("Invalid archive path")
            rel = PurePosixPath(*path.parts[1:])
            if not member.isfile() or not rel.parts or not selected(str(rel)):
                continue
            data = tar.extractfile(member).read()
            dest = root.joinpath(*rel.parts)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            members[str(rel)] = hashlib.sha256(data).hexdigest()
    native = json.loads((root / "qwen-extension.json").read_bytes())
    if native["name"] != service["name"] or native["version"] != service["version"]:
        raise ValueError("Pinned upstream identity differs from catalog")
    bridge = {k: native[k] for k in ("name", "version", "description", "mcpServers")}
    target = root / ".claude-plugin/plugin.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(bridge, ensure_ascii=False, indent=2) + "\n")
    return {"repo": "AceDataCloud/" + service["repo"], "commit": service["head"], "files": members}


if __name__ == "__main__":
    ledger = {}
    for service in json.loads((ROOT / "services.json").read_text()):
        url = "https://api.github.com/repos/AceDataCloud/" + service["repo"] + "/tarball/" + service["head"]
        with urlopen(Request(url, headers={"User-Agent": "AceDataCloud Qwen catalog"}), timeout=45) as response:
            ledger[service["slug"]] = unpack(service, response.read())
    (ROOT / "source-lock.json").write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")
