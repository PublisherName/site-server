from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer


# View for creating a new newsletter subscription
class NewsletterCreateView(CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer


# View for unsubscribing using the unique unsubscribe token
class UnsubscribeView(UpdateAPIView):

    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    lookup_field = "unsubscribe_token"

    def update(self, request, *args, **kwargs):
        """
        Deactivate the newsletter subscription for the subscriber.

        This method retrieves the subscriber using the
            `unsubscribe_token`, marks the subscriber
            as inactive, and saves the
            updated state in the database.

        Args:
            request (Request): The HTTP request object containing
                data from the client.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response with a success message.
        """
        subscriber = self.get_object()
        subscriber.is_active = False
        subscriber.save()
        return Response(
            {
                "message": "Unsubscribed Successfully",
            }
        )
