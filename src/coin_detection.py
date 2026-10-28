import cv2
import numpy as np

def estimate_coin_value(radius):
    """
    Yarıçapa göre en yakın Euro değerini öğrenci mantığıyla (if-elif) bulur.
    """
    if radius >= 110:
        return 2.0, "2 Euro"
    elif radius >= 103:
        return 0.50, "50 Cent"
    elif radius >= 97:
        return 1.0, "1 Euro"
    elif radius >= 90:
        return 0.20, "20 Cent"
    elif radius >= 87:
        return 0.05, "5 Cent"
    elif radius >= 82:
        return 0.10, "10 Cent"
    elif radius >= 74:
        return 0.02, "2 Cent"
    else:
        return 0.01, "1 Cent"

def detect_coins(blurred_image):
    """Hough Circle Transform ile fotoğraftaki dairesel şekilleri yakalar."""
    if blurred_image is None:
        return []

    circles = cv2.HoughCircles(
        blurred_image,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=120,
        param1=50,
        param2=50,
        minRadius=60,
        maxRadius=135
    )

    if circles is not None:
        return np.round(circles[0, :]).astype("int")
    return []

def analyze_and_draw(original_image, circles):
    """Tespit edilen paraları çizer ve toplam değeri hesaplar."""
    output = original_image.copy()
    total_val = 0.0
    detected_count = len(circles)

    for (x, y, r) in circles:
        val, label = estimate_coin_value(r)
        total_val += val

        # Yeşil çember ve kırmızı merkez çiz
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)
        cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

        # Para değerini yaz
        cv2.putText(output, label, (x - 35, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0), 2)

    # Özet metni ekle
    summary_text = f"Toplam: {detected_count} Adet | Tutar: ~{total_val:.2f} EUR"
    cv2.putText(output, summary_text, (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    return output, detected_count, total_val #çalışmıyo düzgün kalibre edemedim boyutları