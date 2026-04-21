# 🚀 AI Data Analyst Agent

An intelligent, full-stack AI application that allows users to upload CSV datasets, ask questions in natural language, and receive **insightful analysis with visual charts and tables** — just like a real data analyst.

---

## 🧠 Overview

The **AI Data Analyst Agent** transforms raw data into meaningful insights using a combination of:

* Data processing (Pandas)
* Backend APIs (FastAPI)
* AI-generated explanations (LLM)
* Interactive frontend (Next.js + Chart.js)

It enables **non-technical users** to explore data without writing code.

---

## ✨ Key Features

* 📂 **CSV Upload & Parsing**

  * Upload structured datasets instantly
  * Automatic schema detection (columns, types, nulls)

* 💬 **Natural Language Querying**

  * Ask questions like:

    * *“Top 5 products by revenue”*
    * *“Show monthly trend”*

* 📊 **Automatic Data Visualization**

  * Bar charts for comparisons
  * Line charts for trends
  * Auto-generated based on query intent

* 🧾 **Insight Generation**

  * AI explains results in simple language
  * Includes insights and recommendations

* 📋 **Tabular Data Output**

  * Structured tables for deeper inspection

---

## 🏗️ Tech Stack

### 🔹 Frontend

* Next.js (React Framework)
* Tailwind CSS
* Chart.js (Data Visualization)

### 🔹 Backend

* FastAPI
* Pandas

### 🔹 AI Layer

* Gemini API (LLM for explanation)

---

## 📁 Project Structure

```bash
AI-Data-Analyst/
│
├── backend/
│   ├── main.py          # FastAPI server
│   ├── analyst.py       # Data analysis logic
│   ├── utils.py         # AI explanation layer
│
├── frontend/
│   ├── src/app/page.tsx
│   ├── src/components/ChartView.tsx
│
├── README.md
```

---

## ⚙️ How It Works

1. User uploads a CSV file
2. Backend processes dataset using Pandas
3. User asks a question
4. Backend:

   * Analyzes data (`analyst.py`)
   * Generates explanation (`utils.py`)
5. Frontend displays:

   * Answer
   * Chart (if applicable)
   * Table data

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-data-analyst-agent.git
cd ai-data-analyst-agent
```

---

### 2️⃣ Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python -m uvicorn main:app --reload
```

---

### 3️⃣ Setup Frontend

```bash
cd frontend

npm install
npm run dev
```

---

### 4️⃣ Open in Browser

```text
http://localhost:3000
```

---

## 🧪 Example Queries

* Top 5 products by revenue
* Compare revenue by category
* Show monthly revenue trend
* Total revenue
* Average price

---

## 📸 Screenshots

> Add screenshots here after deployment
> Example:

* Upload UI
* Chart output
* AI insights

---

## 🔐 Environment Variables

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ Never upload `.env` to GitHub.

---

## 📈 Future Improvements

* Support large datasets (50k+ rows with chunking)
* Smart chart selection using AI
* Export insights as PDF/Excel
* Multi-file analysis
* Dashboard mode (multiple charts)

---

## 💡 Use Cases

* Business analytics
* Sales insights
* Student projects
* Data exploration tools
* AI-powered BI assistant

---

## 👨‍💻 Author

**Nitin Rawat**
Aspiring AI Engineer | Gen AI Developer

---

## ⭐ Contribute

If you like this project:

* Star ⭐ the repo
* Fork 🍴 and improve
* Open PRs 🚀

---

## 📜 License

This project is open-source and available under the MIT License.
