# Generated by Django 4.0.2 on 2022-03-01 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_rename_answer_quesmodel_ans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='ans',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='question',
            new_name='questions',
        ),
    ]