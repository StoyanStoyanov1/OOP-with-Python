from typing import List

from exams.retake_exam_18_april_2022.project.movie_specification.movie import Movie
from exams.retake_exam_18_april_2022.project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List = []
        self.users_collection: List = []

    def _find_user_in_users_collection(self, username: str):
        for user in self.users_collection:
            if user.username == username:
                return user

    def _find_movie_in_movies_collection(self, current_movie: object):
        for movie in self.movies_collection:
            if movie == current_movie:
                return movie

    def register_user(self, username: str, age: int):
        if self._find_user_in_users_collection(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._find_user_in_users_collection(username)
        if not user:
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for current_movie in user.movies_owned:
            if current_movie == movie:
                raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        current_movie = self._find_movie_in_movies_collection(movie)
        if not current_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if current_movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():
            setattr(current_movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_movie = self._find_movie_in_movies_collection(movie)
        if current_movie:
            self.movies_collection.remove(current_movie)
            return f"{username} successfully deleted {movie.title} movie."

        raise Exception(f"The movie {movie.title} is not uploaded!")

    def like_movie(self, username: str, movie: Movie):
        user = self._find_user_in_users_collection(username)
        current_movie = self._find_movie_in_movies_collection(movie)

        if current_movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        for like_movie in user.movies_liked:
            if like_movie == current_movie:
                raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(current_movie)
        current_movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):

        user = self._find_user_in_users_collection(username)
        if not user:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        current_movie = self._find_movie_in_movies_collection(movie)

        for like_movie in user.movies_liked:
            if like_movie == current_movie:
                user.movies_liked.remove(like_movie)
                movie.likes -= 1
                return f"{username} disliked {movie.title} movie."

        raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        result = "\n".join([movie.details() for movie in sorted_movies])
        return result if result else "No movies found."

    def __str__(self):
        all_users = ', '.join(user.username for user in self.users_collection) or "No users."
        all_movies = ', '.join(movie.title for movie in self.movies_collection) or "No movies."

        return f"All users: {all_users}\nAll movies: {all_movies}"
