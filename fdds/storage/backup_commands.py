# fdds/storage/backup_commands.py

class CreateBackupCommand:
    """
    Command to create a backup of a database in FDDS.
    """

    def __init__(self, backup_manager):
        self.backup_manager = backup_manager

    def execute(self, db_name):
        """
        Executes the command to create a backup.
        
        :param db_name: The name of the database to back up.
        :return: A confirmation message.
        """
        result = self.backup_manager.create_backup(db_name)
        return result

class RestoreBackupCommand:
    """
    Command to restore a database from a backup in FDDS.
    """

    def __init__(self, backup_manager):
        self.backup_manager = backup_manager

    def execute(self, db_name):
        """
        Executes the command to restore a database.
        
        :param db_name: The name of the database to restore.
        :return: A confirmation message.
        """
        result = self.backup_manager.restore_backup(db_name)
        return result
