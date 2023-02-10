# Generated by Django 3.0.14 on 2022-07-10 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0016_add_last_login_on_interactive_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChequeImport',
            fields=[
                ('idChequeImport', models.AutoField(db_column='ChequeImportID', primary_key=True, serialize=False)),
                ('importDate', models.DateTimeField()),
                ('stored_file', models.FileField(blank=True, db_column='ImportFile', default='', null=True, upload_to='csImports/%Y/%m/')),
                ('user', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='core.InteractiveUser')),
            ],
            options={
                'db_table': 'tblChequeSanteImport',
            },
        ),
        migrations.CreateModel(
            name='ChequeImportLine',
            fields=[
                ('idChequeImportLine', models.AutoField(primary_key=True, serialize=False)),
                ('chequeImportLineCode', models.CharField(max_length=100)),
                ('chequeImportLineDate', models.DateTimeField()),
                ('chequeImportLineStatus', models.CharField(max_length=50)),
                ('chequeImportId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cs.ChequeImport')),
            ],
            options={
                'db_table': 'tblChequeSanteImportLine',
            },
        ),
    ]