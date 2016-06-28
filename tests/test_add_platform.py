

def test_test_add_platform(app):

    app.session.login(username="admin@rsso.ru", password="bigthree3")
    app.platform_helper.fill_new_platform_form()