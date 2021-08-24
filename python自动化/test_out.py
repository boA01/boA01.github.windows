from playwright.sync_api import Playwright, sync_playwright #同步
from playwright.async_api import Playwright as aPlaywright, async_playwright
from time import sleep
import asyncio

# 同步
def run1(playwright:Playwright):
    # 分别对应多个浏览器驱动
    for browser_type in [playwright.firefox]:
        browser = browser_type.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("http:/182.151.33.125:1888/#/login")

        with page.expect_navigation():
            page.click("button:has-text(\"登录\")")

        # 停留5s
        sleep(10)

        context.close()
        #关闭浏览器
        browser.close()

# 异步
async def run2(playwright: aPlaywright):
    for browser_type in [playwright.firefox]:
        # 指定为有头模式，方便查看
        browser = await browser_type.launch(headless=False)
        context = await browser.new_context()

        page = context.new_page()
        await page.get("http:/182.151.33.125:1888/#/login")

        async with page.expect_navigation():
            await page.click("button:has-text(\"登录\")")

        
        # 执行一次检索
        # await page.fill("input[name=\"wd\"]","hello")
        # await page.press("input[name=\"wd\"]","Enter")

        # 截图
        # page.screenshot(path=f"test-{browser_type.name}.png")

        # 关闭
        await context.close()
        await browser.close()

async def main():
    async with async_playwright() as p:
        await run2(p)

if __name__=="__main__":
    with sync_playwright() as p:
        run1(p)


    # asyncio.run(main())
    # asyncio.get_event_loop().run_until_complete(run2())