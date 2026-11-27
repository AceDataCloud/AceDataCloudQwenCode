import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PinnedSourcesTest(unittest.TestCase):
    def test_native_snapshot_matches_the_source_lock(self):
        services = json.loads((ROOT / 'services.json').read_text())
        lock = json.loads((ROOT / 'source-lock.json').read_text())
        self.assertEqual(set(lock), {s['slug'] for s in services})
        for s in services:
            row = lock[s['slug']]
            self.assertEqual(row['commit'], s['head'])
            self.assertEqual(row['repo'], 'AceDataCloud/' + s['repo'])
            destination = ROOT / 'extensions' / s['slug']
            for path, digest in row['files'].items():
                self.assertEqual(hashlib.sha256((destination / path).read_bytes()).hexdigest(), digest)
            native = json.loads((destination / 'qwen-extension.json').read_text())
            bridge = json.loads((destination / '.claude-plugin/plugin.json').read_text())
            self.assertEqual(bridge, {key:native[key] for key in ('name','version','description','mcpServers')})
