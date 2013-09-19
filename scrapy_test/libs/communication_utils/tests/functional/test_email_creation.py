from django.core.exceptions import ValidationError
import pytest
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.tests.email_test_data import email_1, email_3

email_str = u"""--BoUnDaRyStRiNg
Content-Disposition: form-data; name="headers"

Received: by 127.0.0.1 with SMTP id 82yyH0rXMn Wed, 18 Sep 2013 13:19:42 -0500 (CDT)
Received: from mail-wi0-f169.google.com (mail-wi0-f169.google.com [209.85.212.169]) by mx3.sendgrid.net (Postfix) with ESMTPS id 1728814E173D for <dude@garbagetracker.com>; Wed, 18 Sep 2013 13:19:41 -0500 (CDT)
Received: by mail-wi0-f169.google.com with SMTP id hj3so6790063wib.0 for <dude@garbagetracker.com>; Wed, 18 Sep 2013 11:19:41 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=gmail.com; s=20120113; h=mime-version:sender:date:message-id:subject:from:to:cc:content-type; bh=x6iFLZEfsi3q/M7JR1K7Mi6vJPXgBQMYpo85Bo8IkKg=; b=eC5rmQg0UzlR53mVM0YaFKB34gblaZ7hx7eg2zN1vda2hpsrwl2/GSIm0SfSor5poj 8BVXmCtuo3QbjvXaU6efRjfKGCBV/2ZFAxDyf5kiQLPAtjeVpLFVOdQuNRmUHxqIN5XA UuFT5EytOxsoY5nBAKNYs5xe0NizdRDPWxiNPIqraRNYIjatEv1+Rj/pyKia8sVfN1Qv ajgkQSXjFylJIDyqI24Q8X4Ek2XDEZ7juHfB34nRc++OPr6oOkLUaL2aTr3Ps//NB+I8 4etKKZ4eboT1qG8z38tPMsBkeAGTyZWkT6IOfJ1BUFF+XLTgyEh/Q33jTnaVnvzGZOw0 mYRg==
MIME-Version: 1.0
X-Received: by 10.180.11.37 with SMTP id n5mr8183272wib.25.1379528380941; Wed, 18 Sep 2013 11:19:40 -0700 (PDT)
Sender: scoarescoare@gmail.com
Received: by 10.194.78.82 with HTTP; Wed, 18 Sep 2013 11:19:40 -0700 (PDT)
Date: Wed, 18 Sep 2013 14:19:40 -0400
X-Google-Sender-Auth: zE8IiRZJXpGBooQRsyrcfg-Szf8
Message-ID: <CAKGSGYxmaQ-g-hRrOnBTRm6XVRn0VwFbfzgmc8mw+rgeDR+bvg@mail.gmail.com>
Subject: Hi
From: Scott Coates <scott.c.coates@gmail.com>
To: Some Guy <dude@garbagetracker.com>, someone@somewhere.net
Cc: ccuser@cctest.com
Content-Type: multipart/alternative; boundary=001a11c25b481a923c04e6ac7bd0

--BoUnDaRyStRiNg
Content-Disposition: form-data; name="dkim"

{@gmail.com : pass}
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="to"

Some Guy <dude@garbagetracker.com>, someone@somewhere.net
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="cc"

ccuser@cctest.com
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="html"

<div dir="ltr">This is a test, okay</div>

--BoUnDaRyStRiNg
Content-Disposition: form-data; name="from"

Scott Coates <scott.c.coates@gmail.com>
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="text"

This is a test, okay

--BoUnDaRyStRiNg
Content-Disposition: form-data; name="spam_report"

Spam detection software, running on the system "mx3.sendgrid.net", has
identified this incoming email as possible spam.  The original message
has been attached to this so you can view it (if it isn't spam) or label
similar future email.  If you have any questions, see
the administrator of that system for details.

Content preview:  This is a test, okay This is a test, okay [...]

Content analysis details:   (0.1 points, 5.0 required)

 pts rule name              description
---- ---------------------- --------------------------------------------------
 0.0 FREEMAIL_FROM          Sender email is commonly abused enduser mail provider
                            (scott.c.coates[at]gmail.com)
-1.9 BAYES_00               BODY: Bayes spam probability is 0 to 1%
                            [score: 0.0000]
 0.0 HTML_MESSAGE           BODY: HTML included in message
 2.0 MIME_NO_TEXT           No (properly identified) text body parts


--BoUnDaRyStRiNg
Content-Disposition: form-data; name="envelope"

{"to":["dude@garbagetracker.com"],"from":"scoarescoare@gmail.com"}
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="attachments"

0
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="subject"

Hi
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="spam_score"

0.101
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="charsets"

{"to":"UTF-8","cc":"UTF-8","html":"ISO-8859-1","subject":"UTF-8","from":"UTF-8","text":"ISO-8859-1"}
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="SPF"

pass
--BoUnDaRyStRiNg--"""

@pytest.mark.django_db_with_migrations
def test_email_is_created_from_post(client):
  response = client.post('/communication/external/email/', email_3)
  assert 1 == Email.objects.count()

