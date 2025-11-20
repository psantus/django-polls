from django.db import migrations


class Migration(migrations.Migration):

    initial = True
    atomic = False

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE django_content_type (
                    id integer NOT NULL PRIMARY KEY,
                    app_label varchar(100) NOT NULL,
                    model varchar(100) NOT NULL,
                    UNIQUE (app_label, model)
                )
            """,
            reverse_sql="DROP TABLE django_content_type"
        ),
    ]
