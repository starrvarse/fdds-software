# fdds/indexing/hashindex.py

class HashIndex:
    """
    Hash-based index for FDDS.
    """

    def __init__(self):
        """
        Initializes the hash index.
        """
        self.index = {}

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash index.
        
        :param key: The key to index.
        :param value: The value associated with the key.
        """
        if key in self.index:
            self.index[key].append(value)
        else:
            self.index[key] = [value]

    def search(self, key):
        """
        Searches for a key in the hash index.
        
        :param key: The key to search for.
        :return: A list of values associated with the key, or None if not found.
        """
        return self.index.get(key, None)

    def delete(self, key, value=None):
        """
        Deletes a key or a specific value associated with a key from the hash index.
        
        :param key: The key to delete.
        :param value: The specific value to delete (if None, delete the key entirely).
        """
        if key in self.index:
            if value is None:
                del self.index[key]
            else:
                self.index[key] = [v for v in self.index[key] if v != value]
                if not self.index[key]:
                    del self.index[key]
