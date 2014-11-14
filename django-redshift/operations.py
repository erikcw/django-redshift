from __future__ import unicode_literals

from django.db.backends.postgresql_psycopg2.operations import DatabaseOperations as BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):
    def last_insert_id(self, cursor, table_name, pk_name):
        # Use pg_get_serial_sequence to get the underlying sequence name
        # from the table name and column name (available since PostgreSQL 8)
        cursor.execute("SELECT MAX(%s) FROM %s" % (
             pk_name, self.quote_name(table_name)))
        return cursor.fetchone()[0]
