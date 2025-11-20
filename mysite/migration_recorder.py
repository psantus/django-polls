from django.db.migrations.recorder import MigrationRecorder as BaseMigrationRecorder

class MigrationRecorder(BaseMigrationRecorder):
    def record_applied(self, app, name):
        """Record that a migration was applied, generating ID manually."""
        # Get the next ID
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM django_migrations")
            next_id = cursor.fetchone()[0]
        
        # Create the migration record with explicit ID
        self.migration_qs.create(id=next_id, app=app, name=name)
