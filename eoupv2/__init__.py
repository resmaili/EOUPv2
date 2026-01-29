"""EOUP v2 - Earth Observations Using Python"""

__version__ = "1.0.0"

from .data import setup_book_data, load_chapter_data
from .utils import *

__all__ = ["setup_book_data", "load_chapter_data"]