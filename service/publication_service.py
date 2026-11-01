class PublicationService:
    def __init__(self, publication_repository):
        self.repository = publication_repository

    def get_categories(self):
        return self.repository.get_categories()

    def save_categories(self, data, author):
        self.__validate_data(data)
        return self.repository.save_data(data, author)

    def __validate_data(self, data):
        pass

    def get_publications(self):
        return self.repository.get_publications()

    def get_user(self, login="ivan"):
        return self.repository.get_user(login)

    def get_mentors(self, theme=None):
        return self.repository.get_mentors(theme)

    def get_rating_data(self, specialist_id):
        return self.repository.get_rating_data(specialist_id)