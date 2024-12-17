from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum
from django.utils.dateparse import parse_date
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.decorators import action

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            try:
                return Expense.objects.filter(user__id=int(user_id))
            except ValueError:
                return Expense.objects.none()
        return Expense.objects.all()

    @action(detail=False, methods=["GET"])
    def list_by_date(self, request):
        user_id = request.query_params.get("user_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        if user_id and start_date and end_date:
            expenses = Expense.objects.filter(
                user__id=user_id,
                date__range=[parse_date(start_date), parse_date(end_date)],
            )
            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        return Response({"error": "Provide user_id, start_date, and end_date"}, status=400)

    @action(detail=False, methods=["GET"])
    def category_summary(self, request):
        user_id = request.query_params.get("user_id")
        month = request.query_params.get("month")
        year = request.query_params.get("year")
        if user_id and month and year:
            expenses = Expense.objects.filter(
                user__id=user_id, date__year=year, date__month=month
            ).values("category").annotate(total=Sum("amount"))
            return Response(expenses)
        return Response({"error": "Provide user_id, month, and year"}, status=400)
