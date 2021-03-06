# Generated by Django 3.2.9 on 2022-05-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_lexdto_id_miss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lexdto',
            name='id_lex',
            field=models.ManyToManyField(blank=True, null=True, related_name='LexDTO_lex_id_lex', to='api.Lexemes'),
        ),
        migrations.AlterField(
            model_name='lexdto',
            name='id_variant',
            field=models.ManyToManyField(blank=True, null=True, related_name='LexDTO_lex_id_variant', to='api.Lexemes'),
        ),
    ]
