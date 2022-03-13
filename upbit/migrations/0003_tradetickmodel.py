# Generated by Django 3.2.5 on 2022-03-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upbit', '0002_markettickermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeTickModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(max_length=15)),
                ('trade_date_utc', models.CharField(max_length=15)),
                ('trade_time_utc', models.CharField(max_length=10)),
                ('timestamp', models.IntegerField()),
                ('trade_price', models.FloatField()),
                ('trade_volume', models.FloatField()),
                ('prev_closing_price', models.FloatField()),
                ('change_price', models.FloatField()),
                ('ask_bid', models.CharField(max_length=5)),
                ('sequential_id', models.IntegerField()),
            ],
            options={
                'unique_together': {('market', 'trade_date_utc', 'trade_time_utc')},
            },
        ),
    ]