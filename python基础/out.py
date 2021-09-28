from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://182.151.33.125:1888/
    page.goto("http://182.151.33.125:1888/")

    # Go to http://182.151.33.125:1888/#/
    page.goto("http://182.151.33.125:1888/#/")

    # Go to http://182.151.33.125:1888/#/login
    page.goto("http://182.151.33.125:1888/#/login")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://182.151.33.125:1888/#/wel/index"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click li:nth-child(2) div .el-submenu__icon-arrow
    page.click("li:nth-child(2) div .el-submenu__icon-arrow")

    # Click .el-submenu.is-opened div .el-submenu__icon-arrow
    page.click(".el-submenu.is-opened div .el-submenu__icon-arrow")

    # Click .el-submenu__icon-arrow
    page.click(".el-submenu__icon-arrow")

    # Click div:nth-child(4) .el-submenu .el-submenu__title .el-submenu__icon-arrow
    page.click("div:nth-child(4) .el-submenu .el-submenu__title .el-submenu__icon-arrow")

    # Click text=点巡检内容
    # with page.expect_navigation(url="http://182.151.33.125:1888/#/maintenance/spotcheck/spotcheckinfo"):
    with page.expect_navigation():
        page.click("text=点巡检内容")

    # Click .el-table__fixed-right .el-table__fixed-body-wrapper .el-table__body tbody .el-table__row.hover-row .el-table_2_column_14 .cell button
    page.click(".el-table__fixed-right .el-table__fixed-body-wrapper .el-table__body tbody .el-table__row.hover-row .el-table_2_column_14 .cell button")

    # Click [placeholder="请选择 点巡检方式"]
    page.click("[placeholder=\"请选择 点巡检方式\"]")

    # Click [placeholder="请选择 点巡检方式"]
    page.click("[placeholder=\"请选择 点巡检方式\"]")

    # Click [placeholder="请输入 点巡检标准"]
    page.click("[placeholder=\"请输入 点巡检标准\"]")

    # Fill [placeholder="请输入 点巡检标准"]
    page.fill("[placeholder=\"请输入 点巡检标准\"]", "boa666666")

    # Click button:has-text("修 改")
    page.click("button:has-text(\"修 改\")")

    # Click text=点巡检模板
    # with page.expect_navigation(url="http://182.151.33.125:1888/#/maintenance/spotchecktemplate/spotchecktemplate"):
    with page.expect_navigation():
        page.click("text=点巡检模板")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入 点巡检模板名称"]
    page.click("[placeholder=\"请输入 点巡检模板名称\"]")

    # Fill [placeholder="请输入 点巡检模板名称"]
    page.fill("[placeholder=\"请输入 点巡检模板名称\"]", "boa666666")

    # Click [placeholder="请选择 点巡检模板类型"]
    page.click("[placeholder=\"请选择 点巡检模板类型\"]")

    # Click text=日模板周模板月模板 >> span
    page.click("text=日模板周模板月模板 >> span")

    # Click textarea
    page.click("textarea")

    # Fill textarea
    page.fill("textarea", "7777777777777")

    # Click button:has-text("新 增")
    page.click("button:has-text(\"新 增\")")

    # Click [placeholder="设备名称"]
    page.click("[placeholder=\"设备名称\"]")

    # Click [placeholder="设备名称"]
    page.click("[placeholder=\"设备名称\"]")

    # Fill [placeholder="设备名称"]
    page.fill("[placeholder=\"设备名称\"]", "boa")

    # Click button:has-text("搜 索")
    page.click("button:has-text(\"搜 索\")")

    # Click :nth-match(li:has-text("3"), 4)
    page.click(":nth-match(li:has-text(\"3\"), 4)")

    # Click button:has-text("取消")
    page.click("button:has-text(\"取消\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
