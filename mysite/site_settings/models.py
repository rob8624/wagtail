from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    """social media settings for our custom website"""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter =  models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube =  models.URLField(blank=True, null=True, help_text="Youtube URL")

    panel = [
        MultiFieldPanel([
            FieldPanel("Facebook"),
            FieldPanel("Twitter"),
            FieldPanel("Youtube"),
        ], heading="Social Media Settings")
    ]