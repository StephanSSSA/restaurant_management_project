from django.shortcuts import render

from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {"form": form})
