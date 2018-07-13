from glob import glob


def merge():
    r = ''
    for i in range(len(glob('./img/*.jpg'))):
        path = './img/%d.jpg' % i
        r += """
            <img src="%s" /><br />
        """ % path
    with open('index.html', 'w') as f:
        f.write("""
<!DOCTYPE html>
    <html>
        <head>
            <title>웹툰 이어붙이기</title>
            <style>
            img {
                margin-bottom: -5px;
            }
            </style>
        </head>
        <body>
            %s
        </body>
    </html>
        """ % r)
