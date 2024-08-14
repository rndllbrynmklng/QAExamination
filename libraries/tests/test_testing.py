import pytest
import libraries.util.appcommon as uAppComm
import libraries.data.common as dCommon

@pytest.mark.thisTest()
def test_TC001_LogInAndLogout(page):
    """Step 1 - Go To Demoblaze Website"""
    uAppComm.ln.goToDemoblazeURL(page)
    """Step 2 - Login to Demoblaze Website"""
    uAppComm.ln.loginDemoblaze(page, dCommon.users.strUsername, dCommon.users.strPassword)
    """Step 3- Logout to Demoblaze"""
    uAppComm.ln.logoutDemoblaze(page)
    

