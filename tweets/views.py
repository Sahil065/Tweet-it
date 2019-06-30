from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import tweet
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView,DetailView,ListView,CreateView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.views import View
from django.http import HttpResponseRedirect


class RetweetView(View):
    def get(self,request,pk, *args,**kwargs):
        Tweet=get_object_or_404(tweet,pk=pk)
        if request.user.is_authenticated():
            new_tweet=tweet.objects.retweet(request.user,Tweet)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin,UpdateView):
    queryset = tweet.objects.all()
    form_class=TweetModelForm
    template_name = 'tweets/update_view.html'
    #success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model=tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")


class TweetDetailView(DetailView):
    queryset=tweet.objects.all()



class TweetListView(LoginRequiredMixin,ListView):

    def get_queryset(self, *args, **kwargs):
        qs=tweet.objects.all()

        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter( Q(content__icontains=query)
                          |
                          Q(user__username__icontains=query))
        return qs


    def get_context_data(self, *args, **kwargs):
        context=super(TweetListView,self).get_context_data(*args, **kwargs)
        context['create_form']=TweetModelForm
        context['create_url']=reverse_lazy("tweet:create")
        return context
