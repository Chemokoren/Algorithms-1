"""
can be used such that multiple components in your app will have a shared source of Truth
But how can all the components listen for updates in realtime? --- Observer pattern
(Behavioral pattern)
"""
class ApplicationState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False
        
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance=ApplicationState()
        return ApplicationState.instance
    
appState1 =ApplicationState.getAppState()
print(appState1.isLoggedIn) # False

appState2 =ApplicationState.getAppState()
print("::", appState2.isLoggedIn)
appState1.isLoggedIn=True

print("first::",appState1.isLoggedIn) # True
print("second::", appState2.isLoggedIn) # True
