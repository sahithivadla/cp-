# A Caesar Cipher is a simple cipher that works by shifting each letter in
# the given message by a certain number. For example, if we shift the message
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given
# message by shift letters. You are guaranteed that message is a string, and
# that shift is an integer between -25 and 25. Capital letters should stay capital
# and lowercase letters should stay lowercase, and non-letter characters should not be changed.
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
    res = ""
    for i in msg :
        if(i == " "):
            res=res+" "
            continue
        if(shift>0):
            if ord(i)>=65 and ord(i)<=90 and ord(i) + shift > 90:
        	    res=res+ chr(ord(i)-26+shift)
            elif(ord(i)>=97 and ord(i)<=122 and ord(i) + shift > 122):
        	    res=res+ chr(ord(i)-26+shift)
            else:
                res=res+chr(ord(i)+shift)

        if(shift<0):
            if ord(i)>=65 and ord(i)<=90 and ord(i) +shift <65:
        	    res=res+ chr(ord(i)+26+shift)
            elif(ord(i)>=97 and ord(i)<=122 and ord(i) + shift <96):
        	    res=res+ chr(ord(i)+26+shift)
            else:
                res=res+chr(ord(i)+shift)

    return res



