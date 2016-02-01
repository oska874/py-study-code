import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        print("1")
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        print("2")
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        print("3")
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
        print("4")
        return self.app.post('/login', data=dict(
                username=username,
                password=password
                ), follow_redirects=True)

    def logout(self):
        print("5")
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        print("6")
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    def test_messages(self):
        print("7")
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
                    title='<Hello>',
                    text='<strong>HTML</strong> allowed here'
                    ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

if __name__ == '__main__':
    unittest.main()
