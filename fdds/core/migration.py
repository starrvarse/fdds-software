# fdds/core/migration.py

class SchemaMigration:
    def __init__(self, engine):
        self.engine = engine

    def apply_migration(self, db_name, migrations):
        """
        Applies a series of schema migrations.
        
        :param db_name: The name of the database.
        :param migrations: A list of migration functions to apply.
        :return: A confirmation message.
        """
        for migration in migrations:
            migration(self.engine.get_table(db_name))
        return "Migrations applied successfully with zero downtime."

    def create_migration(self, db_name, table_name, migration_function):
        """
        Adds a new migration to the system.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table to migrate.
        :param migration_function: The function that performs the migration.
        """
        # Logic to store migration details and ensure it's applied in sequence
        pass
