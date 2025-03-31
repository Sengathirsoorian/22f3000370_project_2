
# AI Assignment Solver

This project builds a web-based API that allows users to upload files, ask questions, and receive AI-generated answers using **Puter.js**. It integrates **FastAPI** for the backend and provides a sleek frontend interface.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Output Examples](#output-examples)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features
- **File Upload**: Upload CSV or ZIP files for processing.
- **AI-Powered Answers**: Use Puter.js to answer questions based on uploaded files or standalone queries.
- **User-Friendly Interface**: Modern glassmorphism design with smooth interactions.
- **Automatic Login**: Pre-configured credentials for seamless access to Puter.js.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for Vercel deployment)
- A Puter.js account (credentials pre-configured in this project)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sengathirsoorian/22f3000370_project_2.git
   cd 22f3000370_project_2
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application Locally**:
   Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Usage

### File Upload
1. Click the "Choose File" button and select a CSV or ZIP file.
2. Click "Upload" to process the file.
3. A success message will confirm the upload.

### Ask a Question
1. Enter your question in the input field.
2. Click "Submit" to get an AI-generated response.
3. If a file was uploaded, the response will consider its content.

---

## Output Examples

### 1. Frontend UI
![Frontend](https://github.com/Sengathirsoorian/22f3000370_project_2/blob/main/images/image_2025-03-31_180443516.png))  


### 2. AI Response
![AI Response](https://github.com/Sengathirsoorian/22f3000370_project_2/blob/main/images/image_2025-03-31_180556876.png)  


---

## Deployment

### Deploy to Vercel
1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Log in to Vercel:
   ```bash
   vercel login
   ```

3. Deploy the project:
   ```bash
   vercel
   ```

4. Access the deployed app via the provided URL.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your commit message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

