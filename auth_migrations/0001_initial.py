from django.db import migrations


class Migration(migrations.Migration):

    initial = True
    atomic = False

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="CREATE TABLE auth_permission (id integer NOT NULL PRIMARY KEY, name varchar(255) NOT NULL, content_type_id integer NOT NULL, codename varchar(100) NOT NULL, UNIQUE (content_type_id, codename))",
            reverse_sql="DROP TABLE auth_permission"
        ),
        migrations.RunSQL(
            sql="CREATE TABLE auth_group (id integer NOT NULL PRIMARY KEY, name varchar(150) NOT NULL UNIQUE)",
            reverse_sql="DROP TABLE auth_group"
        ),
        migrations.RunSQL(
            sql="CREATE TABLE auth_group_permissions (id integer NOT NULL PRIMARY KEY, group_id integer NOT NULL, permission_id integer NOT NULL, UNIQUE (group_id, permission_id))",
            reverse_sql="DROP TABLE auth_group_permissions"
        ),
        migrations.RunSQL(
            sql="CREATE TABLE auth_user (id integer NOT NULL PRIMARY KEY, password varchar(128) NOT NULL, last_login timestamp with time zone, is_superuser boolean NOT NULL, username varchar(150) NOT NULL UNIQUE, first_name varchar(150) NOT NULL, last_name varchar(150) NOT NULL, email varchar(254) NOT NULL, is_staff boolean NOT NULL, is_active boolean NOT NULL, date_joined timestamp with time zone NOT NULL)",
            reverse_sql="DROP TABLE auth_user"
        ),
        migrations.RunSQL(
            sql="CREATE TABLE auth_user_groups (id integer NOT NULL PRIMARY KEY, user_id integer NOT NULL, group_id integer NOT NULL, UNIQUE (user_id, group_id))",
            reverse_sql="DROP TABLE auth_user_groups"
        ),
        migrations.RunSQL(
            sql="CREATE TABLE auth_user_user_permissions (id integer NOT NULL PRIMARY KEY, user_id integer NOT NULL, permission_id integer NOT NULL, UNIQUE (user_id, permission_id))",
            reverse_sql="DROP TABLE auth_user_user_permissions"
        ),
    ]
