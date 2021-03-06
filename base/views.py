import uuid
from os import abort


from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms.StudentForm import StudentForm
from .forms.NewsletterForm import NewsletterForm
from .forms.MemberForm import MemberForm    
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import Event, City, Student, EventByStudent, Volunteer, Study, Level, MdjMember, Message, Newsletter, \
    Role
from blog.models import Post, PostCategory


def home(request):

    mdj_members = MdjMember.objects.all()

    for mdj_member in mdj_members:
        mdj_member.indent = uuid.uuid4()
        mdj_member.save()
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
    cities = City.objects.all().order_by('name')
    formFooter = NewsletterForm
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            city = City.objects.get(name=form.cleaned_data['city'])
            role = Role.objects.get(name=request.POST['prix'])

            _member = MdjMember.objects.create(first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'],
                                               email=form.cleaned_data['email'], address=form.cleaned_data['address'],
                                               birthday=form.cleaned_data['birthday'],
                                               phone_number=form.cleaned_data['phone_number'], city=city, role=role,
                                               profession=request.POST['profession'], code_parrain=request.POST['code_parrain']
                                               )
            _member.save()
            try:
                send_mail(
                    'Adhesion MDJ',
                    "Bienvenu(e) dans l???association" 
                    "la MDJ Guyane Merci pour votre confiance et votre engagement"
                    "au sein de la Maison Des Jeunes de Guyane."
                    "Vous ??tes d??sarmais Membre pour une dur??e de 364 jours." 
                    "Par votre adh??sion participez, au rayonnement des Jeunes de Guyane.",
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned_data['email']],

                )

            except:
                pass

            # redirect to a new URL:
            return render(request, "payments/product_detail.html",
                          context={'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY, 'member': _member})


    else:
        form = StudentForm

    context = {
        'formFooter': formFooter,
        'cities': cities,
        'form': form
    }

    return render(request, 'base/member.html', context)


def student(request):
    cities = City.objects.all().order_by('name')
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
            # R??cup??ration de la ville
            city = City.objects.get(name=form.cleaned_data['city'])

            # R??cup??ration du niveau d'??tude
            level = Level.objects.get(name=form.cleaned_data['level'])

            # R??cup??ration des ??tudes en cours
            study = Study.objects.get(name=form.cleaned_data['study'])

            _student = Student.objects.create(first_name=form.cleaned_data['first_name'],
                                              last_name=form.cleaned_data['last_name'],
                                              email=form.cleaned_data['email'], address=form.cleaned_data['address'],
                                              birthday=form.cleaned_data['birthday'],
                                              phone_number=form.cleaned_data['phone_number'],
                                              school=form.cleaned_data['school'], study=study, level=level, city=city)
            _student.save()
            try:
                send_mail(
                    'R??seau ??tudiant MDJ',
                    "Bienvenu(e) au R??seau Etudiant de Guyane"
                    "Ce r??seau est outil pour les ??tudiants de Guyane hors du territoire."
                    "Merci pour la confiance accord??e ?? ce r??seau ??tudiant, nous vous souhaitons dores et d??j?? "
                    "nos voeux de r??ussite pour votre formation d???enseignement sup??rieur."
                    "Votre Section locale de "
                    "l???association vous sera communiqu?? dans un prochain mail.",
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned_data['email']],

                )
            except:
                pass

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
    role = [3, 4, 5, 6, 7, 8]

    # Membre du bureau
    mdj_members = MdjMember.objects.filter(role__in=role).order_by('ordre')

    # Chef de section
    section = MdjMember.objects.filter(role=9).order_by('ordre')

    # formulaire News letters
    formFooter = NewsletterForm

    # param??tres
    context = {
        'formFooter': formFooter,
        'mdj_members': mdj_members,
        'section': section
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
        try:

            send_mail(
                'Accus?? de r??ception MDJ Guyane',
                'Merci pour votre message, celui-ci sera trait?? dans les meilleurs d??lais.',
                settings.DEFAULT_FROM_EMAIL,
                [request.POST['mail']],
            )

            message = Message.objects.create(first_name=request.POST['name'], last_name=request.POST['nom'],
                                             email=request.POST['mail'], message=request.POST['message'],
                                             )
            message.save()
        except:
            pass

        return redirect('home')
    else:
        formFooter = NewsletterForm
        context = {
            'formFooter': formFooter,
        }
        return render(request, 'base/contact.html', context)


def project_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
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

