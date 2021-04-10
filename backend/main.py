from API import create_app

app = create_app('config.Config')
print(app.config)
if __name__ == '__main__':
    app.run(debug=True)
