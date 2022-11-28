import uvicorn




if __name__ == '__main__':
    uvicorn.run("she_says.app:app",port=8000, reload=True)