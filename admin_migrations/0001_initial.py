from django.db import migrations


class Migration(migrations.Migration):

    initial = True
    atomic = False

    dependencies = [
        ('auth', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="CREATE TABLE django_admin_log (id integer NOT NULL PRIMARY KEY, action_time timestamp with time zone NOT NULL, object_id text, object_repr varchar(200) NOT NULL, action_flag smallint NOT NULL, change_message text NOT NULL, content_type_id integer, user_id integer NOT NULL)",
            reverse_sql="DROP TABLE django_admin_log"
        ),
    ]
