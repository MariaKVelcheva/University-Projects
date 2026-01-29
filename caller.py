"""
1. to='profiles.Profile'
2. utils -> get_user_object(): return Profile.objects.first()  (None or object)
3. Home = ListView, BaseFormView
model = Album
form_class = CreateProfileForm
success_url = reverse_lazy('home')
def get_template_names(self): profile = get_user_object()
def form_valid(self, form):
form.save()
return super().form_valid(form)
4. pk_url_kwarg = 'id'
5. DeleteView:
def get_initial(self):
return self.object.__dict__
+
def form_invalid(self, form):
return self.form_valid()
6. def get_object(self, queryset=None):
return get_user_object()
7. def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs)
context['profile'] = get_user_object()
return context
"""