from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self._find_by_name(name, self.musicians):
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)

        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self._find_by_name(name, self.bands):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._find_by_place(place, self.concerts)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_by_name(musician_name, self.musicians)
        band = self._find_by_name(band_name, self.bands)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_by_name(band_name, self.bands)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        for musician in band.members:
            if musician.name == musician_name:
                band.members.remove(musician)
                return f"{musician_name} was removed from {band_name}."

        raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):
        concert = self._find_by_place(concert_place, self.concerts)
        band = self._find_by_name(band_name, self.bands)
        drummer = self._find_musical_by_type("Drummer", band.members)
        singer = self._find_musical_by_type("Singer", band.members)
        guitarist = self._find_musical_by_type("Guitarist", band.members)

        if not drummer or not singer or not guitarist:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if self._play_concert()[concert.genre]["Drummer"] not in drummer.skills or any(
                skill not in singer.skills for skill in self._play_concert()[concert.genre]["Singer"]) or \
                self._play_concert()[concert.genre]["Guitarist"] not in guitarist.skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    @staticmethod
    def _find_by_name(name, arr):
        for el in arr:
            if el.name == name:
                return el

    @staticmethod
    def _find_by_place(place, arr):
        for concert in arr:
            if concert.place == place:
                return concert

    @staticmethod
    def _find_musical_by_type(current_type, arr):
        for musician in arr:
            if musician.__class__.__name__ == current_type:
                return musician

    @staticmethod
    def _play_concert():
        return {"Rock": {
            "Drummer": "play the drums with drumsticks",
            "Singer": ["sing high pitch notes"],
            "Guitarist": "play rock"},
            "Metal": {
                "Drummer": "play the drums with drumsticks",
                "Singer": ["sing low pitch notes"],
                "Guitarist": "play metal"},
            "Jazz": {
                "Drummer": "play the drums with drum brushes",
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
                "Guitarist": "play jazz"}
        }
