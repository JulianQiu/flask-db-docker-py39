# flask-db-docker-py39

这是一个基于 Flask 和 Python 3.9 开发的示例项目，主要包含一个空的登录页面，并集成了数据库支持。项目同时提供了 Docker 化部署方案，方便快速启动和分发。

![{0D62ED30-8120-49B5-9E49-29FF6862E0F7}](https://github.com/user-attachments/assets/b0f91bee-2d10-4155-ae6c-853d70e3b1f3)


# 项目介绍 

本项目旨在为后续开发提供一个基础框架，包含以下内容：

- 空登录页面：提供简单的前端登录页面模板，便于后续扩展用户认证功能。
- 数据库支持：后端已集成数据库功能，为数据存储和管理打下基础。
- Flask 框架：使用 Flask 构建轻量级 Web 应用。
- Python 3.9：确保在 Python 3.9 环境下运行。
- Docker 化部署：通过 Docker 实现环境隔离，简化部署流程。

# 项目结构 #

plaintext
Copy
flask-db-docker-py39/
├── debug/
│   └── init_db.py        # 用于初始化数据库（如果你希望建立自己的数据库，请先运行该脚本）
├── run.py                # 启动 Flask 服务的入口文件（用于本地运行）
├── app.py                # Flask 主应用文件
├── test_db.py            # 用于测试数据库连接
├── templates/
│   └── login.html        # 登录页面模板
├── static/               # 静态文件目录（CSS、JS、图片等）
├── Dockerfile            # Docker 构建配置文件
├── requirements.txt      # Python 依赖列表
└── README.md             # 项目说明文件

# 环境配置 #
Docker：请确保已安装 Docker。
Python 依赖：所有依赖均列于 requirements.txt 文件中，可通过 pip 安装。

# 快速开始 #
使用 Docker 部署
构建镜像

docker build -t flask-db-docker-py39 .
启动容器

docker run -p 5000:5000 flask-db-docker-py39
访问应用

打开浏览器，访问 http://localhost:5000 查看效果。

本地运行
克隆项目

git clone https://github.com/JulianQiu/flask-db-docker-py39.git
cd flask-db-docker-py39
安装依赖


pip install -r requirements.txt
启动 Flask 服务

执行以下命令启动服务：

python run.py
访问应用

打开浏览器，访问 http://localhost:5000 查看效果。

数据库初始化与测试
当前项目数据库已预置了一些内容，但如果你希望建立自己的数据库，请先运行位于 debug 目录下的 init_db.py 脚本进行初始化。


python debug/init_db.py
运行 test_db.py 脚本可以验证数据库是否成功连接。


python test_db.py
你也可以根据需要修改数据库配置来适配不同的数据库系统（如 SQLite、MySQL、PostgreSQL 等）。

# 功能说明 #
登录页面：当前提供一个空的登录页面模板，方便后续添加表单和认证逻辑。
数据库集成：后端预留了数据库功能，你可以使用预置的数据库内容，也可以根据需要自行初始化数据库并进行连接测试。
未来计划
添加用户注册、登录及认证功能
扩展数据库模型，实现数据持久化和业务逻辑
优化前端页面和用户交互
完善 API 接口，支持更多功能

# 贡献 #
欢迎大家通过 issue 或 pull request 提出建议和改进。如有疑问或合作意向，请联系项目维护者。

授权许可
本项目采用 MIT License 开源协议。更多详情请参见 LICENSE 文件。
