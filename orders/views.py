from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import OrderSerializer
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

class OrderDeltaView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]