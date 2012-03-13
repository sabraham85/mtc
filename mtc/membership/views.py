from mtc.membership.models import Member, Parish, FamilyMember
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from reportlab.pdfgen import canvas
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


    # resp = render_to_response('membership/member_directory.html', {'memberdetails': paginate(request, Member.objects.order_by('last_name'))})
    #---------------------------------------------- result = StringIO.StringIO()
    #------------------------------------------ pdf=pisa.CreatePDF(html, result)
    #----------------------------------------------------------- if not pdf.err:
        #---- return HttpResponse(result.getvalue(), mimetype='application/pdf')
    #----- return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def render_to_pdf3(request):
    template = get_template('membership/member_directory.html')
    context = Context({'pagesize':'A4', 'memberdetails': Member.objects.all().order_by('last_name'), })
    html  = template.render(context)
    return HttpResponse(html)
    result = StringIO.StringIO()
    pdf=pisa.CreatePDF(html, result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def render_to_pdf(template_src, context_dict):
    #template = get_template(template_src)
    #context=Context(context_dict)
    #html=template.render(context)
    html=render_to_response(template_src, context_dict)
    result=StringIO.StringIO()
    pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def directoryview_pdf(request):
    return render_to_pdf('membership/member_directory.html',{'pagesize':'A4', 'memberdetails': paginate(request, Member.objects.all().order_by('last_name'))})
    #return render_to_response('membership/member_directory.html', {'memberdetails': memberdetails})
    
def paginate(request, modelobj):
    paginator = Paginator(modelobj, 100)
    page = request.GET.get('page', 1)
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return details

def render_to_pdf2(request):
    html = render_to_response('membership/member_directory.html', {'memberdetails': paginate(request, Member.objects.order_by('last_name'))})
    
    response = HttpResponse()
    response['Content-Type'] ='application/pdf'
    response['Content-Disposition']='attachment; filename=%s.pdf'%('blah')
    
    pisa.CreatePDF(
    src=html,
    dest=response,
    show_error_as_pdf=True)
    
    #response.flush()
    return response         
    
def directoryview(request):
    #memberdetails = Members.objects.all().order_by('last_name')
    return render_to_response('membership/member_directory.html', {'memberdetails': paginate(request, Member.objects.order_by('last_name'))})
    #return render_to_response('membership/member_directory.html', {'memberdetails': Member.objects.all()})