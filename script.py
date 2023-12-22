import os

def create_project_structure(base_path):
    # 定义目录结构
    paths = [
        "/app/api/dependencies",
        "/app/api/endpoints",
        "/app/api/routers",
        "/app/core",
        "/app/crud",
        "/app/models",
        "/app/schemas",
        "/app/utils",
        "/tests/api",
        "/tests/crud",
        "/tests/utils",
        "/alembic"
    ]

    # 定义需要创建的空文件
    files = [
        "/app/core/config.py",
        "/app/core/security.py",
        "/Dockerfile",
        "/requirements.txt",
        "/main.py"
    ]

    # 创建目录
    for path in paths:
        os.makedirs(base_path + path, exist_ok=True)

    # 创建文件
    for file in files:
        with open(base_path + file, 'w') as fp:
            pass  # 只是创建文件，不写入内容

    print(f"Project structure created under {base_path}")

if __name__ == "__main__":
    import fire 
    fire.Fire(create_project_structure)


