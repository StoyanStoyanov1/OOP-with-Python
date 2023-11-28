from exams.exam_10_december_2022.project import Category
from exams.exam_10_december_2022.project import Document
from exams.exam_10_december_2022.project import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def find_by_id(self, current_id, received_list):
        for obj in received_list:
            if obj.id == current_id:
                return obj

    def edit_category(self, category_id, new_name):
        category = self.find_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.find_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove(self.find_by_id(category_id, self.categories))

    def delete_topic(self, topic_id):
        self.topics.remove(self.find_by_id(topic_id, self.topics))

    def delete_document(self, document_id):
        self.documents.remove(self.find_by_id(document_id, self.documents))

    def get_document(self, document_id):
        return self.find_by_id(document_id, self.documents)

    def __repr__(self):
        result = []
        for document in self.documents:
            result.append(repr(document))

        return "\n".join(result)