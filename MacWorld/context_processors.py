def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    login_form = AuthenticationForm()
    return {'login_form': login_form}