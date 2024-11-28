# Overview

This is a Python-based recruitment analysis system that uses various technologies to process resumes, extract relevant information, and provide a scoring system for candidate suitability. The system uses Google Drive for storing resumes and other files, and relies on a custom-built AI model to analyze resumes and provide insights.

---
# How It Works

1. The system uses Google Drive to store PDF files.
2. Users upload CVs to Google Drive, which are then processed by the system.
3. The system uses FitZ to read and extract text from the resumes.
4. The extracted text is then analyzed by the GroqClient AI model, which provides insights and scores for each candidate.
5. The scores are used to rank candidates and provide a dashboard for users to view resume data and scores.
6. The system uses TinyDB to store resume data and other metadata.

---

## Getting Started

### Configure Google Drive API Key  

First, you need to generate a Google Drive API Key. Follow the steps in this [guide](https://abrir.link/FppKf):  
- In the **scope phase**, you don’t need to configure authentication. This part will be managed by the application.  
- In **Step 9**, select **Desktop App**.  

After that, update the `*folder_id*` in `drive/download_cv.py`.  

You can find your *folder_id* like this:  

![image](https://github.com/user-attachments/assets/5c3a7ea0-e083-48a2-ab35-0e6413cf195e)  

**Important:** All CVs must be in PDF format. Other file types are not supported.  

---

### Configure GROQ API Key  

You also need a Groq API Key, which can be obtained [here](https://console.groq.com/keys).  

Next, create a `.env` file with the following structure:  

```
GROQ_API_KEY='YOUR_API_KEY'
```  

**Ensure your *.gitignore* is properly configured to exclude `.env` files.**  

---

### Install Dependencies  

This project requires **Python 3.11** or above. Dependencies may not work with earlier Python versions.  

If you don’t have Pip installed, refer to the [installation guide](https://pip.pypa.io/en/stable/installation/).  

Once Pip is installed, run the following command to install the dependencies:  

```bash
pip install -r requirements.txt
```  

---

### Configure Job and AI  

1. **Download CVs:**  
   Update the Google Drive API Key and ensure dependencies are installed. Then, run:  

   ```bash
   python download_cv.py
   ```  

   This will download all CVs from the configured Google Drive folder into the `/curriculos` directory.  

2. **Create Job Announcement:**  
   Edit the `create_job.py` file and define the following variables:  
   - **name:** Job title.  
   - **activities:** Job responsibilities.  
   - **prerequisites:** Minimum requirements.  
   - **differentials:** Nice-to-have qualifications.  

   After updating, run:  

   ```bash
   python create_job.py
   ```  

   This will store the job announcement in TinyDB, a lightweight NoSQL database.  

3. **Configure AI Analysis:**  
   Open `ai.py` and explore the following functions:  
   - `resume_cv`: Customizable prompt to display key information.  
   - `generate_score`: Customizable prompt to evaluate the weight of each CV's details.  
   - `generate_opinion`: Configurable prompt to provide an opinion about each CV.  

---

### Run the Project  

Once all configurations are complete:  

1. **Analyze CVs:**  
   Run the following command:  

   ```bash
   python import_cv.py
   ```  

   This uses the **Groq API** to analyze CVs in the `/curriculos` folder with the `llama-3.1-70b-versatile` model.  

2. **Start the Frontend:**  
   The project uses Streamlit for the frontend. Launch it by running:  

   ```bash
   streamlit run app.py
   ```  

   Access the frontend at [localhost:8501](http://localhost:8501).  

---

## Screenshots  

### Frontend Overview  
<img width="1380" alt="image" src="https://github.com/user-attachments/assets/3e6242c7-54e8-414f-8397-1cd3ec3e0329">  

### Detailed View  
<img width="1387" alt="image" src="https://github.com/user-attachments/assets/37e92bbd-fd78-4195-8302-8a4a243b5b1a">  

### Results Summary  
<img width="1395" alt="image" src="https://github.com/user-attachments/assets/3e9925f7-983b-46dd-8c27-15ca468bdfbd">  

---

# Future Development

1. **Integrate with other AI models**: The system could be enhanced by integrating with other AI models, such as natural language processing (NLP) or machine learning algorithms, to improve the accuracy of candidate scoring.
2. **Add more features**: The system could be expanded to include more features, such as automated resume screening, skills testing, or interview scheduling.
3. **Improve user interface**: The UI could be improved to provide a more user-friendly experience for users, including features such as filtering, sorting, and searching.
