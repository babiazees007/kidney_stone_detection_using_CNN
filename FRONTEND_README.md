# Kidney Stone Detection Frontend

## Overview
This is a comprehensive web-based frontend for the Kidney Stone Detection AI model. The application provides an intuitive interface for uploading CT scan images and receiving AI-powered analysis results.

## Features

### 🏠 Home Page (`home.html`)
- **Image Upload**: Easy drag-and-drop or click-to-upload interface for CT scan images
- **Image Preview**: Real-time preview of uploaded images before analysis
- **Educational Content**: Comprehensive information about kidney stones including:
  - What are kidney stones?
  - Common causes and risk factors
  - Symptoms to watch for
  - Treatment options and remedies
  - Prevention strategies
  - Emergency warning signs

### 📊 Results Page (`result.html`)
- **AI Analysis Results**: Clear display of whether kidney stones were detected
- **Visual Feedback**: Color-coded results with appropriate icons
- **Medical Recommendations**: Tailored advice based on the analysis results
- **Action Items**: Specific next steps for both positive and negative results
- **Print Functionality**: Option to print results for medical records
- **Medical Disclaimer**: Important legal and medical disclaimers

## Technical Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Model**: TensorFlow/Keras CNN model
- **Styling**: Custom CSS with responsive design
- **Fonts**: Google Fonts (Comfortaa, Montserrat)

## File Structure
```
├── app.py                 # Flask application
├── templates/
│   ├── home.html         # Main upload and information page
│   └── result.html       # Results display page
├── static/
│   ├── style.css         # Enhanced styling
│   └── uploads/          # Uploaded images storage
└── kidney_stone_detection_cnn_model.h5  # AI model
```

## How to Use

### 1. Start the Application
```bash
python app.py
```
The application will start on `http://localhost:5000`

### 2. Upload an Image
1. Navigate to the home page
2. Click "Choose CT Scan Image" or drag and drop an image
3. Preview the uploaded image
4. Click "Analyze Image" to process

### 3. View Results
- The AI will analyze the image and redirect to the results page
- View the analysis result (Normal or Stone detected)
- Read the specific recommendations
- Print results if needed
- Upload another image for analysis

## Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- Recommended: CT scan images of kidneys

## Model Information
- **Input Size**: 224x224 pixels
- **Classes**: 
  - Normal (Class 0)
  - Stone (Class 1)
- **Architecture**: Convolutional Neural Network (CNN)
- **Preprocessing**: Automatic resizing and normalization

## Medical Disclaimer
⚠️ **Important**: This application is for educational and screening purposes only. It should not replace professional medical diagnosis or treatment. Always consult with qualified healthcare professionals for accurate diagnosis and appropriate treatment plans.

## Features Highlights

### 🎨 Enhanced UI/UX
- Modern, medical-themed design
- Responsive layout for all devices
- Smooth animations and transitions
- Intuitive navigation

### 📱 Mobile Responsive
- Optimized for smartphones and tablets
- Touch-friendly interface
- Adaptive grid layouts

### 🔒 Safety Features
- Secure file upload handling
- Input validation
- Clear medical disclaimers
- Emergency care guidelines

### 📋 Educational Content
- Comprehensive kidney stone information
- Prevention strategies
- Treatment options
- When to seek medical care

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Performance
- Fast image processing
- Optimized model loading
- Efficient file handling
- Quick response times

## Future Enhancements
- Multiple image upload
- Batch processing
- Result history
- User accounts
- PDF report generation
- Integration with medical systems

## Support
For technical issues or questions about the application, please refer to the main project documentation or contact the development team.

---
**Note**: This frontend is designed to work with the kidney stone detection model trained in `main.ipynb`. Ensure the model file `kidney_stone_detection_cnn_model.h5` is present in the root directory.