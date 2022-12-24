from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("a:has-text(\"1\")").click()
    page.wait_for_url("https://www.saucedemo.com/cart.html")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    page.locator("[data-test=\"checkout\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("ganesh")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("kafle")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("69006")
    page.locator("form:has-text(\"CancelContinue\")").click()
    page.locator("[data-test=\"continue\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    page.locator("[data-test=\"finish\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
    page.locator("[data-test=\"back-to-products\"]").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path = "/Users/ganeshkafle/Playwright/trace.zip")

    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)

