import libraries.data.common as dCommon
import libraries.util.common as uCommon
import libraries.page.common as pCommon

class ln:
    """LOG IN PAGE"""
    def goToDemoblazeURL(page):
        uCommon.goToURL(page, f'{dCommon.url.strBaseURL}')
        uCommon.wait(page, 3)
        uCommon.waitElemToBeVisible(page, pCommon.com.logInLbl)
    
    def loginDemoblaze(page, strUserName =  dCommon.users.strUsername, strPassword = dCommon.users.strPassword):
        ln.clickLoginAndFillDetails(page, strUserName, strPassword)
        uCommon.waitElemToBeVisible(page, pCommon.com.logOutLbl)
        

        
    def clickLoginAndFillDetails(page, strUserName, strPassword):

        uCommon.waitAndClickElem(page, pCommon.com.logInLbl)
        uCommon.wait(page, 2)
        uCommon.waitElemToBeVisible(page, pCommon.com.logInBtn)
        uCommon.setElem(page, pCommon.com.usernameTxtbox, strUserName)
        uCommon.setElem(page, pCommon.com.passwordTxtbox, strPassword)
        uCommon.waitAndClickElem(page, pCommon.com.logInBtn)
        uCommon.waitForLoadState(page)
        uCommon.waitElemToBeVisible(page, pCommon.com.logOutLbl)
    
    def clickLogoutButton(page):
        uCommon.waitAndClickElem(page, pCommon.com.logOutLbl)
        uCommon.waitForLoadState(page)
        uCommon.waitElemToBeVisible(page, pCommon.com.logInLbl)
    
    def logoutDemoblaze(page):
        ln.clickLogoutButton(page)