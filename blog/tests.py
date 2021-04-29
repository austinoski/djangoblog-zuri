from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author=self.user
        )
    
    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', args=[str(1)]))
        no_response = self.client.get(reverse('post-detail', args=[str(1000000)]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='secret')
        get_response = self.client.get(reverse('post-new'))
        post_response = self.client.post(
            reverse('post-new'), {'title': 'test create', 'body': 'great'})
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 302)
    
    def test_post_update_view(self):
        self.client.login(username='testuser', password='secret')
        data = {'title': 'A better title', 'body': 'Nicer body'}
        get_response = self.client.get(reverse('post-update', args=[str(1)]))
        post_response = self.client.post(reverse('post-update', args=[str(1)]), data)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 302)
    
    def test_post_delete_view(self):
        self.client.login(username='testuser', password='secret')
        get_response = self.client.get(reverse('post-delete', args=[str(1)]))
        post_response = self.client.post(reverse('post-delete', args=[str(1)]))
        response = self.client.get(reverse('post-detail', args=[str(1)]))
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 302)
        self.assertEqual(response.status_code, 404)

    def test_user_register(self):
        data = {
            'username':'testuser2',
            'first_name':'TestFirst',
            'last_name':'TestLast',
            'email':'email@testmail.com',
            'password':'topsecret'
        }
        get_response = self.client.get(reverse('register'))
        post_response = self.client.post(reverse('register'), data)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 302)
    
    def test_user_login(self):
        response = self.client.post(
            reverse('login'), {'username': 'testuser', 'password': 'secret'}, follow=True)
        redirect = response.redirect_chain[-1]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(redirect, ('/', 302))

    def test_user_logout(self):
        self.client.login(username="testuser", password="secret")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logged out")

    def test_user_comment(self):
        self.client.login(username="testuser", password="secret")
        data = {"body": "Sweet comment"}
        response = self.client.post(reverse("comment-new", args=[str(1)]), data, follow=True)
        self.assertEqual(response.redirect_chain[-1], ('/post/1/', 302))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sweet comment")
