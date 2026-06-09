import unittest
import zipfile
from tempfile import TemporaryDirectory
from pathlib import Path

from framework.pipeline import ResearchPipeline


class ResearchPipelineTest(unittest.TestCase):
    def test_rejects_empty_topic(self):
        with TemporaryDirectory() as tmp:
            pipeline = ResearchPipeline(workspace=Path(tmp))
            with self.assertRaisesRegex(ValueError, "topic must not be empty"):
                pipeline.run("   ")

    def test_rejects_unsafe_run_id(self):
        with TemporaryDirectory() as tmp:
            pipeline = ResearchPipeline(workspace=Path(tmp))
            with self.assertRaisesRegex(ValueError, "run_id may only contain"):
                pipeline.run("demo", run_id="../outside")

    def test_normalizes_topic_and_writes_artifacts(self):
        with TemporaryDirectory() as tmp:
            pipeline = ResearchPipeline(workspace=Path(tmp))
            ctx = pipeline.run("  demo  ", run_id="demo-run")

            self.assertEqual(ctx.topic, "demo")
            self.assertTrue((Path(tmp) / "runs" / "demo-run" / "01_prd.json").exists())

    def test_delivery_manifest_and_bundle_are_created(self):
        with TemporaryDirectory() as tmp:
            pipeline = ResearchPipeline(workspace=Path(tmp))
            ctx = pipeline.run("demo", run_id="bundle-run")

            manifest = ctx.run_dir / "manifest.json"
            bundle = ctx.run_dir / "bundle-run_bundle.zip"

            self.assertTrue(manifest.exists())
            self.assertTrue(bundle.exists())
            with zipfile.ZipFile(bundle) as zf:
                names = set(zf.namelist())
            self.assertIn("manifest.json", names)
            self.assertIn("README_DELIVERY.md", names)


if __name__ == "__main__":
    unittest.main()
