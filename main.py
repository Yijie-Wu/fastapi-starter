"""
入口文件
"""

from src import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=8000, reload=True)
