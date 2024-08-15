# fdds/storage/backup.py

import os
import shutil

class BackupManager:
    """
    Manages backups and recovery for FDDS.
    """

    def __init__(self, storage_path):
        """
        Initializes the backup manager.
        
        :param storage_path: Path to the storage directory.
        """
        self.storage_path = storage_path
        self.backup_path = os.path.join(storage_path, "backups")
        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)

    def create_backup(self, db_name):
        """
        Creates a backup of the specified database.
        
        :param db_name: The name of the database to back up.
        :return: A confirmation message.
        """
        db_path = os.path.join(self.storage_path, db_name)
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database '{db_name}' not found.")
        
        backup_name = f"{db_name}_backup"
        backup_path = os.path.join(self.backup_path, backup_name)
        shutil.copytree(db_path, backup_path)
        return f"Backup for database '{db_name}' created successfully at '{backup_path}'."

    def restore_backup(self, db_name):
        """
        Restores a database from its backup.
        
        :param db_name: The name of the database to restore.
        :return: A confirmation message.
        """
        backup_name = f"{db_name}_backup"
        backup_path = os.path.join(self.backup_path, backup_name)
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"Backup for database '{db_name}' not found.")
        
        db_path = os.path.join(self.storage_path, db_name)
        if os.path.exists(db_path):
            shutil.rmtree(db_path)
        
        shutil.copytree(backup_path, db_path)
        return f"Database '{db_name}' restored successfully from backup."
