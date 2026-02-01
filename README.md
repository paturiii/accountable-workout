# 🏋️‍♂️ Accountable Workout

**Accountable Workout** is a mobile application that helps gym-goers improve exercise form by analyzing recorded workout videos and identifying **bad reps** (e.g. incomplete range of motion, asymmetry, poor depth).

Unlike generic fitness apps, SmartForm focuses on **objective, explainable feedback** using pose estimation and biomechanical rules — not vague “AI scores”.

---

## 🚨 Problem

Most beginners (and many intermediates) perform exercises with poor form due to:
- Lack of coaching
- No immediate feedback
- No objective way to review reps

Bad form leads to:
- Slower progress
- Increased injury risk
- Reinforcing incorrect movement patterns

---

## ✅ Solution

SmartForm allows users to:
1. Record workout videos
2. Automatically detect reps
3. Classify reps as good or bad
4. Explain *why* a rep is bad
5. Track workouts and estimated calorie burn

Feedback is generated using **pose estimation + rule-based biomechanics**, ensuring transparency and debuggability.

---

## 🧠 System Architecture
```
React Native App
│
├── Video recording & playback
├── Workout tracking UI
├── Rep feedback visualization
│
└── REST API
↓
Python Backend (FastAPI)
│
├── Authentication
├── Workout CRUD
├── Video upload & storage
├── Pose estimation pipeline
├── Rep detection
├── Form analysis
└── Results persistence
```

---

## 🛠 Tech Stack

### Frontend (Mobile)
- **React Native (Expo)**
- **TypeScript**
- `expo-camera`, `expo-av`
- **TanStack Query**
- **Axios**
- Minimal UI-first design (function > aesthetics)

---

### Backend
- **Python**
- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **SQLAlchemy / SQLModel**
- **AWS S3** (video storage)

---

### Computer Vision & Analysis
- **MediaPipe Pose**
- **NumPy**
- **OpenCV**
- **Pandas**
- **scikit-learn** (future classification layer)

---

This repo demonstrates:
- Applied computer vision
- ML system design thinking
- Backend + mobile integration
- Engineering tradeoff awareness
