from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from user.forms import FileForm
from django.db import transaction
from django.contrib import messages


class ImageView(TemplateView):
    template_name = 'user/image_form.html'

    def get(self, request):
        form = FileForm()
        return render(request, self.template_name, {'form': form})

    @transaction.atomic
    def post(self, request):
        url_list = request.POST.getlist('url')
        for url in url_list:
            form = FileForm(data={'user': request.user, 'url': url})
            if form.is_valid():
                form.save()
            else:
                return render(request, self.template_name, {'form': form})
        messages.success(request, 'Images successfully saved with compressed URL.')
        return redirect('images')
