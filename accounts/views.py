from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdatedForm


# Create your views here.
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdatedForm(
            request.POST, 
            request.FILES,
            instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = ProfileUpdatedForm(instance=request.user)

        return render(request, 'accounts/profile.html', {'form': form})