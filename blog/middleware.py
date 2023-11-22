# visitor_counter/middleware.py
from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        
        # Print the IP address for debugging
        print(f"IP Address: {ip_address}")

        # Use filter instead of get_or_create to handle the case where multiple objects are returned
        visitors = Visitor.objects.filter(ip_address=ip_address)

        if visitors.exists():
            # If a record for the current IP exists, update the count
            visitor_instance = visitors.first()
            visitor_instance.count += 1
            visitor_instance.save()
        else:
            # If no record exists, create a new one
            Visitor.objects.create(ip_address=ip_address)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Extract the first IP address from the list
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
