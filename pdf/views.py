from django.shortcuts import render
from django_xhtml2pdf.utils import generate_pdf
from result.models import Student, Course
from django.http import HttpResponse
from django.views.generic import ListView
from django_xhtml2pdf.views import PdfMixin


class StudentPdfView(PdfMixin,ListView):
    model = Student
    template_name = "pdf/student_pdf.html"










def pdfview(request):
    resp = HttpResponse(content_type='application/pdf')
    context = {
        'students': Student.objects.all()
    }
    result = generate_pdf('pdf/student_pdf.html', file_object=resp, context=context)
    return result
   
