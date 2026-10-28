import cv2
from src import image_processing as ip
from src import coin_detection as cd

def main():
    # Fotograf dosya adini burayla eslestiriyoruz
    image_path = "euro_coins.jpg"

    print("1. Adim: Gorsel yukleniyor...")
    image = ip.load_image(image_path)
    if image is None:
        return

    print("2. Adim: On isleme (Gri tonlama + Blur)...")
    blurred = ip.preprocess_image(image)

    print("3. Adim: Madeni paralar tespit ediliyor...")
    circles = cd.detect_coins(blurred)

    print("4. Adim: Sonuclar ciziliyor ve hesaplaniyor...")
    result_image, count, total_amount = cd.analyze_and_draw(image, circles)

    print("--------------------------------------------------")
    print(f"Tespit Edilen Para Adedi : {count}")
    print(f"Hesaplanan Toplam Tutar   : {total_amount:.2f} EUR")
    print("--------------------------------------------------")

    cv2.imshow("Euro Coin Detection", result_image)
    print("Pencereyi kapatmak icin herhangi bir tusa basin...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()