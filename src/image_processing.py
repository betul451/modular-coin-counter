import cv2

def load_image(image_path: str):
    """Resmi yukle kontrol et"""
    image = cv2.imread(image_path)
    if image is None:
        print(f"[HATA] '{image_path}' dosyasi bulunamadi!")
    return image

def preprocess_image(image):
    """
    Resmi gri tonlamaya cevirir ve parazitleri/kabartmalari 
    yumusatmak icin Gaussian Blur uygular.
    """
    if image is None:
        return None
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    return blurred