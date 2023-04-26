"""
singleton is a class that can only have a single instance of it that's 
instantiated. 
It has many use cases e.g. maintaining a single copy of our application state.

example: 
By providing Store access to App component,all child component of App gets
access to the store as shown
                            [Store]
                               ^
                               |
                               V
                            [provider]
                                ^
                                |
                              [App]
                                |
                                V
                    -------------------------
                    |                       |
                    V                       V
                [Child 1]               [Child 2]
                                            |
                                            V
                                --------------------------
                                |                        |
                                V                        V
                            [Child 3]               [Child 4]

This pattern can be useful so that multiple components in your app can have 
a single source of truth.
But how can all the components listen for updates at the same time(real-time),
- this is where the observer pattern comes in.                                 
"""
class ApplicationState:
    instance = None
    
    def __init_(self):
        self.isLoggedIn =False
        
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance=ApplicationState()
        return ApplicationState.instance
    
appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn) # False

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn=True

print(appState1.isLoggedIn) # True
print(appState2.isLoggedIn) # True