import re
def validation_of_Donor(name,pincode,mobile,email_id):
    v1=re.match(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',name)
    v2=re.match("^[0-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
    v3=re.match("(0|91)?[-\s]?[6-9]\d{9}",mobile)
    r1= re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$",email_id)
    if v1 and v2 and v3 and r1 :
        return True
    else:
        return False

