from django.urls import path
from  .views import StudentPdfView, pdfview

urlpatterns =[
          
          path("students", StudentPdfView.as_view(),name="students_pdf" ),
          path("student", pdfview,name="student_pdf" ),

] 

