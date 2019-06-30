# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import tweet
from .forms import TweetModelForm
# Register your models here.

#admin.site.register(tweet)

class TweetModelAdmin(admin.ModelAdmin):
    #form = TweetModelForm
    class Meta:
        model=tweet


admin.site.register(tweet,TweetModelAdmin)