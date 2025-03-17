from app import create_app, db
from app.models.user import User

def init_db():
    app = create_app()
    with app.app_context():
        # 创建所有表
        db.create_all()

        # 创建测试用户
        test_user = User(username='test')
        test_user.set_password('test123')
        
        admin_user = User(username='admin')
        admin_user.set_password('admin123')

        # 添加到数据库
        db.session.add(test_user)
        db.session.add(admin_user)
        
        # 提交更改
        db.session.commit()
        
        print("数据库初始化完成！")
        print("测试用户: test/test123")
        print("管理员用户: admin/admin123")

if __name__ == '__main__':
    init_db()