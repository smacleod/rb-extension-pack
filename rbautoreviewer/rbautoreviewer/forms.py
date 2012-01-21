from django import forms
from django.utils.translation import ugettext as _
from djblets.extensions.forms import SettingsForm


class AutoReviewerSettingsForm(SettingsForm):
    test_field = forms.BooleanField(
        initial=True, required=False,
        help_text=_("This is just a test field."))
