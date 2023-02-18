from weatherapp.models import CustomUser

def create_user(
    username: str,
    password: str,
) -> None:
    # user = CustomUser(
    #     username=username,
    #     password=password,
    # )
    # user.save()
    user = CustomUser.objects.create_user(username=username, password=password)