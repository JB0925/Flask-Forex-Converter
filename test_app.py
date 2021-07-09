from unittest import TestCase
import app


class TestCurrencyConverter(TestCase):
    def test_that_home_route_renders(self):
        with app.app.test_client() as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<label for="from">Convert From</label>', resp.get_data(as_text=True))
    

    def test_post_with_good_data(self):
        with app.app.test_client() as client:
            with client.session_transaction() as sesh:
                args = ['from', 'to', 'amount', 'symbol', 'converted']
                for i in range(len(args)):
                    sesh[args[i]] = ''
            
            data = {
                'from': 'usd',
                'to': 'USD',
                'amount': '1.93'
            }
            
            resp = client.post('/', data=data)
            self.assertEqual(resp.status_code, 302)
            
    

    def test_post_with_bad_data(self):
        with app.app.test_client() as client:
            with client.session_transaction() as sesh:
                args = ['from', 'to', 'amount', 'symbol', 'converted']
                for i in range(len(args)):
                    sesh[args[i]] = ''
            
            data2 = {
                'from': 'usd',
                'to': 'skfhsdfs',
                'amount': '1'
            }
            resp2 = client.post('/', data=data2)
            self.assertEqual(resp2.status_code, 302)
            resp3 = client.post('/', data=data2, follow_redirects=True)
            self.assertEqual(resp3.status_code, 200)
            self.assertIn('<p class="error">Sorry, one or both of your currencies could not be found.</p>',
                          resp3.get_data(as_text=True))
    

    def test_results_route(self):
        with app.app.test_client() as client:
            resp = client.get('/results')
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Here are your results:</h1>', resp.get_data(as_text=True))
