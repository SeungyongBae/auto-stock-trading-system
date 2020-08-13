import configparser
import win32com.client
import pythoncom

class XASession:
    login_state = 0     # login stats check

    def OnLogin(self, code, msg):   # call after login
        if(code == "0000"): # login success
            XASession.login_state = 1

        print(code, msg)

    def OnDisconnect(self):     # call after disconnect
        print("Session disconnected")
        XASession.login_state = 0


class EBest:
    def __init__(self, mode=None):  # load config.ini, save server info
        if mode not in ["PROD", "DEMO"]:
            raise Exception("Need to run_mode(PROD or DEMO)")

        run_mode = "EBEST_" + mode
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.user = config[run_mode]['user']
        self.passwd = config[run_mode]['password']
        self.cert_passwd = config[run_mode]['cert_passwd']
        self.host = config[run_mode]['host']
        self.port = config[run_mode]['port']
        self.account = config[run_mode]['account']

        self.xa_session_client = win32com.client.DispatchWithEvents("XA_Session.XASession", XASession)

    def login(self):
        self.xa_session_client.ConnectServer(self.host, self.port)
        self.xa_session_client.Login(self.user, self.passwd, self.cert_passwd, 0, 0)

        while XASession.login_state == 0:
            pythoncom.PumpWaitingMessages()

    def logout(self):
        XASession.login_state = 0
        self.xa_session_client.DisconnectServer()