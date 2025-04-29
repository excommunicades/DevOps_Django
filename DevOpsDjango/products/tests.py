from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSetTests(APITestCase):
    def setUp(self):
        """Create test products"""
        self.product1 = Product.objects.create(
            name='Product 1',
            description='Description for product 1',
            price=10.0,
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            description='Description for product 2',
            price=20.0,
        )
        self.url = '/api/products/'  # Adjust to your API endpoint

    def test_list_products(self):
        """Test retrieving a list of products"""
        response = self.client.get(self.url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        """Test creating a new product"""
        data = {
            'name': 'Product 3',
            'description': 'Description for product 3',
            'price': 30.0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check if the product is created
        product = Product.objects.get(id=response.data['id'])
        self.assertEqual(product.name, data['name'])
        self.assertEqual(product.description, data['description'])
        self.assertEqual(product.price, data['price'])

    def test_retrieve_product(self):
        """Test retrieving a product by ID"""
        url = f'{self.url}{self.product1.id}/'
        response = self.client.get(url)
        serializer = ProductSerializer(self.product1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_product(self):
        """Test updating a product by ID"""
        url = f'{self.url}{self.product1.id}/'
        data = {
            'name': 'Updated Product',
            'description': 'Updated description',
            'price': 50.0
        }
        response = self.client.put(url, data, format='json')
        
        self.product1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.product1.name, data['name'])
        self.assertEqual(self.product1.description, data['description'])
        self.assertEqual(self.product1.price, data['price'])

    def test_partial_update_product(self):
        """Test partially updating a product by ID"""
        url = f'{self.url}{self.product1.id}/'
        data = {'price': 15.0}
        response = self.client.patch(url, data, format='json')
        
        self.product1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.product1.price, data['price'])

    def test_destroy_product(self):
        """Test deleting a product by ID"""
        url = f'{self.url}{self.product1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify that the product is deleted
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product1.id)
