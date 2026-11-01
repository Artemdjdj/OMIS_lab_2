from models.manager import DBManager


class PublicationRepository:
    def __init__(self):
        self.db_manager = DBManager()

    def get_categories(self):
        return self.db_manager.get_categories()

    def save_data(self, data, author):
        return self.db_manager.save_categories(data, author)

    def get_publications(self):
        return self.db_manager.get_publications()

    def get_user(self, login="ivan"):
        return self.db_manager.get_user(login)

    def get_mentors(self, theme=None):
        return self.db_manager.get_mentors(theme)

    def get_rating_data(self, specialist_id):
        return self.db_manager.get_rating_data(specialist_id)