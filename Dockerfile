FROM python:3.9.16-slim

# 安装 Nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean

WORKDIR /app

# 创建调试目录
RUN mkdir -p /app/JQDebug

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY nginx.conf /etc/nginx/conf.d/default.conf

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 80

# 启动脚本
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]