import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CatalogTests(unittest.TestCase):
    def test_five_distinct_native_archives(self):
        entries = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['plugins']
        self.assertEqual(len(entries), 5)
        self.assertEqual(len({x['name'] for x in entries}), 5)
        self.assertEqual(len({x['source']['url'] for x in entries}), 5)
        for item in entries:
            self.assertEqual(item['author']['name'], 'Ace Data Cloud')
            self.assertTrue(item['source']['url'].endswith('.tar.gz'))
            self.assertRegex(item['source']['url'], r'/archive/[a-f0-9]{40}[.]tar[.]gz$')
            self.assertTrue(item['keywords'])
            self.assertNotIn('installs', item)
            self.assertNotIn('downloads', item)

if __name__ == '__main__': unittest.main()
