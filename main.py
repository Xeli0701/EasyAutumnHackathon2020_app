from urls import app
import uvicorn
 
if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', app=app, port=8000)