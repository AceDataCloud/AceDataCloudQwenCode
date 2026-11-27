import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ServiceArtworkTest(unittest.TestCase):
    def test_artwork_is_pinned_and_visible_in_both_catalog_languages(self):
        services = json.loads((ROOT / "services.json").read_text())
        lock = json.loads((ROOT / "source-lock.json").read_text())
        guides = [(ROOT / path).read_text() for path in ("README.md", "README_zh_Hans.md")]
        for service in services:
            with self.subTest(service=service["slug"]):
                icon = service["icon_path"]
                self.assertIn(icon, lock[service["slug"]]["files"])
                expected_url = f"https://github.com/AceDataCloud/{service['repo']}/blob/{service['head']}/{icon}"
                self.assertEqual(service["icon"], expected_url)
                path = Path("extensions") / service["slug"] / icon
                self.assertTrue((ROOT / path).is_file())
                for guide in guides:
                    self.assertIn(f'src="{path.as_posix()}"', guide)
