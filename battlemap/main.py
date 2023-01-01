from battlemap.views.app import app

def main():
    """
    Start a web server to run the application.
    """
    from battlemap.views import init_api
    init_api()
    # When debug = True, it tries to detect changes,
    # but since it's running with docker it can't really do that so it crashes
    app.run(debug = False, host = '0.0.0.0')