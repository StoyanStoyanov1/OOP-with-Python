from math import ceil


class PhotoAlbum:
    EACH_PAGE_PHOTOS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.EACH_PAGE_PHOTOS)
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.EACH_PAGE_PHOTOS:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(' '.join("[]" for _ in range(len(page))))
            result.append("-" * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
