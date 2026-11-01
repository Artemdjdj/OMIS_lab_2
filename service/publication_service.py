
class PublicationService:
    def __init__(self, publication_repository):
        self.repository = publication_repository

    def get_categories(self):
        return self.repository.get_categories()

    def save_categories(self, data, author):
        self.__validate_data(data)
        self.repository.save_data(data, author)

    def __validate_data(self, data):
        pass