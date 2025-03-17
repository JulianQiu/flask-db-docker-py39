from app import create_app, db

app = create_app()  # 确保这行代码存在

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)