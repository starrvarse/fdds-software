# fdds/utils/encryption.py

from cryptography.fernet import Fernet

class FDDSEncryption:
    """
    Utility for encrypting and decrypting data in FDDS.
    """

    def __init__(self, key=None):
        """
        Initializes the encryption utility.
        
        :param key: The encryption key. If not provided, a new key will be generated.
        """
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """
        Encrypts the given data.
        
        :param data: The data to encrypt (must be bytes).
        :return: The encrypted data.
        """
        if not isinstance(data, bytes):
            raise ValueError("Data to encrypt must be in bytes.")
        return self.cipher.encrypt(data)

    def decrypt(self, encrypted_data):
        """
        Decrypts the given encrypted data.
        
        :param encrypted_data: The data to decrypt (must be bytes).
        :return: The decrypted data.
        """
        if not isinstance(encrypted_data, bytes):
            raise ValueError("Encrypted data must be in bytes.")
        return self.cipher.decrypt(encrypted_data)

    def get_key(self):
        """
        Returns the encryption key.
        
        :return: The encryption key.
        """
        return self.key
