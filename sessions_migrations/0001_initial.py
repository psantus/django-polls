from django.db import migrations


class Migration(migrations.Migration):

    initial = True
    atomic = False

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql="CREATE TABLE django_session (session_key varchar(40) NOT NULL PRIMARY KEY, session_data text NOT NULL, expire_date timestamp with time zone NOT NULL)",
            reverse_sql="DROP TABLE django_session"
        ),
    ]
