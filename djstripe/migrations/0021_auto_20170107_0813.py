# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 08:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0020_auto_20161229_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='application_fee_percent',
            field=djstripe.fields.StripePercentField(decimal_places=2, help_text="A positive decimal that represents the fee percentage of the subscription invoice amount that will be transferred to the application owner's Stripe account each billing period.", max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
