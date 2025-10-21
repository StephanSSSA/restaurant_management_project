from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import OrderSerializer
from .forms import FeedbackForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer

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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        if order.user != request.user:
            return Response({"error": "Not your order"}, status=403)
        if order.status in ['cancelled', 'completed']:
            return Response({"error": f"Already {order.status}"}, status=400)
        order.status = 'cancelled'
        order.save()
        return Response({"message": "order cancelled"}, status=200)