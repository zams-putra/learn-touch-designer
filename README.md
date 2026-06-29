# Blob Tracker

- https://derivative.ca/community-post/tutorial/make-viral-blob-tracking-effect-touchdesigner-free/74680


## add your video:
- klik kanan -> add operator -> move file in -> add+ -> pilih videonya
- fit1 -> 1280 x 720
- bla bla bla aku gatau cara bikin docs nya buat project ini bjir


## Script
```py
import cv2
import numpy as np

def onCook(scriptOp):

    params = op('areaParams') 
    MIN_AREA = int(params['min'])
    MAX_AREA = int(params['max'])

    src = scriptOp.inputs[0].numpyArray(delayed=False)
    src8 = (src * 255).astype('uint8')
    gray = src8[..., 0]

    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    w_img = op('video').width
    h_img = op('video').height

    dat = op('blobData')
    dat.clear()
    dat.appendRow(["id", "u", "v", "width", "height"])

    idx = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_AREA or area > MAX_AREA:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        cx = (x + w / 2) / w_img
        cy = (y + h / 2) / h_img

        sx = w / w_img
        sy = h / h_img

        dat.appendRow([str(idx), str(cx), str(cy), str(sx), str(sy)])
        idx += 1

    return
```

## Keluh Kesah
- nyoba sesuai tutor video tuh kadang sussah juga ya output ku beda soalnya gatau kenapa
- video bahannya juga beda sih btw
- awalnya nyoba, tapi kok blob nya jarangg muncul ya
- terus ku turunin threshold nya untung jadi sering muncul gitu blob nya


## File output 
- https://github.com/zams-putra/learn-touch-designer/releases/download/BlobTracking/blobtrac-angka.toe