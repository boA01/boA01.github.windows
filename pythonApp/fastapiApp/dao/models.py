from tortoise import Model, fields

class Todo(Model):
      id = fields.IntField(pk=True) #主键
      # content = fields.CharField(max_length=100) #内容
      # created_at = fields.DateField(auto_now_add=True) #插入时间
      # updated_at = fields.DateField(auto_now = True) #更新时间