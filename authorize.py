

def authorize_user(auth, role, user_role):
    try:
        if (auth == True):
            if (role == user_role) :
                return True
            else:
                return False, "Wrong User"
        else:
            return False, "Not Login"
    except:
        return False, "Not Login"
