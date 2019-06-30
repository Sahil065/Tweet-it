from django import  forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user=self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList("User Must Be Logged In To Continue")
            return self.form_invalid(form)


class UserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user==self.request.user:
            return super(UserOwnerMixin,self).form_valid(form)
        else:

          form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList("This User is not allowed not make changes. ")
          return self.form_invalid(form)