import unittest, os, time
from app import app, db
from app.models import User, Location
from selenium import webdriver
basedir = os.path.abspath(os.path.dirname(__file__))

#To do, find simple way for switching from test context to development to production.


class SystemTest(unittest.TestCase):
  driver = None
  
  def setUp(self):
    self.driver = webdriver.Firefox(executable_path=os.path.join(basedir,'geckodriver'))

    if not self.driver:
      self.skipTest('Web browser not available')
    else:
      db.init_app(app)
      db.create_all()
      s1 = User(id='22222222',username='Test')
      s2 = User(id='11111111',username='Unit')
      #l = Location(lab='test-lab',time='now')
      db.session.add(s1)
      db.session.add(s2)
      #db.session.add(lab)
      db.session.commit()
      self.driver.maximize_window()
      self.driver.get('http://localhost:5000/')

  def tearDown(self):
    if self.driver:
      self.driver.close()
      db.session.query(User).delete()
      #db.session.query(Project).delete()
      #db.session.query(Lab).delete()
      db.session.commit()
      db.session.remove()
 
  def test_register(self):
    s = User.query.get('22222222')
    self.assertEqual(s.username,'Test',msg='student exists in db')
    self.driver.get('http://localhost:5000/register')
    self.driver.implicitly_wait(5)
    num_field = self.driver.find_element_by_id('id')
    num_field.send_keys('22222222')
    pref_name = self.driver.find_element_by_id('prefered_name')
    pref_name.send_keys('Testy')
    new_pin = self.driver.find_element_by_id('new_pin')
    new_pin.send_keys('0000')
    new_pin2 = self.driver.find_element_by_id('new_pin2')
    new_pin2.send_keys('0000')
    time.sleep(1)
    self.driver.implicitly_wait(5)
    submit = self.driver.find_element_by_id('submit')
    submit.click()
    #check login success
    self.driver.implicitly_wait(5)
    time.sleep(1)
    logout = self.driver.find_element_by_partial_link_text('Logout')
    self.assertEqual(logout.get_attribute('innerHTML'), 'Logout Testy', msg='Logged in')


if __name__=='__main__':
  unittest.main(verbosity=2)