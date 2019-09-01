# Implement middlware for opportunity filtering

class DisplayFilteringMiddleware:
    """
        Middleware class that will assist in processing any requests to /views/opporunities. \
        and then also implement the filtering funcionality by breaking down the 'POST' \
        request paramaters.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_view(request)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """Funciton processed before the view is processed."""
