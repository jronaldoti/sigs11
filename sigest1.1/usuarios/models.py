from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from  django.utils.translation import ugettext_lazy as _
from django.utils import timezone





class UserManager(BaseUserManager):

    def create_superuser(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError(_('Defina o nome do usuario'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                 is_staff=is_staff, is_active=True,
                 is_superuser=is_superuser, last_login=now,
                 date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_user(self, username, email, password, **extra_fields):
            now = timezone.now()
            if not username:
                raise ValueError(_('Defina o nome de usuário'))
            email = self.normalize_email(email)
            user = self.model(username=username, email=email,
                             is_active=False, last_login=now,
                              date_joined=now, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

class Usuario(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(_('Nome completo'), max_length=255,  help_text=_('Defina seu nome completo, exemplo: Fulano da Silva'))
    username = models.CharField(_('usuario'), max_length=15, unique=True, help_text=_('Requer 15 caracteres ou menos'))
    password = models.CharField(_('senha'), max_length=15, help_text=('Digite uma senha com 15 caracteres ou menos'))
    email = models.EmailField(_('email'), max_length=255, unique=True)

    is_superuser = models.BooleanField(_('Status de Superusuário'), default=False,
                                       help_text=_('Designado para Superusuários '))
    is_staff = models.BooleanField(_('Status de staff'), default=False,
                                   help_text=_('Designado para usuarios da equipe'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designado para usuários ativos. \ Em vez de deletar, desative o mesmo.'))

    is_student = models.BooleanField (_('Aluno'), default=False,
                                      help_text=_('Designado para usuarios do tipo Aluno'))

    is_advisor = models.BooleanField(_('Orientador'), default=False,
                                      help_text=_('Designado para usuarios do tipo Orientador'))

    is_supervisor = models.BooleanField(_('Supervisor'), default=False,
                                      help_text=_('Designado para usuarios do tipo Supervisor'))

    date_joined = models.DateTimeField(_('data de ingresso'), default=timezone.now)

    is_trusty = models.BooleanField(_('Email confirmado'), default=False,
                                    help_text=_('Usuários com contas confirmadas.'))

    matricula = models.IntegerField()

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'matricula', 'is_staff', 'is_superuser']
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

class Student(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)



class Advisor(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)



class Supervisor(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)




