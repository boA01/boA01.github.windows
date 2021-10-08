from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect, status, Query, Cookie
from typing import List, Dict, Optional

socketRouter = APIRouter()

class ConnectionManager:
    def __init__(self):
        # 存放**的链接
        self.active_connections: List[Dict[str, WebSocket]] = []

    async def connect(self, user: str, ws: WebSocket):
        # 链接
        await ws.accept()
        self.active_connections.append({"user": user, "ws": ws})

    def disconnect(self, user: str, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove({"user": user, "ws": ws})

    async def send_other_message(self, message: dict, user: str):
        # 发送个人消息
        for connection in self.active_connections:
            if connection["user"] == user:
                await connection['ws'].send_json(message)

    async def broadcast(self, data: str):
        # 广播消息
        for connection in self.active_connections:
            await connection['ws'].send_text(data)

manager = ConnectionManager()

async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
    token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token

@socketRouter.websocket("/ws/{user}")
async def websocket_endpoint(
    websocket: WebSocket,
    user: str,
    cookie_or_token: str = Depends(get_cookie_or_token),
):
    name = user[:-3]
    
    await manager.connect(name, websocket)
    await manager.broadcast(name + "进入聊天室")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{name}：{data}")
    except WebSocketDisconnect as e:
        manager.disconnect(name, websocket)
        await manager.broadcast("用户{}离开".format(name))