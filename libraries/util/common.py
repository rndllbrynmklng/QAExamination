from playwright.sync_api import sync_playwright, Page, expect
import libraries.data.common as dCommon


def goToURL(page:Page, url):
    page.goto(url)
    page.wait_for_load_state('load')
         
def waitElemToBeVisible(page: Page, elem, intTimeOut = dCommon.time.intDefTimeOut):
    page.wait_for_selector(elem, state='visible', timeout = intTimeOut)
    
def clickElem(page: Page, elem):
    page.locator(elem).click(force=True)

def waitAndClickElem(page: Page, elem):
    waitElemToBeVisible(page, elem)
    clickElem(page, elem)
    page.wait_for_load_state('load')

def wait(page: Page, intWaitTime = .5):
    page.wait_for_timeout(1000*intWaitTime)
    
def setElem(page: Page, elem, strValue):
        page.locator(elem).fill(strValue)
        
def waitForLoadState(page: Page, strState = 'load'):
    page.wait_for_load_state(strState)