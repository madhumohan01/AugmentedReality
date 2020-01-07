import numpy as np
import cv2
from Template import Template

def run(videoFile, template1, advert1, minmatch1, ratio1, template2=None, advert2=None, minmatch2 = 0, ratio2 = 0, outputFile = None, show = True):
    MAX_FRAMES = 100000000
    frame_count = 0
    start_from = 0

    cap = cv2.VideoCapture(videoFile)
    templates = []
    template1 = Template(template1, advert1, minmatch1, ratio1)
    templates.append(template1)
    if template2 is not None:
        template2 = Template(template2, advert2, minmatch2, ratio2)
        templates.append(template2)

    if outputFile is not None:
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter(outputFile,fourcc, 30.0, (1280,720))


    while(1):
        ret,frame = cap.read()
        frame_count += 1
        if ret == True:
            if frame_count < start_from:
                continue

            # if frame_count % 2 == 0:
            #     continue


            for template in templates:
                frame = template.processFrame(frame, frame_count)

            if outputFile is None:
                if show is True:
                    cv2.imshow("img3",cv2.flip(frame,-1))
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                out.write(cv2.flip(frame,-1))

            if frame_count > MAX_FRAMES:
                print("Exiting...")
                break

        else:
            break

        # Release everything if job is finished
    cap.release()
    if outputFile is not None:
        out.release()
    cv2.destroyAllWindows()
    return frame_count
