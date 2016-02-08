from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Ad

client = Client()

app_namespace = 'ads'


class AdBaseTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user', email='user@mail.ru', password='pass')

    def create_ad(self, title='Title', description='desc'):
        return Ad.objects.create(author=self.user, title=title, description=description)

    def login(self):
        self.client.login(username=self.user.username, password='pass')


class AdDetailTest(AdBaseTest):

    def test_404(self):
        response = self.client.get(reverse(app_namespace + ':ad_detail', args=(100,)))
        self.assertEqual(response.status_code, 404)

    def test_view(self):
        ad = self.create_ad()
        response = self.client.get(reverse(app_namespace + ':ad_detail', args=(ad.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['object'], Ad)
        self.assertEqual(response.context['object'].pk, ad.pk)

    def test_hits(self):
        # given
        ad = self.create_ad()
        url = reverse('ads:ad_detail', args=(ad.pk,))
        get_hits = lambda: Ad.objects.filter(pk=ad.pk).values_list('hits')[0][0]

        # when
        self.client.get(url)
        # then
        self.assertEqual(get_hits(), ad.hits)

        # when
        self.login()
        self.client.get(url)
        # then
        self.assertEqual(get_hits(), ad.hits+1)

        # when
        self.login()
        self.client.get(url)
        # then
        self.assertEqual(get_hits(), ad.hits+1)

