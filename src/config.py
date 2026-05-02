from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT_DIR / "assets"
GENERATED_DIR = ASSETS_DIR / "generated"
EXPORTS_DIR = ASSETS_DIR / "exports"


def load_environment() -> None:
    """Load local environment variables from .env if present."""
    load_dotenv(ROOT_DIR / ".env")
