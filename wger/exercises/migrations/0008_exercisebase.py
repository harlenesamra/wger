# Generated by Django 3.1.4 on 2020-12-11 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201201_0653'),
        ('exercises', '0007_auto_20201203_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_author', models.CharField(blank=True, help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', max_length=50, null=True, verbose_name='Author')),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1', editable=False, max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercisecategory', verbose_name='Category')),
                ('equipment', models.ManyToManyField(blank=True, to='exercises.Equipment', verbose_name='Equipment')),
                ('license', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.license', verbose_name='License')),
                ('muscles', models.ManyToManyField(blank=True, to='exercises.Muscle', verbose_name='Primary muscles')),
                ('muscles_secondary', models.ManyToManyField(blank=True, related_name='secondary_muscles_base', to='exercises.Muscle', verbose_name='Secondary muscles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
