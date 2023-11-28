from oop.classes_and_objects.exercises.spoopify.project.song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        for current_song in self.songs:
            if current_song.name == song.name:
                return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for current_song in self.songs:
            if current_song.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."

                self.songs.remove(current_song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]

        for song in self.songs:
            result.append(f"== {song.get_info()}")

        return '\n'.join(result)
