from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import message, send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permissions_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'mbryoyo01@gmail.com',
                ['mbryoyo01@gmail.com'],
                fail_silently=False
            )

            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Messagem enviada com sucesso'})

        except:
            return Response({'error': 'Messagem nao enviada , Falha'})