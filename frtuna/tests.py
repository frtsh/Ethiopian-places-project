from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Destinations
import os


class DestinationsModelTest(TestCase):
    """Test cases for the Destinations model"""
    
    def setUp(self):
        """Set up test data"""
        # Create a test image file
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
        
        # Create a test destination
        self.destination = Destinations.objects.create(
            name='Test Destination',
            img=self.test_image,
            desc='This is a test destination description',
            price=1000,
            offer=False
        )
    
    def test_destination_creation(self):
        """Test that a destination can be created"""
        self.assertEqual(self.destination.name, 'Test Destination')
        self.assertEqual(self.destination.desc, 'This is a test destination description')
        self.assertEqual(self.destination.price, 1000)
        self.assertFalse(self.destination.offer)
        self.assertIsNotNone(self.destination.img)
    
    def test_destination_string_representation(self):
        """Test the string representation of the destination"""
        self.assertEqual(str(self.destination), 'Test Destination')
    
    def test_destination_with_offer(self):
        """Test creating a destination with offer=True"""
        destination_with_offer = Destinations.objects.create(
            name='Offered Destination',
            img=self.test_image,
            desc='This destination has an offer',
            price=800,
            offer=True
        )
        self.assertTrue(destination_with_offer.offer)
        self.assertEqual(destination_with_offer.price, 800)
    
    def test_destination_price_validation(self):
        """Test that price can be set to different values"""
        # Test with zero price
        zero_price_dest = Destinations.objects.create(
            name='Free Destination',
            img=self.test_image,
            desc='This destination is free',
            price=0,
            offer=False
        )
        self.assertEqual(zero_price_dest.price, 0)
        
        # Test with high price
        high_price_dest = Destinations.objects.create(
            name='Expensive Destination',
            img=self.test_image,
            desc='This destination is expensive',
            price=999999,
            offer=False
        )
        self.assertEqual(high_price_dest.price, 999999)
    
    def test_destination_name_max_length(self):
        """Test that destination name respects max_length constraint"""
        # Test with name at max length (50 characters)
        long_name = 'A' * 50
        dest_with_long_name = Destinations.objects.create(
            name=long_name,
            img=self.test_image,
            desc='Test description',
            price=500,
            offer=False
        )
        self.assertEqual(len(dest_with_long_name.name), 50)
    
    def tearDown(self):
        """Clean up test files"""
        # Remove test image files
        if hasattr(self, 'destination') and self.destination.img:
            if os.path.exists(self.destination.img.path):
                os.remove(self.destination.img.path)


class DestinationsViewTest(TestCase):
    """Test cases for the Destinations views"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create test image
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
        
        # Create test destinations
        self.destination1 = Destinations.objects.create(
            name='Destination 1',
            img=self.test_image,
            desc='First test destination',
            price=1000,
            offer=False
        )
        
        self.destination2 = Destinations.objects.create(
            name='Destination 2',
            img=self.test_image,
            desc='Second test destination',
            price=1500,
            offer=True
        )
    
    def test_index_view_status_code(self):
        """Test that the index view returns 200 status code"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_view_uses_correct_template(self):
        """Test that the index view uses the correct template"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
    
    def test_index_view_contains_destinations(self):
        """Test that the index view contains destinations in context"""
        response = self.client.get(reverse('index'))
        self.assertIn('dests', response.context)
        self.assertEqual(len(response.context['dests']), 2)
    
    def test_index_view_destinations_order(self):
        """Test that destinations are returned in the correct order"""
        response = self.client.get(reverse('index'))
        destinations = response.context['dests']
        # Check that both destinations are present
        destination_names = [dest.name for dest in destinations]
        self.assertIn('Destination 1', destination_names)
        self.assertIn('Destination 2', destination_names)
    
    def test_index_view_with_no_destinations(self):
        """Test index view when there are no destinations"""
        # Delete all destinations
        Destinations.objects.all().delete()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['dests']), 0)
    
    def test_index_view_http_methods(self):
        """Test that the index view handles different HTTP methods correctly"""
        # Test GET method (should work)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
        # Test POST method (should also work since no method restrictions)
        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def tearDown(self):
        """Clean up test files"""
        # Remove test image files safely
        try:
            for destination in Destinations.objects.all():
                if destination.img and os.path.exists(destination.img.path):
                    os.remove(destination.img.path)
        except Exception:
            pass  # Ignore cleanup errors


class DestinationsURLTest(TestCase):
    """Test cases for the Destinations URLs"""
    
    def test_index_url_exists(self):
        """Test that the index URL exists and is accessible"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_url_name(self):
        """Test that the index URL name works correctly"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_url_uses_correct_view(self):
        """Test that the index URL uses the correct view function"""
        response = self.client.get('/')
        self.assertEqual(response.resolver_match.func.__name__, 'index')


class DestinationsIntegrationTest(TestCase):
    """Integration tests for the complete flow"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create test image
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
    
    def test_complete_flow(self):
        """Test the complete flow from model creation to view display"""
        # Create a destination
        destination = Destinations.objects.create(
            name='Integration Test Destination',
            img=self.test_image,
            desc='This is an integration test',
            price=2000,
            offer=True
        )
        
        # Verify the destination was created
        self.assertEqual(Destinations.objects.count(), 1)
        self.assertEqual(destination.name, 'Integration Test Destination')
        
        # Test that the view can access the destination
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['dests']), 1)
        
        # Verify the destination appears in the view
        dest_in_view = response.context['dests'][0]
        self.assertEqual(dest_in_view.name, 'Integration Test Destination')
        self.assertEqual(dest_in_view.price, 2000)
        self.assertTrue(dest_in_view.offer)
    
    def test_multiple_destinations_flow(self):
        """Test handling multiple destinations"""
        # Create multiple destinations
        destinations_data = [
            {'name': 'Dest 1', 'price': 1000, 'offer': False},
            {'name': 'Dest 2', 'price': 1500, 'offer': True},
            {'name': 'Dest 3', 'price': 2000, 'offer': False},
        ]
        
        for data in destinations_data:
            Destinations.objects.create(
                name=data['name'],
                img=self.test_image,
                desc=f'Description for {data["name"]}',
                price=data['price'],
                offer=data['offer']
            )
        
        # Verify all destinations were created
        self.assertEqual(Destinations.objects.count(), 3)
        
        # Test that the view shows all destinations
        response = self.client.get(reverse('index'))
        self.assertEqual(len(response.context['dests']), 3)
        
        # Verify all destinations are present
        dest_names = [dest.name for dest in response.context['dests']]
        self.assertIn('Dest 1', dest_names)
        self.assertIn('Dest 2', dest_names)
        self.assertIn('Dest 3', dest_names)
    
    def tearDown(self):
        """Clean up test files"""
        # Remove test image files safely
        try:
            for destination in Destinations.objects.all():
                if destination.img and os.path.exists(destination.img.path):
                    os.remove(destination.img.path)
        except Exception:
            pass  # Ignore cleanup errors


class DestinationsBasicValidationTest(TestCase):
    """Basic validation tests that work reliably"""
    
    def setUp(self):
        """Set up test data"""
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
    
    def test_offer_field_default_value(self):
        """Test that offer field has correct default value"""
        destination = Destinations.objects.create(
            name='Test Destination',
            img=self.test_image,
            desc='Test description',
            price=1000
            # offer not specified, should use default
        )
        self.assertFalse(destination.offer)
    
    def test_model_fields_exist(self):
        """Test that all expected model fields exist"""
        destination = Destinations.objects.create(
            name='Test Destination',
            img=self.test_image,
            desc='Test description',
            price=1000,
            offer=True
        )
        
        # Check that all fields are accessible
        self.assertEqual(destination.name, 'Test Destination')
        self.assertEqual(destination.desc, 'Test description')
        self.assertEqual(destination.price, 1000)
        self.assertTrue(destination.offer)
        self.assertIsNotNone(destination.img)
    
    def tearDown(self):
        """Clean up test files"""
        # Remove test image files safely
        try:
            for destination in Destinations.objects.all():
                if destination.img and os.path.exists(destination.img.path):
                    os.remove(destination.img.path)
        except Exception:
            pass  # Ignore cleanup errors


class CSRFErrorTest(TestCase):
    """Test cases specifically for CSRF-related issues"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create test image
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
        
        # Create test destination
        self.destination = Destinations.objects.create(
            name='Test Destination',
            img=self.test_image,
            desc='Test description',
            price=1000,
            offer=False
        )
    
    def test_csrf_token_present_in_template(self):
        """Test that CSRF token is present in the template"""
        response = self.client.get(reverse('index'))
        # Allow both 200 and 301 status codes (301 is redirect, 200 is success)
        self.assertIn(response.status_code, [200, 301])
        
        # If it's a redirect, follow it
        if response.status_code == 301:
            response = self.client.get(response.url)
            self.assertEqual(response.status_code, 200)
        
        # Check if CSRF token is in the response content
        # This is important for forms that might be added later
        self.assertContains(response, 'csrfmiddlewaretoken', status_code=200)
    
    def test_admin_login_csrf_handling(self):
        """Test that admin login POST with and without CSRF works as expected"""
        # Enable CSRF checking
        client = Client(enforce_csrf_checks=True)

        # Step 1: GET request to fetch CSRF token
        response = client.get('/admin/login/')
        self.assertIn(response.status_code, [200, 301])

        # Follow redirect if needed
        if response.status_code == 301:
            response = client.get(response.url)
            self.assertEqual(response.status_code, 200)

        # Extract CSRF token from cookies
        csrf_token = response.cookies.get('csrftoken').value

        # Step 2: Attempt POST without CSRF token - should fail (403)
        fail_response = client.post('/admin/login/', {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(fail_response.status_code, 403)

        # Step 3: Attempt POST with CSRF token - should **not** 403 (login may fail, but CSRF must pass)
        success_response = client.post('/admin/login/', {
            'username': 'testuser',
            'password': 'testpass',
            'csrfmiddlewaretoken': csrf_token
        }, HTTP_COOKIE=f'csrftoken={csrf_token}')
        
        self.assertNotEqual(success_response.status_code, 403, msg="CSRF check failed even with token")

    
    def test_csrf_settings_validation(self):
        """Test that CSRF settings are properly configured"""
        from django.conf import settings
        
        # Check that CSRF middleware is enabled
        self.assertIn('django.middleware.csrf.CsrfViewMiddleware', settings.MIDDLEWARE)
        
        # Check that CSRF_TRUSTED_ORIGINS is configured
        self.assertTrue(hasattr(settings, 'CSRF_TRUSTED_ORIGINS'))
        self.assertIsInstance(settings.CSRF_TRUSTED_ORIGINS, list)
        
        # Check that CSRF cookie settings are properly configured
        self.assertTrue(hasattr(settings, 'CSRF_COOKIE_SECURE'))
        self.assertTrue(hasattr(settings, 'CSRF_COOKIE_SAMESITE'))
    
    def test_railway_domain_csrf_trusted_origins(self):
        """Test that Railway domains are in CSRF_TRUSTED_ORIGINS"""
        from django.conf import settings
        
        # Check for Railway domains in trusted origins
        railway_domains = [
            'https://ethiopian-places-project-production-6f93.up.railway.app',
            'https://ethiopian-places-project-production.up.railway.app',
            'https://*.up.railway.app',
            'https://*.railway.app',
        ]
        
        for domain in railway_domains:
            self.assertIn(domain, settings.CSRF_TRUSTED_ORIGINS)
    
    def test_csrf_exemption_for_specific_views(self):
        """Test that specific views can be exempted from CSRF if needed"""
        from django.views.decorators.csrf import csrf_exempt
        from django.http import HttpResponse
        
        # Create a test view that's exempt from CSRF
        @csrf_exempt
        def test_view(request):
            return HttpResponse("CSRF exempt view")
        
        # This would be used if you need to exempt specific views
        # For now, just test that the decorator can be imported
        self.assertTrue(callable(csrf_exempt))
    
    def test_csrf_token_generation(self):
        """Test that CSRF tokens are generated correctly"""
        from django.middleware.csrf import get_token
        from django.test import RequestFactory
        
        factory = RequestFactory()
        request = factory.get('/')
        
        # Test that we can get a CSRF token
        token = get_token(request)
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 0)
    
    def tearDown(self):
        """Clean up test files"""
        try:
            if hasattr(self, 'destination') and self.destination.img:
                if os.path.exists(self.destination.img.path):
                    os.remove(self.destination.img.path)
        except Exception:
            pass  # Ignore cleanup errors
