from template_flask_app.app import create_app

main_app = create_app()

if __name__ == '__main__':
    main_app.run(debug=True)
