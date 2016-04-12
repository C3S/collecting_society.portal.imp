# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal

from collecting_society_portal.tests.base import (
    IntegrationTestBase,
    DeformFormObject
)
from collecting_society_portal.views.forms.login_web_user import login_form


class TestWebUser(IntegrationTestBase):

    def setUp(self):
        self.session()
        self.url('login')
        self.formid = 'LoginWebuser'
        self.form = DeformFormObject(self.cli, login_form(), self.formid)

    def test_login_with_wrong_credentials(self):
        '''Integration / WebUser: login fails with wrong credentials'''
        self.form.email.set('wrong@credentials.test')
        self.form.password.set('wrong')
        self.form.submit()
        self.screenshot()
        self.assertTrue(
            self.cli.find_elements_by_xpath(
                "//form[@id='" + self.formid + "']//p[@class='errorMsg']"
            )
        )

    def test_login_with_right_credentials(self):
        '''Integration / WebUser: login succeeds with right credentials'''
        self.form.email.set('meik@c3s.cc')
        self.form.password.set('meik')
        self.form.submit()
        self.screenshot()
        self.assertTrue(
            self.cli.find_elements_by_class_name('cs-backend')
        )
