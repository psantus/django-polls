from django.db.backends.postgresql import base


class DatabaseWrapper(base.DatabaseWrapper):
    def _savepoint_allowed(self):
        return False
