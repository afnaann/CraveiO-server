from rest_framework_simplejwt.tokens import RefreshToken

class CustomToken:
    def __init__(self, user):
        self.user = user
        self.token = RefreshToken.for_user(user)  # Generate the token

    @property
    def access_token(self):
        token = self.token.access_token
        
        token['role'] = self.user.role  # Add the role
        token['user_id'] = self.user.id  # Add the user ID
        token['name'] = self.user.name
        
        return token

    def __str__(self):
        return str(self.token)
