# CV-Analyzer
A CV analyzer, made for academic purposes

# How to Configure

## Config Google Drive API Key

First of all, you need to generate an Google Drive API Key. U can see how to in this link: `https://abrir.link/FppKf` 
- In the scope phase, you don't need to configure authentication, this part will be managed by the application;
- In the Step 9, select *Desktop App*

After that, U will need to change the *folder_id* at `drive/download_cv.py` 

U can see your *folder_id* in 

![image](https://github.com/user-attachments/assets/5c3a7ea0-e083-48a2-ab35-0e6413cf195e)

**Important** All CVs need to be a PDF, otherwise, the app will not work

## Install Dependencies

This project is running in Python 3.11 or above. Some dependencies will not work in previous Python versions. If you don't want any bad circunstancies, please use Python 3.11.

You will need Pip, if you don't have it. Please check the installation guide: `https://pip.pypa.io/en/stable/installation/`

After you ensure that Pip is installed, please run


```
pip install requirements.txt
```


This will install all the dependencies that are required for the CV-Analyzer works correctly.

## Configure JOB and AI

- [X] Config Google Drive API Key
- [X] Install Dependencies

First, run this command


```
python download_cv.py
```


This command will download all the CVs from your Google Drive Folder and send them to the `/currilos` folder.

#

Then, you need to create a job announcement in the `create_job.py` file, you have some variables to fill in

- *name* (job title)
#
- *activities* (what the employee will do)
#
- *prerequisites* (the minium requirements to have)
#
- *differentials* (what is nice to have)
#

After you fullfil the previous requirements, run:


```
python create_job.py
```


This command above will deploy the job in the TinyDB, a simple NoSQL database.

#

You can configure the AI analysis changing the `ai.py` file.

In this file you have some cool functions, like:
#
*resume_cv*: configurable prompt with some major infos that you want to display
#
*generate_score*: configurable prompt which will evaluate the weight of each information
#
*generate_opnion*: configurable prompt that generate an opnion about the CVs

## Run Project

- [X] Config Google Drive API Key
- [X] Install Dependencies
- [x] Configure JOB and AI

After all things have already been configured, run:

```
python import_cv.py
```

This will use the *Groq API* to run the *llama-3.1-70b-versatile* to analyse the CVs from the `/curriculos` folder

After that, the analyse is complete. We use Streamlit for Frontend so, run:


```
streamlit run app.py
```


<img width="643" alt="image" src="https://github.com/user-attachments/assets/53cb8dfe-93b2-4a0d-968c-71492decfb57">

#


Then you just acces you localhost:8501

## Some Images from the Frontend


<img width="1380" alt="image" src="https://github.com/user-attachments/assets/3e6242c7-54e8-414f-8397-1cd3ec3e0329">

#

<img width="1387" alt="image" src="https://github.com/user-attachments/assets/37e92bbd-fd78-4195-8302-8a4a243b5b1a">

#

<img width="1395" alt="image" src="https://github.com/user-attachments/assets/3e9925f7-983b-46dd-8c27-15ca468bdfbd">

