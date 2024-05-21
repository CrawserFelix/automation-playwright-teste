import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.huggy.chat/9a710192-8df6-490f-aba1-16986342aa4b")
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="Nome").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="Nome").fill("Lucas Felix Muniz")
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="(99) 9 9999-").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="(99) 9 9999-").fill("61999999999")
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="E-mail").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("textbox", name="E-mail").fill("lucasfelix70@gmail.com")
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("button", name="Iniciar atendimento").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".textareacontainer").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator("#input").fill("Oi")
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-text-input > div:nth-child(5)").click()
    page.wait_for_timeout(2000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".textareacontainer").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator("#input").fill("Teste Huggy")
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-text-input > div:nth-child(5)").click()
    expect(page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator("body")).to_contain_text("Teste passou")
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-button").first.click()
    with page.expect_file_chooser() as fc_info:
        page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_text("Enviar arquivo").click()
    file_chooser = fc_info.value
    file_chooser.set_files("img/imagem.jpg")
    page.wait_for_timeout(2000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-button").first.click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_text("Finalizar atendimento").click()
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("button", name="Reabrir atendimento").click()
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".textareacontainer").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator("#input").fill("mensagem com emogi ")
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-text-input > div:nth-child(4) > .macke").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_title(":grinning:").click()
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-text-input > div:nth-child(5)").click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").locator(".ChatForm-button").first.click()
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_text("Enviar por e-mail").first.click()
    #page.wait_for_timeout(1000)
    page.frame_locator("div >> internal:has-text=/^Chat By$/ >> iframe").get_by_role("button", name="Enviar por e-mail").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
