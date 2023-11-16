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
