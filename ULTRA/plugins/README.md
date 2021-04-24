# PLUGIN

```
from ULTRA.utils import admin_cmd
@borg.on(admin_cmd(pattern="hello"))
async def alive(event):
  await event.edit("**HELLO WORLD**")
  await event.reply("**HELLO WORLD**") 
```

