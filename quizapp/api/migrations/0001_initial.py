# Generated by Django 3.2.2 on 2021-06-18 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizname', models.CharField(max_length=255)),
                ('quizdetails', models.TextField()),
                ('quizdate', models.DateTimeField()),
                ('open', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('host_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.BooleanField(default=False)),
                ('points', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.hostquiz')),
                ('right_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rightoption', to='api.option')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.questions'),
        ),
        migrations.CreateModel(
            name='JoinQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('time_taken', models.DurationField(blank=True, null=True)),
                ('last_joined', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined', to=settings.AUTH_USER_MODEL)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_quiz_name', to='api.hostquiz')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('chosen_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.option')),
                ('joinquiz_id', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='entered_answers', to='api.joinquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questions')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizdata', to='api.hostquiz')),
            ],
        ),
    ]