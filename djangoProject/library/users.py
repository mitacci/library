from djangoProject.library.models import Profile


def get_user():
    user = Profile.objects.first()
    return user

