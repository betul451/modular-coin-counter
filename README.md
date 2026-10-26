🪙 Euro Coin Detection \& Counter



This project is a simple Computer Vision application written in Python using OpenCV. It detects Euro coins from an image, counts them, and estimates their values based on pixel radii.



💡 How It Works



The project is structured into 3 main parts:



1.Image Preprocessing (`src/image\_processing.py`):

&#x20;  - Converts the image to grayscale to remove color noise.

&#x20;  - Applies Gaussian Blur to smooth out coin surface details (numbers, text) so circle detection works better.



2.Coin Detection \& Value Estimation (`src/coin\_detection.py`):

&#x20;  - Uses OpenCV's `HoughCircles` algorithm to locate circular shapes (coins).

&#x20;  - Measures pixel radii and uses a straightforward `if-elif` threshold logic to estimate each coin's value (Cent / Euro).



3.Main Runner (`main.py`):

&#x20;  - Runs the pipeline step by step, draws green circles around detected coins, and displays the total calculated amount.



 📁 Project Structure

modular-coin-counter/

├── src/

│   ├── init.py

│   ├── image\_processing.py

│   └── coin\_detection.py

├── euro\_coins.jpg

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

