# Create your views here.
from django.db import DatabaseError
from django.shortcuts import render

from models import Cluster, Votes
from forms import VotesForm


def load_consent(request):
    return render(request, 'survey/consent.html')


def load_start(request):
    return render(request, 'survey/intro.html')


def load_survey(request):
    try:
        clusters = Cluster.objects.all().prefetch_related("hashtags")
        num_clusters = clusters.count()

        def gen_forms(post):
            _all_forms = []
            i = 0
            for cluster in clusters:
                i += 1
                _forms = []
                _votes = []
                for hashtag in cluster.hashtags.all():
                    v = Votes.objects.filter(cluster=cluster).get(hashtag=hashtag)
                    _votes.append(v)
                    if post:
                        _forms.append(VotesForm(request.POST, instance=v, prefix=hashtag.tag, label_suffix='',
                                                auto_id='%s'))
                    else:
                        _forms.append(VotesForm(instance=v, prefix=hashtag.tag, label_suffix='', auto_id='%s'))
                _all_forms.append({"id": i, "forms": _forms, "votes": _votes})
            return _all_forms

        if request.method == "POST":
            all_forms = gen_forms(True)
            if all([all([form.is_valid() for form in form_group[1]]) for form_group in all_forms]):
                for form_group in all_forms:
                    forms = form_group["forms"]
                    votes = form_group["votes"]
                    for x in xrange(len(forms)):
                        if forms[x]["cleaned_data"]["doesnt_belong"]:
                            votes["x"].nos += 1
                    for vote in votes:
                        vote.seen += 1
                        votes["x"].save()
                return render(request, 'survey/thanks.html')
        else:
            all_forms = gen_forms(False)
            return render(request, "survey/survey.html", {"all_forms": all_forms, "num_clusters": num_clusters})
    except DatabaseError:
        render(request, "database-down.html")

