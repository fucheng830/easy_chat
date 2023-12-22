├── app                 # 主应用目录
│   ├── api             # 负责处理API路由和视图
│   │   ├── dependencies# 存放依赖项
│   │   ├── endpoints   # 存放具体的API端点
│   │   └── routers     # 定义不同的路由器
│   │
│   ├── core            # 项目的核心配置（如配置文件、安全、数据库等）
│   │   ├── config.py   # 配置管理
│   │   └── security.py # 安全和认证
│   │
│   ├── crud            # 存放与数据库交互的CRUD操作
│   ├── models          # 存放数据库模型
│   ├── schemas         # 存放Pydantic模型（用于请求和响应）
│   └── utils           # 实用工具和辅助函数
│
├── tests               # 测试目录
│   ├── api             # 针对API的测试
│   ├── crud            # 针对CRUD操作的测试
│   └── utils           # 针对工具函数的测试
│
├── alembic             # 数据库迁移文件
├── Dockerfile          # 用于容器化的Dockerfile
├── requirements.txt    # 项目依赖文件
└── main.py             # FastAPI应用实例和服务器启动的入口点