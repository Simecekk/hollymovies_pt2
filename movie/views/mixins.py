from django.contrib import messages
from django.http import HttpResponseRedirect


class DeleteSuccessMixin:
    success_message = ''

    def get_success_message(self):
        return self.success_message

    def delete(self, request, *args, **kwargs):
        super(DeleteSuccessMixin, self).delete(request, *args, **kwargs)
        messages.success(request, self.get_success_message())
        return HttpResponseRedirect(self.get_success_url())
