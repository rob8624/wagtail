from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextField
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks

class BlogListingPage(Page):
    """Listing Page lists all the Blog Detail Pages"""

    template = "blog/blog_listing_page.html"

    custom_title = models.CharField(max_length=100,
                                    blank=False,
                                    null=False,
                                    help_text="Overwrites the default Title")

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ]

    def get_context(self, request, *args, **kwargs):
        """Adding cutom stuff to our contect"""

        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context





class BlogDetailPage(Page):
    """Blog Detail Page"""

    custom_title = models.CharField(max_length=100,
                                    blank=False,
                                    null=False,
                                    help_text="Overwrites the default Title")

    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    blog_summary = RichTextField(features=['h3', 'h1', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], max_length=400,
                                    blank=True,
                                    null=True,
                                    help_text="Give a summary of the blog")

    content = StreamField([
        ("Title_and_Text", blocks.TitleAndTextBlock()),
        ("full_richtext", blocks.RichtextBlock()),
        ("simple_richtext", blocks.SimpleRichtextBlock()),
        ("cards", blocks.CardBlock()),
        ("cta", blocks.CTABlock()),

    ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_summary"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]

