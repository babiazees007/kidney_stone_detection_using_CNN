# Kidney Stone Detection Backend

## Overview

This backend powers the Kidney Stone Detection web application. It provides RESTful endpoints for image upload, preprocessing, AI-based prediction, and result delivery using a trained Convolutional Neural Network (CNN) model.

---

## Features

- **Image Upload Handling:** Receives CT scan images from the frontend and securely stores them.
- **Preprocessing:** Automatically resizes and normalizes images to match model requirements.
- **AI Prediction:** Loads the trained CNN model (`kidney_stone_detection_cnn_model.h5`) and predicts whether a kidney stone is present.
- **Result Formatting:** Returns clear, structured results for frontend display, including prediction class and confidence.
- **Error Handling:** Provides informative error messages for unsupported formats or processing failures.
- **Security:** Validates file types and manages uploads securely.

---

## Technical Stack

- **Framework:** Flask (Python)
- **AI Model:** TensorFlow/Keras CNN
- **Image Processing:** Pillow, NumPy
- **Serving:** Local Flask server (can be containerized for deployment)

---

## File Structure

```
├── app.py                 # Main Flask backend application
├── kidney_stone_detection_cnn_model.h5  # Trained AI model
├── static/
│   └── uploads/           # Stores uploaded images
├── requirements.txt       # Backend dependencies
└── BACKEND_README.md      # This documentation
```

---

## API Endpoints

### `/` (GET)
- Returns: Home or status message.

### `/predict` (POST)
- Accepts: Image file (JPEG/PNG)
- Returns: JSON with prediction result, confidence, and recommendations.

---

## How to Run

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Ensure the model file is present:**
   - `kidney_stone_detection_cnn_model.h5` must be in the root directory.

3. **Start the backend server:**
   ```sh
   python app.py
   ```
   - The server will run at `http://localhost:5000`

---

## Model Information

- **Input Size:** 224x224 pixels
- **Classes:** Normal (0), Stone (1)
- **Architecture:** CNN (see main project for details)
- **Preprocessing:** Resize, normalize

---

## Security Notes

- Only accepts `.jpg`, `.jpeg`, `.png` files.
- Uploaded files are stored in `static/uploads/` and can be cleaned up as needed.
- Always validate and sanitize user input.

---

## Future Enhancements

- JWT authentication for API endpoints
- Batch image processing
- Logging and monitoring
- Dockerization for deployment
- Integration with hospital systems

---

## Support

For backend issues or questions, refer to the main project documentation or contact the development team.

---
**Note:** This backend is designed to work with the provided frontend and the trained CNN model. Ensure compatibility for