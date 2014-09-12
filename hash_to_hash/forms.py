from django import forms

from models import Cluster, Hashtag, Votes


class VotesForm(forms.models.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.models.ModelForm, self).__init__(self, *args, **kwargs)
        self.fields["doesnt_belong"].label = kwargs.get("instance").hashtag.tag
    class Meta:
        model = Votes
        fields = ()
    doesnt_belong = forms.BooleanField(required=False)