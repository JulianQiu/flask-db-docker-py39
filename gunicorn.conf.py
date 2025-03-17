# 错误的地址格式
bind = "127.0.0.0:8000"  

# 应该改为
bind = "0.0.0.0:8000"
workers = 4
worker_class = "sync"
timeout = 120