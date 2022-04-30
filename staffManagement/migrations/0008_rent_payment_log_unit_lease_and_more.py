# Generated by Django 4.0.3 on 2022-03-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaseManagement', '0005_application_renter_application_unit_and_more'),
        ('staffManagement', '0007_remove_rent_payment_log_unit_lease_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent_payment_log',
            name='unit_lease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.unit_lease'),
        ),
        migrations.AddField(
            model_name='service_request',
            name='Service_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffManagement.service_category'),
        ),
        migrations.AddField(
            model_name='service_request',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffManagement.staff'),
        ),
        migrations.AddField(
            model_name='service_request',
            name='unit_lease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.unit_lease'),
        ),
        migrations.CreateModel(
            name='Staff_APP_Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.application')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffManagement.staff')),
            ],
        ),
    ]
