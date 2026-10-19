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

    def test_catalog_pins_match_independent_service_releases(self):
        entries = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['plugins']
        services = json.loads((ROOT/'services.json').read_text())
        self.assertEqual({x['name'] for x in entries}, {x['name'] for x in services})
        for service in services:
            entry = next(x for x in entries if x['name'] == service['name'])
            repo = 'https://github.com/AceDataCloud/' + service['repo']
            self.assertEqual(entry['version'], service['version'])
            self.assertEqual(entry['homepage'], repo + '/tree/' + service['head'])
            self.assertEqual(entry['source']['url'], repo + '/archive/' + service['head'] + '.tar.gz')
        gpt = next(x for x in services if x['repo'] == 'GPTImageQwenCode')
        self.assertEqual(gpt['transport'], 'stdio')
        self.assertEqual(gpt['profile'], 'gpt-image')
        self.assertEqual(len(gpt['tools']), 5)
        self.assertTrue(all(x.startswith('gpt_image_') for x in gpt['tools']))

if __name__ == '__main__': unittest.main()
