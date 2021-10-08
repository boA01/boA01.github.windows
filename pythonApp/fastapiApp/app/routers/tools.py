from fastapi import APIRouter, BackgroundTasks
import time

bgRouter=APIRouter()

def write_notification(email: str, message=""):
    time.sleep(200)
    with open("log.txt", mode="w") as email_file:
        content = f"name {email}: {message}"
        email_file.write(content)

@bgRouter.post("/sendtxt/")
async def sendtxt(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="不关注")
    return {"message": "在后台读写"}