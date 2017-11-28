# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 11:23
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Course Type',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.TextField()),
                ('all_do', models.BooleanField(default=False)),
                ('pronunciation', models.CharField(blank=True, max_length=255, null=True)),
                ('context_vocabulary', models.CharField(blank=True, max_length=255, null=True)),
                ('reformulation_text', models.TextField(blank=True, null=True)),
                ('reformulation_audio', models.BooleanField(default=False)),
                ('enrollment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ComSemApp.Enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state_province', models.CharField(choices=[('AK', 'AK'), ('AL', 'AL'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'), ('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MS', 'MS'), ('MT', 'MT'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'), ('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], max_length=2)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SequentialWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Expression')),
            ],
            options={
                'verbose_name_plural': 'Sequential Words',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Institution')),
            ],
            options={
                'verbose_name': 'Session Type',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ComSemApp.Country')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Institution')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ComSemApp.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reformulation_text', models.TextField(blank=True, null=True)),
                ('reformulation_audio', models.BooleanField(default=False)),
                ('correct', models.BooleanField()),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Expression')),
            ],
            options={
                'verbose_name': 'Student Attempt',
            },
        ),
        migrations.CreateModel(
            name='StudentSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ungraded', 'ungraded'), ('complete', 'complete'), ('incomplete', 'incomplete')], default='ungraded', max_length=255)),
                ('enrollment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ComSemApp.Enrollment')),
            ],
            options={
                'verbose_name': 'Student Submission',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ManyToManyField(to='ComSemApp.Institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teaching Instance',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=255)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('released', models.BooleanField(default=False)),
                ('display_original', models.BooleanField(default=True)),
                ('display_reformulation_text', models.BooleanField(default=True)),
                ('display_reformulation_audio', models.BooleanField(default=True)),
                ('display_all_expressions', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Course')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='studentsubmission',
            name='worksheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Worksheet'),
        ),
        migrations.AddField(
            model_name='studentattempt',
            name='student_submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.StudentSubmission'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='sessiontype',
            order_with_respect_to='order',
        ),
        migrations.AddField(
            model_name='session',
            name='session_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.SessionType'),
        ),
        migrations.AddField(
            model_name='sequentialwords',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Word'),
        ),
        migrations.AddField(
            model_name='expression',
            name='worksheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Worksheet'),
        ),
        migrations.AddField(
            model_name='coursetype',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Institution'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.CourseType'),
        ),
        migrations.AddField(
            model_name='course',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Session'),
        ),
        migrations.AddField(
            model_name='admin',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComSemApp.Institution'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]