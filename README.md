# LEARNIQ – Course Content Simplification Agent

> **Learn at your level. Grow beyond your limits.**

LEARNIQ is an AI-powered **Course Content Simplification Agent** designed to help students understand academic content according to their individual learning level.

Students can enter academic content and select a proficiency level — **Beginner, Intermediate, Advanced, or Expert**. LEARNIQ uses **IBM Granite through IBM watsonx.ai** to adapt the content while preserving its original meaning.

The system provides an interactive learning experience with **adapted explanations, key concepts, important terms, real-world analogies, examples, common misconceptions, interactive flashcards, and a quick quiz**.

---

## 🎯 Problem Statement

Academic content is often written at a fixed level of complexity. Students with different levels of prior knowledge may find technical terms, lengthy explanations, and complex concepts difficult to understand.

LEARNIQ addresses this problem by adapting the same academic content to the student's preferred learning level.

---

## 💡 Proposed Solution

LEARNIQ provides an AI-powered personalized learning experience.

The student can:

1. Enter academic content.
2. Select a learning level.
3. Analyze and adapt the content using IBM Granite.
4. Read the personalized explanation.
5. Explore key concepts and important terms.
6. Understand the topic through examples and analogies.
7. Learn about common misconceptions.
8. Practice using interactive flashcards.
9. Take a quick 3-question quiz.
10. View instant feedback and the final score.

---

## 📚 Learning Levels

| Level            | Description                                         |
| ---------------- | --------------------------------------------------- |
| **Beginner**     | Simple language and easy-to-understand explanations |
| **Intermediate** | Moderate detail with relevant terminology           |
| **Advanced**     | Deeper explanation with more technical details      |
| **Expert**       | Detailed and technically advanced explanation       |

---

## ✨ Key Features

### 📖 Adaptive Explanation

Explains the same academic topic according to the student's selected proficiency level.

### 🧠 Key Concepts

Highlights the main concepts that students should understand.

### 📌 Important Terms

Identifies important technical terms related to the topic.

### 🃏 Interactive Flashcards

Presents important terms through interactive flashcards to make learning more engaging.

### 🌍 Real-World Analogy

Uses familiar real-world situations to make difficult concepts easier to understand.

### 💡 Examples

Provides relevant examples to support conceptual understanding.

### ⚠️ Common Misconceptions

Highlights possible misunderstandings students may have about the topic.

### 📝 Quick Quiz

Generates a 3-question multiple-choice quiz based on the learning content.

### ⚡ Instant Feedback

Provides immediate feedback for quiz answers and displays the final score.

### 🔄 Level Switching

Students can try the same topic at different learning levels without entering the content again.

---

## 🤖 Role of Agentic AI

LEARNIQ works as an intelligent learning assistant rather than simply generating a text response.

The AI workflow supports multiple learning tasks:

```text
Content Analysis
       ↓
Content Adaptation
       ↓
Learning Support
       ↓
Interactive Practice
       ↓
Assessment
```

Using **IBM Granite**, the system analyzes academic content and adapts its complexity according to the selected proficiency level.

This makes LEARNIQ more **personalized, adaptive, and interactive** for students.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       Student       │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │    LEARNIQ Frontend     │
                 │    HTML + CSS + JS      │
                 │      index.html         │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     Flask Backend       │
                 │        app.py           │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      IBM watsonx.ai     │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │       IBM Granite       │
                 │ Content Analysis &      │
                 │ Content Adaptation      │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Structured Learning   │
                 │        Response         │
                 └────────────┬────────────┘
                              │
                              ▼
             ┌──────────────────────────────────┐
             │ Explanation • Concepts • Terms   │
             │ Analogy • Example • Misconception│
             │ Flashcards • Quiz                │
             └────────────────┬─────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │       Student       │
                    └─────────────────────┘
```

---

## 🔄 Application Workflow

```text
Student enters academic content
              ↓
Student selects proficiency level
              ↓
         Analyze Content
              ↓
       Flask Backend
              ↓
        IBM watsonx.ai
              ↓
         IBM Granite
              ↓
       Adapted Content
              ↓
 ┌─────────────────────────────┐
 │ Adapted Explanation         │
 │ Key Concepts                │
 │ Important Terms             │
 │ Real-World Analogy          │
 │ Example                     │
 │ Common Misconception        │
 └──────────────┬──────────────┘
                ↓
       Interactive Flashcards
                ↓
           Quick Quiz
                ↓
         Score & Feedback
```

---

## 🛠️ Technologies Used

### IBM Technologies

* **IBM Bob** – Used to build and enhance the LEARNIQ application.
* **IBM Granite** – Used for understanding academic content and adapting explanations according to the selected learning level.
* **IBM watsonx.ai** – Used to connect the application with the IBM Granite model.
* **IBM Cloud** – Provides the cloud environment for the AI-powered application.

### Application Technologies

* **Python** – Backend programming.
* **Flask** – Provides the backend API and connects the frontend with the AI service.
* **HTML** – Used to structure the frontend.
* **CSS** – Used for the user interface and visual styling.
* **JavaScript** – Used for interactive features such as learning levels, flashcards, quiz, and results.

---

## 📂 Project Structure

```text
LEARNIQ/
│
├── static/
│   └── index.html
│
├── app.py
├── test_api.py
├── validate_orchestrate.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File / Folder             | Purpose                                                   |
| ------------------------- | --------------------------------------------------------- |
| `static/`                 | Contains the frontend files                               |
| `static/index.html`       | Main LEARNIQ user interface and interactive learning flow |
| `app.py`                  | Flask backend and IBM Granite integration                 |
| `test_api.py`             | Tests the LEARNIQ API and backend functionality           |
| `validate_orchestrate.py` | Validates the LEARNIQ Orchestrate-related configuration   |
| `requirements.txt`        | Contains the required Python packages                     |
| `README.md`               | Project documentation                                     |
| `.gitignore`              | Prevents unnecessary files from being uploaded            |

---

## 🖥️ User Interface Flow

LEARNIQ provides a simple five-stage learning experience.

### 1. Landing Screen

Introduces LEARNIQ and allows the student to start learning.

### 2. Learning Screen

Students enter their academic content and select one of the four proficiency levels.

### 3. Results Screen

The AI-generated learning material includes:

* Adapted Explanation
* Key Concepts
* Important Terms
* Interactive Flashcards
* Real-World Analogy
* Example
* Common Misconception

### 4. Quiz Screen

Students answer three multiple-choice questions generated from the learning content.

### 5. Celebration Screen

Displays the quiz score, feedback, and options to review the material or learn another topic.

---

## ⚙️ Backend API

### Health Check

```text
GET /api/health
```

This endpoint checks whether the LEARNIQ backend is running correctly.

### Simplify Content

```text
POST /api/simplify
```

The API accepts academic content and the selected proficiency level.

Example request:

```json
{
  "content": "Explain photosynthesis in plants.",
  "level": "Beginner"
}
```

Supported levels:

```text
Beginner
Intermediate
Advanced
Expert
```

The backend processes the request using IBM Granite and returns structured learning content.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the Project

```bash
cd LEARNIQ
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure IBM Cloud / watsonx.ai

Configure the required IBM Cloud and watsonx.ai credentials used by the application.

### 7. Run the Application

```bash
python app.py
```

Open the local URL displayed by the application in your browser.

---

## 🧪 Testing

The project includes `test_api.py` for testing the LEARNIQ backend API.

The application can be tested for:

* Backend health check
* Empty content validation
* Invalid proficiency level validation
* Beginner-level adaptation
* Intermediate-level adaptation
* Advanced-level adaptation
* Expert-level adaptation
* Structured AI response
* Quiz generation
* Frontend-backend communication

### Example

**Input:**

```text
Photosynthesis is the process by which green plants convert
light energy into chemical energy.
```

**Selected Level:**

```text
Beginner
```

LEARNIQ generates a simpler explanation along with supporting learning content and a quick quiz.

---

## 🌟 Novelty and Uniqueness

LEARNIQ combines **Agentic AI, adaptive learning, structured content generation, interactive learning, and assessment** into a single platform.

### Key Unique Features

* **Adaptive Learning Levels** – Same topic can be explained at four different levels.
* **Meaning Preservation** – The complexity is changed while maintaining the original concept.
* **Structured Learning Content** – Goes beyond a simple explanation.
* **Interactive Flashcards** – Helps students learn important terms.
* **Quick Assessment** – Generates a short quiz with instant feedback.
* **Level Switching** – Students can change the difficulty of the same topic.
* **Complete Learning Flow** – Learn → Explore → Practice → Evaluate.

---

## 🎯 Target Users

LEARNIQ can be useful for:

* College students
* School students
* Self-learners
* Students preparing for examinations
* Students learning technical subjects
* Learners who need concepts explained at different difficulty levels

---

## 🔮 Future Scope

* **Multiple Language Support** – Provide explanations in different languages.
* **PDF and Document Support** – Allow students to upload notes and study materials.
* **Personalized Learning Paths** – Recommend learning activities based on student performance.
* **Voice-Based Learning** – Add voice input and audio explanations.
* **Progress Tracking** – Track topics learned, quiz scores, and improvement.
* **Interactive Doubt Clarification** – Allow students to ask follow-up questions about generated content.
* **Advanced AI Tutoring** – Develop LEARNIQ into a more complete AI-based personal tutor.

---

## 📌 Project Information

| Category                 | Details                                       |
| ------------------------ | --------------------------------------------- |
| **Project Name**         | LEARNIQ – Course Content Simplification Agent |
| **Problem Statement**    | 19                                            |
| **Domain**               | Education / EdTech                            |
| **AI Model**             | IBM Granite                                   |
| **AI Platform**          | IBM watsonx.ai                                |
| **Development Platform** | IBM Bob                                       |
| **Backend**              | Python + Flask                                |
| **Frontend**             | HTML + CSS + JavaScript                       |

---

## 👩‍💻 Author

**Deepika E**

Developed as part of the **IBM University Engagement Program**.

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ Conclusion

LEARNIQ transforms academic content into a **personalized and interactive learning experience**.

Instead of giving every student the same explanation, LEARNIQ allows learners to choose their preferred level of understanding — from **Beginner to Expert** — and supports their learning with explanations, concepts, examples, analogies, flashcards, misconceptions, and quizzes.

> **LEARNIQ — Learn at your level. Grow beyond your limits.**
