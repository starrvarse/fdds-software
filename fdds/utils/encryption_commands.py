# fdds/utils/encryption_commands.py

class EncryptDataCommand:
    """
    Command to encrypt data using FDDS encryption utility.
    """

    def __init__(self, encryption_util):
        self.encryption_util = encryption_util

    def execute(self, data):
        """
        Executes the command to encrypt data.
        
        :param data: The data to be encrypted (must be in bytes).
        :return: The encrypted data.
        """
        encrypted_data = self.encryption_util.encrypt(data)
        return encrypted_data

class DecryptDataCommand:
    """
    Command to decrypt data using FDDS encryption utility.
    """

    def __init__(self, encryption_util):
        self.encryption_util = encryption_util

    def execute(self, encrypted_data):
        """
        Executes the command to decrypt data.
        
        :param encrypted_data: The encrypted data to be decrypted (must be in bytes).
        :return: The decrypted data.
        """
        decrypted_data = self.encryption_util.decrypt(encrypted_data)
        return decrypted_data

class GetEncryptionKeyCommand:
    """
    Command to retrieve the current encryption key.
    """

    def __init__(self, encryption_util):
        self.encryption_util = encryption_util

    def execute(self):
        """
        Executes the command to retrieve the encryption key.
        
        :return: The encryption key.
        """
        key = self.encryption_util.get_key()
        return key
