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