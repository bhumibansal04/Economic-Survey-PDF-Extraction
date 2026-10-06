\# Automated Information Extraction from Economic Survey PDFs using NLP



\## 📌 Project Overview



This project automates the extraction of important economic information from \*\*Government of India Economic Survey PDF reports\*\* using \*\*Natural Language Processing (NLP)\*\* and \*\*Named Entity Recognition (NER)\*\*.



The system takes an Economic Survey PDF as input, extracts its text, processes the text using a trained \*\*spaCy NER model\*\*, and identifies important information such as:



\* \*\*Country\*\*

\* \*\*Financial Year\*\*

\* \*\*GDP Growth Percentage\*\*

\* \*\*GDP Value\*\*



The project is designed to reduce the effort required to manually search through lengthy Economic Survey documents and extract structured information.



\---



\## 🎯 Objectives



The main objectives of this project are:



\* Extract useful information automatically from Economic Survey PDFs.

\* Apply NLP techniques to unstructured PDF text.

\* Build and use a custom Named Entity Recognition model.

\* Identify economic entities from government reports.

\* Convert unstructured document information into structured output.

\* Reduce manual effort and improve information retrieval.



\---



\## 🧠 NLP Approach



The project uses \*\*Named Entity Recognition (NER)\*\* to identify domain-specific entities from Economic Survey documents.



A custom spaCy NER model was trained for the following entities:



| Entity           | Description                            |

| ---------------- | -------------------------------------- |

| `COUNTRY`        | Name of the country                    |

| `FINANCIAL YEAR` | Financial year mentioned in the report |

| `GDP GROWTH %`   | GDP growth percentage                  |

| `GDP VALUE`      | GDP value mentioned in the report      |



\---



\## 📊 Dataset



The dataset was created using Economic Survey reports available from the Government of India's Economic Survey resources.



The project uses:



\* \*\*20 Economic Survey reports\*\*

\* \*\*50 annotated examples per target field\*\*

\* Custom annotations for domain-specific entities



The annotated data was used to train the custom NER model.



\---



\## 🤖 Model



The trained model is based on \*\*spaCy Named Entity Recognition\*\*.



The trained model is included in this repository under:



```text

EconomicReportModel/

```



The model contains the required vocabulary, tokenizer, NER model, configuration files, and other spaCy model components.



\### Model Performance



The trained model achieved the following evaluation results:



| Metric           |  Score |

| ---------------- | -----: |

| Entity Precision | 85.21% |

| Entity Recall    | 85.87% |

| Entity F1-Score  | 85.54% |

| Token F1         | 99.57% |

| Tag Accuracy     | 97.38% |



\---



\## 🛠️ Technologies Used



\* \*\*Python\*\*

\* \*\*spaCy\*\*

\* \*\*Natural Language Processing (NLP)\*\*

\* \*\*Named Entity Recognition (NER)\*\*

\* \*\*PyMuPDF\*\*

\* \*\*Regular Expressions\*\*

\* \*\*Git\*\*

\* \*\*Git LFS\*\*



\---



\## 📁 Project Structure



```text

Economic-Survey-PDF-Extraction/

│

├── EconomicReportModel/

│   ├── attribute\_ruler/

│   ├── lemmatizer/

│   ├── ner/

│   ├── parser/

│   ├── senter/

│   ├── tagger/

│   ├── tok2vec/

│   ├── vocab/

│   ├── config.cfg

│   ├── meta.json

│   └── ...

│

├── output.py

├── requirements.txt

├── .gitignore

├── .gitattributes

└── README.md

```



\---



\## ⚙️ Installation



\### 1. Clone the repository



Clone this repository to your local system.



\### 2. Install the required Python packages



Open a terminal inside the project directory and run:



```bash

pip install -r requirements.txt

```



The main dependencies are:



```text

spacy

PyMuPDF

```



\### 3. Git LFS



The trained spaCy model contains a large vector file. Therefore, \*\*Git LFS (Large File Storage)\*\* is used to store the model correctly.



Make sure Git LFS is installed and initialized before cloning/downloading the complete model:



```bash

git lfs install

```



Then clone the repository normally.



\---



\## ▶️ How to Run



After installing the required dependencies, run:



```bash

python output.py

```



The program will ask:



```text

Enter the full path of the pdf :

```



Enter the path of the Economic Survey PDF that you want to process.



The program will then:



1\. Read the PDF.

2\. Extract the text using PyMuPDF.

3\. Clean and normalize the extracted text.

4\. Apply the trained spaCy NER model.

5\. Identify the required entities.

6\. Apply regular-expression based fallback extraction where required.

7\. Display the extracted economic information.



\---



\## 🔍 Example Output



The system extracts information in the following format:



```text

COUNTRY

FINANCIAL YEAR

GDP GROWTH %

GDP VALUE

```



The exact values depend on the Economic Survey PDF provided as input.



\---



\## 🔄 Workflow



```text

Economic Survey PDF

&#x20;       ↓

PDF Text Extraction

&#x20;       ↓

Text Preprocessing

&#x20;       ↓

spaCy NER Model

&#x20;       ↓

Entity Recognition

&#x20;       ↓

Regex Fallback

&#x20;       ↓

Structured Economic Information

```



\---



\## ✨ Key Features



\* Automated information extraction from PDF documents

\* Custom domain-specific NER model

\* Supports Economic Survey reports

\* Extracts multiple economic entities

\* Uses a trained spaCy model

\* PDF text extraction using PyMuPDF

\* Regex fallback for improved extraction

\* Local/offline processing

\* Large trained model stored using Git LFS



\---



\## 📌 Future Enhancements



Possible future improvements include:



\* Adding more Economic Survey reports to the dataset

\* Increasing the number of annotated training examples

\* Adding more economic entities

\* Improving entity recognition accuracy

\* Creating a graphical user interface

\* Supporting batch processing of multiple PDFs

\* Exporting extracted information to CSV or Excel

\* Adding visualization of extracted economic indicators



\---



\## 📚 Source



The Economic Survey reports used for this project are obtained from the Government of India's Economic Survey resources.



\---



\## 👩‍💻 Author



\*\*Bhumi Bansal\*\*



MCA Student | Natural Language Processing | Machine Learning | Software Development



\---



\## ⭐ Project Purpose



This project demonstrates the practical application of \*\*Natural Language Processing, Named Entity Recognition, and document information extraction\*\* to transform unstructured government reports into structured and useful economic information.



