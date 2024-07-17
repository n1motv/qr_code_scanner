import cv2
from pyzbar.pyzbar import decode
import numpy as np


def scan_qr_code(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
        return


    decoded_objects = decode(img)


    if not decoded_objects:
        print("Aucun code QR détecté.")
        return

    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))

        rect_points = obj.polygon
        if len(rect_points) == 4:
            pts = [(point.x, point.y) for point in rect_points]
            pts = np.array(pts, np.int32)
            pts = pts.reshape((-1, 1, 2))
            img = cv2.polylines(img, [pts], True, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scan QR codes from an image file.")
    parser.add_argument("image_path", type=str, help="Path to the image file containing the QR code.")

    args = parser.parse_args()

    scan_qr_code(args.image_path)
