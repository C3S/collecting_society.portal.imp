# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal

from collecting_society_portal.tests.base import (
    IntegrationTestBase,
    DeformFormObject
)

from collecting_society_portal.views.forms.login_web_user import login_form
from collecting_society_portal.views.forms.register_web_user import (
    register_form
)


class TestWebUser(IntegrationTestBase):

    def test_010_registration(self):
        '''
        registration registers and logs user in
        '''

        self.url('register')
        formid = 'RegisterWebuser'
        form = DeformFormObject(self.cli, register_form(), formid)
        form.email.set('a@webuser.test')
        form.password.set('awebuser')
        form.submit()
        self.screenshot()
        self.assertTrue(
            self.cli.find_elements_by_class_name('cs-backend')
        )

    def test_020_logout(self):
        '''
        logout logs user out
        '''

        self.url('logout')
        self.assertTrue(
            self.cli.find_elements_by_class_name('cs-frontend')
        )

    def test_030_login_with_wrong_credentials(self):
        '''
        login with wrong credentials fails
        '''

        self.url('login')
        formid = 'LoginWebuser'
        form = DeformFormObject(self.cli, login_form(), formid)
        form.email.set('a@webuser.test')
        form.password.set('wrongpassword')
        form.submit()
        self.screenshot()
        self.assertTrue(
            self.cli.find_elements_by_xpath(
                "//form[@id='" + formid + "']//p[@class='errorMsg']"
            )
        )

    def test_040_login_with_right_credentials(self):
        '''
        login with right credentials logs user in
        '''

        self.url('login')
        formid = 'LoginWebuser'
        form = DeformFormObject(self.cli, login_form(), formid)
        form.email.set('a@webuser.test')
        form.password.set('awebuser')
        form.submit()
        self.screenshot()
        self.assertTrue(
            self.cli.find_elements_by_class_name('cs-backend')
        )
