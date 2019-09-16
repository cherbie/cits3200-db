class CustomExceptionHandling:
    __init__(self, get_response):
        self.get_response = get_response

    __call__(self, request):
        # before view
        response = self.get_response
        # after view
