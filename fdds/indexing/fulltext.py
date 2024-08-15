# fdds/indexing/fulltext.py

import re
from collections import defaultdict

class FullTextIndex:
    """
    Full-text search index for FDDS.
    """

    def __init__(self):
        """
        Initializes the full-text index.
        """
        self.index = defaultdict(list)

    def index_document(self, doc_id, content):
        """
        Indexes a document for full-text search.
        
        :param doc_id: The unique identifier of the document.
        :param content: The content of the document to index.
        """
        words = re.findall(r'\w+', content.lower())
        for word in words:
            self.index[word].append(doc_id)

    def search(self, term):
        """
        Searches for a term in the full-text index.
        
        :param term: The search term.
        :return: A list of document IDs where the term appears.
        """
        return self.index.get(term.lower(), [])

    def delete_document(self, doc_id):
        """
        Removes a document from the full-text index.
        
        :param doc_id: The unique identifier of the document to remove.
        """
        for word, doc_ids in self.index.items():
            self.index[word] = [id for id in doc_ids if id != doc_id]
            if not self.index[word]:
                del self.index[word]
