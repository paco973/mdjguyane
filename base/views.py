import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms.StudentForm import StudentForm
from .forms.NewsletterForm import NewsletterForm
from .forms.MemberForm import MemberForm
from django.conf import settings

from .models import Event, City, Student, EventByStudent, Volunteer, Study, Level, MdjMember, Message, Newsletter, \
    ProductCategory, Product
from blog.models import Post, PostCategory


def home(request):
    posts = Post.objects.filter(published=True).order_by('date_created')[:3]

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formFooter = NewsletterForm(request.POST)
        # check whether it's valid:
        if formFooter.is_valid():
            _email = Newsletter.objects.create(
                email=formFooter.cleaned_data['email'])
            _email.save()
            return redirect('home')

    else:
        formFooter = NewsletterForm
    context = {
        # 'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'formFooter': formFooter,
        'posts': posts,
    }

    return render(request, 'base/home.html', context)


def detail(request, event_slug=None):
    detail = Event.objects.get(slug=event_slug)

    cities = City.objects.all()

    context = {
        'detail': detail,
        'cities': cities,
    }

    return render(request, 'base/detail.html', context)


def register(request, event_id=None):
    city = City.objects.get(name=request.POST['city'])
    student = Student.objects.create(first_name=request.POST['nom'], last_name=request.POST['prenom'],
                                     email=request.POST['mail'], address=request.POST['address'],
                                     birthday=request.POST['date'], city=city)
    student.save()

    event = Event.objects.get(id=event_id)

    studenbyenv = EventByStudent.objects.create(student=student, event=event)

    studenbyenv.save()

    return redirect('home')


def member(request):
    cities = City.objects.all()
    formFooter = NewsletterForm
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            city = City.objects.get(name=form.cleaned_data['city'])

            _member = MdjMember.objects.create(first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'],
                                               email=form.cleaned_data['email'], address=form.cleaned_data['address'],
                                               birthday=form.cleaned_data['birthday'],
                                               phone_number=form.cleaned_data['phone_number'], city=city
                                               )
            _member.save()

            # redirect to a new URL:
            return redirect('api_checkout_session')

    else:
        form = StudentForm

    context = {
        'formFooter': formFooter,
        'cities': cities,
        'form': form
    }

    return render(request, 'base/member.html', context)


def student(request):
    cities = City.objects.all()
    studies = Study.objects.all()
    levels = Level.objects.all()
    formFooter = NewsletterForm
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # Récupération de la ville
            city = City.objects.get(name=form.cleaned_data['city'])

            # Récupération du niveau d'étude
            level = Level.objects.get(name=form.cleaned_data['level'])

            # Récupération des études en cours
            study = Study.objects.get(name=form.cleaned_data['study'])

            _student = Student.objects.create(first_name=form.cleaned_data['first_name'],
                                              last_name=form.cleaned_data['last_name'],
                                              email=form.cleaned_data['email'], address=form.cleaned_data['address'],
                                              birthday=form.cleaned_data['birthday'],
                                              phone_number=form.cleaned_data['phone_number'],
                                              school=form.cleaned_data['school'], study=study, level=level, city=city)
            _student.save()
            return redirect('home')

    else:
        form = StudentForm

    context = {
        'formFooter': formFooter,
        'levels': levels,
        'cities': cities,
        'studies': studies,
        'form': form
    }

    return render(request, 'base/student.html', context)


def getVolunteer(request):
    volunteers = Volunteer.objects.all()

    context = {
        'volunteers': volunteers,
    }
    return render(request, 'base/gestionVol.html', context)


def contact(request):
    formFooter = NewsletterForm

    context = {
        'formFooter': formFooter
    }
    return render(request, 'base/contact.html', context)


def about(request):
    mdj_members = MdjMember.objects.all().exclude(role=None).order_by('ordre')

    formFooter = NewsletterForm
    context = {
        'formFooter': formFooter,
        'mdj_members': mdj_members,
    }
    return render(request, 'base/about.html', context)


def service(request):
    formFooter = NewsletterForm

    context = {
        'formFooter': formFooter,
    }
    return render(request, 'base/service.html', context)


def project(request):
    posts = Post.objects.filter(published=True)
    formFooter = NewsletterForm

    context = {
        # 'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'formFooter': formFooter,
        'posts': posts,
    }

    return render(request, 'base/project.html', context)


def sendmail(request):
    if request.method == 'POST':
        send_mail(
            request.POST['name'] + ' ' + request.POST['nom'],
            request.POST['message'],
            settings.DEFAULT_FROM_EMAIL,
            ['padeodjo973@icloud.com'],
        )

        message = Message.objects.create(first_name=request.POST['name'], last_name=request.POST['nom'],
                                         email=request.POST['mail'], message=request.POST['message'],
                                         )
        message.save()

        return redirect('home')

    else:
        formFooter = NewsletterForm
        context = {
            'formFooter': formFooter,
        }
        return render(request, 'base/contact.html', context)


def project_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id).filter(published=True)
    categories = PostCategory.objects.all()
    formFooter = NewsletterForm

    context = {
        # 'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'categories': categories,
        'formFooter': formFooter,
        'post': post,
    }

    return render(request, 'base/project_detail.html', context)


def success(request):
    return render(request, 'base/success.html')


def cancel(request):
    return render(request, 'base/cancel.html')


def shop(request):
    product_categories = ProductCategory.objects.all()
    categories = {}
    for product_category in product_categories:
        categories[product_category.name] = {
            'product': Product.objects.filter(category=product_category),
            'total': len(Product.objects.filter(category=product_category)),

        }

    print(categories[product_category.name]['total'])

    context = {
        'coutn': 0,
        'product_categories': product_categories,
        'categories': categories
    }
    return render(request, 'base/shop.html', context)
