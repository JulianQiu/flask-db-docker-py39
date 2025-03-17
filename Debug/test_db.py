from app import create_app, db
from app.models.user import User

def test_db():
    app = create_app()
    with app.app_context():
        try:
            # 测试数据库连接
            users = User.query.all()
            print("\n=== 数据库连接测试成功 ===")
            print("当前用户列表：")
            for user in users:
                print(f"用户名: {user.username}")
            
            # 测试查询特定用户
            test_user = User.query.filter_by(username='test').first()
            if test_user:
                print("\n成功找到测试用户 'test'")
            else:
                print("\n警告：未找到测试用户 'test'")
                
        except Exception as e:
            print("\n=== 数据库连接测试失败 ===")
            print(f"错误信息: {str(e)}")

if __name__ == '__main__':
    test_db()