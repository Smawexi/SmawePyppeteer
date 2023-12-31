### 一个使用pyppeteer对指定的请求url进行渲染的库

---
### 安装
``` text
pip install smawe-pyppeteer
```

---

### **快速开始**

```python
from smawe_pyppeteer import get, run, goto, logger

if __name__ == '__main__':
    # 写法一
    from pathlib import Path

    async def main():
        script = "document.cookie"
        r = await get(
            "http://www.fangdi.com.cn/index.html", auto_close=True, delay=5, pretend=True, headless=True,
            user_data_dir=Path("./test").resolve(),
            args=[], script=script, callable=handle,
            enabled_interception=True, enabled_maximize=False, cookies={"name": "k1", "value": "v1"}
        )
        print(r.text)
        print(r.request)
        print(r.status)
        print(r.script_result)
        print(r.cookies)

    async def handle(request):
        print(request.url)
        await request.continue_()

    run(main())

    logger.debug("=" * 50)

    # 写法二
    # 等价于r = run(get(*args, **kwargs))
    r = goto("http://www.fangdi.com.cn/index.html", pretend=True, delay=2)
    print(r.text)
```


### **API参考**  
- async def smawe_pyppeteer.get( 
    url, delay=None, wait_for=None, page_width=None, page_height=None,
    enabled_interception=None, script=None, callable=None, cookies=None,**kwargs
):      
  &nbsp;&nbsp;使用pyppeteer对指定url进行渲染    
> - param url: url  
> - param wait_for: css选择器或者xpath, 等待指定的元素出现在页面上  
> - param delay: 打开指定url后要等待的秒数, 默认为None不进行等待(同时指定了delay和wait_for,则先delay,然后再wait_for)  
> - param page_width: 页面宽度  
> - param page_height: 页面高度  
> - param enabled_interception: 是否启用请求拦截  
> - param callable: 启动了请求拦截后要调用的协程函数, 它接受单个request参数, 未提供则使用默认实现.  
> - param script: js表达式/js函数, 脚本在最后才执行, 即page关闭前执行. 结果可通过PyppeteerResponse.script_result属性获取.  
> - param cookies: 一个字典或者包含字典的可迭代对象, 在当前打开的page中设置cookie(在访问页面之前设置), e.g. {"name": "n1", "value": "v1"}
> - param kwargs(包含以下关键字参数):  
>   -  headless(bool): 是否启动无头模式, 默认是True.(启用了此参数(参数被设置为True时), auto_close被强制设为True)  
>   -  path(str): 要运行的 Chromium 或 Chrome 可执行文件的路径.  
>   -  auto_close(bool): 脚本完成后自动关闭浏览器进程. 默认为 True.  
>   -  window_width(str): 浏览器窗口宽度, 以像素为单位.注意window_width和window_height必须同时设置, 否则会不生效  
>   -  window_height(str): 浏览器窗口高度, 以像素为单位.注意window_width和window_height必须同时设置, 否则会不生效  
>   -  args(list\[str\]): 传递给浏览器进程的附加参数.  
>   -  enabled_maximize(bool): 是否启用窗口最大化, 默认为True, 如果同时指定了注意window_width和window_height, 此参数不会生效  
> -  return: PyppeteerResponse  


- smawe_pyppeteer.run(f: Coroutine)  
  &nbsp;&nbsp;运行future对象(包括协程对象), 返回future的结果  


- smawe_pyppeteer.goto(*args, **kwargs)  
  参数同smawe_pyppeteer.get, 等同于调用run(get(*args, **kwargs)), 返回一个PyppeteerResponse.  


- smawe.logger  
  logging.Logger对象, 调用logger.debug("message""), 输出格式如下  
  2023-11-15 22:51:12,342 | DEBUG | message

---

**有问题请提交issue**
