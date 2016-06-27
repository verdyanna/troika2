def test_login(app):
    app.session.login("admin@rsso.ru", "bigthree3")
   # assert app.session.is_logged_in_as("admin@rsso.ru")
