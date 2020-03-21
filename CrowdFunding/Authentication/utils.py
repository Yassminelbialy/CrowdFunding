from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.six import six
class TokenGenerator(PasswordResetTokenGenerator):
    # def _make_hash_value(self,user,timestamp):
    #     return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))
    pass
generate_token=TokenGenerator()