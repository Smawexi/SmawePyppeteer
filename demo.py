from smawe_pyppeteer.utils import get, run

if __name__ == '__main__':
    from pathlib import Path

    async def main():
        script = "document.cookie"
        r = await get(
            "http://www.fangdi.com.cn/index.html", auto_close=True, delay=5, pretend=True,
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
