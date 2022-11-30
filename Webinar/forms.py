# from django import forms
# # from captcha.fields import ReCaptchaField
# # from captcha.widgets import ReCaptchaV2Checkbox


# # class ContactForm(forms.Form):
# #     email = forms.EmailField()
# #     feedback = forms.CharField(widget=forms.Textarea)
# #     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


# from django import forms
# from .models import HCPConnectModel


# # creating a form
# class HCPConnectForm(forms.ModelForm):

#     # create meta class
#     class Meta:
#         # specify model to be used
#         model = HCPConnectModel

#         # specify fields to be used
#         fields = [
#             "Blog_title",
#             "Blog_author",
#             "Blog_date",
#             "Blog_description",
#             "Blog_image",
#         ]
from .models import ClinicalTool
from django import forms
import datetime

class ClinicalToolForm(forms.ModelForm):
    ## change the widget of the date field.
    score_date = forms.DateField(
        label='What is your score date?', 
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )
    
    def __init__(self, *args, **kwargs):
        super(ClinicalToolForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for patient_name in self.fields.keys():
            self.fields[patient_name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = ClinicalTool
        fields = ("__all__")