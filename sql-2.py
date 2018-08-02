import pymysql.cursors
import time
import datetime

def addNewMuseum(museum_nameInput, curator_emailInput) :
    if museum_nameInput == "" or curator_emailInput == "" or museum_nameInput is None:
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput in row :
                return False
            if curator_emailInput is not None :
                sql = "SELECT email FROM VISITOR"
                cursor.execute(sql)
                row = [item[0] for item in cursor.fetchall()]
                if curator_emailInput not in row :
                    return False
            sql = "INSERT INTO MUSEUM VALUES (%s, %s)"
            cursor.execute(sql, (museum_nameInput, curator_emailInput))
    finally:
        connection.close()
    return True

def addNewVisitor(emailInput, passwordInput, credit_card_numInput, expiration_monthInput, expiration_yearInput, credit_card_security_numInput) :
    if "" in (emailInput, passwordInput, credit_card_numInput, expiration_monthInput, expiration_yearInput, credit_card_security_numInput) :
        return False
    if None in (emailInput, passwordInput, credit_card_numInput, expiration_monthInput, expiration_yearInput, credit_card_security_numInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput in row :
                return False
            sql = "INSERT INTO VISITOR VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (emailInput, passwordInput, credit_card_numInput, int(expiration_monthInput), expiration_yearInput, int(credit_card_security_numInput)))
    finally:
        connection.close()
    return True

def purchaseTicket(emailInput, museum_nameInput, priceInput) :
    if "" in (emailInput, museum_nameInput) :
        return False
    if None in (emailInput, museum_nameInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput not in row :
                return False
            sql = "SELECT museum_name FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput not in row :
                return False
            sql = "SELECT museum_name FROM TICKET WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput in row :
                return False
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO TICKET VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (emailInput, museum_nameInput, priceInput, timestamp))
    finally:
        connection.close()
    return True

def makeReview(emailInput, museum_nameInput, commentInput, ratingInput) :
    if "" in (emailInput, museum_nameInput, ratingInput) :
        return False
    if None in (emailInput, museum_nameInput, ratingInput) :
        return False
    if ratingInput > 5 or ratingInput < 1 :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput not in row :
                return False
            sql = "SELECT museum_name FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput not in row :
                return False
            sql = "SELECT museum_name FROM TICKET WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput not in row :
                return False
            sql = "SELECT museum_name FROM REVIEW WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput in row :
                sql = "UPDATE REVIEW SET comment = %s, rating = %s WHERE museum_name = %s AND email = %s"
                cursor.execute(sql, (commentInput, int(ratingInput), museum_nameInput, emailInput))
            else :
                sql = "INSERT INTO REVIEW VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (emailInput, museum_nameInput, commentInput, int(ratingInput)))
    finally:
        connection.close()
    return True

def makeCuratorRequest(emailInput, museum_nameInput) :
    if "" in (emailInput, museum_nameInput) :
        return False
    if None in (emailInput, museum_nameInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput not in row :
                return False
            sql = "SELECT museum_name FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput not in row :
                return False
            sql = "SELECT museum_name FROM CURATOR_REQUEST WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput in row :
                return False
            sql = "SELECT curator_email FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput in row :
                return False
            sql = "INSERT INTO CURATOR_REQUEST VALUES (%s, %s)"
            cursor.execute(sql, (emailInput, museum_nameInput))
    finally:
        connection.close()
    return True

def addExhibit(museum_nameInput, exhibit_nameInput, yearInput, urlInput) :
    if "" in (museum_nameInput, exhibit_nameInput) :
        return False
    if None in (museum_nameInput, exhibit_nameInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if museum_nameInput not in row :
                return False
            sql = "SELECT exhibit_name FROM EXHIBIT WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if exhibit_nameInput in row :
                return False
            sql = "INSERT INTO EXHIBIT VALUES (%s, %s, %s, %s)"
            if yearInput is None or yearInput is "" :
                cursor.execute(sql, (museum_nameInput, exhibit_nameInput, None, urlInput))
            else :
                cursor.execute(sql, (museum_nameInput, exhibit_nameInput, int(yearInput), urlInput))
    finally:
        connection.close()
    return True

def viewSpecificMuseum(museum_nameInput) :
    if "" == museum_nameInput or None is museum_nameInput :
        return []
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT exhibit_name, year, url FROM EXHIBIT WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def viewAllReviewsForMusuem(museum_nameInput) :
    if "" == museum_nameInput or None is museum_nameInput :
        return
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT comment, rating FROM REVIEW WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def viewAllMuseums() :
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name, AVG(rating) FROM MUSEUM NATURAL LEFT OUTER JOIN REVIEW GROUP BY museum_name"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def viewTicketHistory(emailInput) :
    if "" == emailInput or None is emailInput :
        return
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name, purchase_timestamp, price FROM TICKET WHERE email = %s"
            cursor.execute(sql, (emailInput))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def viewReviewHistory(emailInput) :
    if "" == emailInput or None is emailInput :
        return
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name, comment, rating FROM REVIEW WHERE email = %s"
            cursor.execute(sql, (emailInput))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def viewMyMuseums(emailInput) :
    if "" == emailInput or None is emailInput :
        return []
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name, Count(Distinct exhibit_name), Avg(rating) FROM MUSEUM NATURAL LEFT OUTER JOIN EXHIBIT NATURAL LEFT OUTER JOIN REVIEW WHERE curator_email = %s GROUP BY museum_name"
            cursor.execute(sql, (emailInput))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def deleteExhibit(museum_nameInput, exhibit_nameInput) :
    if "" in (museum_nameInput, exhibit_nameInput) :
        return
    if None in (museum_nameInput, exhibit_nameInput) :
        return
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "DELETE FROM EXHIBIT WHERE museum_name = %s AND exhibit_name = %s"
            cursor.execute(sql, (museum_nameInput, exhibit_nameInput))
    finally:
        connection.close()

def deleteMuseum(museum_nameInput) :
    if "" == museum_nameInput or None is museum_nameInput :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "DELETE FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
    finally:
        connection.close()
    return True

def deleteVisitor(emailInput) :
    if "" == emailInput or None is emailInput :
        return
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "UPDATE MUSEUM SET curator_email = NULL WHERE curator_email = %s"
            cursor.execute(sql, (emailInput))
            sql = "DELETE FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
    finally:
        connection.close()

def rejectCuratorRequest(emailInput, museum_nameInput) :
    if "" in (emailInput, museum_nameInput) :
        return False
    if None in (emailInput, museum_nameInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM CURATOR_REQUEST WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput not in row :
                return False
            sql = "DELETE FROM CURATOR_REQUEST WHERE email = %s AND museum_name = %s"
            cursor.execute(sql, (emailInput, museum_nameInput))
    finally:
        connection.close()
    return True

def acceptCuratorRequest(emailInput, museum_nameInput) :
    if "" in (emailInput, museum_nameInput) :
        return False
    if None in (emailInput, museum_nameInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT email FROM CURATOR_REQUEST WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if emailInput not in row :
                return False
            sql = "UPDATE MUSEUM SET curator_email = %s WHERE museum_name = %s"
            cursor.execute(sql, (emailInput, museum_nameInput))
            sql = "DELETE FROM CURATOR_REQUEST WHERE email = %s AND museum_name = %s"
            cursor.execute(sql, (emailInput, museum_nameInput))
    finally:
        connection.close()
    return True

def logIn(emailInput, passwordInput) :
    if "" in (emailInput, passwordInput) :
        return False
    if None in (emailInput, passwordInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT password FROM VISITOR WHERE email = %s"
            cursor.execute(sql, (emailInput))
            row = [item[0] for item in cursor.fetchall()]
            if passwordInput not in row :
                return False
            else :
                return True
    finally:
        connection.close()

def isCurator(emailInput) :
    if "" == emailInput or None is emailInput :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT curator_email FROM MUSEUM"
            cursor.execute(sql)
            row = [item[0] for item in cursor.fetchall()]
            if emailInput in row :
                return True
            else :
                return False
    finally:
        connection.close()

def adminLogin(emailInput, passwordInput) :
    if "" in (emailInput, passwordInput) :
        return False
    if None in (emailInput, passwordInput) :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ADMINN"
            cursor.execute(sql)
            row = [item[0] for item in cursor.fetchall()]
            if emailInput in row :
                return True
            else :
                return False
    finally:
        connection.close()

def listOfMuseums() :
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT museum_name FROM MUSEUM"
            cursor.execute(sql)
            row = [item[0] for item in cursor.fetchall()]
            return row
    finally:
        connection.close()

def viewCuratorRequests():
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT email, museum_name FROM CURATOR_REQUEST"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close

def checkForCurator(museum_nameInput):
    if "" == museum_nameInput or None is museum_nameInput :
        return False
    connection = pymysql.connect(host='localhost', user='root', password='cs4400max', db='BMTRS', autocommit=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT curator_email FROM MUSEUM WHERE museum_name = %s"
            cursor.execute(sql, (museum_nameInput))
            row = [item[0] for item in cursor.fetchall()]
            if row[0] is None :
                return False
            else :
                return True
    finally:
        connection.close
