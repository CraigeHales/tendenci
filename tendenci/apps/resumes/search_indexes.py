from haystack import indexes

from tendenci.apps.resumes.models import Resume
from tendenci.apps.perms.indexes import TendenciBaseSearchIndex
from tendenci.apps.base.utils import strip_html

from tendenci.apps.base.utils import extract_pdf

class ResumeIndex(TendenciBaseSearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    activation_dt = indexes.DateTimeField(model_attr='activation_dt', null=True)
    expiration_dt = indexes.DateTimeField(model_attr='expiration_dt', null=True)
    syndicate = indexes.BooleanField(model_attr='syndicate', null=True)

    @classmethod
    def get_model(self):
        return Resume

    def prepare_description(self, obj):
        return strip_html(obj.description)


    def prepare_text(self, obj):
        # wch testing, add the pdf text here using the extract_pdf ... append it to the description...
        # TendenciBaseSearchIndex made the 'text' field, this will prepare it...
        # almost all other searchers need attention here!
        # https://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view
        # search seems to find the pdf and the file-app downloads it.
        # the file app will want a better front end, perhaps with a download/view-in-browser choice.
        if obj and obj.resume_file and obj.resume_file.file:
            txt = extract_pdf(obj.resume_file.file) 
        else:
            txt = ""
        return txt
