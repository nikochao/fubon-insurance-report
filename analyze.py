import base64 #Decode Normal Captcha

def captcha(browser):
	img_base64 = browser.execute_script("""
    var ele = arguments[0];
    var cnv = document.createElement('canvas');
    cnv.width = 480; cnv.height = 90;
    cnv.getContext('2d').drawImage(ele, 0, 0);
    return cnv.toDataURL('image/jpeg').substring(22);
    """, browser.find_element("xpath","//*[@id='kaptchaImage']"))

	with open("captcha_login.png", 'wb') as image:
	    image.write(base64.b64decode(img_base64))
	    print(image)
	import ddddocr
	ocr = ddddocr.DdddOcr()
	with open('captcha_login.png', 'rb') as f:
	    img_bytes = f.read()
	res = ocr.classification(img_bytes)
	print(res)
	return res