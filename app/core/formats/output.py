from abc import abstractmethod, ABC
from core.models import Program


# pylint: disable=too-few-public-methods
class Page:
    def __init__(self, content: bytes):
        self.content = content


class Chapter:
    def __init__(self):
        self.pages = []

    def add_pages(self, pages: list[Page]) -> None:
        self.pages.extend(pages)

    def add_page(self, page: Page) -> None:
        return self.add_pages([page])


class OutputFormat(ABC):
    def __init__(self, program: Program):
        self.chapters: list[Chapter]  = []
        self.program = program

    def add_chapters(self, chapters: list[Chapter]) -> None:
        self.chapters.extend(chapters)

    def add_chapter(self, chapter: Chapter) -> None:
        self.add_chapters([chapter])

    @abstractmethod
    def format_name(self) -> str:
        pass

    @abstractmethod
    def output(self, filename: str, **kwargs) -> None:
        pass
