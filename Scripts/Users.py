import pandas as pd
import os as os

file = "/database/db.csv"


class Users:
    username = ""
    password = ""
    email = ""
    firstname = ""
    lastname = ""


def __init__(self):
    # print "test"
    self.username = "username"
    # self.username = username
    # self.password = password #sha256_crypt.encrypt(password)
    # self.FirstName = FirstName
    # self.LastName = LastName


def getUsername(self):
    return self.username


def getPasswordVerified(self, username):
    pass
    # sha256_crypt.verify(self.password, password)


def insertData(self, path, username, password, email, firstname, lastname):
    file = path + "/database/db.csv"
    df = pd.read_csv(file)
    columns = ['username', 'password', 'email', 'firstname', 'lastname']
    df2 = pd.DataFrame([[username, password, email, firstname, lastname]], columns=columns)
    df = df.append(df2, ignore_index=True)
    df.to_csv(file, index=False)
    print("Data inserted")


def validateUsername(self, path, username):
    file = path + "/database/db.csv"
    df = pd.read_csv(file)
    # print (df)
    newdf = (df.loc[df['username'] == username])
    if (len(newdf) > 0):
        return True
    else:
        return False


def validatePassword(self, path, username, password):
    file = path + "/database/db.csv"
    df = pd.read_csv(file)
    # print (df)
    newdf = (df.loc[df['username'] == username])
    if len(newdf) > 0:
        print(newdf['password'].tolist()[0])
        print(password)
        if (str(newdf['password'].tolist()[0]) == password):
            return True
        else:
            return False
    else:
        return False


def getUserProfile(self, path, username):
    file = path + "/database/db.csv"
    df = pd.read_csv(file)
    # print (df)
    newdf = (df.loc[df['username'] == username])
    userlist = [newdf['username'].tolist()[0],
                newdf['password'].tolist()[0],
                newdf['email'].tolist()[0],
                newdf['firstname'].tolist()[0],
                newdf['lastname'].tolist()[0],
                ]
    return userlist
