import unittest, os
from app import app, db
from app.models import User

class UserModelCase(unittest.TestCase):

  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']=\
        'sqlite:///'+os.path.join(basedir,'test.db')
    self.app = app.test_client()#creates a virtual test environment
    db.create_all()
    s1 = User(id='0',username='Test',email="123@fake.com")
    s2 = User(id='1',username='Unit',email="1234@fake.com")
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_password_hashing(self):
    s = User.query.get('0')
    s.set_password('test')
    self.assertFalse(s.check_password('case'))
    self.assertTrue(s.check_password('test'))

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/login', content_type='html/text')
    self.assertEqual(response.status_code, 200)

  def test_default_score(self):
    s = User.query.get('0')
    self.assertTrue(s.high_score_easy == 0)
    self.assertTrue(s.high_score_normal == 0)
    self.assertTrue(s.high_score_hard == 0)



if __name__=='__main__':
  unittest.main(verbosity=2)