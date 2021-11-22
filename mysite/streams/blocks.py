"""Stream fields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock



class TitleAndTextBlock(blocks.StructBlock):
    """title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add your Title")
    date = blocks.DateBlock(required=True, help_text="Enter a Date (required)")
    text = blocks.TextBlock(required=True, help_text="Add additional text")


    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button"""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first"))

            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichtextBlock(blocks.RichTextBlock):
    """All the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "Document Full"
        label = "Full Richtext"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Without All the features"""
    def __init__(self, required=True, help_text=None, editor='default', features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "Italic",
            "Link",
        ]


    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple Richtext"

class CTABlock(blocks.StructBlock):
    """A simple call to action section"""

    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Learn More', max_length=40)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"