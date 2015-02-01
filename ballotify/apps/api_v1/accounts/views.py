from rest_framework import generics

from .serializers import AccountSerializer
from ..streams.serializers import StreamSerializer
from accounts.models import User
from core.utils import memoized


class AccountDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of `username` account.

    """
    serializer_class = AccountSerializer
    lookup_field = "username"

    def get_queryset(self):
        return User.objects.all()

account_detail_view = AccountDetailView.as_view()


class AccountStreamMixin(object):
    @memoized
    def get_account(self):
        return generics.get_object_or_404(User, username=self.kwargs.get("username"))

    def get_streams(self):
        return self.get_account().owned_streams.public()


class AccountStreamsView(AccountStreamMixin, generics.ListAPIView):
    """
    List streams owned by `username` account.

    """
    serializer_class = StreamSerializer

    def get_queryset(self):
        return self.get_streams()

account_streams_view = AccountStreamsView.as_view()
